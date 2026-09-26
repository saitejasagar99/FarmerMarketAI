---
title: Farmer Market Intelligence
emoji: 🌾
colorFrom: green
colorTo: yellow
sdk: docker
app_port: 7860
pinned: false
---

# 🌾 Farmer-to-Market Intelligence

AI-Powered Crop Selling Decision Support System for Farmers in Telangana.

## 🚀 Features
- **Live Mandi Rates**: Daily verified APMC prices from regional Telangana markets.
- **AI Agricultural Market Advisor**: Multilingual recommendations powered by LangGraph & GPT-4o-mini.
- **Smart Profit Analysis**: True net profit calculation considering transport fuel, vehicle type, and mandi fees.
- **3-Day ML Price Forecast**: Machine learning price trends (RandomForest / LinearRegression).
- **Voice Assistant**: Multilingual voice recognition with auto-detection for Telugu, Hindi, and English.
- **Rythu Bazar Routing**: Zero-commission local market routing for smallholders.

## 🐳 Docker Deployment

### 1. Build and Run Locally with Docker
```bash
docker build -t farmer-market-ai .
docker run -p 7860:7860 -e OPENAI_API_KEY="your-api-key" farmer-market-ai
```
Access the application at `http://localhost:7860`.

### 2. Deploy to Hugging Face Spaces (Free Cloud Hosting)
1. Go to [Hugging Face Spaces](https://huggingface.co/spaces) and click **Create new Space**.
2. Name your space (e.g. `farmer-market-ai`), select **Docker** as the Space SDK, and choose **Blank**.
3. In your Space's Settings, add your secret:
   - `OPENAI_API_KEY`: Your OpenAI API key (optional for template fallbacks).
4. Push this repository to your Hugging Face Space Git repository:
```bash
git remote add space https://huggingface.co/spaces/<your-hf-username>/<your-space-name>
git push space main
```
Hugging Face will automatically build the Docker image and deploy your live app!
