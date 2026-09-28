import os
import sys

# Guarantee project root is in sys.path so services, backend, ml are always importable
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd
import altair as alt
import urllib.parse
import importlib
import secrets
import time
import datetime

# Ensure fresh translations and voice services when Streamlit hot-reloads
for mod_name in ["frontend.translations", "translations", "services.voice_service", "voice_service"]:
    if mod_name in sys.modules:
        try:
            importlib.reload(sys.modules[mod_name])
        except Exception:
            pass


try:
    from frontend.translations import (
        SUPPORTED_LANGUAGES,
        DEFAULT_LANGUAGE,
        t,
        format_crop,
        format_quality,
        format_weather_condition,
        format_weather_alert,
        format_transit_advice,
        format_shelf_life,
        format_damage_risk,
        format_perishability,
        format_spoilage_rate,
        format_holding_verdict,
        format_crop_explanation,
        format_damage_factors,
        get_localized_recommendation,
        get_localized_farmer_advice,
        CROP_CATEGORIES,
        CROP_CATEGORY_MAP,
        CROPS_DISPLAY,
    )
except ImportError:
    from translations import (
        SUPPORTED_LANGUAGES,
        DEFAULT_LANGUAGE,
        t,
        format_crop,
        format_quality,
        format_weather_condition,
        format_weather_alert,
        format_transit_advice,
        format_shelf_life,
        format_damage_risk,
        format_perishability,
        format_spoilage_rate,
        format_holding_verdict,
        format_crop_explanation,
        format_damage_factors,
        get_localized_recommendation,
        get_localized_farmer_advice,
        CROP_CATEGORIES,
        CROP_CATEGORY_MAP,
        CROPS_DISPLAY,
    )

try:
    from services.sms_service import send_otp_sms
except ImportError:
    try:
        from sms_service import send_otp_sms
    except ImportError:
        def send_otp_sms(phone, otp):
            return {"success": False, "provider": "unconfigured", "otp": otp}

try:
    from services.market_intel import evaluate_crop_quality_from_harvest_date
except ImportError:
    try:
        from market_intel import evaluate_crop_quality_from_harvest_date
    except ImportError:
        def evaluate_crop_quality_from_harvest_date(crop, harvest_date, ref_date=None):
            import datetime
            h = harvest_date if isinstance(harvest_date, datetime.date) else datetime.date.today()
            r = ref_date if isinstance(ref_date, datetime.date) else datetime.date.today()
            diff = max(0, (r - h).days)
            c = (crop or "").lower().strip()
            if "rice" in c or "paddy" in c:
                q = "Grade A" if diff <= 60 else ("Grade B" if diff <= 180 else "Grade C")
                desc = "Prime translucent dry grain, moisture <12%, Grade A." if q == "Grade A" else ("Aged godown storage paddy, Grade B." if q == "Grade B" else "Extended storage aged grain, Grade C.")
                tl = "Grade A: 0–60d • Grade B: 61–180d • Grade C: 181+d (Shelf Life: 200d)"
            elif "cotton" in c or "kapas" in c:
                q = "Grade A" if diff <= 30 else ("Grade B" if diff <= 90 else "Grade C")
                desc = "Bright white high-luster lint, Grade A." if q == "Grade A" else ("Standard ginning lint, Grade B." if q == "Grade B" else "Discolored fiber, Grade C.")
                tl = "Grade A: 0–30d • Grade B: 31–90d • Grade C: 91+d (Shelf Life: 100d)"
            elif "maize" in c or "corn" in c:
                q = "Grade A" if diff <= 20 else ("Grade B" if diff <= 60 else "Grade C")
                desc = "Dry golden kernel, optimal moisture, Grade A." if q == "Grade A" else ("Standard commercial dry grain, Grade B." if q == "Grade B" else "Weevil risk grain, Grade C.")
                tl = "Grade A: 0–20d • Grade B: 21–60d • Grade C: 61+d (Shelf Life: 75d)"
            elif "onion" in c:
                q = "Grade A" if diff <= 7 else ("Grade B" if diff <= 25 else "Grade C")
                desc = "Cured dry papery skins, tight closed neck, Grade A." if q == "Grade A" else ("Commercial sound bulb, Grade B." if q == "Grade B" else "Sprouting & neck rot risk, Grade C.")
                tl = "Grade A: 0–7d • Grade B: 8–25d • Grade C: 26+d (Shelf Life: 30d)"
            elif "chilli" in c or "mirchi" in c:
                q = "Grade A" if diff <= 2 else ("Grade B" if diff <= 5 else "Grade C")
                desc = "Crisp green pod, glossy shine, Grade A." if q == "Grade A" else ("Mild moisture loss, Grade B." if q == "Grade B" else "Shriveling & stem rot, Grade C.")
                tl = "Grade A: 0–2d • Grade B: 3–5d • Grade C: 6+d (Shelf Life: 6d)"
            else:
                q = "Grade A" if diff <= 1 else ("Grade B" if diff <= 3 else "Grade C")
                desc = "Firm skin, peak red luster, Grade A." if q == "Grade A" else ("Slight ambient softening, Grade B." if q == "Grade B" else "Soft rot hazard, Grade C.")
                tl = "Grade A: 0–1d • Grade B: 2–3d • Grade C: 4+d (Shelf Life: 4d)"
            return {
                "quality": q,
                "days_elapsed": diff,
                "status": q,
                "reason": f"Harvested {diff} days ago: {desc}",
                "timeline_summary": tl
            }

try:
    from services.voice_service import (
        generate_farmer_voice_script,
        generate_speech_audio_base64,
        generate_speech_audio_bytes,
        extract_parameters_with_llm_fallback,
        transcribe_audio_bytes,
        QuotaExhaustedError,
        build_webspeech_html,
    )
except ImportError:
    try:
        from voice_service import (
            generate_farmer_voice_script,
            generate_speech_audio_base64,
            generate_speech_audio_bytes,
            extract_parameters_with_llm_fallback,
            transcribe_audio_bytes,
            QuotaExhaustedError,
            build_webspeech_html,
        )
    except ImportError:
        class QuotaExhaustedError(Exception):
            pass
        def generate_farmer_voice_script(rec, lang="te"):
            return "Recommendation voice script"
        def generate_speech_audio_base64(script, lang="te"):
            return ""
        def generate_speech_audio_bytes(script, lang="te"):
            return b""
        def extract_parameters_with_llm_fallback(text, default_lang="te"):
            return {"crop": None, "quantity": None, "location": None, "language": default_lang}
        def transcribe_audio_bytes(audio_bytes, filename="voice.wav"):
            return ""

VOICE_MIC_DIR = os.path.join(ROOT_DIR, "frontend", "components", "voice_mic")
if os.path.exists(VOICE_MIC_DIR):
    voice_mic_component = components.declare_component("farmer_voice_mic", path=VOICE_MIC_DIR)
else:
    voice_mic_component = None

def build_webspeech_html(lang: str = "te") -> str:
    """
    Generates a standalone, zero-cost HTML5/JavaScript Web Speech API microphone widget.
    Natively recognizes spoken Indic languages (Telugu te-IN, Hindi hi-IN, English en-IN)
    in Chrome, Edge, and Android mobile browsers without requiring paid external API credits.
    """
    bcp47_map = {
        "te": ("te-IN", "🌾 తెలుగు (Telugu)", "🎙️ మాట్లాడండి (Tap to Speak in Telugu)", "💡 బటన్ నొక్కి మీ పంట, పరిమాణం, ఊరు మాట్లాడండి"),
        "hi": ("hi-IN", "🌾 हिन्दी (Hindi)", "🎙️ बोलिए (Tap to Speak in Hindi)", "💡 बटन दबाएं और फसल, मात्रा व मंडी का नाम बोलें"),
        "en": ("en-IN", "🌐 English (India)", "🎙️ Tap to Speak in English", "💡 Tap button to speak: crop, quantity & location"),
        "ta": ("ta-IN", "🌾 தமிழ் (Tamil)", "🎙️ பேசுங்கள் (Tap to Speak in Tamil)", "💡 பொத்தானைத் தட்டி பயிர், அளவு, ஊர் சொல்லுங்கள்"),
        "kn": ("kn-IN", "🌾 ಕನ್ನಡ (Kannada)", "🎙️ ಮಾತನಾಡಿ (Tap to Speak in Kannada)", "💡 ಬಟನ್ ಒತ್ತಿ ಬೆಳೆ, ಪ್ರಮಾಣ, ಊರು ಮಾತನಾಡಿ"),
        "mr": ("mr-IN", "🌾 मराठी (Marathi)", "🎙️ बोला (Tap to Speak in Marathi)", "💡 बटण दाबा आणि पीक, प्रमाण व गाव सांगा")
    }
    bcp_code, lang_display, speak_label, help_label = bcp47_map.get(
        lang,
        ("en-IN", "🌐 English", "🎙️ Tap to Speak in English", "💡 Tap button to speak: crop, quantity & location")
    )

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
  body {{ background: transparent; padding: 1px; margin: 0; overflow: hidden; }}
  .speech-card {{
    background: #ffffff;
    border: 1.5px solid #10b981;
    border-radius: 12px;
    padding: 12px 14px;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.08);
  }}
  .card-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
  }}
  .card-title {{
    font-size: 13px;
    font-weight: 700;
    color: #065f46;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .badge {{
    font-size: 11px;
    font-weight: 700;
    color: #047857;
    background: #dcfce7;
    padding: 2px 8px;
    border-radius: 12px;
    border: 1px solid #a7f3d0;
  }}
  .mic-btn {{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: #059669;
    color: white;
    border: none;
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 13.5px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 2px 6px rgba(5, 150, 105, 0.25);
    transition: all 0.2s ease;
  }}
  .mic-btn:hover {{ background: #047857; }}
  .mic-btn.recording {{
    background: #dc2626;
    box-shadow: 0 0 12px rgba(220, 38, 38, 0.5);
    animation: pulse 1.2s infinite;
  }}
  @keyframes pulse {{
    0% {{ transform: scale(1); opacity: 1; }}
    50% {{ transform: scale(1.02); opacity: 0.92; }}
    100% {{ transform: scale(1); opacity: 1; }}
  }}
  .status-text {{
    font-size: 11.5px;
    color: #64748b;
    margin-top: 6px;
    text-align: center;
    line-height: 1.35;
  }}
  .result-box {{
    display: none;
    margin-top: 8px;
    background: #f0fdf4;
    border: 1.5px solid #86efac;
    border-radius: 8px;
    padding: 8px 10px;
  }}
  .result-label {{
    font-size: 10.5px;
    font-weight: 700;
    color: #166534;
    text-transform: uppercase;
    margin-bottom: 2px;
  }}
  .result-content {{
    font-size: 13px;
    font-weight: 600;
    color: #0f172a;
    line-height: 1.35;
    word-break: break-word;
  }}
  .action-row {{
    display: flex;
    gap: 6px;
    margin-top: 6px;
  }}
  .btn-action {{
    flex: 1;
    background: #059669;
    color: white;
    border: none;
    padding: 6px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
  }}
  .btn-action:hover {{ background: #047857; }}
  .btn-copy {{
    background: #f1f5f9;
    color: #334155;
    border: 1px solid #cbd5e1;
    padding: 6px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
  }}
  .btn-copy:hover {{ background: #e2e8f0; }}
  .toast {{
    display: none;
    font-size: 11px;
    color: #059669;
    font-weight: 700;
    margin-top: 4px;
    text-align: center;
  }}
</style>
</head>
<body>
<div class="speech-card">
  <div class="card-top">
    <span class="card-title">
      🎙️ Live Browser Mic (Free)
    </span>
    <span class="badge">{lang_display}</span>
  </div>

  <button id="micBtn" class="mic-btn" onclick="toggleSpeech()">
    <span id="micIcon">🎙️</span>
    <span id="micText">{speak_label}</span>
  </button>

  <div id="statusText" class="status-text">
    {help_label}
  </div>

  <div id="resultBox" class="result-box">
    <div class="result-label">🗣️ Recognized Voice Query:</div>
    <div id="resultContent" class="result-content"></div>
    <div class="action-row">
      <button class="btn-action" onclick="sendToStreamlit()">🚀 Analyze Now</button>
      <button class="btn-copy" onclick="copyText()">📋 Copy</button>
    </div>
    <div id="toast" class="toast">✅ Copied to clipboard! Paste into box.</div>
  </div>
</div>

<script>
let recognition = null;
let isRecording = false;
let speechText = '';
const langCode = '{bcp_code}';

if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {{
  const SpeechConstructor = window.SpeechRecognition || window.webkitSpeechRecognition;
  recognition = new SpeechConstructor();
  recognition.lang = langCode;
  recognition.continuous = false;
  recognition.interimResults = true;

  recognition.onstart = function() {{
    isRecording = true;
    speechText = '';
    const btn = document.getElementById('micBtn');
    btn.classList.add('recording');
    document.getElementById('micIcon').textContent = '🔴';
    document.getElementById('micText').textContent = 'Listening... Speak now';
    document.getElementById('statusText').textContent = '🟢 Listening to your voice... Speak clearly.';
  }};

  recognition.onresult = function(event) {{
    let interim = '';
    for (let i = event.resultIndex; i < event.results.length; ++i) {{
      if (event.results[i].isFinal) {{
        speechText += event.results[i][0].transcript;
      }} else {{
        interim += event.results[i][0].transcript;
      }}
    }}
    const display = speechText || interim;
    if (display) {{
      document.getElementById('resultBox').style.display = 'block';
      document.getElementById('resultContent').textContent = display;
    }}
  }};

  recognition.onerror = function(event) {{
    console.warn('Speech recognition status:', event.error);
    stopRecording();
    document.getElementById('statusText').textContent = '⚠️ Mic notice: ' + event.error;
  }};

  recognition.onend = function() {{
    stopRecording();
    if (speechText) {{
      document.getElementById('statusText').textContent = '✅ Voice captured! Click "Analyze Now" above.';
      autoCopy(speechText);
    }}
  }};
}} else {{
  document.getElementById('micBtn').disabled = true;
  document.getElementById('micBtn').style.opacity = '0.6';
  document.getElementById('statusText').innerHTML = '⚠️ Browser live speech requires Google Chrome, Edge, or Android Chrome.';
}}

function stopRecording() {{
  isRecording = false;
  const btn = document.getElementById('micBtn');
  btn.classList.remove('recording');
  document.getElementById('micIcon').textContent = '🎙️';
  document.getElementById('micText').textContent = '{speak_label}';
}}

function toggleSpeech() {{
  if (!recognition) return;
  if (isRecording) {{
    recognition.stop();
    stopRecording();
  }} else {{
    speechText = '';
    try {{
      recognition.start();
    }} catch(e) {{
      console.warn(e);
    }}
  }}
}}

function autoCopy(text) {{
  if (navigator.clipboard) {{
    navigator.clipboard.writeText(text).catch(function(){{}});
  }}
}}

function sendToStreamlit() {{
  const text = (document.getElementById('resultContent').textContent || speechText).trim();
  if (!text) return;
  autoCopy(text);
  try {{
    window.top.location.href = window.top.location.pathname + '?voice_query=' + encodeURIComponent(text);
  }} catch (e1) {{
    try {{
      window.parent.location.href = window.parent.location.pathname + '?voice_query=' + encodeURIComponent(text);
    }} catch (e2) {{
      alert('Voice query copied to clipboard! Paste into the box below and click Analyze.');
    }}
  }}
}}

function copyText() {{
  const text = (document.getElementById('resultContent').textContent || speechText).trim();
  if (!text) return;
  if (navigator.clipboard) {{
    navigator.clipboard.writeText(text).then(function() {{
      const toast = document.getElementById('toast');
      toast.style.display = 'block';
      setTimeout(function() {{ toast.style.display = 'none'; }}, 3000);
    }});
  }}
}}
</script>
</body>
</html>"""





# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Farmer Market Intelligence",
    page_icon="🌾",
    layout="wide"
)


# ============================================================
# API CONFIGURATION
# ============================================================

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

# ============================================================
# FARMER PROFILE SESSION
# ============================================================

if "farmer_logged_in" not in st.session_state:
    st.session_state.farmer_logged_in = False

if "farmer_name" not in st.session_state:
    st.session_state.farmer_name = ""

if "farmer_phone" not in st.session_state:
    st.session_state.farmer_phone = ""

if "farmer_language" not in st.session_state:
    st.session_state.farmer_language = DEFAULT_LANGUAGE

if "farmer_otp_sent" not in st.session_state:
    st.session_state.farmer_otp_sent = False

if "farmer_otp_code" not in st.session_state:
    st.session_state.farmer_otp_code = ""

if "farmer_otp_timestamp" not in st.session_state:
    st.session_state.farmer_otp_timestamp = 0.0

if "farmer_temp_name" not in st.session_state:
    st.session_state.farmer_temp_name = ""

if "farmer_temp_phone" not in st.session_state:
    st.session_state.farmer_temp_phone = ""

if "farmer_sms_status" not in st.session_state:
    st.session_state.farmer_sms_status = {}

if "voice_detected_query" not in st.session_state:
    st.session_state.voice_detected_query = None

if "voice_parsed_details" not in st.session_state:
    st.session_state.voice_parsed_details = None

def apply_farmer_inputs(crop=None, quantity=None, location=None, harvest_date=None, price_date=None, trigger_analysis=True):
    """
    Stores farmer inputs in session state and triggers analysis run.
    Widget keys are updated prior to widget instantiation on rerun to avoid StreamlitWidgetAlreadyInstantiatedError.
    """
    if crop:
        st.session_state.app_crop = crop
    if quantity is not None:
        try:
            st.session_state.app_quantity = float(quantity)
        except (ValueError, TypeError):
            pass
    if location:
        st.session_state.app_location = str(location).strip()
    if harvest_date:
        if isinstance(harvest_date, str):
            try:
                harvest_date = datetime.date.fromisoformat(harvest_date)
            except Exception:
                pass
        if isinstance(harvest_date, datetime.date):
            st.session_state.app_harvest_date = harvest_date
    if price_date:
        if isinstance(price_date, str):
            try:
                price_date = datetime.date.fromisoformat(price_date)
            except Exception:
                pass
        if isinstance(price_date, datetime.date):
            st.session_state.app_price_date = price_date

    if trigger_analysis:
        st.session_state.trigger_preset_run = True


# Check for incoming speech recognition query from browser Web Speech API
try:
    voice_query_param = st.query_params.get("voice_query")
    if voice_query_param and str(voice_query_param).strip():
        cleaned_param = str(voice_query_param).strip()
        parsed = extract_parameters_with_llm_fallback(
            cleaned_param,
            default_lang=st.session_state.get("farmer_language", DEFAULT_LANGUAGE)
        )
        apply_farmer_inputs(
            crop=parsed.get("crop"),
            quantity=parsed.get("quantity"),
            location=parsed.get("location"),
            harvest_date=parsed.get("harvest_date"),
            price_date=parsed.get("price_date"),
            trigger_analysis=True
        )
        st.session_state.voice_detected_query = cleaned_param
        st.session_state.voice_parsed_details = parsed
        st.query_params.clear()
except Exception:
    pass



# ============================================================
# CUSTOM CSS
# ============================================================

# ============================================================
# ADAPTIVE SYSTEM DEFAULT THEME & RAZORPAY BUILDATHON STYLING
# ============================================================

st.markdown(
    """
    <style>
    /* CSS Variables for Agricultural SaaS Visual Identity */
    :root {
        --primary-forest: #123B2A;
        --secondary-green: #2E7D4F;
        --accent-light: #B7E4C7;
        --bg-warm: #F7F8F3;
        --card-bg: #FFFFFF;
        --border-card: #E5E7EB;
        --border-subtle: #D8E2DC;
        --text-forest: #123B2A;
        --text-charcoal: #2D3748;
        --text-muted: #64748B;
        --shadow-card: 0 4px 16px rgba(18, 59, 42, 0.06);
        --shadow-card-hover: 0 8px 24px rgba(18, 59, 42, 0.12);
        
        /* Razorpay compatibility bridge variables */
        --rzp-bg: #F7F8F3;
        --rzp-card-bg: #FFFFFF;
        --rzp-card-border: #E5E7EB;
        --rzp-card-hover-border: #2E7D4F;
        --rzp-text: #123B2A;
        --rzp-text-muted: #4A5568;
        --rzp-accent: #2E7D4F;
        --rzp-accent-amber: #D97706;
        --rzp-accent-rose: #E11D48;
        --rzp-card-shadow: 0 4px 16px rgba(18, 59, 42, 0.06);
        --rzp-card-hover-shadow: 0 8px 24px rgba(18, 59, 42, 0.12);
        --rzp-badge-bg: rgba(46, 125, 79, 0.10);
        --rzp-table-head-bg: #F1F6F3;
        --rzp-table-border: #E5E7EB;
        --rzp-table-hover: #F7FBF8;
        --rzp-active-row-bg: rgba(46, 125, 79, 0.09);
        --rzp-active-col-bg: rgba(46, 125, 79, 0.08);
    }

    /* Clean, Professional Dashboard Card & Metric Styles */
    div[data-testid="stMetric"] {
        background: #FFFFFF !important;
        border: 1px solid #E5E7EB !important;
        border-radius: 14px !important;
        padding: 14px 18px !important;
        box-shadow: 0 4px 16px rgba(18, 59, 42, 0.06) !important;
        transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
    }
    div[data-testid="stMetric"]:hover {
        border-color: #2E7D4F !important;
        box-shadow: 0 8px 24px rgba(18, 59, 42, 0.12) !important;
        transform: translateY(-2px);
    }
    div[data-testid="stMetric"] [data-testid="stMetricLabel"] {
        color: #4A5568 !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.2px;
    }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #123B2A !important;
        font-weight: 800 !important;
        font-size: 1.5rem !important;
    }
    div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
        font-weight: 600 !important;
        font-size: 0.82rem !important;
    }

    /* Primary CTA Buttons */
    button[kind="primary"], .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #123B2A 0%, #2E7D4F 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 14px rgba(18, 59, 42, 0.2) !important;
        transition: all 0.2s ease !important;
    }
    button[kind="primary"]:hover, .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #0d2b1f 0%, #24643f 100%) !important;
        box-shadow: 0 6px 20px rgba(18, 59, 42, 0.28) !important;
        transform: translateY(-1px);
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 2px solid #E5E7EB;
        background: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        color: #4A5568;
        border-radius: 8px 8px 0 0;
        padding: 10px 18px;
        background: transparent;
    }
    .stTabs [aria-selected="true"] {
        color: #123B2A !important;
        font-weight: 700 !important;
        border-bottom: 3px solid #2E7D4F !important;
        background: rgba(46, 125, 79, 0.06) !important;
    }

    /* Sleek Sidebar Navigation Radio Items */
    .st-key-app_main_navigation [role="radiogroup"] {
        gap: 6px;
        display: flex;
        flex-direction: column;
    }
    .st-key-app_main_navigation [role="radiogroup"] label {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 10px;
        padding: 8px 12px;
        transition: all 0.15s ease-in-out;
        cursor: pointer;
        width: 100%;
        margin-bottom: 2px;
    }
    .st-key-app_main_navigation [role="radiogroup"] label:hover {
        border-color: #2E7D4F;
        background: #F1F6F3;
        transform: translateX(2px);
    }
    .st-key-app_main_navigation [role="radiogroup"] label[data-checked="true"],
    .st-key-app_main_navigation [role="radiogroup"] label:has(input:checked) {
        background: rgba(46, 125, 79, 0.10) !important;
        border-color: #2E7D4F !important;
        font-weight: 700 !important;
        color: #123B2A !important;
        box-shadow: 0 2px 8px rgba(18, 59, 42, 0.08) !important;
    }

    /* Multi-Day Quality Degradation Matrix Table */
    .rzp-matrix-wrapper {
        overflow-x: auto;
        border-radius: 14px;
        border: 1px solid var(--rzp-card-border);
        margin: 16px 0;
        box-shadow: var(--rzp-card-shadow);
    }

    .rzp-matrix-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 13.5px;
        background: var(--rzp-card-bg);
    }

    .rzp-matrix-table th {
        padding: 12px 14px;
        font-weight: 700;
        text-align: center;
        border-bottom: 2px solid var(--rzp-table-border);
        color: var(--rzp-text);
        background: var(--rzp-table-head-bg);
        white-space: nowrap;
    }

    .rzp-matrix-table th.first-col {
        text-align: left;
        padding-left: 18px;
    }

    .rzp-matrix-table th.active-col-header {
        background: var(--rzp-active-col-bg);
        color: var(--rzp-accent);
        border-bottom: 2px solid var(--rzp-accent);
    }

    .rzp-matrix-table td {
        padding: 11px 12px;
        text-align: center;
        border-bottom: 1px solid var(--rzp-table-border);
        white-space: nowrap;
    }

    .rzp-matrix-table td.crop-name {
        text-align: left;
        padding-left: 18px;
        color: var(--rzp-text);
    }

    .rzp-matrix-table tr:hover td {
        background: var(--rzp-table-hover);
    }

    .rzp-matrix-table tr.active-crop-row td {
        background: var(--rzp-active-row-bg) !important;
    }

    .rzp-matrix-table td.active-cell-highlight {
        background: var(--rzp-active-col-bg) !important;
    }

    .rzp-matrix-table td.active-cell-highlight span {
        box-shadow: 0 0 14px var(--rzp-accent);
        border-width: 2px;
        transform: scale(1.08);
        display: inline-block;
    }

    .active-tag {
        display: block;
        font-size: 10px;
        font-weight: 700;
        color: var(--rzp-accent);
        letter-spacing: 0.5px;
        margin-top: 2px;
    }

    .selected-chip {
        font-size: 10px;
        font-weight: 700;
        color: var(--rzp-accent);
        background: var(--rzp-badge-bg);
        padding: 2px 6px;
        border-radius: 4px;
        margin-left: 4px;
    }

    .rzp-badge-grade-a {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 6px;
        background: rgba(46, 125, 79, 0.15);
        color: #123B2A;
        border: 1px solid rgba(46, 125, 79, 0.35);
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 0.3px;
    }

    .rzp-badge-grade-b {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 6px;
        background: rgba(245, 158, 11, 0.15);
        color: var(--rzp-accent-amber);
        border: 1px solid rgba(245, 158, 11, 0.35);
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 0.3px;
    }

    .rzp-badge-grade-c {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 6px;
        background: rgba(244, 63, 94, 0.15);
        color: var(--rzp-accent-rose);
        border: 1px solid rgba(244, 63, 94, 0.35);
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 0.3px;
    }

    /* Legacy compatibility classes */
    .main-title {
        font-size: 36px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 4px;
        color: var(--primary-forest);
    }
    .subtitle {
        text-align: center;
        font-size: 16px;
        margin-bottom: 24px;
        color: var(--text-muted);
    }
    .hero-box {
        padding: 22px 28px;
        border-radius: 18px;
        background: var(--card-bg);
        border: 1px solid var(--border-card);
        margin: 10px 0 24px 0;
        text-align: center;
        box-shadow: var(--shadow-card);
    }
    </style>
    """,
    unsafe_allow_html=True
)


def render_degradation_matrix_html(active_crop: str = "Tomato", days_elapsed: int = 0) -> str:
    """
    Renders the interactive Multi-Day Quality Degradation Matrix table matching the user's photo.
    Dynamically highlights the active crop row and current elapsed days column with glowing badges.
    """
    crops = ["Tomato", "Chilli", "Onion", "Maize", "Cotton", "Rice"]
    bracket_labels = ["0 Days", "2 Days", "5 Days", "11 Days", "25 Days", "70 Days", "120 Days"]
    
    # Identify active column bracket
    if days_elapsed <= 0:
        active_col = 0
    elif days_elapsed <= 2:
        active_col = 1
    elif days_elapsed <= 5:
        active_col = 2
    elif days_elapsed <= 11:
        active_col = 3
    elif days_elapsed <= 25:
        active_col = 4
    elif days_elapsed <= 70:
        active_col = 5
    else:
        active_col = 6

    matrix = {
        "Tomato": ["Grade A", "Grade B", "Grade C", "Grade C", "Grade C", "Grade C", "Grade C"],
        "Chilli": ["Grade A", "Grade A", "Grade B", "Grade C", "Grade C", "Grade C", "Grade C"],
        "Onion":  ["Grade A", "Grade A", "Grade A", "Grade B", "Grade B", "Grade C", "Grade C"],
        "Maize":  ["Grade A", "Grade A", "Grade A", "Grade A", "Grade B", "Grade C", "Grade C"],
        "Cotton": ["Grade A", "Grade A", "Grade A", "Grade A", "Grade A", "Grade B", "Grade C"],
        "Rice":   ["Grade A", "Grade A", "Grade A", "Grade A", "Grade A", "Grade B", "Grade B"]
    }

    # Normalize active_crop safely to handle None, empty strings, etc.
    active_crop_clean = (active_crop or "").strip()

    # If active crop is an expanded crop not in base 6, dynamically evaluate its degradation curve
    active_canonical = next((c for c in matrix.keys() if active_crop_clean and c.lower() == active_crop_clean.lower()), None)
    if not active_canonical and active_crop_clean:
        crops.append(active_crop_clean)
        ref_today = datetime.date.today()
        bracket_days = [0, 2, 5, 11, 25, 70, 120]
        matrix[active_crop_clean] = [
            evaluate_crop_quality_from_harvest_date(
                active_crop_clean,
                ref_today - datetime.timedelta(days=d),
                ref_today
            )["quality"]
            for d in bracket_days
        ]

    html = ['<div class="rzp-matrix-wrapper">']
    html.append('<table class="rzp-matrix-table">')
    html.append('<thead><tr><th class="first-col">Crop</th>')
    for i, label in enumerate(bracket_labels):
        if i == active_col and active_crop_clean:
            html.append(f'<th class="active-col-header">{label} <span class="active-tag">📍 Your Age (~{days_elapsed}d)</span></th>')
        else:
            html.append(f'<th>{label}</th>')
    html.append('</tr></thead><tbody>')

    for c in crops:
        is_active_crop = bool(active_crop_clean and c.lower() == active_crop_clean.lower())
        row_cls = ' class="active-crop-row"' if is_active_crop else ''
        crop_display = f'⭐ <strong>{c}</strong> <span class="selected-chip">Selected</span>' if is_active_crop else f'<strong>{c}</strong>'
        html.append(f'<tr{row_cls}>')
        html.append(f'<td class="crop-name">{crop_display}</td>')

        for col_idx, grade in enumerate(matrix[c]):
            badge_cls = "rzp-badge-grade-a" if grade == "Grade A" else ("rzp-badge-grade-b" if grade == "Grade B" else "rzp-badge-grade-c")
            is_active_cell = (is_active_crop and col_idx == active_col)
            cell_cls = ' class="active-cell-highlight"' if is_active_cell else ''
            html.append(f'<td{cell_cls}><span class="{badge_cls}">{grade}</span></td>')

        html.append('</tr>')

    html.append('</tbody></table></div>')
    return "".join(html)


def render_historical_price_trend_chart(history_data, lang):
    """
    Renders the exact Historical Market Price Trend multi-line chart
    matching the user's reference image:
    - Average Price (Blue: #2563eb)
    - Maximum Price (Light Blue: #60a5fa)
    - Minimum Price (Red: #ef4444)
    """
    if not history_data:
        st.warning(t("tab1_no_data", lang))
        return

    history = history_data.get("history", [])
    if not history:
        st.warning(t("tab1_no_data", lang))
        return

    history_df = pd.DataFrame(history)
    history_df["date"] = pd.to_datetime(history_df["date"])
    history_df = history_df.sort_values("date").set_index("date")

    col_avg = t("lbl_avg_price", lang)
    col_max = t("lbl_max_price", lang)
    col_min = t("lbl_min_price", lang)

    chart_data = history_df[
        [
            "average_price",
            "maximum_price",
            "minimum_price"
        ]
    ].copy()

    chart_data.columns = [col_avg, col_max, col_min]

    st.line_chart(
        chart_data,
        color=["#2E7D4F", "#123B2A", "#D97706"],
        use_container_width=True
    )

    st.caption(t("tab3_caption", lang))


def render_market_price_altair_chart(df: pd.DataFrame, lang: str = "en"):
    """
    Renders an Altair bar chart comparing mandi prices in ₹/kg.
    Highlights the best available price in vibrant fresh green (#2E7D4F) with soft rounded tops.
    """
    if df.empty or "market" not in df.columns or "price_per_kg" not in df.columns:
        return
    chart_df = df.copy()
    max_price = chart_df["price_per_kg"].max()
    chart_df["is_highest"] = (chart_df["price_per_kg"] == max_price)
    
    chart = alt.Chart(chart_df).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X('market:N', title=t('col_market', lang), sort='-y', axis=alt.Axis(labelAngle=-25, labelColor='#123B2A', titleColor='#123B2A', labelFontSize=12)),
        y=alt.Y('price_per_kg:Q', title=t('col_price', lang) + ' (₹/kg)', axis=alt.Axis(labelColor='#123B2A', titleColor='#123B2A')),
        color=alt.condition(
            alt.datum.is_highest,
            alt.value('#2E7D4F'),  # Fresh Green for highest price
            alt.value('#A7D7C5')   # Light green for other mandis
        ),
        tooltip=[
            alt.Tooltip('market:N', title=t('col_market', lang)),
            alt.Tooltip('price_per_kg:Q', title=t('col_price', lang) + ' (₹/kg)', format='.2f'),
            alt.Tooltip('location:N', title=t('col_location', lang))
        ]
    ).properties(
        height=320
    ).configure_view(
        strokeWidth=0
    ).configure_axis(
        gridColor='#E5E7EB',
        domainColor='#E5E7EB'
    )
    st.altair_chart(chart, use_container_width=True)


def render_decision_scores_altair_chart(sell_score: float, wait_score: float, lang: str = "en"):
    """
    Renders an Altair horizontal comparison bar chart of Sell Now vs Wait decision-support scores.
    """
    score_data = pd.DataFrame({
        'Option': [t('lbl_sell_score', lang), t('lbl_wait_score', lang)],
        'Score': [sell_score, wait_score],
        'Color': ['#2E7D4F' if sell_score >= wait_score else '#A7D7C5',
                  '#D97706' if wait_score > sell_score else '#FDE68A']
    })
    chart = alt.Chart(score_data).mark_bar(cornerRadiusTopRight=8, cornerRadiusBottomRight=8).encode(
        y=alt.Y('Option:N', title=None, axis=alt.Axis(labelFontSize=13, labelFontWeight='bold', labelColor='#123B2A')),
        x=alt.X('Score:Q', title='Score (%)', scale=alt.Scale(domain=[0, 100]), axis=alt.Axis(labelColor='#123B2A', titleColor='#123B2A')),
        color=alt.Color('Color:N', scale=None),
        tooltip=[
            alt.Tooltip('Option:N', title='Action'),
            alt.Tooltip('Score:Q', title='Score (%)', format='.0f')
        ]
    ).properties(
        height=130
    ).configure_view(
        strokeWidth=0
    ).configure_axis(
        gridColor='#E5E7EB'
    )
    st.altair_chart(chart, use_container_width=True)


def render_net_profit_altair_chart(profit_df: pd.DataFrame, lang: str = "en"):
    """
    Renders an Altair bar chart comparing net profit across mandis in ₹.
    Highlights the highest net profit mandi in vibrant fresh green (#2E7D4F).
    """
    if profit_df.empty or "market" not in profit_df.columns or "net_profit" not in profit_df.columns:
        return
    chart_df = profit_df.copy()
    max_profit = chart_df["net_profit"].max()
    chart_df["is_highest"] = (chart_df["net_profit"] == max_profit)
    chart = alt.Chart(chart_df).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
        x=alt.X('market:N', title=t('col_market', lang), sort='-y', axis=alt.Axis(labelAngle=-25, labelColor='#123B2A', titleColor='#123B2A', labelFontSize=12)),
        y=alt.Y('net_profit:Q', title=t('col_net_profit', lang) + ' (₹)', axis=alt.Axis(labelColor='#123B2A', titleColor='#123B2A')),
        color=alt.condition(
            alt.datum.is_highest,
            alt.value('#2E7D4F'),
            alt.value('#A7D7C5')
        ),
        tooltip=[
            alt.Tooltip('market:N', title=t('col_market', lang)),
            alt.Tooltip('net_profit:Q', title=t('col_net_profit', lang) + ' (₹)', format=',.2f'),
            alt.Tooltip('price_per_kg:Q', title=t('col_price', lang) + ' (₹/kg)', format='.2f')
        ]
    ).properties(
        height=320
    ).configure_view(
        strokeWidth=0
    ).configure_axis(
        gridColor='#E5E7EB',
        domainColor='#E5E7EB'
    )
    st.altair_chart(chart, use_container_width=True)


# ============================================================
# FARMER PROFILE / LOGIN
# ============================================================

if not st.session_state.farmer_logged_in:
    current_lang = st.session_state.farmer_language

    st.markdown(
        f"""
        <div class="hero-box">
            <h3>{t('login_hero_title', current_lang)}</h3>
            <p>{t('login_hero_desc', current_lang)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    login_col1, login_col2, login_col3 = st.columns([1, 2, 1])

    with login_col2:
        # Language Selector Bar
        st.markdown(
            f"""
            <div style="background: rgba(34, 197, 94, 0.08); padding: 10px 14px; border-radius: 12px; border: 1px solid rgba(34, 197, 94, 0.3); margin-bottom: 12px;">
                <span style="font-weight: 600; font-size: 14px;">🌐 {t('choose_language', current_lang)}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        lang_options = list(SUPPORTED_LANGUAGES.keys())
        current_idx = lang_options.index(current_lang) if current_lang in lang_options else 0

        selected_lang = st.selectbox(
            label="Language / భాష / भाषा",
            options=lang_options,
            format_func=lambda code: SUPPORTED_LANGUAGES[code],
            index=current_idx,
            label_visibility="collapsed",
            key="login_language_select"
        )

        if selected_lang != st.session_state.farmer_language:
            st.session_state.farmer_language = selected_lang
            st.rerun()

        if not st.session_state.farmer_otp_sent:
            # INSTANT DEMO ACCESS CARDS
            st.markdown(
                f"""
                <div style="background: rgba(16, 185, 129, 0.08);
                            border: 1.5px solid rgba(16, 185, 129, 0.35);
                            border-radius: 14px;
                            padding: 16px 18px;
                            margin-bottom: 16px;">
                    <div style="font-weight: 700; font-size: 15px; color: var(--rzp-accent); margin-bottom: 4px;">
                        {t('quick_start_demo_title', current_lang)}
                    </div>
                    <div style="font-size: 13px; color: var(--rzp-text-muted); margin-bottom: 12px;">
                        {t('quick_start_demo_desc', current_lang)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            dcol1, dcol2, dcol3 = st.columns(3)
            with dcol1:
                if st.button(t("demo_farmer_1_name", current_lang), use_container_width=True, key="login_demo_1"):
                    st.session_state.farmer_logged_in = True
                    st.session_state.farmer_name = "Mallesh"
                    st.session_state.farmer_phone = "9876543210"
                    apply_farmer_inputs(crop="Rice", quantity=50.0, location="Jangaon", trigger_analysis=True)
                    st.rerun()

            with dcol2:
                if st.button(t("demo_farmer_2_name", current_lang), use_container_width=True, key="login_demo_2"):
                    st.session_state.farmer_logged_in = True
                    st.session_state.farmer_name = "Ramulu"
                    st.session_state.farmer_phone = "9848012345"
                    apply_farmer_inputs(crop="Tomato", quantity=1200.0, location="Shamshabad", trigger_analysis=True)
                    st.rerun()

            with dcol3:
                if st.button(t("demo_farmer_3_name", current_lang), use_container_width=True, key="login_demo_3"):
                    st.session_state.farmer_logged_in = True
                    st.session_state.farmer_name = "Venkat"
                    st.session_state.farmer_phone = "9988776655"
                    apply_farmer_inputs(crop="Onion", quantity=300.0, location="Bhongir", trigger_analysis=True)
                    st.rerun()

            st.markdown(
                f"""
                <div style="display: flex; align-items: center; margin: 18px 0; color: var(--rzp-text-muted); font-size: 12px;">
                    <div style="flex: 1; height: 1px; background: var(--rzp-card-border);"></div>
                    <span style="padding: 0 10px; font-weight: 700; letter-spacing: 0.5px;">OR LOGIN WITH MOBILE OTP</span>
                    <div style="flex: 1; height: 1px; background: var(--rzp-card-border);"></div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # STEP 1: Enter Farmer Name & Mobile Number
            st.subheader(t("login_box_title", current_lang))

            farmer_name_input = st.text_input(
                t("farmer_name_label", current_lang),
                placeholder=t("farmer_name_placeholder", current_lang),
                value=st.session_state.farmer_temp_name or st.session_state.farmer_name
            )

            farmer_phone_input = st.text_input(
                t("farmer_phone_label", current_lang),
                placeholder=t("farmer_phone_placeholder", current_lang),
                help=t("farmer_phone_help", current_lang),
                max_chars=10,
                value=st.session_state.farmer_temp_phone or st.session_state.farmer_phone
            )

            if st.button(t("send_otp_btn", current_lang), use_container_width=True, type="primary"):
                if not farmer_name_input.strip():
                    st.error(t("err_name_required", current_lang))
                elif (
                    not farmer_phone_input.isdigit()
                    or len(farmer_phone_input) != 10
                ):
                    st.error(t("err_phone_invalid", current_lang))
                else:
                    otp_code = str(secrets.randbelow(900000) + 100000)
                    st.session_state.farmer_otp_code = otp_code
                    st.session_state.farmer_otp_timestamp = time.time()
                    st.session_state.farmer_temp_name = farmer_name_input.strip()
                    st.session_state.farmer_temp_phone = farmer_phone_input.strip()
                    st.session_state.farmer_otp_sent = True
                    # Dispatch SMS notification
                    sms_result = send_otp_sms(farmer_phone_input.strip(), otp_code)
                    st.session_state.farmer_sms_status = sms_result
                    st.rerun()

            # Farmer Benefits Box
            st.markdown(
                f"""
                <div style="margin-top: 24px; padding: 14px 18px; background-color: rgba(255, 255, 255, 0.03); border-radius: 12px; border: 1px dashed rgba(128, 128, 128, 0.35);">
                    <div style="font-weight: 600; font-size: 14px; margin-bottom: 8px;">{t('benefits_title', current_lang)}</div>
                    <div style="font-size: 13px; margin-bottom: 5px; opacity: 0.9;">{t('benefit_1', current_lang)}</div>
                    <div style="font-size: 13px; margin-bottom: 5px; opacity: 0.9;">{t('benefit_2', current_lang)}</div>
                    <div style="font-size: 13px; opacity: 0.9;">{t('benefit_3', current_lang)}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            # STEP 2: Mobile OTP Verification
            st.subheader(t("otp_box_title", current_lang))

            st.info(t("otp_sent_to", current_lang, phone=st.session_state.farmer_temp_phone))

            # SMS Notification Sent Notice - NO OTP IS DISPLAYED ON SCREEN
            st.markdown(
                f"""
                <div style="background: rgba(34, 197, 94, 0.08);
                            border: 1px solid rgba(34, 197, 94, 0.35);
                            border-radius: 12px;
                            padding: 16px 18px;
                            margin: 12px 0 18px 0;">
                    <div style="font-size: 15px; font-weight: 700; color: #22c55e; margin-bottom: 4px;">
                        📲 {t('sms_notif_card_title', current_lang)}
                    </div>
                    <div style="font-size: 13px; opacity: 0.9;">
                        {t('otp_check_phone_notice', current_lang)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            entered_otp = st.text_input(
                t("otp_label", current_lang),
                placeholder=t("otp_placeholder", current_lang),
                max_chars=6,
                key="farmer_entered_otp"
            )

            verify_col, change_col = st.columns([1, 1])
            with verify_col:
                if st.button(t("verify_otp_btn", current_lang), use_container_width=True, type="primary"):
                    entered_clean = entered_otp.strip()
                    if time.time() - st.session_state.farmer_otp_timestamp > 300:
                        st.error(t("err_otp_expired", current_lang))
                    elif not entered_clean:
                        st.error(t("err_otp_required", current_lang))
                    elif len(entered_clean) != 6 or not entered_clean.isdigit() or entered_clean != st.session_state.farmer_otp_code:
                        st.error(t("err_otp_invalid", current_lang))
                    else:
                        st.session_state.farmer_logged_in = True
                        st.session_state.farmer_name = st.session_state.farmer_temp_name
                        st.session_state.farmer_phone = st.session_state.farmer_temp_phone
                        st.session_state.farmer_otp_sent = False
                        st.session_state.farmer_otp_code = ""
                        st.session_state.farmer_otp_timestamp = 0.0
                        st.session_state.farmer_sms_status = {}
                        st.rerun()

            with change_col:
                if st.button(t("change_phone_btn", current_lang), use_container_width=True):
                    st.session_state.farmer_otp_sent = False
                    st.session_state.farmer_otp_code = ""
                    st.session_state.farmer_sms_status = {}
                    st.rerun()

            if st.button(t("resend_otp_btn", current_lang), use_container_width=True):
                new_otp = str(secrets.randbelow(900000) + 100000)
                st.session_state.farmer_otp_code = new_otp
                st.session_state.farmer_otp_timestamp = time.time()
                sms_result = send_otp_sms(st.session_state.farmer_temp_phone, new_otp)
                st.session_state.farmer_sms_status = sms_result
                st.toast(t("sms_dispatched_toast", current_lang, phone=st.session_state.farmer_temp_phone))
                st.rerun()

            # SMS Gateway Status & Testing Helper
            sms_status = st.session_state.get("farmer_sms_status", {})
            provider = sms_status.get("provider")

            if provider == "fast2sms_pending_kyc":
                st.warning(
                    f"⚠️ **Fast2SMS Key Connected — One-Time Verification Needed**\n\n"
                    f"Your API key was detected! Fast2SMS returned: *\"{sms_status.get('message')}\"*\n\n"
                    "Indian telecom rules (TRAI) require completing a one-time verification in the Fast2SMS dashboard (under *Dev API -> OTP Message*) before live cellular SMS can be sent.\n\n"
                    "👉 **You can test the entire app right now using the instant buttons below:**"
                )

                col_test1, col_test2 = st.columns([1, 1])
                with col_test1:
                    if st.button("🔑 Show Code for Testing", use_container_width=True):
                        st.info(f"👉 Current Verification Code: **{st.session_state.farmer_otp_code}**")
                with col_test2:
                    if st.button("⚡ Quick Fill & Continue", use_container_width=True):
                        st.session_state.farmer_logged_in = True
                        st.session_state.farmer_name = st.session_state.farmer_temp_name
                        st.session_state.farmer_phone = st.session_state.farmer_temp_phone
                        st.session_state.farmer_otp_sent = False
                        st.session_state.farmer_otp_code = ""
                        st.session_state.farmer_otp_timestamp = 0.0
                        st.session_state.farmer_sms_status = {}
                        st.rerun()

            elif provider == "unconfigured":
                st.warning(
                    f"⚠️ **SMS Gateway Not Connected Yet**\n\n"
                    "Telecommunication networks (Airtel, Jio, Vi) require an SMS Gateway API key to transmit SMS messages to physical mobile phones. "
                    "Since no SMS Gateway key is set in `.env` yet, messages cannot reach mobile devices automatically."
                )

                col_test1, col_test2 = st.columns([1, 1])
                with col_test1:
                    if st.button("🔑 Show Code for Testing", use_container_width=True):
                        st.info(f"👉 Current Verification Code: **{st.session_state.farmer_otp_code}**")
                with col_test2:
                    if st.button("⚡ Quick Fill & Continue", use_container_width=True):
                        st.session_state.farmer_logged_in = True
                        st.session_state.farmer_name = st.session_state.farmer_temp_name
                        st.session_state.farmer_phone = st.session_state.farmer_temp_phone
                        st.session_state.farmer_otp_sent = False
                        st.session_state.farmer_otp_code = ""
                        st.session_state.farmer_otp_timestamp = 0.0
                        st.session_state.farmer_sms_status = {}
                        st.rerun()

            elif sms_status.get("success"):
                st.success(f"✅ Live SMS notification transmitted to +91 {st.session_state.farmer_temp_phone}!")

    st.stop()


# ============================================================
# API HELPER (Defined first so available everywhere)
# ============================================================

def get_api_data(endpoint, params=None):
    try:
        response = requests.get(
            f"{API_URL}{endpoint}",
            params=params,
            timeout=15
        )
        if response.status_code == 200:
            return response.json()
        st.error(f"❌ API Error: {response.status_code}")
        st.code(response.text, language="json")
        return None
    except requests.exceptions.ConnectionError:
        st.error(
            "❌ Cannot connect to FastAPI.\n\n"
            "Please start the backend using:\n\n"
            "`uvicorn backend.main:app --reload`"
        )
        return None
    except requests.exceptions.Timeout:
        st.error("⏱️ Backend request timed out.")
        return None
    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")
        return None


# ============================================================
# DASHBOARD TOP BAR & PROFESSIONAL HEADER
# ============================================================

lang = st.session_state.farmer_language

st.markdown(
    f"""
    <div style="background: var(--card-bg);
                border: 1px solid var(--border-card);
                border-radius: 14px;
                padding: 14px 22px;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                box-shadow: var(--shadow-card);
                gap: 14px;
                flex-wrap: wrap;">
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 28px; line-height: 1;">🌱</span>
            <div>
                <div style="font-weight: 800; font-size: 18px; color: var(--primary-forest); letter-spacing: -0.2px;">
                    Farmer Market Intelligence
                </div>
                <div style="font-size: 13px; color: var(--text-muted); font-weight: 500;">
                    {t("app_subtitle_redesign", lang)}
                </div>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
            <div style="display: inline-flex; align-items: center; gap: 6px; font-size: 12.5px; font-weight: 600; color: #2E7D4F; background: rgba(46, 125, 79, 0.10); padding: 5px 12px; border-radius: 20px; border: 1px solid rgba(46, 125, 79, 0.25);">
                <span style="width: 7px; height: 7px; border-radius: 50%; background: #2E7D4F; display: inline-block;"></span>
                <span>{t("feed_live_indicator", lang)} • Today</span>
            </div>
            <div style="font-size: 13px; font-weight: 600; color: var(--primary-forest); padding: 5px 12px; background: #F1F6F3; border-radius: 8px; border: 1px solid var(--border-card);">
                👨‍🌾 {st.session_state.farmer_name}
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR - CLEAN NAVIGATION & SETTINGS
# ============================================================

st.sidebar.markdown(
    f"""
    <div style="padding: 10px 4px 14px 4px; border-bottom: 1px solid var(--border-card); margin-bottom: 12px;">
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 22px;">🌱</span>
            <span style="font-weight: 800; font-size: 16px; color: var(--primary-forest);">Farmer Market AI</span>
        </div>
        <div style="font-size: 11.5px; color: var(--text-muted); margin-top: 2px;">AgTech Intelligence Platform</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Farmer Profile Card in Sidebar
st.sidebar.markdown(
    f"""
    <div style="background: #FFFFFF; border: 1px solid var(--border-card); border-radius: 10px; padding: 12px; margin-bottom: 12px; box-shadow: 0 2px 6px rgba(18, 59, 42, 0.04);">
        <div style="font-weight: 700; font-size: 13.5px; color: var(--primary-forest);">👨‍🌾 {st.session_state.farmer_name}</div>
        <div style="font-size: 12px; color: var(--text-muted); margin-top: 2px;">📱 +91 {st.session_state.farmer_phone}</div>
        <div style="display: inline-block; font-size: 10.5px; font-weight: 700; color: #2E7D4F; background: rgba(46, 125, 79, 0.12); padding: 2px 8px; border-radius: 12px; margin-top: 6px;">Verified Farmer</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Language selector in Sidebar
sidebar_lang_options = list(SUPPORTED_LANGUAGES.keys())
sidebar_current_idx = sidebar_lang_options.index(lang) if lang in sidebar_lang_options else 0
chosen_sidebar_lang = st.sidebar.selectbox(
    t("sidebar_language", lang),
    options=sidebar_lang_options,
    format_func=lambda code: SUPPORTED_LANGUAGES[code],
    index=sidebar_current_idx,
    key="sidebar_language_select"
)
if chosen_sidebar_lang != st.session_state.farmer_language:
    st.session_state.farmer_language = chosen_sidebar_lang
    st.rerun()

st.sidebar.markdown("---")

# Navigation Sections matching the 5 Core Intelligence Tabs
nav_options = [
    t("tab_market_comparison", lang),
    t("tab_profit_analysis", lang),
    t("tab_price_trends", lang),
    t("tab_freshness_matrix", lang),
    t("tab_ai_advisor", lang)
]
st.sidebar.markdown(f"**🧭 {t('platform_navigation', lang)}**")
active_nav = st.sidebar.radio(
    t("platform_navigation", lang),
    nav_options,
    index=0,
    key="app_main_navigation",
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.caption("⚙️ **Analysis Settings & Tools**")

radius_km = st.sidebar.slider(
    t("slider_radius", lang),
    min_value=10,
    max_value=60,
    value=st.session_state.get("app_radius_km", 45),
    step=5,
    key="sidebar_radius_slider"
)
st.session_state["app_radius_km"] = radius_km

if st.sidebar.button(t("btn_sync_live", lang), use_container_width=True):
    with st.spinner(t("analyzing_spinner", lang)):
        try:
            sync_res = requests.post(
                f"{API_URL}/sync-live-data",
                params={
                    "crop": st.session_state.get("app_crop", "Rice"),
                    "location": st.session_state.get("app_location", "Jangaon"),
                    "date": str(datetime.date.today())
                },
                timeout=12
            )
            if sync_res.status_code == 200:
                st.sidebar.success(t("sync_success", lang, date=str(datetime.date.today())))
                time.sleep(0.5)
                st.rerun()
            else:
                st.sidebar.error(f"Sync failed: {sync_res.status_code}")
        except Exception as err:
            st.sidebar.error(f"Connection error: {err}")

if st.session_state.get("current_analysis"):
    if st.sidebar.button(f"🔄 {t('btn_new_analysis', lang)}", use_container_width=True):
        st.session_state["current_analysis"] = None
        st.rerun()

if st.sidebar.button(t("sidebar_logout", lang), use_container_width=True):
    st.session_state.farmer_logged_in = False
    st.session_state.farmer_name = ""
    st.session_state.farmer_phone = ""
    st.session_state.farmer_otp_sent = False
    st.session_state.farmer_otp_code = ""
    st.session_state.farmer_otp_timestamp = 0.0
    st.session_state.farmer_temp_name = ""
    st.session_state.farmer_temp_phone = ""
    st.session_state["current_analysis"] = None
    st.rerun()

# ============================================================
# MAIN PAGE: WELCOME SECTION & FARMER INPUT CARD
# ============================================================

# Crop values initialization
if st.session_state.get("trigger_preset_run"):
    if st.session_state.get("app_crop"):
        st.session_state["main_crop_picker"] = st.session_state["app_crop"]
        st.session_state["sidebar_crop_picker"] = st.session_state["app_crop"]
        st.session_state["main_crop_category_pills"] = "all"
    if st.session_state.get("app_quantity") is not None:
        try:
            st.session_state["main_qty_picker"] = float(st.session_state["app_quantity"])
            st.session_state["sidebar_qty_picker"] = float(st.session_state["app_quantity"])
        except (ValueError, TypeError):
            pass
    if st.session_state.get("app_location"):
        st.session_state["main_loc_picker"] = str(st.session_state["app_location"])
        st.session_state["sidebar_loc_picker"] = str(st.session_state["app_location"])
    if st.session_state.get("app_harvest_date"):
        st.session_state["main_harvest_date_picker"] = st.session_state["app_harvest_date"]
    if st.session_state.get("app_price_date"):
        st.session_state["main_price_date_picker"] = st.session_state["app_price_date"]

all_crops = list(CROPS_DISPLAY.keys())
default_crop = st.session_state.get("app_crop", None)
crop_list = all_crops
crop_idx = crop_list.index(default_crop) if (default_crop and default_crop in crop_list) else None

default_qty = st.session_state.get("app_quantity", None)
if default_qty is not None:
    try:
        default_qty = float(default_qty)
    except (ValueError, TypeError):
        default_qty = None
default_loc = st.session_state.get("app_location", "")
default_harvest_date = st.session_state.get("app_harvest_date", datetime.date.today())
default_price_date = st.session_state.get("app_price_date", datetime.date.today())

crop = default_crop
quantity = default_qty
location = default_loc
harvest_date = default_harvest_date
price_date = default_price_date
quality = "Grade A"
radius_km = st.session_state.get("app_radius_km", 45)
days_diff = 0
assessed_quality = "Grade A"
quality_reason = ""
timeline_summary = ""

analyze_button = False

# Render Welcome Banner & Farmer Input Card
has_analysis = bool(st.session_state.get("current_analysis"))

# Welcome section
st.markdown(
    f"""
    <div style="padding: 22px 26px;
                border-radius: 16px;
                background: #FFFFFF;
                border: 1px solid var(--border-card);
                margin-bottom: 22px;
                box-shadow: var(--shadow-card);">
        <h2 style="font-size: 24px; font-weight: 800; margin: 0 0 6px 0; color: var(--primary-forest);">
            {t('welcome_smart_decision', lang)}
        </h2>
        <p style="font-size: 14.5px; color: var(--text-muted); margin: 0 0 16px 0; line-height: 1.5;">
            {t('welcome_desc', lang)}
        </p>
        <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            <span style="font-size: 12px; font-weight: 600; color: var(--primary-forest); background: #F1F6F3; padding: 4px 10px; border-radius: 6px; border: 1px solid var(--border-card);">📍 GPS Verified Mandis</span>
            <span style="font-size: 12px; font-weight: 600; color: var(--primary-forest); background: #F1F6F3; padding: 4px 10px; border-radius: 6px; border: 1px solid var(--border-card);">⏱️ Loaded Heavy-Cargo Transit Model</span>
            <span style="font-size: 12px; font-weight: 600; color: var(--primary-forest); background: #F1F6F3; padding: 4px 10px; border-radius: 6px; border: 1px solid var(--border-card);">🌾 Harvest Freshness Grading</span>
            <span style="font-size: 12px; font-weight: 600; color: var(--primary-forest); background: #F1F6F3; padding: 4px 10px; border-radius: 6px; border: 1px solid var(--border-card);">🤖 AI Net Arbitrage Recommendation</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Farmer Input Card
input_container = st.expander("✏️ **" + t("crop_input_title", lang) + "**", expanded=(not has_analysis)) if has_analysis else st.container(border=True)
with input_container:
    if not has_analysis:
        st.markdown(f"<h3 style='margin: 0 0 4px 0; color: var(--primary-forest); font-weight: 800;'>🌾 {t('crop_input_title', lang)}</h3>", unsafe_allow_html=True)
        st.caption(t('crop_input_subtitle', lang))

    # Category Filter Pills for easily finding crops
    st.markdown(
        f"<div style='font-size: 13px; font-weight: 700; color: var(--primary-forest); margin: 4px 0 2px 0;'>"
        f"🏷️ {t('filter_by_category', lang)}:"
        f"</div>",
        unsafe_allow_html=True
    )
    selected_cat = st.pills(
        t("lbl_crop_category", lang),
        options=list(CROP_CATEGORIES.keys()),
        format_func=lambda k: CROP_CATEGORIES[k].get(lang, CROP_CATEGORIES[k].get("en", k)),
        default="all",
        label_visibility="collapsed",
        key="main_crop_category_pills"
    )

    if selected_cat and selected_cat != "all":
        crop_list = [c for c in CROPS_DISPLAY.keys() if CROP_CATEGORY_MAP.get(c) == selected_cat]
    else:
        crop_list = list(CROPS_DISPLAY.keys())

    default_crop = st.session_state.get("app_crop", None)
    if default_crop and default_crop not in crop_list:
        crop_list = [default_crop] + [c for c in crop_list if c != default_crop]

    crop_idx = crop_list.index(default_crop) if (default_crop and default_crop in crop_list) else None

    # Responsive Grid: Row 1
    r1_c1, r1_c2, r1_c3 = st.columns([1.2, 1.0, 1.2])
    with r1_c1:
        crop = st.selectbox(
            t("select_crop", lang),
            crop_list,
            index=crop_idx,
            placeholder=t("select_crop_placeholder", lang),
            format_func=lambda c: format_crop(c, lang),
            key="main_crop_picker"
        )
        if crop:
            st.session_state.app_crop = crop

    with r1_c2:
        quantity = st.number_input(
            t("quantity_kg", lang),
            min_value=1.0,
            value=default_qty,
            placeholder=t("quantity_placeholder", lang),
            step=10.0,
            key="main_qty_picker"
        )
        if quantity is not None:
            st.session_state.app_quantity = quantity

    with r1_c3:
        location = st.text_input(
            t("farmer_location", lang),
            value=default_loc,
            placeholder=t("farmer_loc_placeholder", lang),
            key="main_loc_picker"
        )
        if location:
            st.session_state.app_location = location

    # Responsive Grid: Row 2
    r2_c1, r2_c2, r2_c3 = st.columns([1.2, 1.0, 1.2])
    with r2_c1:
        harvest_date = st.date_input(
            t("expected_harvest", lang),
            value=default_harvest_date,
            help=t("harvest_date_help", lang),
            key="main_harvest_date_picker"
        )
        st.session_state.app_harvest_date = harvest_date

    with r2_c2:
        price_date = st.date_input(
            t("select_price_date", lang),
            value=default_price_date,
            key="main_price_date_picker"
        )
        st.session_state.app_price_date = price_date

    # Dynamic Quality Evaluation
    if crop:
        harvest_eval = evaluate_crop_quality_from_harvest_date(crop, harvest_date, price_date)
        assessed_quality = harvest_eval["quality"]
        days_diff = harvest_eval["days_elapsed"]
        quality_reason = harvest_eval["reason"]
        timeline_summary = harvest_eval.get("timeline_summary", "")

        quality_options = ["Grade A", "Grade B", "Grade C"]
        widget_key = f"widget_quality_{crop}"
        current_tracking_token = f"{crop}_{harvest_date}_{price_date}"
        last_token = st.session_state.get(f"last_eval_token_{crop}")

        if last_token != current_tracking_token:
            st.session_state[f"last_eval_token_{crop}"] = current_tracking_token
            st.session_state[widget_key] = assessed_quality

        if widget_key not in st.session_state:
            st.session_state[widget_key] = assessed_quality

        with r2_c3:
            quality = st.selectbox(
                t("crop_quality", lang),
                quality_options,
                key=widget_key,
                format_func=lambda q: format_quality(q, lang),
                help=t("crop_quality_help", lang)
            )

        # Dynamic Freshness Assessment Badge
        st.markdown(
            f"""
            <div style="background: #F1F6F3; border: 1px solid var(--border-card); border-radius: 8px; padding: 9px 14px; margin: 10px 0 14px 0; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
                <span style="font-size: 13px; color: var(--primary-forest); font-weight: 600;">
                    🌱 <strong>{t('lbl_auto_assessed', lang)}:</strong> {format_quality(assessed_quality, lang)} ({quality_reason})
                </span>
                <span style="font-size: 12px; color: var(--text-muted);">
                    ⏱️ {format_crop(crop, lang)} Freshness: {timeline_summary}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        with r2_c3:
            quality = st.selectbox(
                t("crop_quality", lang),
                ["Grade A", "Grade B", "Grade C"],
                index=0,
                key="widget_quality_unselected",
                format_func=lambda q: format_quality(q, lang),
                help=t("crop_quality_help", lang)
            )
        st.markdown(
            f"""
            <div style="background: #F8FAF9; border: 1px dashed var(--border-card); border-radius: 8px; padding: 9px 14px; margin: 10px 0 14px 0; color: var(--text-muted); font-size: 13px;">
                {t('lbl_freshness_pending', lang)}
            </div>
            """,
            unsafe_allow_html=True
        )

    # Direct Voice Assistant & Presets inside Card
    with st.expander(f"🎙️ {t('voice_assistant_title', lang)} ({SUPPORTED_LANGUAGES.get(lang, lang)} Voice Command)", expanded=False):
        if voice_mic_component:
            voice_payload = voice_mic_component(language=lang, key="main_farmer_voice_mic_widget")
            if isinstance(voice_payload, dict):
                v_text = voice_payload.get("text", "").strip()
                v_ts = voice_payload.get("timestamp", 0)
                if v_text and v_ts != st.session_state.get("last_processed_voice_ts"):
                    st.session_state.last_processed_voice_ts = v_ts
                    with st.spinner(f"🌾 AI is analyzing market prices for '{v_text}'..."):
                        # Automatic Language Detection
                        v_lang = voice_payload.get("detected_lang")
                        if not v_lang or v_lang not in SUPPORTED_LANGUAGES:
                            try:
                                from services.voice_service import detect_language
                                v_lang = detect_language(v_text)
                            except Exception:
                                v_lang = lang
                        if v_lang and v_lang in SUPPORTED_LANGUAGES:
                            st.session_state.farmer_language = v_lang
                            lang = v_lang
                        parsed = extract_parameters_with_llm_fallback(v_text, default_lang=lang)
                        apply_farmer_inputs(
                            crop=parsed.get("crop"),
                            quantity=parsed.get("quantity"),
                            location=parsed.get("location"),
                            harvest_date=parsed.get("harvest_date"),
                            price_date=parsed.get("price_date"),
                            trigger_analysis=True
                        )
                        st.session_state.voice_detected_query = v_text
                        st.session_state.voice_parsed_details = parsed
                        st.rerun()
        else:
            components.html(build_webspeech_html(lang), height=215)

        # 1-Tap Voice Samples
        st.caption(t('voice_quick_examples_title', lang))
        vc1, vc2, vc3 = st.columns(3)
        with vc1:
            if st.button(t("voice_sample_1", lang), use_container_width=True, key="main_vsample_1"):
                apply_farmer_inputs(crop="Rice", quantity=50.0, location="Jangaon", trigger_analysis=True)
                st.session_state.voice_detected_query = t("voice_sample_1", lang)
                st.rerun()
        with vc2:
            if st.button(t("voice_sample_2", lang), use_container_width=True, key="main_vsample_2"):
                apply_farmer_inputs(crop="Tomato", quantity=1200.0, location="Shamshabad", trigger_analysis=True)
                st.session_state.voice_detected_query = t("voice_sample_2", lang)
                st.rerun()
        with vc3:
            if st.button(t("voice_sample_3", lang), use_container_width=True, key="main_vsample_3"):
                apply_farmer_inputs(crop="Onion", quantity=300.0, location="Bhongir", trigger_analysis=True)
                st.session_state.voice_detected_query = t("voice_sample_3", lang)
                st.rerun()

    # Prominent Green Action Button: "Analyze Market"
    analyze_button = st.button(
        f"🚀 {t('btn_analyze_harvest', lang)}",
        type="primary",
        use_container_width=True,
        key="btn_analyze_my_harvest"
    )

if st.session_state.pop("trigger_preset_run", False):
    analyze_button = True


# ============================================================
# ANALYZE MARKET
# ============================================================

if analyze_button:

    # Robust Fallback to session state in case widget was desynchronized
    if not crop and st.session_state.get("app_crop"):
        crop = st.session_state.get("app_crop")
    if (quantity is None or quantity <= 0) and st.session_state.get("app_quantity"):
        try:
            quantity = float(st.session_state.get("app_quantity"))
        except (ValueError, TypeError):
            pass
    if (not location or not str(location).strip()) and st.session_state.get("app_location"):
        location = str(st.session_state.get("app_location")).strip()
    if not harvest_date and st.session_state.get("app_harvest_date"):
        harvest_date = st.session_state.get("app_harvest_date")
    if not price_date and st.session_state.get("app_price_date"):
        price_date = st.session_state.get("app_price_date")

    # Validate required user inputs before making API calls
    if not crop:
        st.warning(f"⚠️ {t('err_crop_required', lang)}")
        st.stop()
    if quantity is None or quantity <= 0:
        st.warning(f"⚠️ {t('err_qty_required', lang)}")
        st.stop()
    if not location or not str(location).strip():
        st.warning(f"⚠️ {t('err_loc_required', lang)}")
        st.stop()

    recommendation_data = None
    comparison_data = None
    history_data = None
    profit_data = None

    # --------------------------------------------------------
    # LOADING
    # --------------------------------------------------------

    with st.spinner(
        t("analyzing_spinner", lang)
    ):

        comparison_data = get_api_data(
            "/market-comparison",
            {
                "crop": crop,
                "location": location,
                "date": str(price_date),
                "radius_km": radius_km
            }
        )

        history_data = get_api_data(
            "/price-history",
            {
                "crop": crop,
                "location": location
            }
        )

        profit_data = get_api_data(
            "/net-profit",
            {
                "crop": crop,
                "location": location,
                "quantity": quantity,
                "date": str(price_date),
                "radius_km": radius_km
            }
        )

        # ----------------------------------------------------
        # ML PRICE PREDICTION DETAILS
        # ----------------------------------------------------

        prediction_data = get_api_data(
            "/price-prediction",
            {
                "crop": crop,
                "days": 3
            }
        )

        # ----------------------------------------------------
        # AI RECOMMENDATION
        # ----------------------------------------------------

        try:

            recommendation_response = requests.post(
                f"{API_URL}/ai-recommendation",

                json={
                    "crop": crop,
                    "location": location,
                    "quantity": quantity,
                    "quality": quality,
                    "harvest_date": str(harvest_date),
                    "price_date": str(price_date),
                    "radius_km": radius_km,
                    "detected_language": lang
                },

                timeout=30
            )

            if recommendation_response.status_code == 200:

                recommendation_data = (
                    recommendation_response.json()
                )

            else:

                st.error(
                    t("api_err_recommendation", lang)
                )

                st.code(
                    recommendation_response.text,
                    language="json"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                t("api_err_connection", lang)
            )

        except requests.exceptions.Timeout:

            st.error(
                t("api_err_timeout", lang)
            )

        except Exception as e:

            st.error(
                t("api_err_generic", lang, e=str(e))
            )


    # ========================================================
    # DISPLAY RESULTS
    # ========================================================

        if recommendation_data:
            st.session_state["current_analysis"] = {
                "recommendation_data": recommendation_data,
                "comparison_data": comparison_data,
                "history_data": history_data,
                "profit_data": profit_data,
                "prediction_data": prediction_data,
                "crop": crop,
                "quantity": quantity,
                "location": location,
                "harvest_date": harvest_date,
                "price_date": price_date,
                "quality": quality,
                "radius_km": radius_km,
                "days_diff": days_diff,
                "assessed_quality": assessed_quality,
                "quality_reason": quality_reason,
                "timeline_summary": timeline_summary
            }
            st.rerun()

# ============================================================
# DISPLAY PERSISTED ANALYSIS OR INITIAL SCREEN
# ============================================================

current_analysis = st.session_state.get("current_analysis")

if current_analysis and current_analysis.get("recommendation_data"):

    recommendation_data = current_analysis["recommendation_data"]
    comparison_data = current_analysis.get("comparison_data")
    history_data = current_analysis.get("history_data")
    profit_data = current_analysis.get("profit_data")
    prediction_data = current_analysis.get("prediction_data")

    crop = current_analysis.get("crop", default_crop)
    quantity = current_analysis.get("quantity", default_qty)
    location = current_analysis.get("location", default_loc)
    harvest_date = current_analysis.get("harvest_date", datetime.date.today())
    price_date = current_analysis.get("price_date", datetime.date.today())
    quality = current_analysis.get("quality", "Grade A")
    radius_km = current_analysis.get("radius_km", 45)
    days_diff = current_analysis.get("days_diff", 0)
    assessed_quality = current_analysis.get("assessed_quality", "Grade A")
    quality_reason = current_analysis.get("quality_reason", "")
    timeline_summary = current_analysis.get("timeline_summary", "")

    st.success(
        t("analysis_success", lang)
    )

    if recommendation_data:


        # ====================================================
        # EXTRACT DATA
        # ====================================================

        best_market = recommendation_data.get(
            "best_market",
            "N/A"
        )

        best_location = recommendation_data.get(
            "best_market_location",
            "N/A"
        )

        best_distance = float(
            recommendation_data.get(
                "best_market_distance",
                0
            )
        )

        current_price = float(
            recommendation_data.get(
                "best_price",
                0
            )
        )

        predicted_price = float(
            recommendation_data.get(
                "predicted_price",
                current_price
            )
        )

        sell_score = float(
            recommendation_data.get(
                "sell_now_score",
                0
            )
        )

        wait_score = float(
            recommendation_data.get(
                "wait_score",
                0
            )
        )

        decision = recommendation_data.get(
            "decision",
            "NEUTRAL"
        )

        quantity_value = float(
            recommendation_data.get(
                "quantity",
                quantity
            )
        )

        is_small_quantity = bool(recommendation_data.get("is_small_quantity", quantity_value <= 500.0))
        suggested_small_market = recommendation_data.get("suggested_small_market")
        small_batch_advisory = recommendation_data.get("small_batch_advisory", "")

        financial_info = recommendation_data.get(
            "financial_breakdown",
            {}
        )

        if financial_info and "predicted_gross_revenue" in financial_info:
            current_revenue = float(financial_info.get("gross_revenue", quantity_value * current_price))
            predicted_revenue = float(financial_info.get("predicted_gross_revenue", quantity_value * predicted_price))
            revenue_difference = float(financial_info.get("net_difference", predicted_revenue - current_revenue))
            future_salable_qty = float(financial_info.get("future_salable_quantity", quantity_value))
            spoilage_loss_kg = float(financial_info.get("spoilage_loss_kg", 0.0))
        else:
            current_revenue = (
                quantity_value *
                current_price
            )
            predicted_revenue = (
                quantity_value *
                predicted_price
            )
            revenue_difference = (
                predicted_revenue -
                current_revenue
            )
            future_salable_qty = quantity_value
            spoilage_loss_kg = 0.0

        google_rating = recommendation_data.get(
            "google_rating",
            "4.2 ⭐ (Google reviews)"
        )

        weather_info = recommendation_data.get(
            "weather",
            {}
        )

        spoilage_info = recommendation_data.get(
            "spoilage_risk",
            {}
        )

        # ----------------------------------------------------
        # ML PREDICTION DETAILS
        # ----------------------------------------------------

        if prediction_data and "error" not in prediction_data:

            ml_current_price = float(
                prediction_data.get(
                    "current_price",
                    current_price
                )
            )

            ml_predicted_price = float(
                prediction_data.get(
                    "predicted_price",
                    predicted_price
                )
            )

            prediction_lower = float(
                prediction_data.get(
                    "lower_bound",
                    ml_predicted_price
                )
            )

            prediction_upper = float(
                prediction_data.get(
                    "upper_bound",
                    ml_predicted_price
                )
            )

            prediction_confidence = prediction_data.get(
                "confidence",
                "Unavailable"
            )

            model_mae = float(
                prediction_data.get(
                    "mae",
                    0
                )
            )

            model_r2 = float(
                prediction_data.get(
                    "r2",
                    0
                )
            )

        else:

            ml_current_price = current_price
            ml_predicted_price = predicted_price
            prediction_lower = predicted_price
            prediction_upper = predicted_price
            prediction_confidence = "Unavailable"
            model_mae = 0
            model_r2 = 0

        # Derived prediction & presentation variables
        conf_key = f"confidence_{(prediction_confidence or 'unavailable').lower()}"
        localized_confidence = t(conf_key, lang)
        percentage_change = (
            ((predicted_price - current_price) / current_price) * 100
            if current_price > 0
            else 0
        )

        # Derived shelf-life & spoilage variables
        shelf_life_str = format_shelf_life(spoilage_info.get("shelf_life", "3-5 Days"), lang)
        safe_days = spoilage_info.get('safe_wait_days', 2)
        safe_window_str = t("lbl_safe_window", lang, days=safe_days)
        damage_risk_str = format_damage_risk(spoilage_info.get("damage_risk", "MODERATE"), lang)
        perish_str = format_perishability(spoilage_info.get("perishability", "Moderate"), lang)
        spoilage_rate_str = format_spoilage_rate(spoilage_info.get("spoilage_rate", "3-5% daily"), lang)
        verdict_raw = spoilage_info.get("holding_verdict", "Monitor closely")
        verdict_display = format_holding_verdict(verdict_raw, lang)
        crop_explanation = format_crop_explanation(crop, lang, spoilage_info.get('explanation', ''))

        # Weather & transit display strings
        weather_condition = format_weather_condition(weather_info.get("condition", "Partly Cloudy"), lang)
        weather_alert = format_weather_alert(weather_info.get("weather_alert", "Favorable"), lang)
        transit_advice = format_transit_advice(weather_info.get("transit_advice", "Favorable transit conditions."), lang)
        wind_speed = weather_info.get("wind_speed", "")
        weather_time = weather_info.get("last_updated", "")

        # Transport & transit time strings
        heavy_minutes = max(15, int((best_distance / 24.0) * 60) + 3)
        car_minutes = max(10, int((best_distance / 42.0) * 60))
        heavy_time_str = t("time_hours_mins", lang, h=heavy_minutes // 60, m=heavy_minutes % 60) if heavy_minutes >= 60 else t("time_mins", lang, m=heavy_minutes)
        car_time_str = t("time_hours_mins", lang, h=car_minutes // 60, m=car_minutes % 60) if car_minutes >= 60 else t("time_mins", lang, m=car_minutes)
        travel_time_str = f"{heavy_time_str} ({t('lbl_heavy_load', lang)})"
        est_transport_cost = best_distance * 2.5

        # Determine best profit
        if profit_data:
            best_profit = float(profit_data.get("best_net_profit", 0))
        else:
            best_profit = current_revenue

        price_difference = predicted_price - current_price
        price_diff_label = f"{price_difference:+,.2f} ₹/kg 3d" if price_difference != 0 else "Stable"

        transport_charges = float(financial_info.get("transport_charges", best_distance * 2.5))
        total_deductions = float(financial_info.get("total_deductions", transport_charges + quantity_value * 0.5))

        # ====================================================
        # TIER 1: 4 MARKET OVERVIEW KPIS
        # ====================================================
        st.markdown(
            f"""
            <div style="margin-top: 4px; margin-bottom: 12px;">
                <h3 style="margin: 0; color: var(--primary-forest); font-weight: 800; font-size: 20px;">
                    📊 {t('glance_title', lang)}
                </h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        ov_col1, ov_col2, ov_col3, ov_col4 = st.columns(4)
        with ov_col1:
            st.metric(
                t("metric_current_market_price", lang),
                f"₹{current_price:.2f}/kg",
                f"Best at {best_market}"
            )
        with ov_col2:
            st.metric(
                t("metric_best_available_market", lang),
                best_market,
                f"{best_location} • {best_distance:.1f} km"
            )
        with ov_col3:
            st.metric(
                t("metric_estimated_revenue", lang),
                f"₹{current_revenue:,.2f}",
                f"Net Profit: ₹{best_profit:,.2f}"
            )
        with ov_col4:
            st.metric(
                t("metric_distance_to_market", lang),
                f"{best_distance:.1f} km",
                f"~{heavy_time_str} ({t('lbl_heavy_load', lang)})"
            )

        # ====================================================
        # TIER 2: AI RECOMMENDATION CARD & DECISION SCORES
        # ====================================================
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        with st.container(border=True):
            # Header with Badge
            if decision == "SELL NOW":
                rec_badge_html = f"""
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 14px;">
                    <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(46, 125, 79, 0.14); border: 1.5px solid #2E7D4F; padding: 6px 16px; border-radius: 24px;">
                        <span style="font-size: 16px;">🟢</span>
                        <span style="font-weight: 800; font-size: 16px; color: #123B2A; letter-spacing: 0.5px;">{t('dec_sell_now', lang)}</span>
                    </div>
                    <span style="font-size: 13px; font-weight: 600; color: #2E7D4F;">⚡ Maximum Immediate Realization</span>
                </div>
                """
            elif decision == "WAIT":
                rec_badge_html = f"""
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 14px;">
                    <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(217, 119, 6, 0.14); border: 1.5px solid #D97706; padding: 6px 16px; border-radius: 24px;">
                        <span style="font-size: 16px;">🟡</span>
                        <span style="font-weight: 800; font-size: 16px; color: #92400E; letter-spacing: 0.5px;">{t('dec_wait', lang)}</span>
                    </div>
                    <span style="font-size: 13px; font-weight: 600; color: #D97706;">⏳ Price Expected to Rise in 3 Days</span>
                </div>
                """
            else:
                rec_badge_html = f"""
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 14px;">
                    <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(100, 116, 139, 0.14); border: 1.5px solid #64748B; padding: 6px 16px; border-radius: 24px;">
                        <span style="font-size: 16px;">⚖️</span>
                        <span style="font-weight: 800; font-size: 16px; color: #334155; letter-spacing: 0.5px;">{t('dec_neutral', lang)}</span>
                    </div>
                    <span style="font-size: 13px; font-weight: 600; color: #64748B;">📊 Monitor Market Closely</span>
                </div>
                """
            st.markdown(rec_badge_html, unsafe_allow_html=True)

            # Plain language farmer explanation
            localized_rec = get_localized_recommendation(
                crop=crop,
                quantity=quantity_value,
                best_market=best_market,
                best_location=best_location,
                best_distance=best_distance,
                best_price=current_price,
                predicted_price=predicted_price,
                decision=decision,
                lang=lang
            )
            st.markdown(f"#### 💡 {t('tab4_rationale_title', lang)}")
            st.markdown(
                f"<div style='font-size: 14.5px; line-height: 1.6; color: var(--text-charcoal); margin-bottom: 16px;'>"
                f"{localized_rec}"
                f"</div>",
                unsafe_allow_html=True
            )

            # Expected Revenue Comparison
            r_c1, r_c2, r_c3 = st.columns(3)
            with r_c1:
                st.metric(
                    t("lbl_sell_now_rev", lang),
                    f"₹{current_revenue:,.2f}",
                    f"₹{current_price:.2f}/kg × {quantity_value:g} kg"
                )
            with r_c2:
                st.metric(
                    t("lbl_expected_rev", lang),
                    f"₹{predicted_revenue:,.2f}",
                    f"₹{revenue_difference:+,.2f} net"
                )
            with r_c3:
                pct_str = f"{percentage_change:+.1f}%" if current_price > 0 else "0%"
                st.metric(
                    t("lbl_pred_3days", lang),
                    f"₹{predicted_price:.2f}/kg",
                    f"{pct_str} price change"
                )

            # Spoilage Impact Banner (if any)
            if spoilage_loss_kg > 0:
                st.warning(
                    f"📉 **{t('lbl_spoilage_risk', lang)}:** Holding {crop} for 3 days results in ~{spoilage_loss_kg:g} kg rot/discard loss, "
                    f"leaving {future_salable_qty:g} kg salable produce. Net difference after spoilage: ₹{revenue_difference:+,.2f}."
                )
            else:
                st.success(
                    f"✅ **{crop} Holding Durability:** Minimal or zero storage spoilage expected over 3 days. Salable harvest remains {quantity_value:g} kg."
                )

            st.markdown("---")

            # Decision Support Scores with Altair
            st.markdown(f"<h5 style='margin: 0 0 6px 0; color: var(--primary-forest); font-weight: 700;'>📊 {t('decision_scores_title', lang)}</h5>", unsafe_allow_html=True)
            render_decision_scores_altair_chart(sell_score, wait_score, lang)
            st.caption(f"ℹ️ {t('decision_scores_disclaimer', lang)}")

        # Voice command recognition banner if query came from speech
        if st.session_state.get("voice_detected_query"):
            v_text = st.session_state.get("voice_detected_query")
            resolved_loc_disp = recommendation_data.get("resolved_location") or location
            st.info(
                f"🎙️ **{t('voice_detected_badge', lang)}**: *\"{v_text}\"*\n\n"
                f"🌱 **{format_crop(crop, lang)}** • ⚖️ **{quantity_value:g} kg** • 📍 **{resolved_loc_disp}**"
            )

        # Spoken Voice Advice Card (Mother Tongue TTS Audio Player)
        with st.container(border=True):
            st.markdown(
                f"""
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 6px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 22px;">🔊</span>
                        <h4 style="margin: 0; color: var(--primary-forest); font-weight: 800;">
                            {t('voice_advice_title', lang)}
                        </h4>
                    </div>
                    <span style="font-size: 12px; background: rgba(46, 125, 79, 0.12); color: #2E7D4F; font-weight: 700; padding: 3px 10px; border-radius: 6px;">
                        🎙️ {SUPPORTED_LANGUAGES.get(lang, lang)}
                    </span>
                </div>
                <p style="font-size: 13.5px; color: var(--text-muted); margin-bottom: 12px;">
                    {t('voice_advice_desc', lang)}
                </p>
                """,
                unsafe_allow_html=True
            )

            # Generate natural, respectful voice script
            voice_script = generate_farmer_voice_script(recommendation_data, lang=lang)

            # Play audio in farmer's mother tongue
            try:
                voice_audio_bytes = generate_speech_audio_bytes(voice_script, lang=lang)
                if voice_audio_bytes:
                    st.audio(voice_audio_bytes, format="audio/mp3", autoplay=False)
            except Exception as _tts_err:
                st.caption(f"Audio ready: {voice_script}")

            with st.expander(f"📜 {t('voice_advice_title', lang)} (Text Script)", expanded=False):
                st.markdown(f"🗣️ *\"{voice_script}\"*")

        # ====================================================
        # TIER 3: RECOMMENDED MARKET & LOGISTICS ACTION
        # ====================================================
        resolved_loc = recommendation_data.get("resolved_location") or location
        canonical_origin = f"{resolved_loc}, Telangana, India"
        nav_origin = urllib.parse.quote_plus(canonical_origin)
        nav_dest = urllib.parse.quote_plus(f"{best_market}, {best_location}")
        google_maps_url = (
            f"https://www.google.com/maps/dir/?api=1"
            f"&origin={nav_origin}"
            f"&destination={nav_dest}"
            f"&travelmode=driving"
        )

        # Clean title strings (prevent duplicate emojis)
        rec_title = t("recommended_market_title", lang)
        if not rec_title.startswith("🏪"):
            rec_title = f"🏪 {rec_title}"

        # LINE 1: PRIMARY RECOMMENDED MARKET CARD (FULL WIDTH)
        with st.container(border=True):
            m_head1, m_head2 = st.columns([3, 1.4])
            with m_head1:
                st.markdown(f"#### {rec_title}")
                st.markdown(f"## **{best_market}**")
            with m_head2:
                st.metric("💰 Mandi Rate", f"₹{current_price:.2f}/kg")

            # Arranged in separate clean lines
            st.markdown(f"📍 **Location**: *{best_location}*")
            if google_rating:
                st.markdown(f"⭐ **Rating & Reviews**: {google_rating}")
            st.markdown(f"🛣️ **Road Distance**: **{best_distance:.1f} km**")
            st.markdown(f"⏱️ **Transit (Heavy Load)**: **~{heavy_time_str}** ({t('lbl_heavy_load', lang)})")
            st.markdown(f"🚗 **Transit (Car / Auto / Bike)**: **~{car_time_str}**")

            st.markdown("")
            st.link_button(
                t("btn_start_nav", lang, market=best_market),
                google_maps_url,
                type="primary",
                use_container_width=True
            )

        # LINE 2: SECONDARY / SMALL MARKET CARD (FULL WIDTH)
        if suggested_small_market:
            sm_mkt = suggested_small_market.get("market")
            sm_loc = suggested_small_market.get("location", "")
            sm_dist = float(suggested_small_market.get("distance_km", 0.0))
            sm_price = float(suggested_small_market.get("price_per_kg", 0.0))
            sm_time = suggested_small_market.get("travel_time", "15 mins")
            sm_net = float(suggested_small_market.get("small_batch_net_profit", sm_price * quantity_value - 30.0))
            sm_gmaps = suggested_small_market.get("gmaps_url", "")

            is_same_as_best = ((sm_mkt or "").strip().lower() == (best_market or "").strip().lower())
            
            raw_sm_title = t("small_market_card_title", lang)
            clean_sm_title = raw_sm_title.replace("🏪", "").strip()
            if is_same_as_best:
                card_title = f"🛵 0% Commission Small Batch Benefit ({sm_mkt})"
            else:
                card_title = f"🛵 {clean_sm_title}"

            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            with st.container(border=True):
                s_head1, s_head2 = st.columns([3, 1.4])
                with s_head1:
                    st.markdown(f"#### {card_title}")
                    st.markdown(f"## **{sm_mkt}**")
                with s_head2:
                    st.metric("💰 Rate & Net", f"₹{sm_price:.2f}/kg", f"Net: ₹{sm_net:,.0f}")

                # Arranged in separate clean lines
                st.markdown(f"📍 **Location**: *{sm_loc}*")
                st.markdown(f"🛵 **Local Distance**: **{sm_dist:.1f} km** (~{sm_time} by two-wheeler or auto)")
                st.markdown(f"🏷️ **Commission**: **0% Commission** (Direct Retail / Government Rythu Bazar)")
                st.markdown(f"💵 **Take-Home Net Cash**: **₹{sm_net:,.2f}** (Zero truck hire & zero auction fees)")
                st.markdown(f"💡 **Logistics Guidance**: Bike / Auto-rickshaw friendly • Ideal for batches ≤ 500 kg")

                st.markdown("")
                if sm_gmaps:
                    st.link_button(
                        t("btn_navigate_small_market", lang, market=sm_mkt),
                        sm_gmaps,
                        use_container_width=True
                    )
                else:
                    st.caption("🛵 Bike/Auto Friendly • No heavy truck required")
        else:
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            with st.container(border=True):
                st.markdown(f"#### 🚛 {t('lbl_heavy_load', lang)} Logistics Summary")
                st.markdown(f"📍 **Origin**: {resolved_loc}, Telangana")
                st.markdown(f"🏢 **Destination Mandi**: {best_market}")
                st.markdown(f"⚖️ **Cargo Batch**: **{quantity_value:g} kg** • Commercial APMC Weighbridge & Auction")
                st.info(f"💡 **Transit Guidance**: {t('transit_heavy_load_note', lang)}")

        st.markdown("---")


        # ====================================================
        # COMPREHENSIVE MANDI DEEP-DIVES & DETAILED TABS
        # ====================================================

        tab_list = [
            t("tab_market_comparison", lang),
            t("tab_profit_analysis", lang),
            t("tab_price_trends", lang),
            t("tab_freshness_matrix", lang),
            t("tab_ai_advisor", lang)
        ]
        active_tab_default = active_nav if (active_nav and active_nav in tab_list) else tab_list[0]
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            tab_list,
            default=active_tab_default
        )


        # ====================================================
        # TAB 1 - MARKET COMPARISON
        # ====================================================

        with tab1:

            st.subheader(
                f"🏪 {t('tab1_header', lang)}"
            )

            # Live Agmarknet Feed Status Banner
            st.markdown(
                f"""
                <div style="background: rgba(34, 197, 94, 0.1);
                            border: 1px solid rgba(34, 197, 94, 0.4);
                            border-radius: 10px;
                            padding: 10px 16px;
                            margin-bottom: 14px;
                            display: flex;
                            align-items: center;
                            justify-content: space-between;">
                    <div style="font-weight: 700; color: #22c55e; font-size: 14px;">
                        {t('live_prices_badge', lang)}
                    </div>
                    <div style="font-size: 13px; opacity: 0.9;">
                        🗓️ {t('price_date_info', lang, date=str(price_date))}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if comparison_data:

                markets = comparison_data.get(
                    "markets",
                    []
                )

                if markets:

                    st.info(
                        f"📍 **{t('lbl_discovered_markets', lang, radius=radius_km, count=len(markets))}** — "
                        f"{t('badge_gps_verified', lang, radius=radius_km)}"
                    )

                    filter_opts = [
                        t("filter_all_markets", lang),
                        t("filter_small_markets", lang),
                        t("filter_wholesale_markets", lang)
                    ]
                    selected_mkt_filter = st.radio(
                        t("lbl_filter_markets", lang),
                        filter_opts,
                        horizontal=True,
                        key="tab1_filter_radio"
                    )

                    filtered_markets = markets
                    if selected_mkt_filter == t("filter_small_markets", lang):
                        filtered_markets = [m for m in markets if m.get("is_small_market", False)]
                    elif selected_mkt_filter == t("filter_wholesale_markets", lang):
                        filtered_markets = [m for m in markets if not m.get("is_small_market", False)]

                    if not filtered_markets:
                        filtered_markets = markets

                    df = pd.DataFrame(filtered_markets)
                    if "price_per_kg" in df.columns:
                        df["est_revenue"] = df["price_per_kg"] * quantity_value

                    cols_to_show = ["market"]
                    if "market_category" in df.columns:
                        cols_to_show.append("market_category")
                    cols_to_show.extend(["location", "price_per_kg"])
                    if "est_revenue" in df.columns:
                        cols_to_show.append("est_revenue")
                    if "distance_km" in df.columns:
                        cols_to_show.append("distance_km")
                    if "travel_time" in df.columns:
                        cols_to_show.append("travel_time")
                    if "est_transport_cost" in df.columns:
                        cols_to_show.append("est_transport_cost")
                    if "google_rating" in df.columns:
                        cols_to_show.append("google_rating")
                    cols_to_show.append("date")

                    display_df = df[cols_to_show].copy()

                    rename_map = {
                        "market": t("col_market", lang),
                        "market_category": t("col_market_category", lang),
                        "location": t("col_location", lang),
                        "distance_km": t("col_distance", lang),
                        "price_per_kg": t("col_price", lang),
                        "est_revenue": t("metric_estimated_revenue", lang) + " (₹)",
                        "est_transport_cost": t("col_transit_cost", lang),
                        "travel_time": t("col_travel_time", lang),
                        "google_rating": t("col_rating", lang),
                        "date": t("col_date", lang)
                    }
                    display_df = display_df.rename(columns=rename_map)

                    st.dataframe(
                        display_df,
                        use_container_width=True,
                        hide_index=True
                    )

                    with st.expander(f"🗺️ {t('btn_navigate_map', lang)} ({len(markets)})", expanded=False):
                        for m_item in markets[:12]:
                            col_m1, col_m2 = st.columns([3, 1])
                            with col_m1:
                                dist_str = f" • {m_item['distance_km']} km" if "distance_km" in m_item else ""
                                time_str = f" • ⏱️ {m_item['travel_time']}" if "travel_time" in m_item else ""
                                st.write(f"**{m_item['market']}** ({m_item['location']}){dist_str}{time_str} — ₹{m_item['price_per_kg']}/kg")
                            with col_m2:
                                if "gmaps_url" in m_item:
                                    st.link_button(t("btn_navigate_map", lang), m_item["gmaps_url"], use_container_width=True)

                    st.markdown(
                        f"### 📊 {t('tab1_chart_title', lang)}"
                    )

                    render_market_price_altair_chart(df, lang)

                else:

                    st.warning(
                        t("tab1_no_data", lang)
                    )

            else:

                st.warning(
                    t("tab1_no_data", lang)
                )


        # ====================================================
        # TAB 2 - PROFIT ANALYSIS
        # ====================================================

        with tab2:

            st.subheader(
                f"💰 {t('tab2_header', lang)}"
            )

            if profit_data:

                profit_markets = profit_data.get(
                    "markets",
                    []
                )

                if profit_markets:

                    filter_opts_p = [
                        t("filter_all_markets", lang),
                        t("filter_small_markets", lang),
                        t("filter_wholesale_markets", lang)
                    ]
                    selected_p_filter = st.radio(
                        t("lbl_filter_markets", lang),
                        filter_opts_p,
                        horizontal=True,
                        key="tab2_filter_radio"
                    )

                    filtered_profit_markets = profit_markets
                    if selected_p_filter == t("filter_small_markets", lang):
                        filtered_profit_markets = [m for m in profit_markets if m.get("is_small_market", False)]
                    elif selected_p_filter == t("filter_wholesale_markets", lang):
                        filtered_profit_markets = [m for m in profit_markets if not m.get("is_small_market", False)]

                    if not filtered_profit_markets:
                        filtered_profit_markets = profit_markets

                    profit_df = pd.DataFrame(
                        filtered_profit_markets
                    )

                    profit_cols = [
                        "market"
                    ]
                    if "market_category" in profit_df.columns:
                        profit_cols.append("market_category")
                    profit_cols.extend([
                        "price_per_kg",
                        "distance_km"
                    ])
                    if "google_rating" in profit_df.columns:
                        profit_cols.append("google_rating")
                    profit_cols.append("gross_revenue")
                    profit_cols.append("transport_cost")
                    if "commission_cost" in profit_df.columns:
                        profit_cols.append("commission_cost")
                    profit_cols.extend([
                        "handling_cost",
                        "net_profit"
                    ])

                    display_profit_df = profit_df[[c for c in profit_cols if c in profit_df.columns]].copy()

                    profit_rename = {
                        "market": t("col_market", lang),
                        "market_category": t("col_market_category", lang),
                        "price_per_kg": t("col_price", lang),
                        "distance_km": t("col_distance", lang),
                        "google_rating": t("col_rating", lang),
                        "gross_revenue": t("col_gross_rev", lang),
                        "transport_cost": t("col_transport_cost", lang),
                        "commission_cost": t("col_commission", lang),
                        "handling_cost": t("col_handling_cost", lang),
                        "net_profit": t("col_net_profit", lang)
                    }
                    display_profit_df = display_profit_df.rename(columns=profit_rename)

                    st.dataframe(
                        display_profit_df,
                        use_container_width=True,
                        hide_index=True
                    )


                    # ----------------------------------------
                    # BEST PROFIT MARKET
                    # ----------------------------------------

                    best_profit_market = (
                        profit_data.get(
                            "best_market",
                            "N/A"
                        )
                    )

                    best_net_profit = float(
                        profit_data.get(
                            "best_net_profit",
                            0
                        )
                    )

                    st.success(
                        t("tab2_best_profit_banner", lang, market=best_profit_market, profit=f"₹{best_net_profit:,.2f}")
                    )

                    best_profit_nav_dest = urllib.parse.quote_plus(f"{best_profit_market}, Telangana, India")
                    profit_maps_url = f"https://www.google.com/maps/dir/?api=1&origin={nav_origin}&destination={best_profit_nav_dest}&travelmode=driving"
                    st.link_button(
                        t("tab2_btn_nav", lang, market=best_profit_market),
                        profit_maps_url,
                        use_container_width=True
                    )


                    # ----------------------------------------
                    # PROFIT CHART
                    # ----------------------------------------

                    st.markdown(
                        f"### 📊 {t('tab2_chart_title', lang)}"
                    )

                    render_net_profit_altair_chart(profit_df, lang)


                    st.caption(
                        t("tab2_transport_caption", lang)
                    )

                else:

                    st.warning(
                        t("tab1_no_data", lang)
                    )

            else:

                st.warning(
                    t("tab1_no_data", lang)
                )


        # ====================================================
        # TAB 3 - PRICE TRENDS
        # ====================================================

        with tab3:

            st.subheader(
                f"📈 {t('tab3_header', lang)}"
            )

            if history_data:

                history = history_data.get(
                    "history",
                    []
                )

                if history:

                    history_df = pd.DataFrame(
                        history
                    )

                    history_df["date"] = (
                        pd.to_datetime(
                            history_df["date"]
                        )
                    )

                    history_df = (
                        history_df.set_index(
                            "date"
                        )
                    )

                    chart_data = history_df[
                        [
                            "average_price",
                            "maximum_price",
                            "minimum_price"
                        ]
                    ].copy()

                    chart_data.columns = [
                        t("lbl_avg_price", lang),
                        t("lbl_max_price", lang),
                        t("lbl_min_price", lang)
                    ]

                    st.line_chart(
                        chart_data,
                        color=["#2E7D4F", "#123B2A", "#D97706"],
                        use_container_width=True
                    )

                    st.caption(
                        t("tab3_caption", lang)
                    )

                else:

                    st.warning(
                        t("tab1_no_data", lang)
                    )

            else:

                st.warning(
                    t("tab1_no_data", lang)
                )


            # ------------------------------------------------
            # ML PREDICTION
            # ------------------------------------------------

            st.subheader(
                f"🔮 {t('tab3_pred_header', lang)}"
            )

            has_ml_model = recommendation_data.get("has_prediction_model", True) if recommendation_data else True
            if not has_ml_model:
                st.info(
                    f"🌾 **{t('spot_advisory_title', lang)}**\n\n"
                    f"{t('spot_advisory_desc', lang)}"
                )

            prediction_col1, prediction_col2, prediction_col3 = (
                st.columns(3)
            )

            with prediction_col1:

                st.metric(
                    t("lbl_current_best_price", lang),
                    f"₹{ml_current_price:.2f}/kg"
                )

            with prediction_col2:

                st.metric(
                    t("lbl_pred_3days", lang),
                    f"₹{ml_predicted_price:.2f}/kg"
                )

            with prediction_col3:

                st.metric(
                    t("metric_confidence", lang),
                    localized_confidence
                )

            range_col1, range_col2 = st.columns(2)

            with range_col1:

                st.metric(
                    t("lbl_lower_est", lang),
                    f"₹{prediction_lower:.2f}/kg"
                )

            with range_col2:

                st.metric(
                    t("lbl_upper_est", lang),
                    f"₹{prediction_upper:.2f}/kg"
                )

            st.info(
                t("tab3_range_info", lang, lower=f"₹{prediction_lower:.2f}", upper=f"₹{prediction_upper:.2f}")
            )

            if has_ml_model and (model_r2 > 0 or model_mae > 0):
                metric_col1, metric_col2 = st.columns(2)

                with metric_col1:

                    st.metric(
                        t("lbl_model_r2", lang),
                        f"{model_r2:.2f}"
                    )

                with metric_col2:

                    st.metric(
                        t("lbl_model_mae", lang),
                        f"₹{model_mae:.2f}/kg"
                    )

            if percentage_change > 0:

                st.success(
                    t("tab3_increase", lang, pct=f"{percentage_change:.1f}")
                )

            elif percentage_change < 0:

                st.warning(
                    t("tab3_decrease", lang, pct=f"{abs(percentage_change):.1f}")
                )

            else:

                st.info(
                    t("tab3_stable", lang)
                )


        # ====================================================
        # TAB 4 - CROP FRESHNESS MATRIX & DEGRADATION
        # ====================================================

        with tab4:

            # Live Agro-Weather & Transit Alert
            weather_time = weather_info.get("last_updated", "")
            live_badge = f" • 🕒 Live GPS Weather ({weather_time})" if weather_time else ""
            st.subheader(f"🌤️ {t('weather_title', lang)}{live_badge}")

            with st.container(border=True):
                w_col1, w_col2, w_col3, w_col4 = st.columns(4)
                weather_condition = format_weather_condition(weather_info.get("condition", "Partly Cloudy"), lang)
                weather_alert = format_weather_alert(weather_info.get("weather_alert", "Favorable"), lang)
                transit_advice = format_transit_advice(weather_info.get("transit_advice", "Favorable transit conditions."), lang)
                wind_speed = weather_info.get("wind_speed", "")

                with w_col1:
                    st.metric(f"🌡️ {t('lbl_temperature', lang)}", weather_info.get("temperature", "31°C"), weather_condition)
                with w_col2:
                    st.metric(f"💧 {t('lbl_humidity', lang)}", weather_info.get("humidity", "62%"))
                with w_col3:
                    st.metric(f"🌧️ {t('lbl_rain_prob', lang)}", weather_info.get("rain_probability", "15%"))
                with w_col4:
                    st.metric(f"🚛 {t('lbl_transit_adv', lang)}", weather_alert, f"💨 {wind_speed}" if wind_speed else None)

                st.info(f"💡 **{t('lbl_transit_guide', lang)}:** {transit_advice}")

            st.markdown("---")

            st.subheader(
                f"🌾 {t('matrix_title', lang)}"
            )
            st.caption(
                t('matrix_subtitle', lang)
            )

            # Render full interactive matrix matching the photo
            st.markdown(
                render_degradation_matrix_html(crop, days_diff),
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div style="margin-top: 14px; margin-bottom: 20px; font-size: 13.5px; color: var(--rzp-text-muted); line-height: 1.6;">
                    {t('matrix_caption_photo', lang)}
                </div>
                """,
                unsafe_allow_html=True
            )

            mat_col1, mat_col2, mat_col3, mat_col4 = st.columns(4)
            with mat_col1:
                st.metric(f"⏳ {t('lbl_shelf_life', lang)}", shelf_life_str, safe_window_str)
            with mat_col2:
                st.metric(f"📅 {t('expected_harvest', lang)}", f"{harvest_date}", f"{format_quality(quality, lang)}")
            with mat_col3:
                st.metric(f"⚠️ {t('lbl_spoilage_risk', lang)}", damage_risk_str, perish_str)
            with mat_col4:
                st.metric(f"📉 {t('lbl_spoilage_rate', lang)}", spoilage_rate_str)

            if timeline_summary:
                st.info(f"⏱️ **{crop} Freshness Scale:** {timeline_summary}")

            if spoilage_loss_kg > 0:
                st.error(
                    f"📉 **Financial Degradation Impact:** If waiting 3 days to sell, {spoilage_loss_kg:g} kg out of {quantity_value:g} kg "
                    f"will spoil or rot, leaving only {future_salable_qty:g} kg salable produce. "
                    f"Expected difference after storage rot: ₹{revenue_difference:+,.2f}."
                )
            else:
                st.success(
                    f"✅ **Zero Spoilage Risk for {crop}:** This crop has exceptional holding stability in standard dry storage. "
                    f"No physical weight degradation expected over the 3-day holding window."
                )

        # ====================================================
        # TAB 5 - AI ADVISOR
        # ====================================================

        with tab5:

            st.subheader(
                f"💬 {t('tab4_header', lang)}"
            )

            # ------------------------------------------------
            # DECISION
            # ------------------------------------------------
            # RECOMMENDATION HERO CARD
            # ------------------------------------------------

            localized_rec = get_localized_recommendation(
                crop=crop,
                quantity=quantity_value,
                best_market=best_market,
                best_location=best_location,
                best_distance=best_distance,
                best_price=current_price,
                predicted_price=predicted_price,
                decision=decision,
                lang=lang
            )

            with st.container(border=True):
                rec_col1, rec_col2 = st.columns([2.8, 1.2])
                with rec_col1:
                    if decision == "SELL NOW":
                        st.success(
                            f"### 🟢 {t('decision_sell', lang)}\n\n{localized_rec}"
                        )
                    elif decision == "WAIT":
                        st.warning(
                            f"### 🟡 {t('decision_wait', lang)}\n\n{localized_rec}"
                        )
                    else:
                        st.info(
                            f"### ⚖️ {t('dec_neutral', lang)}\n\n{localized_rec}"
                        )
                with rec_col2:
                    st.metric(
                        t("lbl_rec_market", lang),
                        best_market,
                        f"~{best_distance:.1f} km"
                    )
                    st.metric(
                        t("metric_current_price", lang),
                        f"₹{current_price:.2f}/kg"
                    )

            # ------------------------------------------------
            # DECISION SCORES
            # ------------------------------------------------

            with st.container(border=True):
                st.markdown(
                    f"**📊 {t('tab4_scores_title', lang)}**"
                )
                score_col1, score_col2 = st.columns(2)
                with score_col1:
                    st.write(
                        f"💰 **{t('lbl_sell_score', lang)}**: {sell_score:.0f}%"
                    )
                    st.progress(
                        min(max(sell_score / 100, 0), 1)
                    )
                with score_col2:
                    st.write(
                        f"⏳ **{t('lbl_wait_score', lang)}**: {wait_score:.0f}%"
                    )
                    st.progress(
                        min(max(wait_score / 100, 0), 1)
                    )

            # ------------------------------------------------
            # STRUCTURED ADVISORY GRID
            # ------------------------------------------------

            st.markdown(
                f"### 🌾 {t('tab4_advisor_title', lang)}"
            )

            adv_col1, adv_col2 = st.columns(2)

            with adv_col1:
                with st.container(border=True):
                    st.markdown(
                        f"#### 📊 {t('tab4_rationale_title', lang)}"
                    )
                    if recommendation_data.get("reason"):
                        st.markdown(
                            f"**{t('tab4_reason_label', lang)}:** {recommendation_data['reason']}"
                        )
                    elif decision == "SELL NOW":
                        st.markdown(
                            f"**{t('tab4_reason_label', lang)}:** {t('tab3_decrease', lang, pct=f'{abs(percentage_change):.1f}')}"
                        )
                    elif decision == "WAIT":
                        st.markdown(
                            f"**{t('tab4_reason_label', lang)}:** {t('tab3_increase', lang, pct=f'{percentage_change:.1f}')}"
                        )
                    else:
                        st.markdown(
                            f"**{t('tab4_reason_label', lang)}:** {t('tab3_stable', lang)}"
                        )
                    st.markdown(
                        f"- 📍 **{t('lbl_to_mandi', lang)}:** {best_market} ({best_location})\n\n"
                        f"- 🔮 **{t('lbl_pred_3days', lang)}:** ₹{predicted_price:.2f}/kg\n\n"
                        f"- 🎯 **{t('metric_confidence', lang)}:** {localized_confidence}"
                    )

            with adv_col2:
                with st.container(border=True):
                    st.markdown(
                        f"#### 💵 {t('tab4_financial_impact', lang)}"
                    )
                    fin_c1, fin_c2 = st.columns(2)
                    with fin_c1:
                        st.metric(
                            t("lbl_sell_now_rev", lang),
                            f"₹{current_revenue:,.2f}"
                        )
                    with fin_c2:
                        st.metric(
                            t("lbl_expected_rev", lang),
                            f"₹{predicted_revenue:,.2f}",
                            f"₹{revenue_difference:+,.2f}"
                        )
                    st.caption(
                        f"⚖️ **{t('lbl_exp_difference', lang)}:** ₹{revenue_difference:,.2f}"
                    )
                    if spoilage_loss_kg > 0:
                        st.caption(
                            f"📉 **Post-Harvest Spoilage:** {future_salable_qty:g} kg salable "
                            f"(-{spoilage_loss_kg:g} kg rots/discarded in 3 days)."
                        )
                        if revenue_difference < 0:
                            st.error(
                                f"⚠️ **{financial_info.get('holding_verdict', 'Net Deficit from Spoilage')}**"
                            )

            adv_col3, adv_col4 = st.columns(2)

            with adv_col3:
                with st.container(border=True):
                    st.markdown(
                        f"#### ⭐ {t('tab4_quality_guidance', lang)}"
                    )
                    st.markdown(
                        f"**{format_quality(quality, lang)}**\n"
                    )
                    if quality == "Grade A":
                        st.markdown(t("quality_advice_grade_a", lang))
                    elif quality == "Grade B":
                        st.markdown(t("quality_advice_grade_b", lang))
                    else:
                        st.markdown(t("quality_advice_grade_c", lang))

                    st.caption(
                        f"📅 **{t('expected_harvest', lang)}:** {harvest_date} "
                        f"({days_diff} {t('lbl_days_post_harvest', lang) if days_diff > 0 else t('quality_fresh_status', lang)})\n\n"
                        f"_{quality_reason}_\n\n"
                        f"⏱️ **{crop} Freshness Scale:** {timeline_summary}"
                    )

            with adv_col4:
                with st.container(border=True):
                    st.markdown(
                        f"#### 🚚 {t('tab4_logistics_guidance', lang)}"
                    )
                    st.markdown(
                        f"- ⏱️ **{t('lbl_travel_time', lang)}:** {travel_time_str}\n\n"
                        f"- ⛽ **{t('lbl_transport_cost', lang)}:** ₹{est_transport_cost:,.2f}\n\n"
                        f"- 🌤️ **{t('weather_title', lang)}:** {weather_condition}\n\n"
                        f"- 💡 {transit_advice}"
                    )

            # ------------------------------------------------
            # SUMMARY
            # ------------------------------------------------

            st.markdown(
                f"### 📋 {t('tab4_summary_title', lang)}"
            )

            with st.container(border=True):
                summary_col1, summary_col2, summary_col3 = (
                    st.columns([1, 1, 1.4])
                )

                with summary_col1:
                    st.metric(
                        t("lbl_farmer", lang),
                        st.session_state.farmer_name
                    )

                with summary_col2:
                    st.metric(
                        t("lbl_quantity", lang),
                        f"{quantity_value:g} kg"
                    )

                with summary_col3:
                    st.metric(
                        t("lbl_quality", lang),
                        format_quality(quality, lang)
                    )


        # ====================================================
        # REVENUE SUMMARY
        # ====================================================

        st.markdown("---")

        st.subheader(
            f"💵 {t('rev_header', lang)}"
        )

        revenue_col1, revenue_col2, revenue_col3 = (
            st.columns(3)
        )

        with revenue_col1:

            st.metric(
                t("lbl_sell_now_rev", lang),
                f"₹{current_revenue:,.2f}"
            )

        with revenue_col2:

            st.metric(
                t("lbl_expected_rev", lang),
                f"₹{predicted_revenue:,.2f}"
            )

        with revenue_col3:

            st.metric(
                t("lbl_exp_difference", lang),
                f"₹{revenue_difference:,.2f}"
            )

        if spoilage_loss_kg > 0:
            st.caption(
                f"📉 **{t('shelflife_title', lang)}:** {t('lbl_expected_rev', lang)} reflects post-harvest storage decay. "
                f"{future_salable_qty:g} kg salable produce remaining after 3 days (-{spoilage_loss_kg:g} kg lost to rot)."
            )


        # ====================================================
        # DISCLAIMER
        # ====================================================

        st.markdown("---")

        st.caption(
            t("disclaimer_1", lang)
        )

        st.caption(
            t("disclaimer_2", lang)
        )


# ============================================================
# INITIAL SCREEN
# ============================================================

else:

    # ========================================================
    # 🎙️ FARMER VOICE COMMAND ASSISTANT (MOTHER TONGUE AI)
    # ========================================================

    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(59, 130, 246, 0.08) 100%);
                    border: 1.8px solid #10b981;
                    border-radius: 16px;
                    padding: 24px 26px;
                    margin-bottom: 22px;
                    box-shadow: var(--rzp-card-shadow);">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 8px;">
                <h3 style="margin: 0; color: var(--rzp-text); font-weight: 800; font-size: 21px;">
                    {t('voice_assistant_title', lang)}
                </h3>
                <span style="font-size: 13px; color: #059669; font-weight: 700; background: rgba(16, 185, 129, 0.15); padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(16, 185, 129, 0.3);">
                    🎙️ {SUPPORTED_LANGUAGES.get(lang, lang)} Active
                </span>
            </div>
            <p style="font-size: 14.5px; color: var(--rzp-text-muted); margin-bottom: 16px; line-height: 1.55;">
                {t('voice_assistant_desc', lang)}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Direct Native Voice Microphone Component (Zero Popup, Direct Market Analysis)
    if voice_mic_component:
        voice_payload = voice_mic_component(language=lang, key="farmer_voice_mic_widget")
        if isinstance(voice_payload, dict):
            v_text = voice_payload.get("text", "").strip()
            v_ts = voice_payload.get("timestamp", 0)
            if v_text and v_ts != st.session_state.get("last_processed_voice_ts"):
                st.session_state.last_processed_voice_ts = v_ts
                with st.spinner(f"🌾 AI is analyzing market prices for '{v_text}'..."):
                    # Automatic Language Detection
                    v_lang = voice_payload.get("detected_lang")
                    if not v_lang or v_lang not in SUPPORTED_LANGUAGES:
                        try:
                            from services.voice_service import detect_language
                            v_lang = detect_language(v_text)
                        except Exception:
                            v_lang = lang
                    if v_lang and v_lang in SUPPORTED_LANGUAGES:
                        st.session_state.farmer_language = v_lang
                        lang = v_lang
                    parsed = extract_parameters_with_llm_fallback(v_text, default_lang=lang)
                    apply_farmer_inputs(
                        crop=parsed.get("crop"),
                        quantity=parsed.get("quantity"),
                        location=parsed.get("location"),
                        harvest_date=parsed.get("harvest_date"),
                        price_date=parsed.get("price_date"),
                        trigger_analysis=True
                    )
                    st.session_state.voice_detected_query = v_text
                    st.session_state.voice_parsed_details = parsed
                    st.rerun()
        elif isinstance(voice_payload, str) and voice_payload.strip() and voice_payload.strip() != st.session_state.get("last_processed_voice_query"):
            v_text = voice_payload.strip()
            st.session_state.last_processed_voice_query = v_text
            with st.spinner(f"🌾 AI is analyzing market prices for '{v_text}'..."):
                try:
                    from services.voice_service import detect_language
                    v_lang = detect_language(v_text)
                except Exception:
                    v_lang = lang
                if v_lang and v_lang in SUPPORTED_LANGUAGES:
                    st.session_state.farmer_language = v_lang
                    lang = v_lang
                parsed = extract_parameters_with_llm_fallback(v_text, default_lang=lang)
                apply_farmer_inputs(
                    crop=parsed.get("crop"),
                    quantity=parsed.get("quantity"),
                    location=parsed.get("location"),
                    harvest_date=parsed.get("harvest_date"),
                    price_date=parsed.get("price_date"),
                    trigger_analysis=True
                )
                st.session_state.voice_detected_query = v_text
                st.session_state.voice_parsed_details = parsed
                st.rerun()
    else:
        components.html(build_webspeech_html(lang), height=215)

    with st.expander(f"🎙️ {t('voice_audio_record_help', lang)} (Audio File Fallback)", expanded=False):
        audio_prompt = st.audio_input(t("voice_btn_speak", lang), key="farmer_voice_recorder")
        if audio_prompt is not None:
            audio_bytes = audio_prompt.read()
            if audio_bytes and len(audio_bytes) > 100:
                with st.spinner("🤖 AI is listening to your voice..."):
                    try:
                        transcribed_text = transcribe_audio_bytes(audio_bytes)
                        if transcribed_text:
                            try:
                                from services.voice_service import detect_language
                                v_lang = detect_language(transcribed_text)
                            except Exception:
                                v_lang = lang
                            if v_lang and v_lang in SUPPORTED_LANGUAGES:
                                st.session_state.farmer_language = v_lang
                                lang = v_lang
                            parsed = extract_parameters_with_llm_fallback(transcribed_text, default_lang=lang)
                            apply_farmer_inputs(
                                crop=parsed.get("crop"),
                                quantity=parsed.get("quantity"),
                                location=parsed.get("location"),
                                harvest_date=parsed.get("harvest_date"),
                                price_date=parsed.get("price_date"),
                                trigger_analysis=True
                            )
                            st.session_state.voice_detected_query = transcribed_text
                            st.session_state.voice_parsed_details = parsed
                            st.rerun()
                    except QuotaExhaustedError:
                        if lang == "te":
                            st.warning("⚠️ **OpenAI క్లౌడ్ కోటా ముగిసింది.** దయచేసి పైన ఉన్న ఉచిత **'లైవ్ బ్రౌజర్ మైక్రోఫోన్'** లేదా క్రింది **'1-ట్యాప్ వాయిస్ బటన్లు'** ఉపయోగించండి!")
                        elif lang == "hi":
                            st.warning("⚠️ **OpenAI क्लाउड कोटा समाप्त हो गया है।** कृपया ऊपर दिए गए निःशुल्क **'लाइव ब्राउज़र माइक्रोफ़ोन'** या नीचे दिए गए **'1-टैप वॉयस बटन'** का उपयोग करें!")
                        else:
                            st.warning("⚠️ **OpenAI Whisper API quota exhausted.** Please use the free **Browser Live Microphone** above or **1-Tap Voice Presets**!")
                    except Exception as audio_err:
                        if lang == "te":
                            st.info("💡 దయచేసి పైన ఉన్న బ్రౌజర్ లైవ్ మైక్రోఫోన్ లేదా 1-ట్యాప్ వాయిస్ బటన్లు ఉపయోగించండి.")
                        elif lang == "hi":
                            st.info("💡 कृपया ऊपर दिए गए ब्राउज़र लाइव माइक्रोफ़ोन या 1-टैप वॉयस बटन का उपयोग करें।")
                        else:
                            st.info("💡 Please use the free Browser Live Microphone above or 1-Tap Voice buttons.")

    # 1-Tap Spoken Sample Phrases (Voice Command Simulation)
    st.markdown(
        f"<div style='font-size: 13.5px; font-weight: 700; color: var(--rzp-text); margin: 12px 0 6px 0;'>"
        f"{t('voice_quick_examples_title', lang)}"
        f"</div>",
        unsafe_allow_html=True
    )
    vbtn_c1, vbtn_c2, vbtn_c3 = st.columns(3)

    with vbtn_c1:
        if st.button(t("voice_sample_1", lang), use_container_width=True, key="vsample_btn_1"):
            raw_q = t("voice_sample_1", lang)
            parsed = extract_parameters_with_llm_fallback(raw_q, default_lang=lang)
            c = parsed.get("crop") or "Rice"
            q = float(parsed.get("quantity") or 50.0)
            loc = parsed.get("location") or "Jangaon"
            apply_farmer_inputs(
                crop=c,
                quantity=q,
                location=loc,
                harvest_date=parsed.get("harvest_date"),
                price_date=parsed.get("price_date"),
                trigger_analysis=True
            )
            st.session_state.voice_detected_query = raw_q
            st.session_state.voice_parsed_details = parsed
            st.rerun()

    with vbtn_c2:
        if st.button(t("voice_sample_2", lang), use_container_width=True, key="vsample_btn_2"):
            raw_q = t("voice_sample_2", lang)
            parsed = extract_parameters_with_llm_fallback(raw_q, default_lang=lang)
            c = parsed.get("crop") or "Tomato"
            q = float(parsed.get("quantity") or 1200.0)
            loc = parsed.get("location") or "Shamshabad"
            apply_farmer_inputs(
                crop=c,
                quantity=q,
                location=loc,
                harvest_date=parsed.get("harvest_date"),
                price_date=parsed.get("price_date"),
                trigger_analysis=True
            )
            st.session_state.voice_detected_query = raw_q
            st.session_state.voice_parsed_details = parsed
            st.rerun()

    with vbtn_c3:
        if st.button(t("voice_sample_3", lang), use_container_width=True, key="vsample_btn_3"):
            raw_q = t("voice_sample_3", lang)
            parsed = extract_parameters_with_llm_fallback(raw_q, default_lang=lang)
            c = parsed.get("crop") or "Onion"
            q = float(parsed.get("quantity") or 300.0)
            loc = parsed.get("location") or "Bhongir"
            apply_farmer_inputs(
                crop=c,
                quantity=q,
                location=loc,
                harvest_date=parsed.get("harvest_date"),
                price_date=parsed.get("price_date"),
                trigger_analysis=True
            )
            st.session_state.voice_detected_query = raw_q
            st.session_state.voice_parsed_details = parsed
            st.rerun()

    st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

    # ========================================================
    # 1-CLICK HARVEST ANALYSIS PRESETS (HERO ACTION CENTER)
    # ========================================================

    st.markdown(
        f"""
        <div style="background: var(--rzp-card-bg);
                    border: 1.5px solid var(--rzp-card-border);
                    border-radius: 16px;
                    padding: 24px 26px;
                    margin-bottom: 22px;
                    box-shadow: var(--rzp-card-shadow);">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 8px;">
                <h3 style="margin: 0; color: var(--rzp-text); font-weight: 800; font-size: 20px;">
                    {t('quick_scenario_title', lang)}
                </h3>
                <span style="font-size: 13px; color: var(--rzp-accent); font-weight: 700; background: var(--rzp-badge-bg); padding: 4px 10px; border-radius: 6px;">
                    ⚡ 1-Tap Instant Run
                </span>
            </div>
            <p style="font-size: 14px; color: var(--rzp-text-muted); margin-bottom: 18px; line-height: 1.5;">
                {t('quick_scenario_desc', lang)}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    qcol1, qcol2, qcol3 = st.columns(3)

    with qcol1:
        if st.button(t("quick_btn_paddy", lang), use_container_width=True, type="primary", key="preset_btn_paddy"):
            apply_farmer_inputs(crop="Rice", quantity=50.0, location="Jangaon", trigger_analysis=True)
            st.session_state.voice_detected_query = t("quick_btn_paddy", lang)
            st.rerun()

    with qcol2:
        if st.button(t("quick_btn_tomato", lang), use_container_width=True, key="preset_btn_tomato"):
            apply_farmer_inputs(crop="Tomato", quantity=1200.0, location="Shamshabad", trigger_analysis=True)
            st.session_state.voice_detected_query = t("quick_btn_tomato", lang)
            st.rerun()

    with qcol3:
        if st.button(t("quick_btn_onion", lang), use_container_width=True, key="preset_btn_onion"):
            apply_farmer_inputs(crop="Onion", quantity=300.0, location="Bhongir", trigger_analysis=True)
            st.session_state.voice_detected_query = t("quick_btn_onion", lang)
            st.rerun()


    st.info(
        f"👈 **{t('btn_customize_inputs', lang)}** — {t('initial_info', lang)}"
    )

    # ========================================================
    # MULTI-DAY QUALITY DEGRADATION MATRIX
    # ========================================================

    with st.expander(f"🌾 {t('educational_matrix_title', lang)}", expanded=True):
        active_display = crop if crop else (t('lbl_none_selected', lang) if t('lbl_none_selected', lang) != 'lbl_none_selected' else "None (Select Crop in Form)")
        st.caption(f"{t('matrix_subtitle', lang)} • Active: {active_display}")

        st.markdown(
            render_degradation_matrix_html(crop, days_diff),
            unsafe_allow_html=True
        )

        crop_highlight = f"selected crop (**{crop}**)" if crop else "crop"
        st.info(
            f"💡 **Scientific Degradation Modeling:** Rows show each crop's degradation progression from harvest day (0 Days) up to 120 Days. "
            f"The table dynamically highlights your currently {crop_highlight} and elapsed days (**~{days_diff or 0}d**). "
            f"Notice how highly perishable crops like **Tomato** drop to Grade C rapidly, incurring severe rot discards, "
            f"whereas durable grains like **Maize**, **Cotton**, and **Rice** retain Grade A for weeks in storage."
        )

    # Feature Overview Cards
    st.markdown(
        f"### 🌾 {t('init_provides', lang)}"
    )

    fcol1, fcol2, fcol3 = st.columns(3)

    with fcol1:
        st.markdown(
            f"""
            <div style="background: var(--rzp-card-bg); border: 1px solid var(--rzp-card-border); border-radius: 14px; padding: 18px; box-shadow: var(--rzp-card-shadow); height: 100%;">
                <h4 style="margin: 0 0 8px 0; color: var(--rzp-text); font-weight: 800;">🏪 Live Mandi Price Radar</h4>
                <p style="font-size: 13.5px; color: var(--rzp-text-muted); line-height: 1.55; margin: 0;">
                    Discovers APMC mandis within your chosen radius (Bowenpally, Gudimalkapur, L.B. Nagar, Shamshabad, etc.) with verified driving distances and live Agmarknet prices.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with fcol2:
        st.markdown(
            f"""
            <div style="background: var(--rzp-card-bg); border: 1px solid var(--rzp-card-border); border-radius: 14px; padding: 18px; box-shadow: var(--rzp-card-shadow); height: 100%;">
                <h4 style="margin: 0 0 8px 0; color: var(--rzp-text); font-weight: 800;">💰 True Net Profit & Logistics</h4>
                <p style="font-size: 13.5px; color: var(--rzp-text-muted); line-height: 1.55; margin: 0;">
                    Calibrated tractor-trolley transit time (~24 km/h), transport fuel rate (₹2.5/km), mandi handling deductions, and post-harvest holding decay to calculate genuine net income.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with fcol3:
        st.markdown(
            f"""
            <div style="background: var(--rzp-card-bg); border: 1px solid var(--rzp-card-border); border-radius: 14px; padding: 18px; box-shadow: var(--rzp-card-shadow); height: 100%;">
                <h4 style="margin: 0 0 8px 0; color: var(--rzp-text); font-weight: 800;">🤖 AI Selling Advisor & Scores</h4>
                <p style="font-size: 13.5px; color: var(--rzp-text-muted); line-height: 1.55; margin: 0;">
                    Multi-factor AI compares future ML price forecasts against crop rot discard penalties to recommend an unambiguous SELL NOW or WAIT decision.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown(
        f"""
        <div style="text-align: center; padding: 16px; color: var(--rzp-text-muted); font-size: 14px;">
            {t('init_how_it_works', lang)}
        </div>
        """,
        unsafe_allow_html=True
    )
