import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def _generate_template_advice(
    crop,
    location,
    quantity,
    quality,
    best_market,
    best_market_location,
    best_market_distance,
    current_price,
    predicted_price,
    decision,
    percentage_change,
    current_revenue,
    predicted_revenue,
    revenue_difference,
    is_small_quantity=False,
    suggested_small_market=None,
    language="en"
):
    if language == "te":
        if decision == "SELL NOW":
            action = f"మీ {crop} పంటను ఇప్పుడే {best_market} మార్కెట్లో అమ్మండి. ప్రస్తుత ధర ₹{current_price:.2f}/కిలో ఎంతో లాభదాయకంగా ఉంది."
            reason = f"3 రోజుల అంచనా ధర ₹{predicted_price:.2f}/కిలో మాత్రమే. నిల్వ ఉంచడం వల్ల పెద్దగా అదనపు లాభం ఉండకపోవచ్చు."
        elif decision == "WAIT":
            action = f"మీ వద్ద సురక్షిత నిల్వ సదుపాయం ఉంటే, {crop} పంటను అమ్మకుండా కొద్ది రోజులు వేచి చూడండి."
            reason = f"రాబోయే మూడు రోజుల్లో ధర సుమారు {percentage_change:.1f}% పెరిగి ₹{predicted_price:.2f}/కిలో అయ్యే అవకాశం ఉంది."
        else:
            action = "మార్కెట్ ధరల హెచ్చుతగ్గులను పరిశీలిస్తూ అమ్మకం నిర్ణయం తీసుకోండి."
            reason = "ధరలో మార్పు తక్కువగా ఉంది."

        quality_advice = "నాణ్యమైన ఏ-గ్రేడ్ పంటకు మార్కెట్లో ఉత్తమ ధర లభిస్తుంది." if quality == "Grade A" else "పంట నాణ్యత తగ్గకముందే జాగ్రత్తగా విక్రయించండి."
        
        return f"""🌾 రైతు మార్కెట్ సలహాదారు (తెలుగు)
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 పంట: {crop}
📍 రైతు ఊరు: {location}
🏪 సిఫార్సు చేసిన మార్కెట్: {best_market} ({best_market_location})
🚚 రహదారి దూరం: {best_market_distance:.1f} కి.మీ
⚖️ పరిమాణం: {quantity:g} కిలోలు
⭐ నాణ్యత: {quality}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 ప్రస్తుత మార్కెట్ ధర: ₹{current_price:.2f}/కిలో
🔮 3 రోజుల అంచనా ధర: ₹{predicted_price:.2f}/కిలో ({percentage_change:+.1f}%)
🤖 AI నిర్ణయం: {decision}
💡 సలహా: {action}
📊 కారణం: {reason}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 రాబడి అంచనా:
• ఇప్పుడే అమ్మితే: ₹{current_revenue:,.2f}
• అంచనా ధర వద్ద: ₹{predicted_revenue:,.2f}
• తేడా: ₹{revenue_difference:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ నాణ్యత సూచన: {quality_advice}
🚚 రవాణా సూచన: సమీప మార్కెట్లను ఎంచుకుంటే రవాణా ఖర్చులు ఆదా అవుతాయి."""

    elif language == "hi":
        if decision == "SELL NOW":
            action = f"अपनी {crop} की उपज को अभी {best_market} में बेचें। वर्तमान भाव ₹{current_price:.2f}/किलो बहुत अच्छा है।"
            reason = f"3 दिन बाद अनुमानित भाव ₹{predicted_price:.2f}/किलो है, इसलिए रुकने से अधिक लाभ की संभावना कम है।"
        elif decision == "WAIT":
            action = f"यदि सुरक्षित भंडारण उपलब्ध है, तो {crop} को कुछ दिन रोककर बेचने पर विचार करें।"
            reason = f"अगले 3 दिनों में भाव {percentage_change:.1f}% बढ़कर लगभग ₹{predicted_price:.2f}/किलो होने का अनुमान है।"
        else:
            action = "मंडी के रुख को ध्यान में रखकर ही बिक्री का अंतिम निर्णय लें।"
            reason = "भाव में परिवर्तन सामान्य रहने की संभावना है।"

        quality_advice = "ग्रेड ए गुणवत्ता की उपज को खरीदार प्राथमिकता और अच्छा भाव देते हैं।" if quality == "Grade A" else "गुणवत्ता में गिरावट से बचने के लिए समय पर बेचें।"

        return f"""🌾 किसान मंडी सलाहकार (हिन्दी)
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 फसल: {crop}
📍 किसान का स्थान: {location}
🏪 अनुशंसित मंडी: {best_market} ({best_market_location})
🚚 सड़क मार्ग दूरी: {best_market_distance:.1f} किमी
⚖️ मात्रा: {quantity:g} किलो
⭐ गुणवत्ता: {quality}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 वर्तमान मंडी भाव: ₹{current_price:.2f}/किलो
🔮 3-दिवसीय अनुमानित भाव: ₹{predicted_price:.2f}/किलो ({percentage_change:+.1f}%)
🤖 AI विक्रय निर्णय: {decision}
💡 सिफारिश: {action}
📊 मुख्य कारण: {reason}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 आय का अनुमान:
• अभी बेचने पर: ₹{current_revenue:,.2f}
• अनुमानित भाव पर: ₹{predicted_revenue:,.2f}
• अपेक्षित अंतर: ₹{revenue_difference:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ गुणवत्ता सलाह: {quality_advice}
🚚 परिवहन सलाह: पास की मंडी चुनने से ढुलाई खर्च में बचत होगी।"""

    elif language == "mr":
        if decision == "SELL NOW":
            action = f"आपला {crop} माल आत्ताच {best_market} बाजारात विकावा. सध्याचा ₹{current_price:.2f}/किलो भाव फायदेशीर आहे."
            reason = f"पुढील ३ दिवसांत अंदाजित भाव ₹{predicted_price:.2f}/किलो असल्याने थांबण्यात जास्त फायदा नाही."
        elif decision == "WAIT":
            action = f"सुरक्षित साठवणूक असल्यास {crop} विक्रीसाठी २-३ दिवस थांबण्याचा विचार करावा."
            reason = f"पुढील ३ दिवसांत भाव {percentage_change:.1f}% वाढून सुमारे ₹{predicted_price:.2f}/किलो होण्याची शक्यता आहे."
        else:
            action = "बाजारातील चढ-उतारांवर लक्ष ठेवून निर्णय घ्या."
            reason = "भावातील बदल मर्यादित आहे."

        quality_advice = "दर्जेदार ग्रेड ए मालाला बाजारात उत्तम भाव मिळतो." if quality == "Grade A" else "मालाची प्रत खराब होण्यापूर्वी वेळेवर विक्री करा."

        return f"""🌾 शेतकरी बाजार सल्लागार (मराठी)
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 पीक: {crop}
📍 शेतकऱ्याचे गाव: {location}
🏪 शिफारस केलेली बाजारपेठ: {best_market} ({best_market_location})
🚚 रस्ता अंतर: {best_market_distance:.1f} किमी
⚖️ प्रमाण: {quantity:g} किलो
⭐ प्रत: {quality}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 सध्याचा बाजारभाव: ₹{current_price:.2f}/किलो
🔮 ३ दिवसांचा अंदाजित भाव: ₹{predicted_price:.2f}/किलो ({percentage_change:+.1f}%)
🤖 AI विक्री निर्णय: {decision}
💡 शिफारस: {action}
📊 कारण: {reason}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 अपेक्षित उत्पन्न:
• आता विकल्यास: ₹{current_revenue:,.2f}
• अंदाजित भावात: ₹{predicted_revenue:,.2f}
• निव्वळ फरक: ₹{revenue_difference:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ प्रत सल्ला: {quality_advice}
🚚 वाहतूक सल्ला: जवळच्या बाजारपेठेत माल नेल्यास वाहतूक खर्च कमी होतो."""

    elif language == "ta":
        if decision == "SELL NOW":
            action = f"உங்கள் {crop} பயிரை இப்போதே {best_market} சந்தையில் விற்கவும். தற்போதைய விலை ₹{current_price:.2f}/கிலோ சிறந்தது."
            reason = f"3 நாள் கணிக்கப்பட்ட விலை ₹{predicted_price:.2f}/கிலோ, எனவே காத்திருப்பதால் அதிக பலன் இல்லை."
        elif decision == "WAIT":
            action = f"பாதுகாப்பான சேமிப்பு வசதி இருந்தால் {crop} விற்பனையை சில நாட்கள் தள்ளிப்போடலாம்."
            reason = f"அடுத்த 3 நாட்களில் விலை {percentage_change:.1f}% உயர்ந்து ₹{predicted_price:.2f}/கிலோ ஆக வாய்ப்புள்ளது."
        else:
            action = "சந்தை நிலவரத்தை கவனித்து முடிவெடுக்கவும்."
            reason = "விலை மாற்றம் குறைவாக உள்ளது."

        quality_advice = "தரம் ஏ பயிர்களுக்கு நல்ல விலை கிடைக்கும்." if quality == "Grade A" else "தரம் குறையும் முன் விற்பனை செய்யவும்."

        return f"""🌾 உழவர் சந்தை ஆலோசகர் (தமிழ்)
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 பயிர்: {crop}
📍 இடம்: {location}
🏪 பரிந்துரைக்கப்பட்ட சந்தை: {best_market} ({best_market_location})
🚚 சாலை தூரம்: {best_market_distance:.1f} கி.மீ
⚖️ அளவு: {quantity:g} கிலோ
⭐ தரம்: {quality}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 தற்போதைய சந்தை விலை: ₹{current_price:.2f}/கிலோ
🔮 கணிக்கப்பட்ட விலை: ₹{predicted_price:.2f}/கிலோ ({percentage_change:+.1f}%)
🤖 AI விற்பனை முடிவு: {decision}
💡 பரிந்துரை: {action}
📊 காரணம்: {reason}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 வருவாய் மதிப்பீடு:
• இப்போது விற்றால்: ₹{current_revenue:,.2f}
• கணிக்கப்பட்ட விலையில்: ₹{predicted_revenue:,.2f}
• எதிர்பார்க்கப்படும் வித்தியாசம்: ₹{revenue_difference:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ தரம் பற்றிய ஆலோசனை: {quality_advice}
🚚 போக்குவரத்து தகவல்: அருகிலுள்ள சந்தைகள் போக்குவரத்து செலவைக் குறைக்கும்."""

    elif language == "kn":
        if decision == "SELL NOW":
            action = f"ನಿಮ್ಮ {crop} ಬೆಳೆಯನ್ನು ಈಗಲೇ {best_market} ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಮಾರಿ. ಪ್ರಸ್ತುತ ₹{current_price:.2f}/ಕೆಜಿ ದರ ಆಕರ್ಷಕವಾಗಿದೆ."
            reason = f"ಮುಂದಿನ 3 ದಿನಗಳ ಮುನ್ಸೂಚನೆ ದರ ₹{predicted_price:.2f}/ಕೆಜಿ ಆಗಿದ್ದು, ಕಾಯುವುದರಿಂದ ಹೆಚ್ಚಿನ ಲಾಭವಿಲ್ಲ."
        elif decision == "WAIT":
            action = f"ಉತ್ತಮ ಗೋದಾಮು ಸೌಲಭ್ಯವಿದ್ದರೆ {crop} ಮಾರಾಟವನ್ನು ಸ್ವಲ್ಪ ದಿನ ಮುಂದೂಡಿ."
            reason = f"ಮುಂದಿನ 3 ದಿನಗಳಲ್ಲಿ ದರ {percentage_change:.1f}% ಏರಿಕೆಯಾಗಿ ₹{predicted_price:.2f}/ಕೆಜಿ ಆಗುವ ಸಾಧ್ಯತೆಯಿದೆ."
        else:
            action = "ಮಾರುಕಟ್ಟೆಯ ಏರಿಳಿತ ಗಮನಿಸಿ ನಿರ್ಧಾರ ತೆಗೆದುಕೊಳ್ಳಿ."
            reason = "ದರ ಬದಲಾವಣೆ ಕಡಿಮೆ ಪ್ರಮಾಣದಲ್ಲಿದೆ."

        quality_advice = "ಗ್ರೇಡ್ ಎ ಬೆಳೆಗೆ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಉತ್ತಮ ಬೆಲೆ ಲಭಿಸುತ್ತದೆ." if quality == "Grade A" else "ಗುಣಮಟ್ಟ ಹಾಳಾಗುವ ಮುನ್ನ ಮಾರಾಟ ಮಾಡಿ."

        return f"""🌾 ರೈತ ಮಾರುಕಟ್ಟೆ ಸಲಹೆಗಾರ (ಕನ್ನಡ)
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 ಬೆಳೆ: {crop}
📍 ರೈತರ ಸ್ಥಳ: {location}
🏪 ಶಿಫಾರಸು ಮಾಡಿದ ಮಾರುಕಟ್ಟೆ: {best_market} ({best_market_location})
🚚 ರಸ್ತೆ ದೂರ: {best_market_distance:.1f} ಕಿ.ಮೀ
⚖️ ಪ್ರಮಾಣ: {quantity:g} ಕೆಜಿ
⭐ ಗುಣಮಟ್ಟ: {quality}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 ಪ್ರಸ್ತುತ ಮಾರುಕಟ್ಟೆ ದರ: ₹{current_price:.2f}/ಕೆಜಿ
🔮 ಮುನ್ಸೂಚನೆ ದರ (3 ದಿನ): ₹{predicted_price:.2f}/ಕೆಜಿ ({percentage_change:+.1f}%)
🤖 AI ಮಾರಾಟ ನಿರ್ಧಾರ: {decision}
💡 ಶಿಫಾರಸು: {action}
📊 ಪ್ರಮುಖ ಕಾರಣ: {reason}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 ಆದಾಯದ ಅಂದಾಜು:
• ಈಗ ಮಾರಾಟ ಮಾಡಿದರೆ: ₹{current_revenue:,.2f}
• ಮುನ್ಸೂಚನೆ ದರದಲ್ಲಿ: ₹{predicted_revenue:,.2f}
• ನಿವ್ವಳ ವ್ಯತ್ಯಾಸ: ₹{revenue_difference:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ ಗುಣಮಟ್ಟ ಸಲಹೆ: {quality_advice}
🚚 ಸಾರಿಗೆ ಮಾಹಿತಿ: ಹತ್ತಿರದ ಮಾರುಕಟ್ಟೆಗಳು ಸಾರಿಗೆ ವೆಚ್ಚವನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತವೆ."""

    # English Default
    if decision == "SELL NOW":
        action = (
            f"Sell your {crop} now at {best_market}. "
            f"The current price of ₹{current_price:.2f}/kg is attractive."
        )
        reason = (
            f"The predicted price is ₹{predicted_price:.2f}/kg, "
            f"so waiting may not provide a significant advantage."
        )
    elif decision == "WAIT":
        action = (
            f"Consider waiting before selling your {crop}, "
            f"provided you have safe storage and can manage "
            f"additional holding costs."
        )
        reason = (
            f"The system predicts the price may increase by "
            f"{percentage_change:.1f}% to approximately "
            f"₹{predicted_price:.2f}/kg."
        )
    else:
        action = "Monitor the market before making the final selling decision."
        reason = "The expected price movement is relatively small."

    if quality == "Grade A":
        quality_advice = (
            "Your Grade A produce may attract better prices "
            "from quality-focused buyers."
        )
    elif quality == "Grade B":
        quality_advice = "Compare multiple nearby markets before selling."
    else:
        quality_advice = (
            "For Grade C produce, consider selling sooner "
            "to reduce quality deterioration."
        )

    sm_section = ""
    if is_small_quantity and suggested_small_market:
        sm_name = suggested_small_market.get("market", "Local Rythu Bazar")
        sm_dist = suggested_small_market.get("distance_km", 0.0)
        sm_net = suggested_small_market.get("small_batch_net_profit", current_revenue)
        sm_section = f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━


🛵 SMALL BATCH ADVICE ({quantity:g} kg)

For a smaller quantity, hiring a commercial vehicle to travel to a distant mandi can erode your profits.
Consider your nearest local market / Rythu Bazar:
• Market: {sm_name} (~{sm_dist:.1f} km away)
• Advantages: 0% middlemen commission, accessible by two-wheeler / auto, direct-to-consumer cash sales.
• Estimated in-hand net: ~₹{sm_net:,.2f}"""

    advice = f"""🌾 FARMER ADVISOR


━━━━━━━━━━━━━━━━━━━━━━━━━━


🌱 Crop:
{crop}

📍 Farmer Location:
{location}

🏪 Recommended Market:
{best_market}

📍 Market Location:
{best_market_location}

🚚 Road Distance to Market:
{best_market_distance:.1f} km (by road)

⚖️ Quantity:
{quantity:g} kg

⭐ Crop Quality:
{quality}


━━━━━━━━━━━━━━━━━━━━━━━━━━


💰 CURRENT MARKET PRICE

₹{current_price:.2f}/kg

🔮 PREDICTED PRICE

₹{predicted_price:.2f}/kg

📈 EXPECTED PRICE CHANGE

{percentage_change:+.1f}%


━━━━━━━━━━━━━━━━━━━━━━━━━━


🤖 AI SELLING DECISION

{decision}

💡 RECOMMENDATION

{action}

📊 WHY?

{reason}


━━━━━━━━━━━━━━━━━━━━━━━━━━


💵 REVENUE ESTIMATION

If sold now:
₹{current_revenue:,.2f}

At predicted price:
₹{predicted_revenue:,.2f}

Expected difference:
₹{revenue_difference:,.2f}


━━━━━━━━━━━━━━━━━━━━━━━━━━


⭐ QUALITY ADVICE

{quality_advice}


━━━━━━━━━━━━━━━━━━━━━━━━━━


🚚 TRANSPORT INFORMATION

Recommended market road distance:
{best_market_distance:.1f} km (driving distance)

Closer markets can reduce transportation
time and transportation expenses.{sm_section}


━━━━━━━━━━━━━━━━━━━━━━━━━━


⚠️ IMPORTANT

Price predictions are estimates based on available
market data. Actual prices may change because of
demand, supply, weather, transportation, storage
conditions and other market factors."""

    return advice.strip()


def _generate_llm_advice(
    crop,
    location,
    quantity,
    quality,
    best_market,
    best_market_location,
    best_market_distance,
    current_price,
    predicted_price,
    decision,
    percentage_change,
    current_revenue,
    predicted_revenue,
    revenue_difference,
    is_small_quantity=False,
    suggested_small_market=None,
    language="en"
):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    from langchain_openai import ChatOpenAI
    from langchain_core.messages import SystemMessage, HumanMessage

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.4,
        max_tokens=600,
        request_timeout=8
    )

    lang_names = {
        "te": "Telugu (తెలుగు)",
        "hi": "Hindi (हिन्दी)",
        "ta": "Tamil (தமிழ்)",
        "kn": "Kannada (ಕನ್ನಡ)",
        "mr": "Marathi (मराठी)",
        "en": "English"
    }
    target_lang_display = lang_names.get(language, "English")

    small_note = ""
    if is_small_quantity and suggested_small_market:
        small_note = f"\n- Small Batch Context: Farmer has only {quantity:g} kg. Emphasize saving transport costs by considering local market / Rythu Bazar {suggested_small_market.get('market')} (~{suggested_small_market.get('distance_km', 0):.1f} km) with 0% commission instead of hiring expensive transport."

    prompt = f"""You are an expert AI Agricultural Market Advisor assisting an Indian farmer in Telangana.
Provide clear, actionable, empathetic, and highly practical selling advice.

LANGUAGE REQUIREMENT:
Write your complete response in {target_lang_display} so the farmer can easily read and understand.
Ensure all numeric values (₹{current_price:.2f}/kg, {quantity:g} kg, {best_market_distance:.1f} km, {percentage_change:+.1f}%) and market names ({best_market}) are kept intact and clear.

FARMER & CROP DETAILS:
- Crop: {crop}
- Location: {location}
- Quantity: {quantity:g} kg
- Quality: {quality}
- Recommended Market: {best_market} ({best_market_location}, ~{best_market_distance:.1f} km away)
- Current Price: ₹{current_price:.2f}/kg
- Predicted Price (3 Days): ₹{predicted_price:.2f}/kg (Expected Change: {percentage_change:+.1f}%)
- System Decision: {decision}
- Estimated Revenue Now: ₹{current_revenue:,.2f}
- Estimated Revenue in 3 Days: ₹{predicted_revenue:,.2f} (Difference: ₹{revenue_difference:,.2f}){small_note}

Format your response cleanly with sections:
1. 💡 Actionable Recommendation ({decision})
2. 📊 Market Rationale & Pricing Outlook
3. 🚚 Logistics & Transportation Guidance (Factor in small batch vs bulk transport cost)
4. 🌾 Quality Handling & Storage Tips

Keep it concise, friendly, and practical for the farmer."""

    messages = [
        SystemMessage(content=f"You are an agricultural economist and mandi advisor in India communicating fluently in {target_lang_display}."),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)
    content = str(response.content).strip()
    return content if content else None


def get_farmer_advice(
    crop,
    location,
    quantity,
    quality,
    best_market,
    best_market_location,
    best_market_distance,
    current_price,
    predicted_price,
    decision,
    is_small_quantity=False,
    suggested_small_market=None,
    language="en"
):
    quantity = float(quantity)
    current_price = float(current_price)
    predicted_price = float(predicted_price)
    best_market_distance = float(best_market_distance)

    price_difference = predicted_price - current_price
    if current_price > 0:
        percentage_change = (price_difference / current_price) * 100
    else:
        percentage_change = 0

    current_revenue = quantity * current_price
    predicted_revenue = quantity * predicted_price
    revenue_difference = predicted_revenue - current_revenue

    # Attempt LLM advice first if available
    try:
        llm_advice = _generate_llm_advice(
            crop, location, quantity, quality,
            best_market, best_market_location, best_market_distance,
            current_price, predicted_price, decision,
            percentage_change, current_revenue, predicted_revenue, revenue_difference,
            is_small_quantity=is_small_quantity,
            suggested_small_market=suggested_small_market,
            language=language
        )
        if llm_advice:
            return llm_advice
    except Exception:
        # Fall back gracefully to template on any error (rate limit, network, timeout)
        pass

    return _generate_template_advice(
        crop, location, quantity, quality,
        best_market, best_market_location, best_market_distance,
        current_price, predicted_price, decision,
        percentage_change, current_revenue, predicted_revenue, revenue_difference,
        is_small_quantity=is_small_quantity,
        suggested_small_market=suggested_small_market,
        language=language
    )