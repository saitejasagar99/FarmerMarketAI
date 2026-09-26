#!/usr/bin/env python3
"""
Unified launcher for Farmer-to-Market Intelligence.
Starts both the FastAPI backend and the Streamlit frontend.
Ideal for single-container / single-dyno cloud deployments (Render, Railway, Hugging Face Spaces, Docker).
"""
import os
import sys
import time
import subprocess
import signal
import urllib.request

def wait_for_backend(url="http://127.0.0.1:8000/", timeout=30):
    """Wait until FastAPI is responsive."""
    print("⏳ Waiting for FastAPI backend to initialize...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                if response.status == 200:
                    print("✅ FastAPI backend is healthy and responding.")
                    return True
        except Exception:
            time.sleep(1)
    print("⚠️ Backend check timed out, proceeding to start Streamlit anyway.")
    return False

def main():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, root_dir)

    # Cloud providers inject $PORT (Hugging Face Spaces uses 7860 by default)
    public_port = os.getenv("PORT", "7860")
    backend_port = os.getenv("BACKEND_PORT", "8000")

    # Ensure frontend points to the local backend port
    os.environ["API_URL"] = f"http://127.0.0.1:{backend_port}"

    print("==================================================")
    print("🌾 Starting Farmer-to-Market Intelligence Platform")
    print(f"🔹 Backend Port:  {backend_port}")
    print(f"🔹 Frontend Port: {public_port}")
    print("==================================================")

    # 1. Start FastAPI backend as subprocess
    backend_cmd = [
        sys.executable, "-m", "uvicorn", "backend.main:app",
        "--host", "127.0.0.1",
        "--port", str(backend_port)
    ]
    backend_proc = subprocess.Popen(backend_cmd, cwd=root_dir)

    # 2. Wait for backend to be ready
    wait_for_backend(f"http://127.0.0.1:{backend_port}/", timeout=20)

    # 3. Start Streamlit frontend on public port
    frontend_cmd = [
        sys.executable, "-m", "streamlit", "run", "frontend/app.py",
        "--server.port", str(public_port),
        "--server.address", "0.0.0.0",
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false"
    ]

    def handle_exit(signum, frame):
        print("\nShutting down services...")
        backend_proc.terminate()
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    frontend_proc = subprocess.Popen(frontend_cmd, cwd=root_dir)

    # Wait for frontend process
    try:
        frontend_proc.wait()
    except KeyboardInterrupt:
        pass
    finally:
        backend_proc.terminate()

if __name__ == "__main__":
    main()
