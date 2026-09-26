# -*- coding: utf-8 -*-
"""
services/voice_service.py
-------------------------
Farmer Voice Intelligence Service:
- Multi-lingual Natural Language & Slang Parser (Telugu, Hindi, English)
- Whisper Audio Transcription
- Conversational Semantic Fallback (OpenAI gpt-4o-mini)
- Localized Farmer Voice Script Generation
- High-Speed Text-to-Speech Audio Generation (gTTS with In-Memory Caching)
"""

import os
import re
import io
import base64
import json
import logging
import datetime
from typing import Dict, Any, Optional, Tuple
from functools import lru_cache
from gtts import gTTS

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

logger = logging.getLogger("voice_service")

# ============================================================
# DICTIONARY & REGEX MAPPINGS FOR CROPS
# ============================================================

CROPS_MAP = {
    # 1. Rice / Paddy
    "వరి": "Rice",
    "వరిధాన్యం": "Rice",
    "ధాన్యం": "Rice",
    "బియ్యం": "Rice",
    "ప్యాడీ": "Rice",
    "వడ్లు": "Rice",
    "వరి పంట": "Rice",
    "వరి ధాన్యం": "Rice",
    "paddy": "Rice",
    "rice": "Rice",
    "dhan": "Rice",
    "धान": "Rice",
    "चावल": "Rice",
    "धान्य": "Rice",
    "அரிசி": "Rice",
    "நெல்": "Rice",
    "ಅಕ್ಕಿ": "Rice",
    "ಭತ್ತ": "Rice",
    "तांदूळ": "Rice",
    "भात": "Rice",

    # 2. Maize
    "మొక్కజొన్న": "Maize",
    "జొన్నలు": "Maize",
    "కంకులు": "Maize",
    "మక్క": "Maize",
    "మక్కలు": "Maize",
    "maize": "Maize",
    "corn": "Maize",
    "makka": "Maize",
    "मक्का": "Maize",
    "भुट्टा": "Maize",
    "மக்காச்சோளம்": "Maize",
    "ಜೋಳ": "Maize",
    "मका": "Maize",

    # 3. Jowar (Sorghum)
    "జొన్న": "Jowar",
    "తెల్ల జొన్న": "Jowar",
    "పచ్చ జొన్న": "Jowar",
    "jowar": "Jowar",
    "sorghum": "Jowar",
    "ज्वार": "Jowar",
    "சோளம்": "Jowar",
    "ಬಿಳಿ ಜೋಳ": "Jowar",
    "ಜ್ವಾರಿ": "Jowar",
    "ज्वारी": "Jowar",

    # 4. Bajra (Pearl Millet)
    "సజ్జలు": "Bajra",
    "సజ్జ": "Bajra",
    "bajra": "Bajra",
    "pearl millet": "Bajra",
    "बाजरा": "Bajra",
    "கம்பு": "Bajra",
    "ಸಜ್ಜೆ": "Bajra",
    "बाजरी": "Bajra",

    # 5. Ragi (Finger Millet)
    "రాగులు": "Ragi",
    "రాగి": "Ragi",
    "తైదలు": "Ragi",
    "ragi": "Ragi",
    "finger millet": "Ragi",
    "रागी": "Ragi",
    "मंडुआ": "Ragi",
    "கேழ்வரகு": "Ragi",
    "ರಾಗಿ": "Ragi",
    "नाचणी": "Ragi",

    # 6. Red Gram (Tur / Arhar)
    "కందులు": "Red Gram",
    "కంది": "Red Gram",
    "కంది పప్పు": "Red Gram",
    "red gram": "Red Gram",
    "tur": "Red Gram",
    "arhar": "Red Gram",
    "toor": "Red Gram",
    "अरहर": "Red Gram",
    "तुअर": "Red Gram",
    "तुवर": "Red Gram",
    "துவரம் பருப்பு": "Red Gram",
    "துவரை": "Red Gram",
    "ತೊಗರಿ": "Red Gram",
    "ತೊಗರಿ ಬೇಳೆ": "Red Gram",
    "तूर": "Red Gram",
    "तूर डाळ": "Red Gram",

    # 7. Bengal Gram (Chana / Chickpea)
    "శనగలు": "Bengal Gram",
    "శనగ": "Bengal Gram",
    "హరిభరా": "Bengal Gram",
    "చనా": "Bengal Gram",
    "bengal gram": "Bengal Gram",
    "chana": "Bengal Gram",
    "gram": "Bengal Gram",
    "chickpea": "Bengal Gram",
    "चना": "Bengal Gram",
    "काबुली चना": "Bengal Gram",
    "కొండైక్కదలై": "Bengal Gram",
    "கொண்டைக்கடலை": "Bengal Gram",
    "கடலை": "Bengal Gram",
    "ಕಡಲೆ": "Bengal Gram",
    "ಕಡಲೆ ಕಾಳು": "Bengal Gram",
    "हरभरा": "Bengal Gram",

    # 8. Green Gram (Moong)
    "పెసలు": "Green Gram",
    "పెసర": "Green Gram",
    "పెసరపప్పు": "Green Gram",
    "green gram": "Green Gram",
    "moong": "Green Gram",
    "mung": "Green Gram",
    "मूंग": "Green Gram",
    "मूंग दाल": "Green Gram",
    "பாசிப்பயறு": "Green Gram",
    "ಹೆಸರು ಕಾಳು": "Green Gram",
    "ಹೆಸರು": "Green Gram",
    "मूग": "Green Gram",

    # 9. Black Gram (Urad)
    "మినుములు": "Black Gram",
    "మినుము": "Black Gram",
    "మినప్పప్పు": "Black Gram",
    "black gram": "Black Gram",
    "urad": "Black Gram",
    "urid": "Black Gram",
    "उड़द": "Black Gram",
    "उरद": "Black Gram",
    "உளுந்து": "Black Gram",
    "உளுந்தம்பருப்பு": "Black Gram",
    "ಉದ್ದಿನ ಬೇಳೆ": "Black Gram",
    "ಉದ್ದು": "Black Gram",
    "उडीद": "Black Gram",

    # 10. Groundnut (Peanut)
    "వేరుశనగ": "Groundnut",
    "పల్లీ": "Groundnut",
    "పల్లీలు": "Groundnut",
    "వేరుశనగకాయలు": "Groundnut",
    "groundnut": "Groundnut",
    "peanut": "Groundnut",
    "peanuts": "Groundnut",
    "palli": "Groundnut",
    "मूंगफली": "Groundnut",
    "நிலக்கடலை": "Groundnut",
    "வேர்க்கடலை": "Groundnut",
    "ಕಡಲೆಕಾಯಿ": "Groundnut",
    "ಶೇಂಗಾ": "Groundnut",
    "शेंगदाणा": "Groundnut",
    "भुईमूग": "Groundnut",

    # 11. Soybean
    "సోయాబీన్": "Soybean",
    "సోయా": "Soybean",
    "soybean": "Soybean",
    "soya": "Soybean",
    "soyabean": "Soybean",
    "सोयाबीन": "Soybean",
    "சோயாபீன்": "Soybean",
    "சோயா": "Soybean",
    "ಸೋಯಾಬೀನ್": "Soybean",

    # 12. Sunflower
    "పొద్దుతిరుగుడు": "Sunflower",
    "పొద్దు తిరుగుడు": "Sunflower",
    "sunflower": "Sunflower",
    "सूरजमुखी": "Sunflower",
    "சூரியகாந்தி": "Sunflower",
    "ಸೂರ್ಯಕಾಂತಿ": "Sunflower",
    "सूर्यफूल": "Sunflower",

    # 13. Sesamum (Til)
    "నువ్వులు": "Sesamum",
    "నువ్వుల": "Sesamum",
    "sesamum": "Sesamum",
    "sesame": "Sesamum",
    "til": "Sesamum",
    "तिल": "Sesamum",
    "எள்": "Sesamum",
    "எள்ளு": "Sesamum",
    "ಎಳ್ಳು": "Sesamum",
    "तीळ": "Sesamum",

    # 14. Castor
    "ఆముదం": "Castor",
    "ఆముదాలు": "Castor",
    "ఆముదపు విత్తనాలు": "Castor",
    "castor": "Castor",
    "castor seed": "Castor",
    "अरंडी": "Castor",
    "ஆமணக்கு": "Castor",
    "ಕೊಟ್ಟೈಮುತ್ತು": "Castor",
    "ಹರಳು": "Castor",
    "ಹರಳೆಣ್ಣೆ": "Castor",
    "एरंडी": "Castor",
    "एरंड": "Castor",

    # 15. Chilli
    "మిర్చి": "Chilli",
    "మిరప": "Chilli",
    "మిరపకాయ": "Chilli",
    "మిరపకాయలు": "Chilli",
    "పచ్చిమిర్చి": "Chilli",
    "ఎండుమిర్చి": "Chilli",
    "chilli": "Chilli",
    "chili": "Chilli",
    "chillies": "Chilli",
    "mirchi": "Chilli",
    "mirch": "Chilli",
    "मिर्च": "Chilli",
    "हरी मिर्च": "Chilli",
    "लाल मिर्च": "Chilli",
    "மிளகாய்": "Chilli",
    "பச்சை மிளகாய்": "Chilli",
    "மெಣಸಿನಕಾಯಿ": "Chilli",
    "ಹಸಿರು ಮೆಣಸಿನಕಾಯಿ": "Chilli",
    "मिरची": "Chilli",
    "हिरवी मिरची": "Chilli",

    # 16. Cotton
    "పత్తి": "Cotton",
    "ప్రత్తి": "Cotton",
    "దూది": "Cotton",
    "కపాస్": "Cotton",
    "cotton": "Cotton",
    "kapas": "Cotton",
    "कपास": "Cotton",
    "रूई": "Cotton",
    "பருத்தி": "Cotton",
    "ಹತ್ತಿ": "Cotton",
    "कापूस": "Cotton",

    # 17. Turmeric
    "పసుపు": "Turmeric",
    "పసుపు కొమ్ములు": "Turmeric",
    "turmeric": "Turmeric",
    "haldi": "Turmeric",
    "हल्दी": "Turmeric",
    "மஞ்சள்": "Turmeric",
    "ಅರಿಶಿನ": "Turmeric",
    "हळद": "Turmeric",

    # 18. Ginger
    "అల్లం": "Ginger",
    "పచ్చి అల్లం": "Ginger",
    "ginger": "Ginger",
    "adrak": "Ginger",
    "अदरक": "Ginger",
    "இஞ்சி": "Ginger",
    "ಶುಂಠಿ": "Ginger",
    "आले": "Ginger",
    "अद्रक": "Ginger",

    # 19. Garlic
    "వెల్లుల్లి": "Garlic",
    "వెల్లుల్లిపాయ": "Garlic",
    "ఎల్లిపాయ": "Garlic",
    "garlic": "Garlic",
    "lahsun": "Garlic",
    "लहसुन": "Garlic",
    "பூண்டு": "Garlic",
    "ಬೆಳ್ಳುಳ್ಳಿ": "Garlic",
    "लसूण": "Garlic",

    # 20. Tomato
    "టమాటా": "Tomato",
    "టమోటా": "Tomato",
    "టమాటాలు": "Tomato",
    "టమోటాలు": "Tomato",
    "తక్కాళి": "Tomato",
    "tomato": "Tomato",
    "tomatoes": "Tomato",
    "tamatar": "Tomato",
    "टमाटर": "Tomato",
    "தக்காளி": "Tomato",
    "ಟೊಮೆಟೊ": "Tomato",
    "टोमॅटो": "Tomato",

    # 21. Onion
    "ఉల్లి": "Onion",
    "ఉల్లిపాయ": "Onion",
    "ఉల్లిపాయలు": "Onion",
    "ఉల్లిగడ్డ": "Onion",
    "ఉల్లిగడ్డలు": "Onion",
    "ఎర్రగడ్డ": "Onion",
    "ఎర్రగడ్డలు": "Onion",
    "onion": "Onion",
    "onions": "Onion",
    "pyaj": "Onion",
    "pyaaz": "Onion",
    "प्याज": "Onion",
    "कांदा": "Onion",
    "வெங்காயம்": "Onion",
    "ಈರುಳ್ಳಿ": "Onion",

    # 22. Brinjal (Eggplant)
    "వంకాయ": "Brinjal",
    "వంకాయలు": "Brinjal",
    "గుత్తి వంకాయ": "Brinjal",
    "brinjal": "Brinjal",
    "eggplant": "Brinjal",
    "baingan": "Brinjal",
    "बैंगन": "Brinjal",
    "கத்தரிக்காய்": "Brinjal",
    "ಬದನೆಕಾಯಿ": "Brinjal",
    "वांगी": "Brinjal",

    # 23. Bhendi (Ladies Finger / Okra)
    "బెండకాయ": "Bhendi",
    "బెండకాయలు": "Bhendi",
    "బెండ": "Bhendi",
    "bhendi": "Bhendi",
    "bhindi": "Bhendi",
    "ladies finger": "Bhendi",
    "okra": "Bhendi",
    "भिंडी": "Bhendi",
    "வெண்டைக்காய்": "Bhendi",
    "ಬೆಂಡೆಕಾಯಿ": "Bhendi",
    "भेंडी": "Bhendi",

    # 24. Bitter Gourd
    "కాకరకాయ": "Bitter Gourd",
    "కాకరకాయలు": "Bitter Gourd",
    "కాకర": "Bitter Gourd",
    "bitter gourd": "Bitter Gourd",
    "karela": "Bitter Gourd",
    "करेला": "Bitter Gourd",
    "பாகற்காய்": "Bitter Gourd",
    "ಹಾಗಲಕಾಯಿ": "Bitter Gourd",
    "कारले": "Bitter Gourd",
}

# ============================================================
# DICTIONARY & REGEX MAPPINGS FOR LOCATIONS
# ============================================================

LOCATIONS_MAP = {
    "జనగాం": "Jangaon",
    "జనగామ": "Jangaon",
    "జనగాన్": "Jangaon",
    "jangaon": "Jangaon",
    "janagaon": "Jangaon",
    "जनगांव": "Jangaon",
    "जनगाँव": "Jangaon",
    "ಜನಗಾಂ": "Jangaon",
    "ஜங்காவ்": "Jangaon",

    "హైదరాబాద్": "Hyderabad",
    "హైదరాబాదు": "Hyderabad",
    "భాగ్యనగరం": "Hyderabad",
    "hyderabad": "Hyderabad",
    "हैदराबाद": "Hyderabad",
    "ಹೈದರಾಬಾದ್": "Hyderabad",
    "ஹைதராபாத்": "Hyderabad",

    "శంషాబాద్": "Shamshabad",
    "shamshabad": "Shamshabad",
    "शमशाबाद": "Shamshabad",
    "ಶಂಶಾಬಾದ್": "Shamshabad",
    "சம்ஷாபாத்": "Shamshabad",

    "భువనగిరి": "Bhongir",
    "భోంగీర్": "Bhongir",
    "భోంగిర్": "Bhongir",
    "bhongir": "Bhongir",
    "bhuvanagiri": "Bhongir",
    "भोंगीर": "Bhongir",
    "भुवनगिरि": "Bhongir",
    "ಭೋಂಗೀರ್": "Bhongir",
    "போங்கிர்": "Bhongir",

    "సిద్దిపేట": "Siddipet",
    "సిద్దిపేట్": "Siddipet",
    "siddipet": "Siddipet",
    "सिद्दिपेट": "Siddipet",
    "सिद्धिपेट": "Siddipet",
    "ಸಿದ್ದಿಪೇಟೆ": "Siddipet",
    "சித்திபேட்டை": "Siddipet",

    "వరంగల్": "Warangal",
    "వారంగల్": "Warangal",
    "warangal": "Warangal",
    "वरंगल": "Warangal",
    "वारंगल": "Warangal",
    "ವಾರಂಗಲ್": "Warangal",
    "வாரங்கல்": "Warangal",

    "సూర్యాపేట": "Suryapet",
    "సూర్యాపేట్": "Suryapet",
    "suryapet": "Suryapet",
    "सूर्यापेट": "Suryapet",
    "ಸೂರ್ಯಾಪೇಟೆ": "Suryapet",
    "சூர்யாபேட்டை": "Suryapet",

    "మేడ్చల్": "Medchal",
    "మెడ్చల్": "Medchal",
    "medchal": "Medchal",
    "मेडचल": "Medchal",
    "ಮೆಡ್ಚಲ್": "Medchal",

    "చేవెళ్ల": "Chevella",
    "చేవెళ్ళ": "Chevella",
    "chevella": "Chevella",
    "चेवेल्ला": "Chevella",

    "గజ్వేల్": "Gajwel",
    "gajwel": "Gajwel",
    "गजवेल": "Gajwel",

    "ఆలేరు": "Alair",
    "alair": "Alair",
    "आलेर": "Alair",

    "షాద్‌నగర్": "Shadnagar",
    "షాద్ నగర్": "Shadnagar",
    "shadnagar": "Shadnagar",
    "शादनगर": "Shadnagar",

    "ఘట్‌కేసర్": "Ghatkesar",
    "ఘట్ కేసర్": "Ghatkesar",
    "ghatkesar": "Ghatkesar",
    "घाटकेसर": "Ghatkesar",

    "బోయిన్‌పల్లి": "Bowenpally",
    "బోయిన్ పల్లి": "Bowenpally",
    "bowenpally": "Bowenpally",
    "बोवेनपल्ली": "Bowenpally",

    "గుడిమల్కాపూర్": "Gudimalkapur",
    "gudimalkapur": "Gudimalkapur",
    "गुडीमलकापुर": "Gudimalkapur",

    "ఎల్బీ నగర్": "L.B. Nagar",
    "ఎల్.బి. నగర్": "L.B. Nagar",
    "lb nagar": "L.B. Nagar",
    "एल बी नगर": "L.B. Nagar",

    "నల్గొండ": "Nalgonda",
    "నల్లగొండ": "Nalgonda",
    "nalgonda": "Nalgonda",
    "नलगाेंडा": "Nalgonda",
    "नलगोंडा": "Nalgonda",
    "ನಲ್ಗೊಂಡ": "Nalgonda",
    "நல்கொண்டா": "Nalgonda",

    "నిజామాబాద్": "Nizamabad",
    "నిజామాబాదు": "Nizamabad",
    "nizamabad": "Nizamabad",
    "निज़ामाबाद": "Nizamabad",
    "निजामाबाद": "Nizamabad",
    "ನಿಜಾಮಾಬಾದ್": "Nizamabad",
    "நிசாமாபாத்": "Nizamabad",

    "కరీంనగర్": "Karimnagar",
    "karimnagar": "Karimnagar",
    "करीमनगर": "Karimnagar",
    "ಕರೀಂನಗರ": "Karimnagar",
    "கரீம்நகர்": "Karimnagar",

    "ఖమ్మం": "Khammam",
    "khammam": "Khammam",
    "खम्मम": "Khammam",
    "खमम": "Khammam",
    "ಖಮ್ಮಂ": "Khammam",
    "கம்மம்": "Khammam",

    "మహబూబ్‌నగర్": "Mahabubnagar",
    "మహబూబ్ నగర్": "Mahabubnagar",
    "mahabubnagar": "Mahabubnagar",
    "महबूबनगर": "Mahabubnagar",
    "ಮಹಬೂಬ್‌ನಗರ": "Mahabubnagar",
    "மகபூப்நகர்": "Mahabubnagar",
}

# Number words mapping (Telugu, Hindi, English, Tamil, Kannada, Marathi)
NUMBER_WORDS = {
    # Telugu
    "పది": 10,
    "ఇరవై": 20,
    "ముప్పై": 30,
    "నలభై": 40,
    "యాభై": 50,
    "అరవై": 60,
    "డెబ్బై": 70,
    "ఎనభై": 80,
    "తొంభై": 90,
    "వంద": 100,
    "రెండు వందలు": 200,
    "రెండు వందల": 200,
    "ఐదు వందలు": 500,
    "ఐదు వందల": 500,
    "వెయ్యి": 1000,
    "వెయ్య": 1000,
    "పన్నెండు వందలు": 1200,
    "పన్నెండు వందల": 1200,
    "పదిహేను వందలు": 1500,
    "రెండు వేలు": 2000,

    # Hindi / Marathi
    "दस": 10,
    "दहा": 10,
    "बीस": 20,
    "वीस": 20,
    "तीस": 30,
    "चालीस": 40,
    "चाळीस": 40,
    "पचास": 50,
    "पन्नास": 50,
    "साठ": 60,
    "सत्तर": 70,
    "अस्सी": 80,
    "ऐंशी": 80,
    "नब्बे": 90,
    "नव्वद": 90,
    "सौ": 100,
    "शंभर": 100,
    "एक सौ": 100,
    "दो सौ": 200,
    "दोनशे": 200,
    "तीन सौ": 300,
    "तीनशे": 300,
    "चार सौ": 400,
    "चारशे": 400,
    "पांच सौ": 500,
    "पाँच सौ": 500,
    "पाचशे": 500,
    "हज़ार": 1000,
    "हजार": 1000,
    "एक हज़ार": 1000,
    "एक हजार": 1000,
    "बारह सौ": 1200,
    "पंद्रह सौ": 1500,
    "दो हज़ार": 2000,
    "दोन हजार": 2000,

    # Tamil
    "பத்து": 10,
    "இருபது": 20,
    "முப்பது": 30,
    "நாற்பது": 40,
    "ஐம்பது": 50,
    "அறுபது": 60,
    "எழுபது": 70,
    "எண்பது": 80,
    "தொண்ணூறு": 90,
    "நூறு": 100,
    "இருநூறு": 200,
    "ஐந்நூறு": 500,
    "ஆயிரம்": 1000,
    "இரண்டாயிரம்": 2000,

    # Kannada
    "ಹತ್ತು": 10,
    "ಇಪ್ಪತ್ತು": 20,
    "ಮೂವತ್ತು": 30,
    "ನಲವತ್ತು": 40,
    "ಐವತ್ತು": 50,
    "ಅರವತ್ತು": 60,
    "ಎಪ್ಪತ್ತು": 70,
    "ಎಂಬತ್ತು": 80,
    "ತೊಂಬತ್ತು": 90,
    "ನೂರು": 100,
    "ಇನ್ನೂರು": 200,
    "ಐನೂರು": 500,
    "ಸಾವಿರ": 1000,
    "ಎರಡು ಸಾವಿರ": 2000,

    # English
    "ten": 10,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "one hundred": 100,
    "two hundred": 200,
    "five hundred": 500,
    "thousand": 1000,
    "one thousand": 1000,
    "twelve hundred": 1200,
    "fifteen hundred": 1500,
    "two thousand": 2000,
}

# Indic digits mapping (Telugu, Devanagari, Kannada, Tamil)
INDIC_DIGITS = {
    '౦': '0', '౧': '1', '౨': '2', '౩': '3', '౪': '4', '౫': '5', '౬': '6', '౭': '7', '౮': '8', '౯': '9',
    '०': '0', '१': '1', '२': '2', '३': '3', '४': '4', '५': '5', '६': '6', '७': '7', '८': '8', '९': '9',
    '೦': '0', '೧': '1', '೨': '2', '೩': '3', '೪': '4', '೫': '5', '೬': '6', '೭': '7', '೮': '8', '೯': '9',
    '௧': '1', '௨': '2', '௩': '3', '௪': '4', '௫': '5', '௬': '6', '௭': '7', '௮': '8', '௯': '9'
}

# Audio cache to prevent re-synthesizing identical text
_TTS_CACHE: Dict[str, str] = {}


def normalize_digits(text: str) -> str:
    """Converts Telugu/Devanagari/Kannada/Tamil numeral characters into standard ASCII digits."""
    for ind, asc in INDIC_DIGITS.items():
        text = text.replace(ind, asc)
    return text


def detect_language(text: str) -> str:
    """
    Automatically detect whether spoken text is in:
    - Telugu (te)
    - Hindi (hi)
    - Tamil (ta)
    - Kannada (kn)
    - Marathi (mr)
    - English (en)
    Uses Unicode script ranges with high-accuracy lexical disambiguation.
    """
    if not text:
        return "en"

    # Telugu script range: \u0C00-\u0C7F
    if re.search(r'[\u0C00-\u0C7F]', text):
        return "te"
    # Tamil script range: \u0B80-\u0BFF
    if re.search(r'[\u0B80-\u0BFF]', text):
        return "ta"
    # Kannada script range: \u0C80-\u0CFF
    if re.search(r'[\u0C80-\u0CFF]', text):
        return "kn"
    # Devanagari script range: \u0900-\u097F (used by Hindi and Marathi)
    if re.search(r'[\u0900-\u097F]', text):
        # Disambiguate Marathi vs Hindi:
        # Marathi unique letter: ळ (\u0933)
        if 'ळ' in text or '\u0933' in text:
            return "mr"
        # Marathi distinctive common words
        marathi_words = ["आहे", "नाही", "शेतकरी", "कांदा", "बाजार", "रुपये", "पाहिजे", "कसा", "गाव", "सांगा", "करा", "भावात", "पोती", "तूर", "मूग", "उडीद"]
        if any(mw in text for mw in marathi_words):
            return "mr"
        return "hi"

    # Romanized speech fallback checking
    text_lower = text.lower()
    marathi_kw = ["kanda", "she शे", "bajar", "ahe", "paje", "bhavat", "rupaye", "poti"]
    telugu_kw = ["kilo", "biyyam", "vaddlu", "patti", "mirchi", "jonna", "kandulu", "basta", "bastal", "eppudu", "ammali", "daggara", "tamata"]
    hindi_kw = ["kisan", "tamatar", "chawal", "dhan", "kapas", "mirch", "makka", "pyaj", "pyaaz", "bechna", "mandi", "bhav"]
    tamil_kw = ["arisi", "thakkali", "vengayam", "paruthi", "vilai", "enna", "moottai"]
    kannada_kw = ["akki", "togari", "bele", "irulli", "dara", "yelli", "mote"]

    for w in telugu_kw:
        if re.search(r'\b' + re.escape(w) + r'\b', text_lower):
            return "te"
    for w in hindi_kw:
        if re.search(r'\b' + re.escape(w) + r'\b', text_lower):
            return "hi"
    for w in tamil_kw:
        if re.search(r'\b' + re.escape(w) + r'\b', text_lower):
            return "ta"
    for w in kannada_kw:
        if re.search(r'\b' + re.escape(w) + r'\b', text_lower):
            return "kn"
    for w in marathi_kw:
        if re.search(r'\b' + re.escape(w) + r'\b', text_lower):
            return "mr"

    return "en"


def parse_spoken_date(s: str) -> Optional[datetime.date]:
    """Parse spoken date formats (DD/MM/YY, DD-MM-YYYY, YYYY-MM-DD, spoken spaced digits like '26 9 20 26', or today/tomorrow)."""
    if not s:
        return None
    s = str(s).strip()
    today = datetime.date.today()
    if re.search(r'\b(today|ఈ\s*రోజు|ఈరోజు|आज)\b', s, re.IGNORECASE):
        return today
    if re.search(r'\b(tomorrow|రేపు|कल)\b', s, re.IGNORECASE):
        return today + datetime.timedelta(days=1)
    if re.search(r'\b(yesterday|నిన్న|बीता\s*कल)\b', s, re.IGNORECASE):
        return today - datetime.timedelta(days=1)

    # DD/MM/YYYY, DD/MM/YY, YYYY-MM-DD, DD-MM-YYYY
    m_slash = re.search(r'(\d{1,4})[\/\-\.](\d{1,2})[\/\-\.](\d{1,4})', s)
    if m_slash:
        p1, p2, p3 = int(m_slash.group(1)), int(m_slash.group(2)), int(m_slash.group(3))
        if p1 > 1000:
            y, m, d = p1, p2, p3
        else:
            d, m, y = p1, p2, p3
            if y < 100:
                y += 2000
        try:
            return datetime.date(y, m, d)
        except ValueError:
            pass

    # Spoken spaced numbers e.g. '26 9 20 26' -> 26, 9, 2026 or '26 9 2026'
    nums = [int(n) for n in re.findall(r'\d+', s)]
    if len(nums) == 4 and nums[2] == 20:
        d, m, y = nums[0], nums[1], 2000 + nums[3]
        try:
            return datetime.date(y, m, d)
        except ValueError:
            pass
    elif len(nums) == 3:
        d, m, y = nums[0], nums[1], nums[2]
        if y < 100:
            y += 2000
        try:
            return datetime.date(y, m, d)
        except ValueError:
            pass

    return None


def extract_dates_from_query(text: str) -> Tuple[Optional[datetime.date], Optional[datetime.date]]:
    """Extract harvest_date and price_date if spoken in the farmer's query."""
    norm = normalize_digits(text.strip())
    h_date = None
    p_date = None

    # Harvest date pattern
    h_pat = re.search(
        r'(?:harvest(?:\s+date)?|harvested(?:\s+on)?|కోత(?:\s*తేదీ)?|కోత|कटाई(?:\s*तारीख)?)(?:\s+is|\s*:)?\s*([0-9\/\-\.\s\w]+?)(?=\s+and|\s+the\s+price|\s+price|\s*$)',
        norm,
        re.IGNORECASE
    )
    if h_pat:
        h_date = parse_spoken_date(h_pat.group(1))

    # Price date pattern
    p_pat = re.search(
        r'(?:price(?:\s+date)?|market(?:\s+date)?|ధర(?:\s*తేదీ)?|మార్కెట్(?:\s*తేదీ)?|भाव(?:\s*तारीख)?)(?:\s+is|\s*:)?\s*([0-9\/\-\.\s\w]+?)(?=\s+and|\s+the\s+harvest|\s+harvest|\s*$)',
        norm,
        re.IGNORECASE
    )
    if p_pat:
        p_date = parse_spoken_date(p_pat.group(1))

    return h_date, p_date


def parse_quantity_and_unit(text: str) -> Optional[float]:
    """Extract numeric quantity considering units (kg, quintal, bag, ton) across all 6 languages."""
    norm = normalize_digits(text.lower())

    # Look for digits WITH an explicit unit first (prevents dates from matching as quantity)
    unit_explicit_pattern = (
        r'(\d+(?:\.\d+)?)\s*'
        r'(కిలోలు|కేజీలు|కేజీ|కిలో|kg|kgs|किलो|किग्रा|கிலோ|கிலோகிராம்|ಕಿಲೋ|ಕಿಲೋಗ್ರಾಂ|'
        r'క్వింటాల్|క్వింటాళ్లు|quintal|quintals|क्विंटल|குவிண்டால்|ಕ್ವಿಂಟಾಲ್|'
        r'బస్తా|బస్తాలు|బాగ్|bags|bag|बोरी|बोरे|మూட்டை|మూட்டைகள்|ಚೀಲ|ಚೀಲಗಳು|पोती|पोत्या|'
        r'టన్నులు|టన్ను|ton|tons|tonne|टन|டன்|ಟನ್)\b'
    )
    match = re.search(unit_explicit_pattern, norm)
    
    if match:
        num = float(match.group(1))
        unit = match.group(2) or ""
    else:
        # Check named number words first if no digits with unit
        base_qty = None
        for word, val in NUMBER_WORDS.items():
            if word in norm:
                base_qty = float(val)
                break

        # Fallback to optional unit pattern
        units_pattern = (
            r'(\d+(?:\.\d+)?)\s*'
            r'(కిలోలు|కేజీలు|కేజీ|కిలో|kg|kgs|किलो|किग्रा|கிலோ|கிலோகிராம்|ಕಿಲೋ|ಕಿಲೋಗ್ರಾಂ|'
            r'క్వింటాల్|క్వింటాళ్లు|quintal|quintals|क्विंटल|குவிண்டால்|ಕ್ವಿಂಟಾಲ್|'
            r'బస్తా|బస్తాలు|బాగ్|bags|bag|बोरी|बोरे|మూட்டை|మూட்டைகள்|ಚೀಲ|ಚೀಲಗಳು|पोती|पोत्या|'
            r'టన్నులు|టన్ను|ton|tons|tonne|टन|டன்|ಟನ್)?'
        )
        m_fallback = re.search(units_pattern, norm)
        if m_fallback and m_fallback.group(2):
            num = float(m_fallback.group(1))
            unit = m_fallback.group(2)
        elif base_qty is not None:
            num = base_qty
            unit = ""
            for u in [
                "క్వింటాల్", "క్వింటాళ్లు", "quintal", "क्विंटल", "குவிண்டால்", "ಕ್ವಿಂಟಾಲ್",
                "బస్తా", "బస్తాలు", "bags", "बोरी", "మూட்டை", "ಚೀಲ", "पोती",
                "టన్ను", "ton", "टन", "டன்", "ಟನ್"
            ]:
                if u in norm:
                    unit = u
                    break
        elif m_fallback and not re.search(r'\b(date|harvest|price|తేదీ|तारीख)\b', norm):
            num = float(m_fallback.group(1))
            unit = ""
        else:
            return None

    unit = unit.lower()
    # Apply unit multipliers
    if any(q in unit for q in ["క్వింటా", "quintal", "क्विंटल", "குவிண்டால்", "ಕ್ವಿಂಟಾಲ್"]):
        return num * 100.0
    elif any(b in unit for b in ["బస్తా", "bag", "బోరి", "बोरी", "बोरे", "మూட்டை", "ಚೀಲ", "पोती"]):
        return num * 50.0  # Standard agri bag is 50kg
    elif any(t in unit for t in ["టన్ను", "ton", "टन", "டன்", "ಟನ್"]):
        return num * 1000.0
    else:
        return num


def extract_parameters_regex(text: str) -> Dict[str, Any]:
    """Extract crop, quantity, location, harvest_date, and price_date using high-speed dictionary & regex matching."""
    norm = normalize_digits(text.strip())
    cleaned = re.sub(r'[,.?!;:\-_"\'()\[\]]', ' ', norm)
    detected_lang = detect_language(norm)

    found_crop = None
    for phrase, canonical in sorted(CROPS_MAP.items(), key=lambda x: -len(x[0])):
        pattern = r'(?:\b|[^\w]|^)' + re.escape(phrase) + r'(?:\b|[^\w]|$)'
        if re.search(pattern, cleaned, re.IGNORECASE) or phrase.lower() in cleaned.lower():
            found_crop = canonical
            break

    found_loc = None
    for phrase, canonical in sorted(LOCATIONS_MAP.items(), key=lambda x: -len(x[0])):
        pattern = r'(?:\b|[^\w]|^)' + re.escape(phrase) + r'(?:\b|[^\w]|$)'
        if re.search(pattern, cleaned, re.IGNORECASE) or phrase.lower() in cleaned.lower():
            found_loc = canonical
            break

    found_qty = parse_quantity_and_unit(cleaned)
    found_harvest_date, found_price_date = extract_dates_from_query(text)

    return {
        "crop": found_crop,
        "quantity": found_qty,
        "location": found_loc,
        "harvest_date": found_harvest_date,
        "price_date": found_price_date,
        "language": detected_lang,
        "raw_text": text
    }


def extract_parameters_with_llm_fallback(text: str, default_lang: str = "te") -> Dict[str, Any]:
    """
    Extract crop, quantity, location, harvest_date, and price_date.
    If regex finds all parameters, returns immediately.
    Otherwise uses OpenAI gpt-4o-mini for complex conversational phrases.
    """
    result = extract_parameters_regex(text)
    
    # If all three core params were cleanly extracted, return immediately
    if result["crop"] and result["quantity"] and result["location"]:
        return result

    # Check for OpenAI API Key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return result

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        valid_crops_str = ", ".join([f'"{c}"' for c in sorted(set(CROPS_MAP.values()))])
        prompt = f"""You are an agricultural voice assistant parsing spoken farmer queries in Telugu, Hindi, English, Tamil, Kannada, or Marathi.
Extract crop, quantity (in kg), farmer location, harvest date (YYYY-MM-DD or null), and price date (YYYY-MM-DD or null) from this spoken query:
"{text}"

Valid Crops: {valid_crops_str}
Note on Quantities:
- Always convert bags (బస్తాలు/बोरी/மூட்டை/ಚೀಲ/पोती) to kg (1 bag = 50 kg)
- Convert quintals (క్వింటాళ్లు/क्विंटल/குவிண்டால்/ಕ್ವಿಂಟಾಲ್) to kg (1 quintal = 100 kg)
- Convert tons to kg (1 ton = 1000 kg)

Return strictly a JSON object with these keys:
{{
  "crop": string | null,
  "quantity": float | null,
  "location": string | null,
  "harvest_date": string | null,
  "price_date": string | null,
  "language": "te" | "hi" | "en" | "ta" | "kn" | "mr"
}}"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.0
        )
        data = json.loads(response.choices[0].message.content)

        h_date = result.get("harvest_date")
        if not h_date and data.get("harvest_date"):
            try:
                h_date = datetime.date.fromisoformat(data["harvest_date"])
            except Exception:
                pass

        p_date = result.get("price_date")
        if not p_date and data.get("price_date"):
            try:
                p_date = datetime.date.fromisoformat(data["price_date"])
            except Exception:
                pass

        # Merge with regex results
        return {
            "crop": data.get("crop") or result["crop"],
            "quantity": float(data["quantity"]) if data.get("quantity") is not None else result["quantity"],
            "location": data.get("location") or result["location"],
            "harvest_date": h_date,
            "price_date": p_date,
            "language": data.get("language") or result["language"],
            "raw_text": text
        }
    except Exception as e:
        logger.warning(f"OpenAI voice fallback parse failed: {e}")
        return result

class QuotaExhaustedError(Exception):
    """Raised when an external speech API has exhausted its quota or credits."""
    pass


def transcribe_audio_bytes(audio_bytes: bytes, filename: str = "voice.wav") -> str:
    """Transcribe audio recorded from user's microphone using OpenAI Whisper with quota-aware handling."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured for Whisper speech transcription.")

    from openai import OpenAI
    client = OpenAI(api_key=api_key)

    audio_file = io.BytesIO(audio_bytes)
    audio_file.name = filename

    try:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        return transcript.text.strip()
    except Exception as e:
        err_msg = str(e)
        logger.warning(f"Whisper transcription error: {err_msg}")
        if (
            "insufficient_quota" in err_msg
            or "credit_balance_exhausted" in err_msg
            or "429" in err_msg
            or "quota" in err_msg.lower()
        ):
            raise QuotaExhaustedError(
                "OpenAI API quota exhausted. Please use Browser Live Microphone or 1-Tap Voice Presets."
            )
        raise


# Localized crop names for natural spoken audio
CROP_SPOKEN_NAMES = {
    "Rice": {"te": "వరి", "hi": "चावल", "ta": "அரிசி", "kn": "ಅಕ್ಕಿ", "mr": "तांदूळ", "en": "Rice"},
    "Maize": {"te": "మొక్కజొన్న", "hi": "मक्का", "ta": "மக்காச்சோளம்", "kn": "ಜೋಳ", "mr": "मका", "en": "Maize"},
    "Jowar": {"te": "జొన్న", "hi": "ज्वार", "ta": "சோளம்", "kn": "ಜೋಳ", "mr": "ज्वारी", "en": "Jowar"},
    "Bajra": {"te": "సజ్జలు", "hi": "बाजरा", "ta": "கம்பு", "kn": "ಸಜ್ಜೆ", "mr": "बाजरी", "en": "Bajra"},
    "Ragi": {"te": "రాగులు", "hi": "रागी", "ta": "கேழ்வரகு", "kn": "ರಾಗಿ", "mr": "नाचणी", "en": "Ragi"},
    "Red Gram": {"te": "కందులు", "hi": "अरहर", "ta": "துவரம் பருப்பு", "kn": "ತೊಗರಿ ಬೇಳೆ", "mr": "तूर डाळ", "en": "Red Gram"},
    "Bengal Gram": {"te": "శనగలు", "hi": "चना", "ta": "கொண்டைக்கடலை", "kn": "ಕಡಲೆ ಕಾಳು", "mr": "हरभरा", "en": "Bengal Gram"},
    "Green Gram": {"te": "పెసలు", "hi": "मूंग", "ta": "பாசிப்பயறு", "kn": "ಹೆಸರು ಕಾಳು", "mr": "मूग", "en": "Green Gram"},
    "Black Gram": {"te": "మినుములు", "hi": "उड़द", "ta": "உளுந்து", "kn": "ಉದ್ದಿನ ಬೇಳೆ", "mr": "उडीद", "en": "Black Gram"},
    "Groundnut": {"te": "వేరుశనగ", "hi": "मूंगफली", "ta": "நிலக்கடலை", "kn": "ಕಡಲೆಕಾಯಿ", "mr": "शेंगदाणा", "en": "Groundnut"},
    "Soybean": {"te": "సోయాబీన్", "hi": "सोयाबीन", "ta": "சோயாபீன்", "kn": "ಸೋಯಾಬೀನ್", "mr": "सोयाबीन", "en": "Soybean"},
    "Sunflower": {"te": "పొద్దుతిరుగుడు", "hi": "सूरजमुखी", "ta": "சூரியகாந்தி", "kn": "ಸೂರ್ಯಕಾಂತಿ", "mr": "सूर्यफूल", "en": "Sunflower"},
    "Sesamum": {"te": "నువ్వులు", "hi": "तिल", "ta": "எள்", "kn": "ಎಳ್ಳು", "mr": "तीळ", "en": "Sesamum"},
    "Castor": {"te": "ఆముదం", "hi": "अरंडी", "ta": "ஆமணக்கு", "kn": "ಹರಳು", "mr": "एरंडी", "en": "Castor"},
    "Chilli": {"te": "మిర్చి", "hi": "मिर्च", "ta": "மிளகாய்", "kn": "ಮೆಣಸಿನಕಾಯಿ", "mr": "मिरची", "en": "Chilli"},
    "Cotton": {"te": "పత్తి", "hi": "कपास", "ta": "பருத்தி", "kn": "ಹತ್ತಿ", "mr": "कापूस", "en": "Cotton"},
    "Turmeric": {"te": "పసుపు", "hi": "हल्दी", "ta": "மஞ்சள்", "kn": "ಅರಿಶಿನ", "mr": "हळद", "en": "Turmeric"},
    "Ginger": {"te": "అల్లం", "hi": "अदरक", "ta": "இஞ்சி", "kn": "ಶುಂಠಿ", "mr": "आले", "en": "Ginger"},
    "Garlic": {"te": "వెల్లుల్లి", "hi": "लहसुन", "ta": "பூண்டு", "kn": "ಬೆಳ್ಳುಳ್ಳಿ", "mr": "लसूण", "en": "Garlic"},
    "Tomato": {"te": "టమాటా", "hi": "टमाटर", "ta": "தக்காளி", "kn": "ಟೊಮೆಟೊ", "mr": "टोमॅटो", "en": "Tomato"},
    "Onion": {"te": "ఉల్లిపాయ", "hi": "प्याज", "ta": "வெங்காயம்", "kn": "ಈರುಳ್ಳಿ", "mr": "कांदा", "en": "Onion"},
    "Brinjal": {"te": "వంకాయ", "hi": "बैंगन", "ta": "கத்தரிக்காய்", "kn": "ಬದನೆಕಾಯಿ", "mr": "वांगी", "en": "Brinjal"},
    "Bhendi": {"te": "బెండకాయ", "hi": "भिंडी", "ta": "வெண்டைக்காய்", "kn": "ಬೆಂಡೆಕಾಯಿ", "mr": "भेंडी", "en": "Bhendi"},
    "Bitter Gourd": {"te": "కాకరకాయ", "hi": "करेला", "ta": "பாகற்காய்", "kn": "ಹಾಗಲಕಾಯಿ", "mr": "कारले", "en": "Bitter Gourd"}
}


def generate_farmer_voice_script(rec: Dict[str, Any], lang: str = "te") -> str:
    """
    Generates a natural, respectful, audio-friendly voice script for farmers.
    Optimized for speech synthesis across 6 languages: Telugu, Hindi, English, Tamil, Kannada, Marathi.
    """
    crop = rec.get("crop", "produce")
    best_market = rec.get("best_market", "APMC Mandi")
    best_distance = float(rec.get("best_market_distance", 0.0))
    current_price = float(rec.get("best_price", 0.0))
    quantity = float(rec.get("quantity", 0.0))
    decision = rec.get("decision", "SELL NOW").upper()
    suggested_small_market = rec.get("suggested_small_market")

    crop_name = CROP_SPOKEN_NAMES.get(crop, {}).get(lang, crop)

    if lang == "te":
        if decision == "SELL NOW":
            dec_speech = "మా AI విశ్లేషణ ప్రకారం, మీ పంటను ఇప్పుడే అమ్మడం ఎంతో లాభదాయకం."
        elif decision == "WAIT":
            dec_speech = "రాబోయే మూడు రోజుల్లో ధర పెరిగే అవకాశం ఉంది, కాబట్టి నిల్వ సదుపాయం ఉంటే వేచి చూడవచ్చు."
        else:
            dec_speech = "మార్కెట్ ధరలను గమనిస్తూ జాగ్రత్తగా అమ్మకం నిర్ణయం తీసుకోండి."

        small_market_note = ""
        if suggested_small_market and quantity <= 500:
            sm_mkt = suggested_small_market.get("market", "రైతు బజార్")
            sm_dist = suggested_small_market.get("distance_km", 5)
            small_market_note = f" మీ వద్ద తక్కువ పరిమాణం ఉంది కాబట్టి, కేవలం {sm_dist} కిలోమీటర్ల దూరంలోని {sm_mkt} స్థానిక మార్కెట్ లేదా రైతు బజార్లో అమ్మితే రవాణా ఖర్చులు బాగా ఆదా అవుతాయి."

        script = (
            f"రైతు సోదరులకు నమస్కారం! మీ {quantity:g} కిలోల {crop_name} కోసం సిఫార్సు చేసిన మార్కెట్ {best_market}. "
            f"ఇక్కడ ప్రస్తుత ధర కిలోకు {current_price:.0f} రూపాయలు. మీ ఊరి నుంచి రహదారి దూరం సుమారు {best_distance:.1f} కిలోమీటర్లు. "
            f"{dec_speech}{small_market_note} వివరాల కోసం గూగుల్ మ్యాప్స్ దిశలను చూడండి. శుభం!"
        )

    elif lang == "hi":
        if decision == "SELL NOW":
            dec_speech = "हमारी AI सलाह के अनुसार, अपनी फसल को अभी बेचना सबसे अधिक फायदेमंद रहेगा।"
        elif decision == "WAIT":
            dec_speech = "अगले तीन दिनों में भाव बढ़ने की संभावना है, इसलिए सुरक्षित भंडारण होने पर कुछ दिन रुक सकते हैं।"
        else:
            dec_speech = "मंडी के रुख पर नज़र रखें और आवश्यकतानुसार निर्णय लें।"

        small_market_note = ""
        if suggested_small_market and quantity <= 500:
            sm_mkt = suggested_small_market.get("market", "रैतु बाज़ार")
            sm_dist = suggested_small_market.get("distance_km", 5)
            small_market_note = f" आपकी मात्रा कम है, इसलिए केवल {sm_dist} किलोमीटर दूर स्थानीय {sm_mkt} में बेचना परिवहन खर्च बचाएगा।"

        script = (
            f"किसान भाई नमस्कार! आपकी {quantity:g} किलो {crop_name} की उपज के लिए सर्वोत्तम मंडी {best_market} है। "
            f"वर्तमान भाव ₹{current_price:.0f} प्रति किलो है, और सड़क मार्ग दूरी लगभग {best_distance:.1f} किलोमीटर है। "
            f"{dec_speech}{small_market_note} पूरी जानकारी के लिए मैप्स नेविगेशन देखें। धन्यवाद!"
        )

    elif lang == "ta":
        if decision == "SELL NOW":
            dec_speech = "எங்கள் AI பகுப்பாய்வின்படி, உங்கள் பயிரை இப்போதே விற்பது அதிக லாபகரமானது."
        elif decision == "WAIT":
            dec_speech = "அடுத்த மூன்று நாட்களில் விலை அதிகரிக்க வாய்ப்புள்ளது, எனவே பாதுகாப்பான சேமிப்பு வசதி இருந்தால் காத்திருக்கலாம்."
        else:
            dec_speech = "சந்தை விலைகளை கவனித்து சரியான நேரத்தில் முடிவெடுங்கள்."

        small_market_note = ""
        if suggested_small_market and quantity <= 500:
            sm_mkt = suggested_small_market.get("market", "உள்ளூர் சந்தை")
            sm_dist = suggested_small_market.get("distance_km", 5)
            small_market_note = f" குறைந்த அளவு விளைச்சல் என்பதால், {sm_dist} கிமீ தூரத்திலுள்ள {sm_mkt} சந்தையில் விற்றால் போக்குவரத்து செலவு மிச்சமாகும்."

        script = (
            f"வணக்கம் விவசாய நண்பரே! உங்கள் {quantity:g} கிலோ {crop_name} பயிருக்கு பரிந்துரைக்கப்பட்ட சந்தை {best_market}. "
            f"இன்றைய விலை கிலோவுக்கு {current_price:.0f} ரூபாய். உங்கள் ஊரிலிருந்து தூரம் சுமார் {best_distance:.1f} கி.மீ. "
            f"{dec_speech}{small_market_note} விவரங்களுக்கு வரைபட வழிகாட்டலைப் பார்க்கவும். நன்றி!"
        )

    elif lang == "kn":
        if decision == "SELL NOW":
            dec_speech = "ನಮ್ಮ AI ವಿಶ್ಲೇಷಣೆಯ ಪ್ರಕಾರ, ನಿಮ್ಮ ಬೆಳೆಯನ್ನು ಈಗಲೇ ಮಾರುವುದು ಹೆಚ್ಚು ಲಾಭದಾಯಕ."
        elif decision == "WAIT":
            dec_speech = "ಮುಂದಿನ ಮೂರು ದಿನಗಳಲ್ಲಿ ಬೆಲೆ ಹೆಚ್ಚಾಗುವ ಸಾಧ್ಯತೆಯಿದೆ, ಆದ್ದರಿಂದ ಸಂಗ್ರಹಣಾ ಸೌಲಭ್ಯವಿದ್ದರೆ ಕಾಯಬಹುದು."
        else:
            dec_speech = "ಮಾರುಕಟ್ಟೆ ದರಗಳನ್ನು ಗಮನಿಸಿ ಎಚ್ಚರಿಕೆಯಿಂದ ನಿರ್ಧಾರ ತೆಗೆದುಕೊಳ್ಳಿ."

        small_market_note = ""
        if suggested_small_market and quantity <= 500:
            sm_mkt = suggested_small_market.get("market", "ರೈತ ಬಜಾರ್")
            sm_dist = suggested_small_market.get("distance_km", 5)
            small_market_note = f" ನಿಮ್ಮ ಬಳಿ ಕಡಿಮೆ ಪ್ರಮಾಣವಿರುವುದರಿಂದ, ಕೇವಲ {sm_dist} ಕಿ.ಮೀ ದೂರದಲ್ಲಿರುವ {sm_mkt} ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿದರೆ ಸಾರಿಗೆ ವೆಚ್ಚ ಉಳಿತಾಯವಾಗುತ್ತದೆ."

        script = (
            f"ನಮಸ್ಕಾರ ರೈತ ಮಿತ್ರರೇ! ನಿಮ್ಮ {quantity:g} ಕೆಜಿ {crop_name} ಬೆಳೆಗೆ ಶಿಫಾರಸು ಮಾಡಿದ ಮಾರುಕಟ್ಟೆ {best_market}. "
            f"ಇಲ್ಲಿ ಪ್ರಸ್ತುತ ದರ ಕೆಜಿಗೆ {current_price:.0f} ರೂಪಾಯಿ. ರಸ್ತೆ ದೂರ ಸುಮಾರು {best_distance:.1f} ಕಿಲೋಮೀಟರ್. "
            f"{dec_speech}{small_market_note} ನಕ್ಷೆಯ ವಿವರಗಳನ್ನು ನೋಡಿ. ಶುಭವಾಗಲಿ!"
        )

    elif lang == "mr":
        if decision == "SELL NOW":
            dec_speech = "आमच्या AI सल्ल्यानुसार, आपला माल आताच विकणे सर्वाधिक फायदेशीर ठरेल."
        elif decision == "WAIT":
            dec_speech = "पुढील तीन दिवसांत भाव वाढण्याची शक्यता आहे, म्हणून साठवणूक सोय असल्यास आपण थांबू शकता."
        else:
            dec_speech = "बाजारातील भावावर लक्ष ठेवा आणि योग्य निर्णय घ्या."

        small_market_note = ""
        if suggested_small_market and quantity <= 500:
            sm_mkt = suggested_small_market.get("market", "स्थानिक बाजार")
            sm_dist = suggested_small_market.get("distance_km", 5)
            small_market_note = f" आपल्याकडे कमी प्रमाण असल्याने, फक्त {sm_dist} किमी अंतरावर असलेल्या {sm_mkt} बाजारात विकल्यास वाहतूक खर्च वाचेल."

        script = (
            f"शेतकरी बंधूंनो नमस्कार! आपल्या {quantity:g} किलो {crop_name} साठी शिफारस केलेली बाजारपेठ {best_market} आहे. "
            f"येथे सध्याचा भाव {current_price:.0f} रुपये प्रति किलो आहे, आणि रस्ता अंतर सुमारे {best_distance:.1f} किलोमीटर आहे. "
            f"{dec_speech}{small_market_note} तपशीलासाठी मॅप्स दिशा पहा. धन्यवाद!"
        )

    else:
        if decision == "SELL NOW":
            dec_speech = "Our AI recommends SELLING NOW for maximum net profit."
        elif decision == "WAIT":
            dec_speech = "Prices are expected to rise over the next three days, so you may consider waiting if you have safe storage."
        else:
            dec_speech = "Monitor market rates closely before selling."

        small_market_note = ""
        if suggested_small_market and quantity <= 500:
            sm_mkt = suggested_small_market.get("market", "Local Market")
            sm_dist = suggested_small_market.get("distance_km", 5)
            small_market_note = f" Since you have a small quantity, selling directly at nearby {sm_mkt} ({sm_dist} km) will save on transport."

        script = (
            f"Hello farmer friend! For your {quantity:g} kg of {crop_name}, the recommended mandi is {best_market}. "
            f"The current price is ₹{current_price:.0f} per kg, and the driving distance is {best_distance:.1f} km. "
            f"{dec_speech}{small_market_note} Have a great harvest!"
        )

    return script


def generate_speech_audio_bytes(script_text: str, lang: str = "te") -> bytes:
    """Generate MP3 audio bytes using gTTS supporting te, hi, en, ta, kn, mr."""
    valid_langs = {"te": "te", "hi": "hi", "en": "en", "ta": "ta", "kn": "kn", "mr": "mr"}
    gtts_lang = valid_langs.get(lang, "te")
    tts = gTTS(text=script_text, lang=gtts_lang, slow=False)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.getvalue()


def generate_speech_audio_base64(script_text: str, lang: str = "te") -> str:
    """
    Generate speech audio and return as a base64 Data URI string.
    Uses in-memory cache for blazing-fast instant playback.
    """
    cache_key = f"{lang}::{script_text.strip()}"
    if cache_key in _TTS_CACHE:
        return _TTS_CACHE[cache_key]

    audio_bytes = generate_speech_audio_bytes(script_text, lang=lang)
    b64 = base64.b64encode(audio_bytes).decode("utf-8")
    data_uri = f"data:audio/mp3;base64,{b64}"
    _TTS_CACHE[cache_key] = data_uri
    return data_uri


def build_webspeech_html(lang: str = "te") -> str:
    """
    Generates a standalone, zero-cost HTML5/JavaScript Web Speech API microphone widget.
    Natively recognizes spoken Indic languages (Telugu te-IN, Hindi hi-IN, English en-IN)
    in Chrome, Edge, and Android mobile browsers without requiring paid external API credits.
    """
    bcp47_map = {
        "te": ("te-IN", "తెలుగు (Telugu)", "🎙️ మాట్లాడండి (Tap to Speak in Telugu)"),
        "hi": ("hi-IN", "हिन्दी (Hindi)", "🎙️ बोलिए (Tap to Speak in Hindi)"),
        "en": ("en-IN", "English", "🎙️ Speak in English"),
        "ta": ("ta-IN", "தமிழ் (Tamil)", "🎙️ பேசுங்கள் (Speak in Tamil)"),
        "kn": ("kn-IN", "ಕನ್ನಡ (Kannada)", "🎙️ ಮಾತನಾಡಿ (Speak in Kannada)"),
        "mr": ("mr-IN", "మराठी (Marathi)", "🎙️ बोला (Speak in Marathi)")
    }
    bcp_code, lang_display, speak_label = bcp47_map.get(lang, ("te-IN", "తెలుగు (Telugu)", "🎙️ మాట్లాడండి (Tap to Speak in Telugu)"))

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
  body {{ background: transparent; padding: 2px; }}
  .speech-card {{
    background: #f0fdf4;
    border: 1.5px solid #86efac;
    border-radius: 12px;
    padding: 12px 14px;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.08);
  }}
  .badge {{
    font-size: 11px;
    font-weight: 700;
    color: #047857;
    background: #dcfce7;
    padding: 2px 8px;
    border-radius: 12px;
    border: 1px solid #bbf7d0;
  }}
  .mic-btn {{
    width: 100%;
    margin-top: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: #059669;
    color: white;
    border: none;
    padding: 9px 12px;
    border-radius: 8px;
    font-size: 13.5px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s ease;
  }}
  .mic-btn:hover {{ background: #047857; }}
  .mic-btn.recording {{
    background: #dc2626;
    animation: pulse 1.2s infinite;
  }}
  @keyframes pulse {{
    0% {{ transform: scale(1); opacity: 1; }}
    50% {{ transform: scale(1.02); opacity: 0.9; }}
    100% {{ transform: scale(1); opacity: 1; }}
  }}
  .status-text {{
    font-size: 11.5px;
    color: #475569;
    margin-top: 6px;
    text-align: center;
    line-height: 1.35;
  }}
  .result-box {{
    display: none;
    margin-top: 8px;
    background: #ffffff;
    border: 1.5px solid #bbf7d0;
    border-radius: 8px;
    padding: 8px 10px;
  }}
  .result-label {{
    font-size: 10.5px;
    font-weight: 700;
    color: #166534;
    text-transform: uppercase;
    margin-bottom: 3px;
  }}
  .result-content {{
    font-size: 13.5px;
    font-weight: 600;
    color: #0f172a;
    line-height: 1.35;
    word-break: break-word;
  }}
  .action-row {{
    display: flex;
    gap: 6px;
    margin-top: 8px;
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
  .toast {{
    display: none;
    font-size: 11px;
    color: #059669;
    font-weight: 700;
    margin-top: 5px;
    text-align: center;
  }}
</style>
</head>
<body>
<div class="speech-card">
  <div style="display: flex; align-items: center; justify-content: space-between;">
    <span style="font-size: 12.5px; font-weight: 700; color: #166534;">
      🎙️ Live Browser Mic (Free • Zero Quota)
    </span>
    <span class="badge">{lang_display}</span>
  </div>

  <button id="micBtn" class="mic-btn" onclick="toggleSpeech()">
    <span id="micIcon">🎙️</span>
    <span id="micText">{speak_label}</span>
  </button>

  <div id="statusText" class="status-text">
    💡 Tap and speak in your mother tongue (Chrome / Edge / Mobile)
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
    return html

