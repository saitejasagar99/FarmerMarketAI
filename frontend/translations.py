# -*- coding: utf-8 -*-
import json

SUPPORTED_LANGUAGES = {'te': '🌾 తెలుగు (Telugu)', 'hi': '🌾 हिन्दी (Hindi)', 'en': '🌐 English', 'ta': '🌾 தமிழ் (Tamil)', 'kn': '🌾 ಕನ್ನಡ (Kannada)', 'mr': '🌾 मराठी (Marathi)'}

DEFAULT_LANGUAGE = 'en'

TRANSLATIONS = {'en': {'ai_decision_title': '🤖 AI Selling Decision', 'analysis_success': '✅ Market analysis completed successfully!', 'analyzing_spinner': '🤖 AI Agent is analyzing market conditions...', 'api_err_connection': '❌ Cannot connect to FastAPI backend.\n\nPlease start the backend using:\n\n`uvicorn backend.main:app --reload`', 'api_err_generic': '❌ AI Agent error: {e}', 'api_err_recommendation': '❌ AI Recommendation API Error', 'api_err_timeout': '⏱️ AI recommendation request timed out.', 'app_hero_desc': 'Compare markets • Predict prices • Calculate transport & profit • Get a clear SELL / WAIT recommendation', 'app_hero_title': '🌾 From Farm to Best Market — Smarter Decisions with AI', 'app_subtitle': 'AI-powered market intelligence for smarter selling decisions', 'app_title': '🌾 Farmer-to-Market Intelligence', 'badge_gps_verified': '📍 GPS Verified ({radius} km Radius)', 'benefit_1': '📊 Compare prices across nearby mandis and markets', 'benefit_2': '🚚 Calculate transportation costs & see your true net profit', 'benefit_3': '🤖 AI Price Prediction: Know whether to SELL NOW or WAIT', 'benefits_title': '💡 What you get with this platform:', 'btn_analyze': '🚀 Analyze Market', 'btn_navigate_map': '🗺️ Directions', 'btn_start_nav': '🧭 Start Navigation to {market} in Google Maps', 'btn_sync_live': '🔄 Refresh Live Mandi Rates', 'change_phone_btn': '✏️ Change Mobile Number', 'choose_language': '🌐 Choose Your Language / భాషను ఎంచుకోండి / अपनी भाषा चुनें', 'col_date': 'Date', 'col_distance': 'Road Distance (km)', 'col_gross_rev': 'Gross Revenue (₹)', 'col_handling_cost': 'Handling Cost (₹)', 'col_location': 'Location', 'col_market': 'Market', 'col_net_profit': 'Net Profit (₹)', 'col_price': 'Price (₹/kg)', 'col_rating': 'Google Rating', 'col_transit_cost': 'Est. Transport', 'col_transport_cost': 'Transport Cost (₹)', 'col_travel_time': 'Est. Travel Time', 'conf_high_msg': '🟢 **High Confidence:** The model shows a strong fit to the available historical data.', 'conf_low_msg': '🔴 **Low Confidence:** Historical data shows limited predictive strength. Use the prediction together with current market conditions.', 'conf_mod_msg': '🟡 **Moderate Confidence:** The model provides a useful estimate, but market conditions can still affect the actual price.', 'confidence_high': 'High', 'confidence_low': 'Low', 'confidence_moderate': 'Moderate', 'confidence_unavailable': 'Unavailable', 'crop_quality': '⭐ Crop Quality', 'dashboard_title': '📊 Your Market Intelligence Dashboard', 'dec_neutral': 'NEUTRAL', 'dec_no_data': 'NO DATA', 'dec_sell_now': 'SELL NOW', 'dec_wait': 'WAIT', 'decision_nodata_banner': '### ℹ️ NO DATA\n\nNot enough information to make a recommendation.', 'decision_sell_banner': '### 🟢 SELL NOW\n\n**{market}** is currently the recommended market.\n\n💰 Current Price: ₹{price}/kg\n\n📍 Distance: {dist} km', 'decision_wait_banner': '### 🟡 WAIT\n\nThe model expects the price to increase.\n\n🔮 Predicted Price: ₹{price}/kg\n\n📈 Consider waiting for a better price.', 'demo_otp_banner': '📲 **[DEMO SMS]** Your FarmerMarketAI login OTP is: **{otp}** (Valid for 5 minutes)', 'disclaimer_1': '📌 This recommendation uses latest available market prices, location filtering, market distance, net-profit analysis and ML-based price prediction.', 'disclaimer_2': '⚠️ Price predictions are estimates. Actual prices may vary due to supply, demand, weather, transportation, storage and other market conditions.', 'dist_approx_km': '~{dist:.1f} km (road)', 'err_name_required': 'Please enter your name.', 'err_otp_expired': '⏱️ OTP expired. Please click Resend OTP.', 'err_otp_invalid': '❌ Invalid OTP. Please enter the correct 6-digit code.', 'err_otp_required': 'Please enter the 6-digit OTP.', 'err_phone_invalid': 'Please enter a valid 10-digit mobile number.', 'expected_harvest': '📅 Expected Harvest Date', 'farmer_location': '📍 Farmer Location', 'farmer_name_label': '👤 Farmer Name', 'farmer_name_placeholder': 'Enter your full name (e.g. Ramesh)', 'farmer_phone_help': 'Used for your personal market updates and records', 'farmer_phone_label': '📱 Mobile Number', 'farmer_phone_placeholder': 'Enter 10-digit mobile number', 'glance_title': 'Decision at a Glance', 'init_ai_intel': '### 🤖 AI Intelligence\n\n- Future price prediction\n- Prediction confidence & price range\n- Sell vs Wait decision\n- Decision scores\n- Farmer advisory', 'init_fin_intel': '### 💰 Financial Intelligence\n\n- Gross revenue\n- Transport cost\n- Handling cost\n- Net profit', 'init_how_it_works': '### 🚀 How it works\n\n**Farmer Input → Market Data → ML Prediction → LangGraph AI Agent → Profit Analysis → Selling Recommendation**', 'init_market_intel': '### 🏪 Market Intelligence\n\n- Current market prices\n- Market comparison\n- Best market recommendation\n- Market distance', 'init_provides': 'What this system provides', 'initial_info': '👈 Enter your crop details in the sidebar and click **🚀 Analyze Market**.', 'lbl_ai_decision': 'AI Decision', 'lbl_avg_price': 'Average Price', 'lbl_best_profit': 'Best Net Profit', 'lbl_current_best_price': 'Current Best Price', 'lbl_damage_factors_title': '🔬 Primary Post-Harvest Damage Factors:', 'lbl_discovered_markets': 'Markets Discovered within {radius} km ({count})', 'lbl_distance': '🚚 Road Distance', 'lbl_distance_km': 'Road Distance: {dist} km', 'lbl_exp_difference': 'Expected Difference', 'lbl_expected_rev': '3-Day Expected Revenue', 'lbl_farmer': 'Farmer', 'lbl_from_loc': 'From (Your Location)', 'lbl_humidity': 'Humidity', 'lbl_location': '📍 Location', 'lbl_lower_est': 'Lower Estimate', 'lbl_market': 'Market', 'lbl_max_price': 'Maximum Price', 'lbl_min_price': 'Minimum Price', 'lbl_model_mae': 'Mean Absolute Error', 'lbl_model_r2': 'Model R² Score', 'lbl_near_farmer': 'Near your location', 'lbl_per_km_rate': 'at ₹2.5/km', 'lbl_pred_3days': 'Predicted Price (3 Days)', 'lbl_price': '💰 Price', 'lbl_quality': 'Quality', 'lbl_quantity': 'Quantity', 'lbl_rain_prob': 'Rain Probability', 'lbl_rating': '⭐ Google Rating', 'lbl_rec_market': 'Recommended Market', 'lbl_safe_window': 'Safe window: ~{days} days', 'lbl_sell_now_rev': 'Sell Now Revenue', 'lbl_sell_score': 'Sell Now Score', 'lbl_shelf_life': 'Max Shelf Life', 'lbl_spoilage_rate': 'Daily Spoilage Rate', 'lbl_spoilage_risk': 'Spoilage / Rot Risk', 'lbl_temperature': 'Temperature', 'lbl_to_mandi': 'To (Target Mandi)', 'lbl_transit_adv': 'Transit Advisory', 'lbl_transit_guide': 'Transit Guidance', 'lbl_transport_cost': 'Est. Transport Cost', 'lbl_travel_time': 'Est. Travel Time', 'lbl_upper_est': 'Upper Estimate', 'lbl_wait_score': 'Wait Score', 'live_prices_badge': '🟢 LIVE DAILY MANDI FEED (Agmarknet APMC)', 'login_box_title': '🔐 Farmer Profile / Login', 'login_btn': '🚀 Continue to Dashboard', 'login_hero_desc': 'Smart market intelligence designed for farmers. Get the best price for your hard-earned harvest.', 'login_hero_title': '👨\u200d🌾 Welcome to Farmer-to-Market Intelligence', 'maps_caption': '📱 Tapping will open Google Maps directly with live GPS directions, real-time traffic, and fastest driving routes.', 'metric_best_market': '🏪 Best Market', 'metric_confidence': '🎯 Confidence', 'metric_current_price': '💰 Current Price', 'metric_net_profit': '💵 Net Profit', 'metric_predicted_price': '🔮 Predicted Price', 'metric_prediction_range': '📊 Prediction Range', 'metric_r2_score': '📈 R² Score', 'ml_analysis_title': '🤖 ML Price Prediction Analysis', 'ml_caption': 'Expected price after 3 days: {lower} – {upper}/kg | Mean Absolute Error: {mae}/kg', 'ml_unavailable_msg': '⚠️ ML prediction details are unavailable for this crop.', 'otp_box_title': '🔐 Mobile OTP Verification', 'otp_check_phone_notice': '📩 Please check your mobile phone messages for the 6-digit OTP code.', 'otp_label': '🔢 Enter 6-Digit OTP', 'otp_placeholder': 'Enter 6-digit OTP (e.g. 582910)', 'otp_resend_success': '✅ New OTP sent successfully to +91 {phone}!', 'otp_sent_to': '📲 Verification code sent via SMS to +91 {phone}', 'price_date_info': 'Rates verified for date: {date}', 'price_decrease_msg': '📉 Expected price decrease: {diff} ({pct})', 'price_increase_msg': '📈 Expected price increase: {diff} ({pct})', 'price_stable_msg': '➡️ No significant price change expected.', 'quality_advice_grade_a': 'Your Grade A produce may attract premium prices from quality-focused buyers. Keep away from moisture.', 'quality_advice_grade_b': 'Standard mandi grade produce. Compare prices across multiple nearby markets before finalizing sales.', 'quality_advice_grade_c': 'Produce is vulnerable to rapid degradation. Consider selling quickly to prevent further value loss.', 'quantity_kg': '⚖️ Quantity (kg)', 'recommended_market_title': '🏪 Recommended Market', 'resend_otp_btn': '🔄 Resend OTP', 'rev_header': 'Revenue Estimation', 'route_logistics_title': 'Route Navigation & Travel Logistics', 'select_crop': '🌱 Select Crop', 'select_price_date': '📅 Price Date', 'send_otp_btn': '📲 Send OTP', 'shelflife_title': 'Crop Shelf-Life & Delayed Selling Risk Analysis', 'sidebar_crop_info_header': 'Enter your crop information below.', 'sidebar_farmer_details': '👨\u200d🌾 Farmer Details', 'sidebar_language': '🌐 Language / భాష', 'sidebar_logout': '🚪 Logout', 'sidebar_phone': '📱 {phone}', 'sidebar_welcome': 'Welcome, {name}!', 'slider_radius': '📍 Search Radius (km)', 'sms_dispatched_toast': '📲 OTP dispatched to +91 {phone} via SMS!', 'sms_notif_card_sub': 'A 6-digit verification code has been transmitted to your mobile number. Enter it below to proceed.', 'sms_notif_card_title': 'SMS Notification Dispatched', 'sync_success': '✅ Fresh daily market prices retrieved for {date}!', 'tab1_chart_title': 'Market Price Chart', 'tab1_header': 'Market Price Comparison', 'tab1_no_data': '⚠️ No market comparison data available.', 'tab2_best_profit_banner': '🏆 **Most Profitable Market:** {market}\n\n💵 **Expected Net Profit:** {profit}', 'tab2_btn_nav': '🧭 Navigate to {market} in Google Maps', 'tab2_chart_title': 'Net Profit by Market', 'tab2_header': 'Smart Net Profit Analysis', 'tab2_transport_caption': '🚚 Transport cost is calculated using approximate market distance and configured transport rate.', 'tab3_caption': '📌 Historical prices are calculated from available market data.', 'tab3_decrease': '📉 Expected decrease: {pct}%', 'tab3_header': 'Historical Market Price Trend', 'tab3_increase': '📈 Expected increase: {pct}%', 'tab3_pred_header': 'ML Price Prediction', 'tab3_range_info': '📊 **Expected 3-day price range:** {lower} – {upper}/kg', 'tab3_stable': '➡️ No major change expected.', 'tab4_advisor_title': 'Farmer Advisory', 'tab4_financial_impact': 'Projected Financial Impact', 'tab4_header': 'AI Farmer Advisor', 'tab4_logistics_guidance': 'Logistics & Transport Advice', 'tab4_quality_guidance': 'Quality & Storage Guidance', 'tab4_rationale_title': 'Market Rationale & Outlook', 'tab4_reason_label': 'Primary Factor', 'tab4_rec_title': 'AI Recommendation', 'tab4_scores_title': 'Decision Scores', 'tab4_summary_title': 'Selling Summary', 'tab_ai_advisor': '🤖 AI Advisor', 'tab_market_comparison': '📊 Market Comparison', 'tab_price_trends': '📈 Price Trends', 'tab_profit_analysis': '💰 Profit Analysis', 'time_hours_mins': '{h}h {m}m', 'time_mins': '{m} mins', 'verify_otp_btn': '🚀 Verify OTP & Continue', 'weather_title': 'Live Agro-Weather & Transit Advisory', 'transit_heavy_load_note': 'Transit time is calibrated for loaded agricultural transport (Tractor-Trolley / Tempo at ~24 km/h with heavy produce cargo). Light car driving time is shown as reference.', 'lbl_heavy_load': 'Heavy Load', 'lbl_car_ref': 'Car', 'lbl_auto_assessed': 'Quality Evaluated from Harvest Date', 'lbl_days_post_harvest': 'days since harvest', 'harvest_date_help': 'Select harvest date. Freshness directly determines crop quality grade in mandi auctions.', 'crop_quality_help': 'Grade A: Freshly harvested/premium; Grade B: Standard mandi grade; Grade C: Distressed/aged.', 'tab_harvest_quality_title': 'Harvest Freshness & Quality Correlation', 'quality_fresh_status': 'Fresh Harvest', 'quality_basis_note': 'Mandi grading is directly linked to post-harvest days', 'tab_freshness_matrix': '🌾 Freshness Matrix', 'btn_new_analysis': 'New Analysis / Reset', 'matrix_title': 'Multi-Day Quality Degradation Matrix', 'matrix_subtitle': 'Live Mandi auction grading directly calibrated against post-harvest days', 'matrix_caption_photo': 'This interactive matrix models physical shelf life across six primary staple crops. Notice that high-water vegetables like tomatoes rapidly degrade to Grade C with catastrophic spoilage, while hardy grains remain Grade A for weeks.'}, 'hi': {'ai_decision_title': '🤖 AI बिक्री निर्णय', 'analysis_success': '✅ बाज़ार का विश्लेषण सफलतापूर्वक पूरा हुआ!', 'analyzing_spinner': '🤖 AI एजेंट बाज़ार की स्थिति का विश्लेषण कर रहा है...', 'api_err_connection': '❌ बैकएंड सर्वर से कनेक्ट नहीं हो सका।\n\nकृपया बैकएंड शुरू करें:\n\n`uvicorn backend.main:app --reload`', 'api_err_generic': '❌ AI एजेंट त्रुटि: {e}', 'api_err_recommendation': '❌ AI सिफारिश API त्रुटि', 'api_err_timeout': '⏱️ AI सिफारिश अनुरोध का समय समाप्त हो गया।', 'app_hero_desc': 'मंडी भावों की तुलना • आगामी मूल्य अनुमान • ढुलाई खर्च और शुद्ध लाभ • तुरंत बेचें या प्रतीक्षा करें की सलाह', 'app_hero_title': '🌾 खेत से सर्वोत्तम बाज़ार तक — AI से सही निर्णय लें', 'app_subtitle': 'किसानों के लिए सटीक मंडी भाव और लाभकारी निर्णय हेतु AI तकनीक', 'app_title': '🌾 किसान बाज़ार मित्र', 'badge_gps_verified': '📍 जीपीएस सत्यापित ({radius} किमी दायरा)', 'benefit_1': '📊 आस-पास की विभिन्न मंडियों के भावों की आसान तुलना', 'benefit_2': '🚚 ढुलाई/परिवहन खर्च काटकर वास्तविक शुद्ध मुनाफ़े का सटीक हिसाब', 'benefit_3': '🤖 AI भाव भविष्यवाणी: जानें फसल अभी बेचें या कुछ दिन रुकें', 'benefits_title': '💡 इस पोर्टल से किसानों को क्या लाभ मिलेंगे:', 'btn_analyze': '🚀 बाज़ार का विश्लेषण करें', 'btn_navigate_map': '🗺️ रास्ता देखें', 'btn_start_nav': '🧭 गूगल मैप्स में {market} के लिए नेविगेशन शुरू करें', 'btn_sync_live': '🔄 ताज़ा मंडी भाव प्राप्त करें', 'change_phone_btn': '✏️ मोबाइल नंबर बदलें', 'choose_language': '🌐 अपनी भाषा चुनें (Choose Language)', 'col_date': 'तारीख', 'col_distance': 'सड़क मार्ग दूरी (किमी)', 'col_gross_rev': 'सकल आय (₹)', 'col_handling_cost': 'हैंडलिंग खर्च (₹)', 'col_location': 'स्थान', 'col_market': 'मंडी', 'col_net_profit': 'शुद्ध मुनाफ़ा (₹)', 'col_price': 'भाव (₹/किग्रा)', 'col_rating': 'गूगल रेटिंग', 'col_transit_cost': 'अनुमानित परिवहन', 'col_transport_cost': 'परिवहन खर्च (₹)', 'col_travel_time': 'यात्रा का समय', 'conf_high_msg': '🟢 **उच्च विश्वसनीयता:** ऐतिहासिक आंकड़ों के आधार पर यह मॉडल अत्यधिक सटीक है।', 'conf_low_msg': '🔴 **कम विश्वसनीयता:** स्थानीय मंडी की वर्तमान स्थिति को देखकर ही अंतिम निर्णय लें।', 'conf_mod_msg': '🟡 **मध्यम विश्वसनीयता:** बाज़ार की बदलती परिस्थितियों के कारण वास्तविक भाव में अंतर आ सकता है।', 'confidence_high': 'उच्च (High)', 'confidence_low': 'कम (Low)', 'confidence_moderate': 'मध्यम (Moderate)', 'confidence_unavailable': 'अनुपलब्ध', 'crop_quality': '⭐ फसल की गुणवत्ता', 'dashboard_title': '📊 आपका बाज़ार आसूचना डैशबोर्ड', 'dec_neutral': 'तटस्थ (NEUTRAL)', 'dec_no_data': 'डेटा नहीं', 'dec_sell_now': 'अभी बेचें (SELL NOW)', 'dec_wait': 'प्रतीक्षा करें (WAIT)', 'decision_nodata_banner': '### ℹ️ डेटा उपलब्ध नहीं\n\nसटीक अनुशंसा करने के लिए पर्याप्त मंडी डेटा उपलब्ध नहीं है।', 'decision_sell_banner': '### 🟢 अभी बेचें (SELL NOW)\n\n**{market}** वर्तमान में सर्वोत्तम अनुशंसित मंडी है।\n\n💰 वर्तमान भाव: ₹{price}/किग्रा\n\n📍 दूरी: {dist} किमी', 'decision_wait_banner': '### 🟡 प्रतीक्षा करें (WAIT)\n\nआने वाले दिनों में भाव बढ़ने की संभावना है।\n\n🔮 अनुमानित भाव: ₹{price}/किग्रा\n\n📈 बेहतर भाव पाने के लिए कुछ दिन रुकना फायदेमंद हो सकता है।', 'demo_otp_banner': '📲 **[डेमो SMS]** आपका किसान बाज़ार AI लॉगिन ओटीपी है: **{otp}** (5 मिनट तक मान्य)', 'disclaimer_1': '📌 यह सलाह नवीनतम मंडी भाव, दूरी, शुद्ध मुनाफ़ा व मशीन लर्निंग मूल्य अनुमान पर आधारित है।', 'disclaimer_2': '⚠️ मूल्य अनुमान सांकेतिक हैं। मांग, आपूर्ति, मौसम और परिवहन के कारण वास्तविक भाव भिन्न हो सकते हैं।', 'dist_approx_km': '~{dist:.1f} किमी (रस्ता)', 'err_name_required': 'कृपया अपना नाम दर्ज करें।', 'err_otp_expired': '⏱️ ओटीपी समाप्त हो गया। कृपया दोबारा ओटीपी भेजें पर क्लिक करें।', 'err_otp_invalid': '❌ अमान्य ओटीपी। कृपया सही 6 अंकों का कोड दर्ज करें।', 'err_otp_required': 'कृपया 6 अंकों का ओटीपी दर्ज करें।', 'err_phone_invalid': 'कृपया 10 अंकों का मान्य मोबाइल नंबर दर्ज करें।', 'expected_harvest': '📅 फसल तैयार होने की तारीख', 'farmer_location': '📍 आपका स्थान / गाँव / शहर', 'farmer_name_label': '👤 किसान का नाम', 'farmer_name_placeholder': 'उदाहरण: रमेश कुमार / अपना नाम दर्ज करें', 'farmer_phone_help': 'आपकी व्यक्तिगत मंडी जानकारी और रिकॉर्ड के लिए', 'farmer_phone_label': '📱 मोबाइल नंबर', 'farmer_phone_placeholder': '10 अंकों का मोबाइल नंबर दर्ज करें', 'glance_title': 'एक नज़र में निर्णय', 'init_ai_intel': '### 🤖 AI विश्लेषण\n\n- आगामी मूल्य भविष्यवाणी\n- विश्वसनीयता व मूल्य दायरा\n- अभी बेचें या रुकें?\n- निर्णय स्कोर\n- किसान सलाह', 'init_fin_intel': '### 💰 वित्तीय विश्लेषण\n\n- कुल सकल आय\n- ढुलाई/परिवहन खर्च\n- लोडिंग व आढ़त खर्च\n- हाथ में आने वाला शुद्ध मुनाफ़ा', 'init_how_it_works': '### 🚀 यह कैसे काम करता है\n\n**किसान विवरण → मंडी डेटा → ML मूल्य अनुमान → AI एजेंट → मुनाफ़ा विश्लेषण → सटीक बिक्री सलाह**', 'init_market_intel': '### 🏪 मंडी आसूचना\n\n- ताज़ा मंडी भाव\n- मंडियों की सीधी तुलना\n- सर्वोत्तम मंडी की सलाह\n- मंडी की दूरी व मार्ग', 'init_provides': 'यह प्रणाली आपको क्या प्रदान करती है', 'initial_info': '👈 बाईं ओर साइडबार में अपनी फसल का विवरण भरें और **🚀 बाज़ार का विश्लेषण करें** पर क्लिक करें।', 'lbl_ai_decision': 'AI निर्णय', 'lbl_avg_price': 'औसत भाव', 'lbl_best_profit': 'अधिकतम शुद्ध मुनाफ़ा', 'lbl_current_best_price': 'वर्तमान सर्वोत्तम भाव', 'lbl_damage_factors_title': '🔬 कटाई के बाद मुख्य नुकसान कारक:', 'lbl_discovered_markets': '{radius} किमी के दायरे में मिली मंडियां ({count})', 'lbl_distance': '🚚 सड़क मार्ग दूरी', 'lbl_distance_km': 'सड़क मार्ग दूरी: {dist} किमी', 'lbl_exp_difference': 'संभावित अंतर / लाभ', 'lbl_expected_rev': '3 दिन बाद अनुमानित आय', 'lbl_farmer': 'किसान', 'lbl_from_loc': 'प्रस्थान (आपका स्थान)', 'lbl_humidity': 'नमी', 'lbl_location': '📍 स्थान', 'lbl_lower_est': 'न्यूनतम अनुमान', 'lbl_market': 'मंडी', 'lbl_max_price': 'अधिकतम भाव', 'lbl_min_price': 'न्यूनतम भाव', 'lbl_model_mae': 'औसत त्रुटि (MAE)', 'lbl_model_r2': 'मॉडल R² स्कोर', 'lbl_near_farmer': 'आपके स्थान के निकट', 'lbl_per_km_rate': '₹2.5/किमी की दर से', 'lbl_pred_3days': 'अनुमानित भाव (3 दिन)', 'lbl_price': '💰 भाव', 'lbl_quality': 'गुणवत्ता', 'lbl_quantity': 'मात्रा', 'lbl_rain_prob': 'बारिश की संभावना', 'lbl_rating': '⭐ गूगल रेटिंग', 'lbl_rec_market': 'अनुशंसित मंडी', 'lbl_safe_window': 'सुरक्षित समय: ~{days} दिन', 'lbl_sell_now_rev': 'अभी बेचने पर आय', 'lbl_sell_score': 'अभी बेचने का स्कोर', 'lbl_shelf_life': 'अधिकतम भंडारण अवधि', 'lbl_spoilage_rate': 'दैनिक गिरावट दर', 'lbl_spoilage_risk': 'खराब होने का जोखिम', 'lbl_temperature': 'तापमान', 'lbl_to_mandi': 'गंतव्य (लक्षित मंडी)', 'lbl_transit_adv': 'परिवहन स्थिति', 'lbl_transit_guide': 'परिवहन सुझाव', 'lbl_transport_cost': 'अनुमानित परिवहन खर्च', 'lbl_travel_time': 'अनुमानित यात्रा समय', 'lbl_upper_est': 'अधिकतम अनुमान', 'lbl_wait_score': 'प्रतीक्षा करने का स्कोर', 'live_prices_badge': '🟢 लाइव दैनिक मंडी भाव (एगमार्कनेट APMC)', 'login_box_title': '🔐 किसान प्रोफाइल / लॉगिन', 'login_btn': '🚀 डैशबोर्ड पर आगे बढ़ें', 'login_hero_desc': 'किसान भाइयों के लिए विशेष रूप से तैयार। अपनी मेहनत की उपज का सबसे अच्छा भाव पाएं।', 'login_hero_title': '👨\u200d🌾 किसान बाज़ार मित्र में आपका स्वागत है!', 'maps_caption': '📱 इस पर क्लिक करने से गूगल मैप्स खुलेगा जहाँ से आप लाइव जीपीएस और ट्रैफ़िक देख सकते हैं।', 'metric_best_market': '🏪 सर्वोत्तम मंडी', 'metric_confidence': '🎯 विश्वसनीयता', 'metric_current_price': '💰 वर्तमान भाव', 'metric_net_profit': '💵 शुद्ध मुनाफ़ा', 'metric_predicted_price': '🔮 अनुमानित भाव', 'metric_prediction_range': '📊 मूल्य सीमा (Range)', 'metric_r2_score': '📈 R² स्कोर', 'ml_analysis_title': '🤖 ML मूल्य भविष्यवाणी विश्लेषण', 'ml_caption': '3 दिनों बाद संभावित भाव: {lower} – {upper}/किग्रा | औसत त्रुटि: {mae}/किग्रा', 'ml_unavailable_msg': '⚠️ इस फसल के लिए ML मूल्य विवरण उपलब्ध नहीं हैं।', 'otp_box_title': '🔐 मोबाइल ओटीपी सत्यापन', 'otp_check_phone_notice': '📩 6 अंकों के ओटीपी के लिए कृपया अपने मोबाइल पर आए एसएमएस (SMS) संदेश को देखें।', 'otp_label': '🔢 6 अंकों का ओटीपी दर्ज करें', 'otp_placeholder': '6 अंकों का ओटीपी दर्ज करें (उदा. 582910)', 'otp_resend_success': '✅ नया ओटीपी +91 {phone} पर सफलतापूर्वक भेजा गया!', 'otp_sent_to': '📲 सत्यापन कोड +91 {phone} पर एसएमएस द्वारा भेजा गया', 'price_date_info': 'सत्यापित दिनांक: {date}', 'price_decrease_msg': '📉 भाव घटने का अनुमान: {diff} ({pct})', 'price_increase_msg': '📈 भाव बढ़ने का अनुमान: {diff} ({pct})', 'price_stable_msg': '➡️ भाव में कोई बड़ा बदलाव अपेक्षित नहीं है।', 'quality_advice_grade_a': 'आपकी ग्रेड A उपज को गुणवत्ता-पसंद खरीदारों से प्रीमियम भाव मिल सकता है। नमी से बचाएं।', 'quality_advice_grade_b': 'मध्यम दर्जे की उपज। बिक्री से पहले आसपास की मंडियों के भावों की तुलना करें।', 'quality_advice_grade_c': 'गुणवत्ता में और गिरावट से बचने के लिए जल्द से जल्द बेचना उचित रहेगा।', 'quantity_kg': '⚖️ मात्रा (किलोग्राम / kg)', 'recommended_market_title': '🏪 अनुशंसित मंडी', 'resend_otp_btn': '🔄 दोबारा ओटीपी भेजें', 'rev_header': 'आय का अनुमान', 'route_logistics_title': 'रास्ता नेविगेशन और परिवहन विवरण', 'select_crop': '🌱 फसल चुनें', 'select_price_date': '📅 बाज़ार भाव दिनांक', 'send_otp_btn': '📲 ओटीपी भेजें (Send OTP)', 'shelflife_title': 'फसल शेल्फ-लाइफ व भंडारण जोखिम विश्लेषण', 'sidebar_crop_info_header': 'नीचे अपनी फसल का विवरण भरें।', 'sidebar_farmer_details': '👨\u200d🌾 किसान विवरण', 'sidebar_language': '🌐 भाषा बदलें', 'sidebar_logout': '🚪 लॉगआउट', 'sidebar_phone': '📱 {phone}', 'sidebar_welcome': 'नमस्ते, {name} जी!', 'slider_radius': '📍 खोज दायरा (किमी)', 'sms_dispatched_toast': '📲 +91 {phone} पर एसएमएस द्वारा ओटीपी भेजा गया!', 'sms_notif_card_sub': 'आपके मोबाइल नंबर पर 6 अंकों का सत्यापन कोड भेजा गया है। आगे बढ़ने के लिए इसे नीचे दर्ज करें।', 'sms_notif_card_title': 'मोबाइल एसएमएस अधिसूचना भेजी गई', 'sync_success': '✅ {date} के ताज़ा मंडी भाव सफलतापूर्वक लोड हो गए!', 'tab1_chart_title': 'मंडी भाव चार्ट', 'tab1_header': 'मंडी भावों की तुलना', 'tab1_no_data': '⚠️ कोई तुलनात्मक मंडी डेटा उपलब्ध नहीं है।', 'tab2_best_profit_banner': '🏆 **सर्वाधिक लाभकारी मंडी:** {market}\n\n💵 **संभावित शुद्ध मुनाफ़ा:** {profit}', 'tab2_btn_nav': '🧭 गूगल मैप्स में {market} का रास्ता देखें', 'tab2_chart_title': 'मंडी अनुसार शुद्ध मुनाफ़ा', 'tab2_header': 'शुद्ध मुनाफ़ा विश्लेषण', 'tab2_transport_caption': '🚚 परिवहन खर्च मंडी की दूरी और निर्धारित दर के अनुसार आंका गया है।', 'tab3_caption': '📌 ऐतिहासिक भाव उपलब्ध मंडी डेटा के आधार पर प्रदर्शित हैं।', 'tab3_decrease': '📉 भाव गिरावट की संभावना: {pct}%', 'tab3_header': 'ऐतिहासिक मंडी भाव रुझान', 'tab3_increase': '📈 भाव वृद्धि की संभावना: {pct}%', 'tab3_pred_header': 'ML मूल्य भविष्यवाणी', 'tab3_range_info': '📊 **3 दिनों का अनुमानित भाव दायरा:** {lower} – {upper}/किग्रा', 'tab3_stable': '➡️ कोई बड़ा बदलाव अपेक्षित नहीं है।', 'tab4_advisor_title': 'किसान परामर्श', 'tab4_financial_impact': 'वित्तीय प्रभाव और आय अनुमान', 'tab4_header': 'AI किसान सलाहकार', 'tab4_logistics_guidance': 'परिवहन और मंडी पहुँचने के सुझाव', 'tab4_quality_guidance': 'गुणवत्ता और रख-रखाव सलाह', 'tab4_rationale_title': 'मंडी विश्लेषण और मूल्य दृष्टिकोण', 'tab4_reason_label': 'मुख्य कारक', 'tab4_rec_title': 'AI अनुशंसा', 'tab4_scores_title': 'निर्णय स्कोर', 'tab4_summary_title': 'बिक्री सारांश', 'tab_ai_advisor': '🤖 AI सलाहकार', 'tab_market_comparison': '📊 मंडियों की तुलना', 'tab_price_trends': '📈 मूल्य रुझान', 'tab_profit_analysis': '💰 मुनाफ़ा विश्लेषण', 'time_hours_mins': '{h} घंटे {m} मिनट', 'time_mins': '{m} मिनट', 'verify_otp_btn': '🚀 ओटीपी सत्यापित करें और आगे बढ़ें', 'weather_title': 'मौसम और परिवहन परामर्श', 'transit_heavy_load_note': 'यात्रा का समय भारी कृषि उपज से लदे वाहन (ट्रैक्टर-ट्रॉली / टेम्पो ~24 किमी/घंटा) के अनुसार तय किया गया है। कार का समय संदर्भ के लिए दिखाया गया है।', 'lbl_heavy_load': 'भारी लोड', 'lbl_car_ref': 'कार', 'lbl_auto_assessed': 'कटाई की तारीख से निर्धारित गुणवत्ता', 'lbl_days_post_harvest': 'दिन पहले कटाई', 'harvest_date_help': 'फसल कटाई की तारीख चुनें। ताज़गी ही मंडी में गुणवत्ता ग्रेड तय करती है।', 'crop_quality_help': 'ग्रेड A: ताज़ा/प्रीमियम; ग्रेड B: मानक मंडी ग्रेड; ग्रेड C: पुराना/कमज़ोर।', 'tab_harvest_quality_title': 'कटाई की ताज़गी और गुणवत्ता प्रभाव', 'quality_fresh_status': 'ताज़ा कटाई', 'quality_basis_note': 'कटाई के बाद के दिनों के अनुसार मंडी ग्रेड बदलता है', 'tab_freshness_matrix': '🌾 फसल गुणवत्ता मैट्रिक्स', 'btn_new_analysis': 'नया विश्लेषण / रीसेट', 'matrix_title': 'बहु-दिवसीय फसल गुणवत्ता गिरावट मैट्रिक्स', 'matrix_subtitle': 'कटाई के बाद के दिनों के अनुसार मंडी नीलामी गुणवत्ता ग्रेडिंग', 'matrix_caption_photo': 'यह मैट्रिक्स छह प्रमुख फसलों के शेल्फ-लाइफ मॉडल को दर्शाता है। टमाटर जैसी फसलें 5 दिनों के बाद तेज़ी से ग्रेड C में गिरती हैं, जबकि मक्का और धान हफ्तों तक ग्रेड A में सुरक्षित रहते हैं।'}, 'kn': {'ai_decision_title': '🤖 AI ಮಾರಾಟ ನಿರ್ಧಾರ', 'analysis_success': '✅ ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಣೆ ಯಶಸ್ವಿಯಾಗಿ ಪೂರ್ಣಗೊಂಡಿದೆ!', 'analyzing_spinner': '🤖 AI ಮಾರುಕಟ್ಟೆ ಪರಿಸ್ಥಿತಿಯನ್ನು ವಿಶ್ಲೇಷಿಸುತ್ತಿದೆ...', 'api_err_connection': '❌ ಸರ್ವರ್ ಸಂಪರ್ಕ ವಿಫಲವಾಗಿದೆ.\n\nದಯವಿಟ್ಟು ಪರಿಶೀಲಿಸಿ:\n\n`uvicorn backend.main:app --reload`', 'api_err_generic': '❌ AI ಏಜೆಂಟ್ ದೋಷ: {e}', 'api_err_recommendation': '❌ AI ಶಿಫಾರಸು API ದೋಷ', 'api_err_timeout': '⏱️ AI ಶಿಫಾರಸು ವಿನಂತಿಯ ಸಮಯ ಮೀರಿದೆ.', 'app_hero_desc': 'ಮಾರುಕಟ್ಟೆ ದರಗಳ ಹೋಲಿಕೆ • ಮುಂದಿನ ಬೆಲೆ ಅಂದಾಜು • ಸಾರಿಗೆ ವೆಚ್ಚ ಮತ್ತು ನಿವ್ವಳ ಲಾಭ • ತಕ್ಷಣ ಮಾರಾಟ ಅಥವಾ ಕಾಯುವ ಕುರಿತು ಸ್ಪಷ್ಟ ಸಲಹೆ', 'app_hero_title': '🌾 ಜಮೀನಿನಿಂದ ಉತ್ತಮ ಮಾರುಕಟ್ಟೆಯವರೆಗೆ — AI ನಿಂದ ಸ್ಮಾರ್ಟ್ ನಿರ್ಧಾರ', 'app_subtitle': 'ರೈತರಿಗೆ ಸೂಕ್ತ ಮಾರುಕಟ್ಟೆ ಮತ್ತು ಉತ್ತಮ ಲಾಭ ಒದಗಿಸುವ AI ವ್ಯವಸ್ಥೆ', 'app_title': '🌾 ರೈತ ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ', 'badge_gps_verified': '📍 GPS ಪರಿಶೀಲಿಸಲಾಗಿದೆ ({radius} ಕಿ.ಮೀ)', 'benefit_1': '📊 ಹತ್ತಿರದ ಮಾರುಕಟ್ಟೆಗಳು ಮತ್ತು ಎಪಿಎಂಸಿ ದರಗಳ ಸುಲಭ ಹೋಲಿಕೆ', 'benefit_2': '🚚 ಸಾರಿಗೆ ವೆಚ್ಚ ಕಳೆದು ಕೈಗೆ ಸಿಗುವ ನಿವ್ವಳ ಲಾಭದ ಲೆಕ್ಕ', 'benefit_3': '🤖 AI ಬೆಲೆ ಭವಿಷ್ಯವಾಣಿ: ಈಗಲೇ ಮಾರಾಟ ಮಾಡಬೇಕೇ ಅಥವಾ ಕಾಯಬೇಕೇ ತಿಳಿಯಿರಿ', 'benefits_title': '💡 ರೈತರಿಗೆ ಸಿಗುವ ಪ್ರಯೋಜನಗಳು:', 'btn_analyze': '🚀 ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಿಸಿ', 'btn_navigate_map': '🗺️ ದಿಕ್ಕುಗಳು', 'btn_start_nav': '🧭 ಗೂಗಲ್ ಮ್ಯಾಪ್ಸ್\u200cನಲ್ಲಿ {market} ಮಾರುಕಟ್ಟೆಗೆ ಮಾರ್ಗ ನೋಡಿ', 'btn_sync_live': '🔄 ನೇರ ಮಾರುಕಟ್ಟೆ ದರಗಳನ್ನು ನವೀಕರಿಸಿ', 'change_phone_btn': '✏️ ಸಂಖ್ಯೆಯನ್ನು ಬದಲಾಯಿಸಿ', 'choose_language': '🌐 ನಿಮ್ಮ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ (Choose Language)', 'col_date': 'ದಿನಾಂಕ', 'col_distance': 'ರಸ್ತೆ ದೂರ (ಕಿ.ಮೀ)', 'col_gross_rev': 'ಒಟ್ಟು ಆದಾಯ (₹)', 'col_handling_cost': 'ನಿರ್ವಹಣಾ ವೆಚ್ಚ (₹)', 'col_location': 'ಸ್ಥಳ', 'col_market': 'ಮಾರುಕಟ್ಟೆ', 'col_net_profit': 'ನಿವ್ವಳ ಲಾಭ (₹)', 'col_price': 'ದರ (₹/ಕೆಜಿ)', 'col_rating': 'ಗೂಗಲ್ ರೇಟಿಂಗ್', 'col_transit_cost': 'ಸಾರಿಗೆ ವೆಚ್ಚ', 'col_transport_cost': 'ಸಾರಿಗೆ ವೆಚ್ಚ (₹)', 'col_travel_time': 'ಪ್ರಯಾಣದ ಸಮಯ', 'conf_high_msg': '🟢 **ಹೆಚ್ಚಿನ ನಿಖರತೆ:** ಹಿಂದಿನ ಮಾರುಕಟ್ಟೆ ಅಂಕಿಅಂಶಗಳ ಪ್ರಕಾರ ಮಾದರಿಯು ಬಲವಾದ ಅಂದಾಜನ್ನು ತೋರಿಸುತ್ತದೆ.', 'conf_low_msg': '🔴 **ಕಡಿಮೆ ನಿಖರತೆ:** ಸ್ಥಳೀಯ ಮಾರುಕಟ್ಟೆ ಪರಿಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ ನಿರ್ಧಾರ ತೆಗೆದುಕೊಳ್ಳಿ.', 'conf_mod_msg': '🟡 **ಮಧ್ಯಮ ನಿಖರತೆ:** ಮಾರುಕಟ್ಟೆ ಪರಿಸ್ಥಿತಿಗಳಿಂದಾಗಿ ಬೆಲೆಯಲ್ಲಿ ಸ್ವಲ್ಪ ಬದಲಾವಣೆಗಳಾಗಬಹುದು.', 'confidence_high': 'ಹೆಚ್ಚು (High)', 'confidence_low': 'ಕಡಿಮೆ (Low)', 'confidence_moderate': 'ಮಧ್ಯಮ (Moderate)', 'confidence_unavailable': 'ಲಭ್ಯವಿಲ್ಲ', 'crop_quality': '⭐ ಬೆಳೆಯ ಗುಣಮಟ್ಟ', 'dashboard_title': '📊 ನಿಮ್ಮ ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ ಡ್ಯಾಶ್\u200cಬೋರ್ಡ್', 'dec_neutral': 'ಸಾಮಾನ್ಯ (NEUTRAL)', 'dec_no_data': 'ಮಾಹಿತಿಯಿಲ್ಲ', 'dec_sell_now': 'ಈಗಲೇ ಮಾರಿ (SELL NOW)', 'dec_wait': 'ಸ್ವಲ್ಪ ಕಾಯಿರಿ (WAIT)', 'decision_nodata_banner': '### ℹ️ ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ\n\nಶಿಫಾರಸು ಮಾಡಲು ಸಾಕಷ್ಟು ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ.', 'decision_sell_banner': '### 🟢 ಈಗಲೇ ಮಾರಿ (SELL NOW)\n\n**{market}** ಪ್ರಸ್ತುತ ಶಿಫಾರಸು ಮಾಡಲಾದ ಉತ್ತಮ ಮಾರುಕಟ್ಟೆ.\n\n💰 ಪ್ರಸ್ತುತ ದರ: ₹{price}/ಕೆಜಿ\n\n📍 ದೂರ: {dist} ಕಿ.ಮೀ', 'decision_wait_banner': '### 🟡 ಸ್ವಲ್ಪ ಕಾಯಿರಿ (WAIT)\n\nಮುಂದಿನ ದಿನಗಳಲ್ಲಿ ಬೆಲೆ ಹೆಚ್ಚಾಗುವ ಸಾಧ್ಯತೆಯಿದೆ.\n\n🔮 ಅಂದಾಜು ದರ: ₹{price}/ಕೆಜಿ\n\n📈 ಉತ್ತಮ ಬೆಲೆಗಾಗಿ ಸ್ವಲ್ಪ ಸಮಯ ಕಾಯುವುದು ಉತ್ತಮ.', 'demo_otp_banner': '📲 **[ಡೆಮೊ SMS]** ನಿಮ್ಮ ಲಾಗಿನ್ OTP: **{otp}** (5 ನಿಮಿಷಗಳವರೆಗೆ ಮಾನ್ಯವಾಗಿದೆ)', 'disclaimer_1': '📌 ಈ ಶಿಫಾರಸು ಇತ್ತೀಚಿನ ಮಾರುಕಟ್ಟೆ ದರಗಳು, ದೂರ, ನಿವ್ವಳ ಲಾಭ ಮತ್ತು ML ಬೆಲೆ ಅಂದಾಜಿನ ಮೇಲೆ ಆಧಾರಿತವಾಗಿದೆ.', 'disclaimer_2': '⚠️ ಬೆಲೆ ಮುನ್ಸೂಚನೆಗಳು ಅಂದಾಜುಗಳಾಗಿವೆ. ಬೇಡಿಕೆ, ಪೂರೈಕೆ ಮತ್ತು ಹವಾಮಾನಕ್ಕೆ ಅನುಗುಣವಾಗಿ ನೈಜ ಬೆಲೆಗಳು ಬದಲಾಗಬಹುದು.', 'dist_approx_km': '~{dist:.1f} ಕಿ.ಮೀ (ರಸ್ತೆ)', 'err_name_required': 'ದಯವಿಟ್ಟು ನಿಮ್ಮ ಹೆಸರನ್ನು ನಮೂದಿಸಿ.', 'err_otp_expired': '⏱️ OTP ಅವಧಿ ಮೀರಿದೆ. ದಯವಿಟ್ಟು ಮತ್ತೆ OTP ಕಳುಹಿಸಿ ಕ್ಲಿಕ್ ಮಾಡಿ.', 'err_otp_invalid': '❌ ತಪ್ಪಾದ OTP. ದಯವಿಟ್ಟು ಸರಿಯಾದ 6 ಅಂಕಿಯ ಕೋಡ್ ನಮೂದಿಸಿ.', 'err_otp_required': 'ದಯವಿಟ್ಟು 6 ಅಂಕಿಯ OTP ನಮೂದಿಸಿ.', 'err_phone_invalid': 'ದಯವಿಟ್ಟು ಮಾನ್ಯವಾದ 10 ಅಂಕಿಯ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.', 'expected_harvest': '📅 ಕೊಯ್ಲು ದಿನಾಂಕ', 'farmer_location': '📍 ನಿಮ್ಮ ಸ್ಥಳ / ಊರು', 'farmer_name_label': '👤 ರೈತರ ಹೆಸರು', 'farmer_name_placeholder': 'ಉದಾಹರಣೆ: ಮಂಜುನಾಥ್ / ನಿಮ್ಮ ಹೆಸರು ನಮೂದಿಸಿ', 'farmer_phone_help': 'ನಿಮ್ಮ ವೈಯಕ್ತಿಕ ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ ಮತ್ತು ದರ ನವೀಕರಣಗಳಿಗಾಗಿ', 'farmer_phone_label': '📱 ಮೊಬೈಲ್ ಸಂಖ್ಯೆ', 'farmer_phone_placeholder': '10 ಅಂಕಿಯ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ', 'glance_title': 'ಒಂದು ನೋಟದಲ್ಲಿ ನಿರ್ಧಾರ', 'init_ai_intel': '### 🤖 AI ತಂತ್ರಜ್ಞಾನ\n\n- ಭವಿಷ್ಯತ್ತಿನ ಬೆಲೆ ಅಂದಾಜು\n- ಬೆಲೆ ಶ್ರೇಣಿ ಮತ್ತು ನಿಖರತೆ\n- ಮಾರಾಟ ಅಥವಾ ಕಾಯುವಿಕೆ ನಿರ್ಧಾರ\n- ನಿರ್ಧಾರದ ಅಂಕಗಳು\n- ರೈತರಿಗೆ ಸಲಹೆ', 'init_fin_intel': '### 💰 ಆರ್ಥಿಕ ಮಾಹಿತಿ\n\n- ಒಟ್ಟು ಆದಾಯ\n- ಸಾರಿಗೆ ವೆಚ್ಚ\n- ನಿರ್ವಹಣಾ ವೆಚ್ಚ\n- ಕೈಗೆ ಸಿಗುವ ನಿವ್ವಳ ಲಾಭ', 'init_how_it_works': '### 🚀 ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ\n\n**ರೈತರ ಮಾಹಿತಿ → ಮಾರುಕಟ್ಟೆ ಡೇಟಾ → ML ಬೆಲೆ ಮುನ್ಸೂಚನೆ → AI ಏಜೆಂಟ್ → ಲಾಭದ ಲೆಕ್ಕ → ಮಾರಾಟದ ಶಿಫಾರಸು**', 'init_market_intel': '### 🏪 ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ\n\n- ಪ್ರಸ್ತುತ ಮಾರುಕಟ್ಟೆ ದರಗಳು\n- ಮಾರುಕಟ್ಟೆಗಳ ಹೋಲಿಕೆ\n- ಉತ್ತಮ ಮಾರುಕಟ್ಟೆ ಶಿಫಾರಸು\n- ಮಾರುಕಟ್ಟೆ ದೂರ', 'init_provides': 'ಈ ವ್ಯವಸ್ಥೆಯು ನಿಮಗೆ ಏನು ಒದಗಿಸುತ್ತದೆ', 'initial_info': '👈 ಸೈಡ್\u200cಬಾರ್\u200cನಲ್ಲಿ ನಿಮ್ಮ ಬೆಳೆ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ ಮತ್ತು **🚀 ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಿಸಿ** ಕ್ಲಿಕ್ ಮಾಡಿ.', 'lbl_ai_decision': 'AI ನಿರ್ಧಾರ', 'lbl_avg_price': 'ಸರಾಸರಿ ದರ', 'lbl_best_profit': 'ಗರಿಷ್ಠ ನಿವ್ವಳ ಲಾಭ', 'lbl_current_best_price': 'ಪ್ರಸ್ತುತ ಉತ್ತಮ ದರ', 'lbl_damage_factors_title': '🔬 ಕೊಯ್ಲಿನ ನಂತರದ ಪ್ರಮುಖ ಹಾನಿ ಅಂಶಗಳು:', 'lbl_discovered_markets': '{radius} ಕಿ.ಮೀ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಪತ್ತೆಯಾದ ಮಾರುಕಟ್ಟೆಗಳು ({count})', 'lbl_distance': '🚚 ರಸ್ತೆ ದೂರ', 'lbl_distance_km': 'ರಸ್ತೆ ದೂರ: {dist} ಕಿ.ಮೀ', 'lbl_exp_difference': 'ನಿರೀಕ್ಷಿತ ವ್ಯತ್ಯಾಸ', 'lbl_expected_rev': '3 ದಿನಗಳ ನಂತರ ನಿರೀಕ್ಷಿತ ಆದಾಯ', 'lbl_farmer': 'ರೈತ', 'lbl_from_loc': 'ಹೊರಡುವ ಸ್ಥಳ (ನಿಮ್ಮ ಸ್ಥಳ)', 'lbl_humidity': 'ಆರ್ದ್ರತೆ', 'lbl_location': '📍 ಸ್ಥಳ', 'lbl_lower_est': 'ಕನಿಷ್ಠ ಅಂದಾಜು', 'lbl_market': 'ಮಾರುಕಟ್ಟೆ', 'lbl_max_price': 'ಗರಿಷ್ಠ ದರ', 'lbl_min_price': 'ಕನಿಷ್ಠ ದರ', 'lbl_model_mae': 'ಸರಾಸರಿ ದೋಷ (MAE)', 'lbl_model_r2': 'ಮಾದರಿ R² ಸ್ಕೋರ್', 'lbl_near_farmer': 'ನಿಮ್ಮ ಸ್ಥಳದ ಹತ್ತಿರ', 'lbl_per_km_rate': '₹2.5/ಕಿ.ಮೀ ದರದಲ್ಲಿ', 'lbl_pred_3days': 'ಅಂದಾಜು ದರ (3 ದಿನಗಳು)', 'lbl_price': '💰 ದರ', 'lbl_quality': 'ಗುಣಮಟ್ಟ', 'lbl_quantity': 'ಪ್ರಮಾಣ', 'lbl_rain_prob': 'ಮಳೆಯ ಸಾಧ್ಯತೆ', 'lbl_rating': '⭐ ಗೂಗಲ್ ರೇಟಿಂಗ್', 'lbl_rec_market': 'ಶಿಫಾರಸು ಮಾಡಿದ ಮಾರುಕಟ್ಟೆ', 'lbl_safe_window': 'ಸುರಕ್ಷಿತ ಅವಧಿ: ~{days} ದಿನಗಳು', 'lbl_sell_now_rev': 'ಈಗಲೇ ಮಾರಾಟದ ಆದಾಯ', 'lbl_sell_score': 'ಈಗಲೇ ಮಾರಾಟದ ಅಂಕಗಳು', 'lbl_shelf_life': 'ಗರಿಷ್ಠ ಶೇಖರಣಾ ಅವಧಿ', 'lbl_spoilage_rate': 'ದೈನಂದಿನ ನಷ್ಟದ ದರ', 'lbl_spoilage_risk': 'ಹಾಳಾಗುವ ಅಪಾಯ', 'lbl_temperature': 'ತಾಪಮಾನ', 'lbl_to_mandi': 'ತಲುಪುವ ಮಾರುಕಟ್ಟೆ', 'lbl_transit_adv': 'ಸಾರಿಗೆ ಪರಿಸ್ಥಿತಿ', 'lbl_transit_guide': 'ಸಾರಿಗೆ ಮಾರ್ಗದರ್ಶನ', 'lbl_transport_cost': 'ಅಂದಾಜು ಸಾರಿಗೆ ವೆಚ್ಚ', 'lbl_travel_time': 'ಅಂದಾಜು ಪ್ರಯಾಣದ ಸಮಯ', 'lbl_upper_est': 'ಗರಿಷ್ಠ ಅಂದಾಜು', 'lbl_wait_score': 'ಕಾಯುವಿಕೆಯ ಅಂಕಗಳು', 'live_prices_badge': '🟢 ನೇರ ದೈನಂದಿನ ಮಾರುಕಟ್ಟೆ ದರಗಳು (Agmarknet APMC)', 'login_box_title': '🔐 ರೈತರ ಪ್ರೊಫೈಲ್ / ಲಾಗಿನ್', 'login_btn': '🚀 ಡ್ಯಾಶ್\u200cಬೋರ್ಡ್\u200cಗೆ ಮುಂದುವರಿಯಿರಿ', 'login_hero_desc': 'ರೈತರಿಗಾಗಿ ವಿಶೇಷವಾಗಿ ರೂಪಿಸಲಾಗಿದೆ. ನಿಮ್ಮ ಕಠಿಣ ಪರಿಶ್ರಮಕ್ಕೆ ಯೋಗ್ಯ ಬೆಲೆ ಪಡೆಯಿರಿ.', 'login_hero_title': '👨\u200d🌾 ರೈತ ಮಿತ್ರ ಪೋರ್ಟಲ್\u200cಗೆ ಸುಸ್ವಾಗತ!', 'maps_caption': '📱 ಕ್ಲಿಕ್ ಮಾಡಿದರೆ ನೇರವಾಗಿ ಲೈವ್ ಜಿಪಿಎಸ್ ಮತ್ತು ಟ್ರಾಫಿಕ್ ಮಾಹಿತಿಯೊಂದಿಗೆ ಗೂಗಲ್ ಮ್ಯಾಪ್ಸ್ ತೆರೆಯುತ್ತದೆ.', 'metric_best_market': '🏪 ಉತ್ತಮ ಮಾರುಕಟ್ಟೆ', 'metric_confidence': '🎯 ನಿಖರತೆ', 'metric_current_price': '💰 ಪ್ರಸ್ತುತ ದರ', 'metric_net_profit': '💵 ನಿವ್ವಳ ಲಾಭ', 'metric_predicted_price': '🔮 ಅಂದಾಜು ದರ', 'metric_prediction_range': '📊 ಬೆಲೆ ಶ್ರೇಣಿ', 'metric_r2_score': '📈 R² ಸ್ಕೋರ್', 'ml_analysis_title': '🤖 ML ಬೆಲೆ ಅಂದಾಜು ವಿಶ್ಲೇಷಣೆ', 'ml_caption': '3 ದಿನಗಳ ನಂತರ ನಿರೀಕ್ಷಿತ ಬೆಲೆ: {lower} – {upper}/ಕೆಜಿ | ಸರಾಸರಿ ದೋಷ: {mae}/ಕೆಜಿ', 'ml_unavailable_msg': '⚠️ ಈ ಬೆಳೆಗೆ ML ಬೆಲೆ ಅಂದಾಜು ವಿವರಗಳು ಲಭ್ಯವಿಲ್ಲ.', 'otp_box_title': '🔐 ಮೊಬೈಲ್ OTP ದೃಢೀಕರಣ', 'otp_check_phone_notice': '📩 6 ಅಂಕಿಯ OTP ಗಾಗಿ ದಯವಿಟ್ಟು ನಿಮ್ಮ ಮೊಬೈಲ್ SMS ಸಂದೇಶಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.', 'otp_label': '🔢 6 ಅಂಕಿಯ OTP ನಮೂದಿಸಿ', 'otp_placeholder': '6 ಅಂಕಿಯ OTP ನಮೂದಿಸಿ (ಉದಾ. 582910)', 'otp_resend_success': '✅ ಹೊಸ OTP ಅನ್ನು +91 {phone} ಗೆ ಯಶಸ್ವಿಯಾಗಿ ಕಳುಹಿಸಲಾಗಿದೆ!', 'otp_sent_to': '📲 ದೃಢೀಕರಣ ಕೋಡ್ +91 {phone} ಗೆ SMS ಮೂಲಕ ಕಳುಹಿಸಲಾಗಿದೆ', 'price_date_info': 'ದೃಢೀಕರಿಸಿದ ದಿನಾಂಕ: {date}', 'price_decrease_msg': '📉 ಬೆಲೆ ಇಳಿಕೆಯ ನಿರೀಕ್ಷೆ: {diff} ({pct})', 'price_increase_msg': '📈 ಬೆಲೆ ಹೆಚ್ಚಳದ ನಿರೀಕ್ಷೆ: {diff} ({pct})', 'price_stable_msg': '➡️ ಬೆಲೆಯಲ್ಲಿ ಹೆಚ್ಚಿನ ಬದಲಾವಣೆ ನಿರೀಕ್ಷೆಯಿಲ್ಲ.', 'quality_advice_grade_a': 'ನಿಮ್ಮ ಗ್ರೇಡ್ A ಬೆಳೆಗೆ ಉತ್ತಮ ಬೆಲೆ ದೊರೆಯಲಿದೆ. ತೇವಾಂಶದಿಂದ ರಕ್ಷಿಸಿ.', 'quality_advice_grade_b': 'ಮಧ್ಯಮ ದರ್ಜೆಯ ಬೆಳೆ. ಮಾರಾಟಕ್ಕೆ ಮುನ್ನ ಸಮೀಪದ ಮಾರುಕಟ್ಟೆಗಳ ದರ ಹೋಲಿಸಿ.', 'quality_advice_grade_c': 'ಗುಣಮಟ್ಟ ಮತ್ತಷ್ಟು ಕುಸಿಯುವ ಮುನ್ನ ತಕ್ಷಣ ಮಾರಾಟ ಮಾಡುವುದು ಸೂಕ್ತ.', 'quantity_kg': '⚖️ ಪ್ರಮಾಣ (ಕೆಜಿ / kg)', 'recommended_market_title': '🏪 ಶಿಫಾರಸು ಮಾಡಿದ ಮಾರುಕಟ್ಟೆ', 'resend_otp_btn': '🔄 ಮತ್ತೆ OTP ಕಳುಹಿಸಿ', 'rev_header': 'ಆದಾಯ ಅಂದಾಜು', 'route_logistics_title': 'ಮಾರ್ಗ ನ್ಯಾವಿಗೇಷನ್ ಮತ್ತು ಸಾರಿಗೆ ಮಾಹಿತಿ', 'select_crop': '🌱 ಬೆಳೆ ಆಯ್ಕೆಮಾಡಿ', 'select_price_date': '📅 ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ದಿನಾಂಕ', 'send_otp_btn': '📲 OTP ಕಳುಹಿಸಿ (Send OTP)', 'shelflife_title': 'ಬೆಳೆ ಬಾಳಿಕೆ ಮತ್ತು ಶೇಖರಣಾ ಅಪಾಯ ವಿಶ್ಲೇಷಣೆ', 'sidebar_crop_info_header': 'ಕೆಳಗೆ ನಿಮ್ಮ ಬೆಳೆ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ.', 'sidebar_farmer_details': '👨\u200d🌾 ರೈತರ ವಿವರಗಳು', 'sidebar_language': '🌐 ಭಾಷೆ ಬದಲಾಯಿಸಿ', 'sidebar_logout': '🚪 ಲಾಗ್\u200cಔಟ್', 'sidebar_phone': '📱 {phone}', 'sidebar_welcome': 'ನಮಸ್ಕಾರ, {name}!', 'slider_radius': '📍 ಹುಡುಕಾಟ ವ್ಯಾಪ್ತಿ (ಕಿ.ಮೀ)', 'sms_dispatched_toast': '📲 +91 {phone} ಗೆ SMS ಮೂಲಕ OTP ಕಳುಹಿಸಲಾಗಿದೆ!', 'sms_notif_card_sub': 'ನಿಮ್ಮ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಗೆ 6 ಅಂಕಿಯ ದೃಢೀಕರಣ ಕೋಡ್ ಕಳುಹಿಸಲಾಗಿದೆ. ಮುಂದುವರಿಯಲು ಅದನ್ನು ಕೆಳಗೆ ನಮೂದಿಸಿ.', 'sms_notif_card_title': 'ಮೊಬೈಲ್ SMS ಅಧಿಸೂಚನೆ ಕಳುಹಿಸಲಾಗಿದೆ', 'sync_success': '✅ {date} ರ ತಾಜಾ ಮಾರುಕಟ್ಟೆ ದರಗಳನ್ನು ಯಶಸ್ವಿಯಾಗಿ ಪಡೆಯಲಾಗಿದೆ!', 'tab1_chart_title': 'ಮಾರುಕಟ್ಟೆ ದರಗಳ ಚಾರ್ಟ್', 'tab1_header': 'ಮಾರುಕಟ್ಟೆ ದರಗಳ ಹೋಲಿಕೆ', 'tab1_no_data': '⚠️ ಮಾರುಕಟ್ಟೆ ಹೋಲಿಕೆ ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ.', 'tab2_best_profit_banner': '🏆 **ಹೆಚ್ಚು ಲಾಭದಾಯಕ ಮಾರುಕಟ್ಟೆ:** {market}\n\n💵 **ನಿರೀಕ್ಷಿತ ನಿವ್ವಳ ಲಾಭ:** {profit}', 'tab2_btn_nav': '🧭 {market} ಮಾರುಕಟ್ಟೆಗೆ ಗೂಗಲ್ ಮ್ಯಾಪ್ಸ್ ಮಾರ್ಗ', 'tab2_chart_title': 'ಮಾರುಕಟ್ಟೆವಾರು ನಿವ್ವಳ ಲಾಭ', 'tab2_header': 'ನಿವ್ವಳ ಲಾಭದ ವಿಶ್ಲೇಷಣೆ', 'tab2_transport_caption': '🚚 ಸಾರಿಗೆ ವೆಚ್ಚವನ್ನು ಮಾರುಕಟ್ಟೆ ದೂರ ಮತ್ತು ನಿಗದಿತ ದರದ ಆಧಾರದ ಮೇಲೆ ಲೆಕ್ಕಹಾಕಲಾಗುತ್ತದೆ.', 'tab3_caption': '📌 ಹಿಂದಿನ ದರಗಳನ್ನು ಲಭ್ಯವಿರುವ ಮಾರುಕಟ್ಟೆ ಡೇಟಾದಿಂದ ಲೆಕ್ಕಹಾಕಲಾಗಿದೆ.', 'tab3_decrease': '📉 ಬೆಲೆ ಇಳಿಕೆಯ ನಿರೀಕ್ಷೆ: {pct}%', 'tab3_header': 'ಹಿಂದಿನ ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಪ್ರವೃತ್ತಿ', 'tab3_increase': '📈 ಬೆಲೆ ಹೆಚ್ಚಳದ ನಿರೀಕ್ಷೆ: {pct}%', 'tab3_pred_header': 'ML ಬೆಲೆ ಅಂದಾಜು', 'tab3_range_info': '📊 **3 ದಿನಗಳ ನಿರೀಕ್ಷಿತ ಬೆಲೆ ಶ್ರೇಣಿ:** {lower} – {upper}/ಕೆಜಿ', 'tab3_stable': '➡️ ಯಾವುದೇ ದೊಡ್ಡ ಬದಲಾವಣೆ ನಿರೀಕ್ಷೆಯಿಲ್ಲ.', 'tab4_advisor_title': 'ರೈತ ಸಲಹಾ ಮಾಹಿತಿ', 'tab4_financial_impact': 'ಆರ್ಥಿಕ ಪರಿಣಾಮ ಮತ್ತು ಆದಾಯ ಅಂದಾಜು', 'tab4_header': 'AI ರೈತ ಸಲಹೆಗಾರ', 'tab4_logistics_guidance': 'ಸಾಗಾಟ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಮಾರ್ಗದರ್ಶನ', 'tab4_quality_guidance': 'ಗುಣಮಟ್ಟ ಮತ್ತು ಶೇಖರಣಾ ಸಲಹೆ', 'tab4_rationale_title': 'ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ದರದ ಮುನ್ನೋಟ', 'tab4_reason_label': 'ಪ್ರಮುಖ ಅಂಶ', 'tab4_rec_title': 'AI ಶಿಫಾರಸು', 'tab4_scores_title': 'ನಿರ್ಧಾರದ ಅಂಕಗಳು', 'tab4_summary_title': 'ಮಾರಾಟದ ಸಾರಾಂಶ', 'tab_ai_advisor': '🤖 AI ಸಲಹೆಗಾರ', 'tab_market_comparison': '📊 ಮಾರುಕಟ್ಟೆ ಹೋಲಿಕೆ', 'tab_price_trends': '📈 ಬೆಲೆ ಪ್ರವೃತ್ತಿ', 'tab_profit_analysis': '💰 ಲಾಭದ ವಿಶ್ಲೇಷಣೆ', 'time_hours_mins': '{h} ಗಂ {m} ನಿ', 'time_mins': '{m} ನಿಮಿಷಗಳು', 'verify_otp_btn': '🚀 OTP ಪರಿಶೀಲಿಸಿ ಮುಂದುವರಿಯಿರಿ', 'weather_title': 'ಹವಾಮಾನ ಮತ್ತು ಸಾರಿಗೆ ಮಾಹಿತಿ', 'transit_heavy_load_note': 'ಪ್ರಯಾಣದ ಸಮಯವನ್ನು ಭಾರಿ ಕೃಷಿ ಸರಕು ವಾಹನ (ಟ್ರಾಕ್ಟರ್ / ಟೆಂಪೋ ~24 ಕಿ.ಮೀ/ಗಂ) ಪ್ರಕಾರ ಲೆಕ್ಕಹಾಕಲಾಗಿದೆ. ಕಾರಿನ ಸಮಯವನ್ನು ಉಲ್ಲೇಖಕ್ಕಾಗಿ ತೋರಿಸಲಾಗಿದೆ.', 'lbl_heavy_load': 'ಭಾರಿ ಲೋಡ್', 'lbl_car_ref': 'ಕಾರು', 'lbl_auto_assessed': 'ಕೊಯ್ಲು ದಿನಾಂಕದ ಆಧಾರದ ಗುಣಮಟ್ಟ', 'lbl_days_post_harvest': 'ದಿನಗಳ ಹಿಂದೆ ಕೊಯ್ಲು', 'harvest_date_help': 'ಕೊಯ್ಲು ದಿನಾಂಕವನ್ನು ಆಯ್ಕೆಮಾಡಿ. ತಾಜಾತನವೇ ಮಾರುಕಟ್ಟೆ ಗ್ರೇಡ್ ನಿರ್ಧರಿಸುತ್ತದೆ.', 'crop_quality_help': 'ಗ್ರೇಡ್ A: ತಾಜಾ/ಅತ್ಯುತ್ತಮ; ಗ್ರೇಡ್ B: ಸಾಮಾನ್ಯ ಗ್ರೇಡ್; ಗ್ರೇಡ್ C: ಹಳೆಯ/ಕಡಿಮೆ ಗುಣಮಟ್ಟ.', 'tab_harvest_quality_title': 'ಕೊಯ್ಲಿನ ತಾಜಾತನ & ಗುಣಮಟ್ಟ', 'quality_fresh_status': 'ತಾಜಾ ಕೊಯ್ಲು', 'quality_basis_note': 'ಕೊಯ್ಲಿನ ದಿನಗಳ ಆಧಾರದ ಮೇಲೆ ಗ್ರೇಡ್ ನಿರ್ಧಾರವಾಗುತ್ತದೆ', 'tab_freshness_matrix': '🌾 ಗುಣಮಟ್ಟ & ತಾಜಾತನ ಮ್ಯಾಟ್ರಿಕ್ಸ್', 'btn_new_analysis': 'ಹೊಸ ವಿಶ್ಲೇಷಣೆ / ಮರುಹೊಂದಿಸಿ', 'matrix_title': 'ಬಹು ದಿನಗಳ ಬೆಳೆ ಗುಣಮಟ್ಟ ಇಳಿಕೆ ಮ್ಯಾಟ್ರಿಕ್ಸ್', 'matrix_subtitle': 'ಕೊಯ್ಲಿನ ನಂತರದ ದಿನಗಳ ಆಧಾರದ ಮೇಲೆ ನೇರ ಮಾರುಕಟ್ಟೆ ಗ್ರೇಡಿಂಗ್', 'matrix_caption_photo': 'ಈ ಮ್ಯಾಟ್ರಿಕ್ಸ್ ಆರು ಮುಖ್ಯ ಬೆಳೆಗಳ ಶೆಲ್ಫ್-ಲೈಫ್ ಮಾದರಿಯನ್ನು ತೋರಿಸುತ್ತದೆ.'}, 'mr': {'ai_decision_title': '🤖 AI विक्री निर्णय', 'analysis_success': '✅ बाजार विश्लेषण यशस्वीरित्या पूर्ण झाले!', 'analyzing_spinner': '🤖 AI एजंट बाजार परिस्थितीचे विश्लेषण करत आहे...', 'api_err_connection': '❌ बॅकएंड सर्व्हरशी संपर्क होऊ शकला नाही.\n\nकृपया बॅकएंड सुरू करा:\n\n`uvicorn backend.main:app --reload`', 'api_err_generic': '❌ AI एजंट त्रुटी: {e}', 'api_err_recommendation': '❌ AI शिफारस API त्रुटी', 'api_err_timeout': '⏱️ AI शिफारस विनंतीची वेळ संपली.', 'app_hero_desc': 'बाजारभावांची तुलना • भावी किमतींचा अंदाज • वाहतूक खर्च व निव्वळ नफा • लगेच विका किंवा थांबा याचा स्पष्ट सल्ला', 'app_hero_title': '🌾 शेतातून सर्वोत्तम बाजारापर्यंत — AI च्या मदतीने योग्य निर्णय', 'app_subtitle': 'शेतकऱ्यांसाठी योग्य बाजारभाव व नफा मिळवून देणारी AI प्रणाली', 'app_title': '🌾 शेतकरी बाजार मित्र', 'badge_gps_verified': '📍 जीपीएस प्रमाणित ({radius} किमी परिसर)', 'benefit_1': '📊 जवळील बाजार समित्यांमधील (APMC) दरांची थेट तुलना', 'benefit_2': '🚚 वाहतूक खर्च वजा करून मिळणाऱ्या निव्वळ नफ्याचा हिशोब', 'benefit_3': '🤖 AI अंदाज: माल आत्ताच विकावा की काही दिवस थांबावे याचा सल्ला', 'benefits_title': '💡 शेतकऱ्यांसाठी मुख्य फायदे:', 'btn_analyze': '🚀 बाजार विश्लेषण करा', 'btn_navigate_map': '🗺️ नकाशा मार्ग', 'btn_start_nav': '🧭 गुगल मॅप्सवर {market} बाजाराचा रस्ता सुरू करा', 'btn_sync_live': '🔄 ताजे बाजार भाव अपडेट करा', 'change_phone_btn': '✏️ नंबर बदला', 'choose_language': '🌐 तुमची भाषा निवडा (Choose Language)', 'col_date': 'तारीख', 'col_distance': 'रस्ता अंतर (किमी)', 'col_gross_rev': 'एकूण महसूल (₹)', 'col_handling_cost': 'हाताळणी खर्च (₹)', 'col_location': 'ठिकाण', 'col_market': 'बाजार', 'col_net_profit': 'निव्वळ नफा (₹)', 'col_price': 'भाव (₹/किलो)', 'col_rating': 'गुगल रेटिंग', 'col_transit_cost': 'अंदाजे वाहतूक', 'col_transport_cost': 'वाहतूक खर्च (₹)', 'col_travel_time': 'प्रवासाचा वेळ', 'conf_high_msg': '🟢 **उच्च अचूकता:** ऐतिहासिक नोंदींच्या आधारे हे मॉडेल मजबूत अंदाज दर्शवते.', 'conf_low_msg': '🔴 **कमी अचूकता:** स्थानिक बाजार परिस्थिती तपासूनच योग्य निर्णय घ्या.', 'conf_mod_msg': '🟡 **मध्यम अचूकता:** बाजारातील परिस्थितीमुळे प्रत्यक्ष भावात थोडा फरक पडू शकतो.', 'confidence_high': 'उच्च (High)', 'confidence_low': 'कमी (Low)', 'confidence_moderate': 'मध्यम (Moderate)', 'confidence_unavailable': 'उपलब्ध नाही', 'crop_quality': '⭐ पिकाचा दर्जा', 'dashboard_title': '📊 आपला बाजार माहिती डॅशबोर्ड', 'dec_neutral': 'तटस्थ (NEUTRAL)', 'dec_no_data': 'माहिती नाही', 'dec_sell_now': 'आत्ताच विका (SELL NOW)', 'dec_wait': 'काही दिवस थांबा (WAIT)', 'decision_nodata_banner': '### ℹ️ माहिती उपलब्ध नाही\n\nशिफारस करण्यासाठी पुरेसा डेटा उपलब्ध नाही.', 'decision_sell_banner': '### 🟢 आत्ताच विका (SELL NOW)\n\n**{market}** ही सध्याची सर्वोत्तम शिफारस केलेली बाजारपेठ आहे.\n\n💰 सध्याचा भाव: ₹{price}/किलो\n\n📍 अंतर: {dist} किमी', 'decision_wait_banner': '### 🟡 काही दिवस थांबा (WAIT)\n\nपुढील काळात भाव वाढण्याची शक्यता आहे.\n\n🔮 अंदाजित भाव: ₹{price}/किलो\n\n📈 चांगल्या भावासाठी थोडी प्रतीक्षा करणे फायदेशीर ठरेल.', 'demo_otp_banner': '📲 **[डेमो SMS]** आपला शेतकरी बाज़ार लॉगिन OTP: **{otp}** (5 मिनिटे वैध)', 'disclaimer_1': '📌 ही शिफारस ताजी बाजार माहिती, अंतर, निव्वळ नफा व ML भावाच्या अंदाजावर आधारित आहे.', 'disclaimer_2': '⚠️ भावाचा अंदाज केवळ मार्गदर्शनासाठी आहे. मागणी, पुरवठा आणि हवामानानुसार प्रत्यक्ष दरात बदल होऊ शकतो.', 'dist_approx_km': '~{dist:.1f} किमी (रस्ता)', 'err_name_required': 'कृपया आपले नाव प्रविष्ट करा.', 'err_otp_expired': '⏱️ OTP ची वेळ संपली. कृपया पुन्हा OTP पाठवा वर क्लिक करा.', 'err_otp_invalid': '❌ चुकीचा OTP. कृपया योग्य 6 अंकी कोड प्रविष्ट करा.', 'err_otp_required': 'कृपया 6 अंकी OTP प्रविष्ट करा.', 'err_phone_invalid': 'कृपया वैध 10 अंकी मोबाइल नंबर प्रविष्ट करा.', 'expected_harvest': '📅 काढणीची तारीख', 'farmer_location': '📍 आपले ठिकाण / गाव', 'farmer_name_label': '👤 शेतकऱ्याचे नाव', 'farmer_name_placeholder': 'उदा: तुकाराम / आपले नाव प्रविष्ट करा', 'farmer_phone_help': 'आपल्या वैयक्तिक बाजार माहिती व नोंदींसाठी', 'farmer_phone_label': '📱 मोबाईल नंबर', 'farmer_phone_placeholder': '10 अंकी मोबाईल नंबर टाका', 'glance_title': 'एका दृष्टीक्षेपात निर्णय', 'init_ai_intel': '### 🤖 AI तंत्रज्ञान\n\n- भावी किमतींचा अंदाज\n- भाव मर्यादा व अचूकता\n- विकावे की थांबावे?\n- निर्णय स्कोअर\n- शेतकरी सल्ला', 'init_fin_intel': '### 💰 आर्थिक नियोजन\n\n- एकूण महसूल\n- वाहतूक खर्च\n- हमाली व खर्च\n- पदरात पडणारा निव्वळ नफा', 'init_how_it_works': '### 🚀 हे कसे कार्य करते\n\n**शेतकरी माहिती → बाजार नोंदी → ML भाव अंदाज → AI एजंट → नफा विश्लेषण → योग्य विक्री सल्ला**', 'init_market_intel': '### 🏪 बाजार माहिती\n\n- सध्याचे बाजारभाव\n- विविध बाजारांची तुलना\n- सर्वोत्तम बाजाराची शिफारस\n- बाजाराचे अंतर', 'init_provides': 'ही प्रणाली आपल्याला काय देते', 'initial_info': '👈 डाव्या बाजूला साइडबारमध्ये पिकाची माहिती भरा आणि **🚀 बाजार विश्लेषण करा** वर क्लिक करा.', 'lbl_ai_decision': 'AI निर्णय', 'lbl_avg_price': 'सरासरी भाव', 'lbl_best_profit': 'सर्वोत्तम निव्वळ नफा', 'lbl_current_best_price': 'सध्याचा सर्वोत्तम भाव', 'lbl_damage_factors_title': '🔬 कापणीनंतरचे मुख्य नुकसान घटक:', 'lbl_discovered_markets': '{radius} किमी परिसरात सापडलेल्या बाजारपेठा ({count})', 'lbl_distance': '🚚 रस्ता अंतर', 'lbl_distance_km': 'रस्ता अंतर: {dist} किमी', 'lbl_exp_difference': 'अपेक्षित फरक', 'lbl_expected_rev': '3 दिवसांनंतर अपेक्षित उत्पन्न', 'lbl_farmer': 'शेतकरी', 'lbl_from_loc': 'प्रस्थान (आपले ठिकाण)', 'lbl_humidity': 'दमटपणा', 'lbl_location': '📍 ठिकाण', 'lbl_lower_est': 'किमान अंदाज', 'lbl_market': 'बाजार', 'lbl_max_price': 'कमाल भाव', 'lbl_min_price': 'किमान भाव', 'lbl_model_mae': 'सरासरी त्रुटी (MAE)', 'lbl_model_r2': 'मॉडेल R² स्कोअर', 'lbl_near_farmer': 'आपल्या स्थानाजवळ', 'lbl_per_km_rate': '₹2.5/किमी दराने', 'lbl_pred_3days': 'अंदाजित भाव (3 दिवस)', 'lbl_price': '💰 भाव', 'lbl_quality': 'दर्जा', 'lbl_quantity': 'प्रमाण', 'lbl_rain_prob': 'पावसाची शक्यता', 'lbl_rating': '⭐ गुगल रेटिंग', 'lbl_rec_market': 'शिफारस केलेली बाजारपेठ', 'lbl_safe_window': 'सुरक्षित कालावधी: ~{days} दिवस', 'lbl_sell_now_rev': 'आत्ता विकल्यास उत्पन्न', 'lbl_sell_score': 'आत्ताच विक्री स्कोअर', 'lbl_shelf_life': 'कमाल साठवणूक कालावधी', 'lbl_spoilage_rate': 'दैनिक नुकसान दर', 'lbl_spoilage_risk': 'खराब होण्याची जोखीम', 'lbl_temperature': 'तापमान', 'lbl_to_mandi': 'गंतव्य (लक्षित बाजार)', 'lbl_transit_adv': 'वाहतूक अनुकूलता', 'lbl_transit_guide': 'वाहतूक मार्गदर्शन', 'lbl_transport_cost': 'अंदाजित वाहतूक खर्च', 'lbl_travel_time': 'अंदाजित प्रवासाची वेळ', 'lbl_upper_est': 'कमाल अंदाज', 'lbl_wait_score': 'प्रतीक्षा स्कोअर', 'live_prices_badge': '🟢 थेट दैनिक बाजार भाव (Agmarknet APMC)', 'login_box_title': '🔐 शेतकरी प्रोफाइल / लॉगिन', 'login_btn': '🚀 डॅशबोर्डवर पुढे जा', 'login_hero_desc': 'शेतकरी बांधवांसाठी विशेष डिझाइन केलेले व्यासपीठ. आपल्या कष्टाच्या मालाला योग्य भाव मिळवा.', 'login_hero_title': '👨\u200d🌾 शेतकरी बाजार मित्रात आपले स्वागत आहे!', 'maps_caption': '📱 क्लिक केल्यास थेट गुगल मॅप्स उघडेल व जलद रस्ता आणि ट्रॅफिक दिसेल.', 'metric_best_market': '🏪 सर्वोत्तम बाजार', 'metric_confidence': '🎯 अचूकता', 'metric_current_price': '💰 सध्याचा भाव', 'metric_net_profit': '💵 निव्वळ नफा', 'metric_predicted_price': '🔮 अंदाजित भाव', 'metric_prediction_range': '📊 अंदाज मर्यादा', 'metric_r2_score': '📈 R² स्कोअर', 'ml_analysis_title': '🤖 ML किंमत अंदाज विश्लेषण', 'ml_caption': '3 दिवसांनंतर अपेक्षित भाव: {lower} – {upper}/किलो | सरासरी त्रुटी: {mae}/किलो', 'ml_unavailable_msg': '⚠️ या पिकासाठी ML अंदाज उपलब्ध नाही.', 'otp_box_title': '🔐 मोबाईल OTP पडताळणी', 'otp_check_phone_notice': '📩 6 अंकी OTP साठी कृपया आपल्या मोबाईलवरील SMS संदेश तपासा.', 'otp_label': '🔢 6 अंकी OTP प्रविष्ट करा', 'otp_placeholder': '6 अंकी OTP टाका (उदा. 582910)', 'otp_resend_success': '✅ नवीन OTP +91 {phone} वर यशस्वीपणे पाठवला आहे!', 'otp_sent_to': '📲 पडताळणी कोड +91 {phone} वर SMS द्वारे पाठवला आहे', 'price_date_info': 'पडताळणी दिनांक: {date}', 'price_decrease_msg': '📈 भाव घसरणीचा अंदाज: {diff} ({pct})', 'price_increase_msg': '📈 भाव वाढीचा अंदाज: {diff} ({pct})', 'price_stable_msg': '➡️ भावात कोणताही मोठा बदल संभवत नाही.', 'quality_advice_grade_a': 'तुमच्या ग्रेड A मालाला बाजारात उत्तम भाव मिळू शकतो. ओलाव्यापासून वाचवा.', 'quality_advice_grade_b': 'मध्यम दर्जाचा माल. विक्रीपूर्वी जवळच्या इतर बाजारांचे भाव तपासा.', 'quality_advice_grade_c': 'मालाचा दर्जा आणखी घसरण्यापूर्वी लवकरात लवकर विक्री करणे फायद्याचे ठरेल.', 'quantity_kg': '⚖️ प्रमाण (किलो / kg)', 'recommended_market_title': '🏪 शिफारस केलेली बाजारपेठ', 'resend_otp_btn': '🔄 पुन्हा OTP पाठवा', 'rev_header': 'उत्पन्नाचा अंदाज', 'route_logistics_title': 'रस्ता नेव्हिगेशन आणि वाहतूक नियोजन', 'select_crop': '🌱 पीक निवडा', 'select_price_date': '📅 बाजार भाव दिनांक', 'send_otp_btn': '📲 OTP पाठवा (Send OTP)', 'shelflife_title': 'पिकाचे आयुष्य व साठवणूक जोखीम विश्लेषण', 'sidebar_crop_info_header': 'खाली आपल्या पिकाची माहिती भरा.', 'sidebar_farmer_details': '👨\u200d🌾 शेतकरी माहिती', 'sidebar_language': '🌐 भाषा बदला', 'sidebar_logout': '🚪 लॉगआउट', 'sidebar_phone': '📱 {phone}', 'sidebar_welcome': 'नमस्कार, {name}!', 'slider_radius': '📍 शोध त्रिज्या (किमी)', 'sms_dispatched_toast': '📲 +91 {phone} वर SMS द्वारे OTP पाठवला गेला!', 'sms_notif_card_sub': 'आपल्या मोबाईल नंबरवर 6 अंकी पडताळणी कोड पाठवला गेला आहे. पुढे जाण्यासाठी तो खाली प्रविष्ट करा.', 'sms_notif_card_title': 'मोबाईल SMS सूचना पाठवली आहे', 'sync_success': '✅ {date} चे ताजे बाजार भाव यशस्वीरित्या लोड झाले!', 'tab1_chart_title': 'बाजारभाव आलेख', 'tab1_header': 'बाजारभाव तुलना', 'tab1_no_data': '⚠️ बाजार माहिती उपलब्ध नाही.', 'tab2_best_profit_banner': '🏆 **सर्वाधिक फायदेशीर बाजारपेठ:** {market}\n\n💵 **अपेक्षित निव्वळ नफा:** {profit}', 'tab2_btn_nav': '🧭 {market} बाजाराचा गुगल मॅप्स रस्ता', 'tab2_chart_title': 'बाजारपेठेनुसार निव्वळ नफा', 'tab2_header': 'निव्वळ नफा विश्लेषण', 'tab2_transport_caption': '🚚 वाहतूक खर्च बाजाराचे अंतर व ठरवून दिलेल्या दरावरून काढला आहे.', 'tab3_caption': '📌 मागील दर उपलब्ध बाजार नोंदींवरून काढले आहेत.', 'tab3_decrease': '📉 घसरणीचा अंदाज: {pct}%', 'tab3_header': 'ऐतिहासिक बाजारभाव कल', 'tab3_increase': '📈 वाढीचा अंदाज: {pct}%', 'tab3_pred_header': 'ML किंमत अंदाज', 'tab3_range_info': '📊 **3 दिवसांचा अपेक्षित भाव पट्टा:** {lower} – {upper}/किलो', 'tab3_stable': '➡️ कोणताही मोठा बदल संभवत नाही.', 'tab4_advisor_title': 'शेतकरी सल्ला', 'tab4_financial_impact': 'आर्थिक परिणाम व उत्पन्न अंदाज', 'tab4_header': 'AI शेतकरी सल्लागार', 'tab4_logistics_guidance': 'वाहतूक आणि बाजार मार्गदर्शन', 'tab4_quality_guidance': 'गुणवत्ता आणि साठवणूक सल्ला', 'tab4_rationale_title': 'बाजार विश्लेषण आणि भाव अंदाज', 'tab4_reason_label': 'मुख्य घटक', 'tab4_rec_title': 'AI शिफारस', 'tab4_scores_title': 'निर्णय स्कोअर', 'tab4_summary_title': 'विक्री सारांश', 'tab_ai_advisor': '🤖 AI सल्लागार', 'tab_market_comparison': '📊 बाजारपेठ तुलना', 'tab_price_trends': '📈 दर कल', 'tab_profit_analysis': '💰 नफा विश्लेषण', 'time_hours_mins': '{h} तास {m} मि', 'time_mins': '{m} मिनिटे', 'verify_otp_btn': '🚀 OTP पडताळणी करा आणि पुढे जा', 'weather_title': 'हवामान आणि वाहतूक सल्ला', 'transit_heavy_load_note': 'प्रवासाचा वेळ शेतमालाने भरलेल्या वाहनानुसार (ट्रॅक्टर-ट्रॉली / टेम्पो ~24 किमी/तास) मोजला गेला आहे. कारचा वेळ संदर्भासाठी दाखवला आहे.', 'lbl_heavy_load': 'भारी लोड', 'lbl_car_ref': 'कार', 'lbl_auto_assessed': 'कापणीच्या तारखेनुसार गुणवत्ता निर्धारण', 'lbl_days_post_harvest': 'दिवसांपूर्वी कापणी', 'harvest_date_help': 'कापणीची तारीख निवडा. ताजेपणाच बाजारातील प्रत ठरवतो.', 'crop_quality_help': 'ग्रेड A: ताजी/उत्तम; ग्रेड B: सामान्य प्रत; ग्रेड C: जुनी/कमी दर्जा.', 'tab_harvest_quality_title': 'कापणीचा ताजेपणा आणि गुणवत्ता', 'quality_fresh_status': 'ताजी कापणी', 'quality_basis_note': 'कापणीनंतरच्या दिवसांनुसार प्रत बदलते', 'tab_freshness_matrix': '🌾 पीक गुणवत्ता मॅट्रिक्स', 'btn_new_analysis': 'नवीन विश्लेषण / रीसेट', 'matrix_title': 'बहु-दिवसीय पीक गुणवत्ता घसरण मॅट्रिक्स', 'matrix_subtitle': 'कापणीनंतरच्या दिवसांनुसार थेट बाजारपेठ प्रतवारी', 'matrix_caption_photo': 'हे मॅट्रिक्स प्रमुख पिकांची साठवण क्षमता दर्शवते.'}, 'ta': {'ai_decision_title': '🤖 AI விற்பனை முடிவு', 'analysis_success': '✅ சந்தை பகுப்பாய்வு வெற்றிகரமாக முடிந்தது!', 'analyzing_spinner': '🤖 AI முகவர் சந்தை நிலவரங்களை ஆராய்கிறது...', 'api_err_connection': '❌ சர்வர் இணைப்பு தோல்வியடைந்தது.\n\nதயவுசெய்து சரிபார்க்கவும்:\n\n`uvicorn backend.main:app --reload`', 'api_err_generic': '❌ AI பிழை: {e}', 'api_err_recommendation': '❌ AI பரிந்துரை API பிழை', 'api_err_timeout': '⏱️ AI பரிந்துரை கோரிக்கை நேரம் முடிந்தது.', 'app_hero_desc': 'சந்தை விலைகள் ஒப்பீடு • விலை கணிப்பு • போக்குவரத்து & நிகர லாபம் • விற்கவா அல்லது காத்திருக்கவா என்ற தெளிவான பரிந்துரை', 'app_hero_title': '🌾 விளைநிலத்திலிருந்து சிறந்த சந்தைக்கு — AI வழிகாட்டல்', 'app_subtitle': 'விவசாயிகள் சிறந்த விற்பனை முடிவுகளை எடுக்க உதவும் AI தளம்', 'app_title': '🌾 உழவர் சந்தை நுண்ணறிவு', 'badge_gps_verified': '📍 GPS சரிபார்க்கப்பட்டது ({radius} கி.மீ)', 'benefit_1': '📊 அருகிலுள்ள சந்தைகளின் தற்போதைய விலை ஒப்பீடு', 'benefit_2': '🚚 போக்குவரத்து செலவு போக உங்கள் உண்மையான நிகர லாபக் கணக்கீடு', 'benefit_3': '🤖 AI விலை கணிப்பு: உடனே விற்க வேண்டுமா அல்லது காத்திருக்க வேண்டுமா என்ற வழிகாட்டல்', 'benefits_title': '💡 விவசாயிகளுக்கான முக்கிய நன்மைகள்:', 'btn_analyze': '🚀 சந்தையை ஆராய்க', 'btn_navigate_map': '🗺️ வழித்தடம்', 'btn_start_nav': '🧭 கூகிள் மேப்ஸில் {market} சந்தைக்கான வழியைத் திறக்கவும்', 'btn_sync_live': '🔄 நேரடி சந்தை விலைகளைப் புதுப்பிக்கவும்', 'change_phone_btn': '✏️ எண்ணை மாற்றவும்', 'choose_language': '🌐 உங்கள் மொழியைத் தேர்ந்தெடுக்கவும் (Choose Language)', 'col_date': 'தேதி', 'col_distance': 'தொலைவு (கி.மீ)', 'col_gross_rev': 'மொத்த வருவாய் (₹)', 'col_handling_cost': 'கையாளுதல் செலவு (₹)', 'col_location': 'இடம்', 'col_market': 'சந்தை', 'col_net_profit': 'நிகர லாபம் (₹)', 'col_price': 'விலை (₹/கிலோ)', 'col_rating': 'கூகிள் மதிப்பீடு', 'col_transit_cost': 'போக்குவரத்து செலவு', 'col_transport_cost': 'போக்குவரத்து செலவு (₹)', 'col_travel_time': 'பயண நேரம்', 'conf_high_msg': '🟢 **அதிக நம்பகத்தன்மை:** வரலாற்றுத் தரவுகளின்படி மாதிரி அதிக துல்லியத்தைக் காட்டுகிறது.', 'conf_low_msg': '🔴 **குறைந்த நம்பகத்தன்மை:** தற்போதைய சந்தை நிலவரத்தையும் கவனித்து முடிவெடுக்கவும்.', 'conf_mod_msg': '🟡 **நடுத்தர நம்பகத்தன்மை:** சந்தை நிலைமைகளால் விலையில் சிறிய மாற்றங்கள் ஏற்படலாம்.', 'confidence_high': 'அதிகம் (High)', 'confidence_low': 'குறைவு (Low)', 'confidence_moderate': 'நடுத்தரம் (Moderate)', 'confidence_unavailable': 'கிடைக்கவில்லை', 'crop_quality': '⭐ பயிர் தரம்', 'dashboard_title': '📊 உங்கள் சந்தை நுண்ணறிவு கட்டுப்பாட்டகம்', 'dec_neutral': 'நடுநிலை (NEUTRAL)', 'dec_no_data': 'தகவல் இல்லை', 'dec_sell_now': 'இப்போதே விற்கவும் (SELL NOW)', 'dec_wait': 'காத்திருக்கவும் (WAIT)', 'decision_nodata_banner': '### ℹ️ தகவல் இல்லை\n\nபரிந்துரை வழங்க போதுமான சந்தை தகவல் இல்லை.', 'decision_sell_banner': '### 🟢 இப்போதே விற்கவும் (SELL NOW)\n\n**{market}** தற்போது பரிந்துரைக்கப்பட்ட சிறந்த சந்தை.\n\n💰 தற்போதைய விலை: ₹{price}/கிலோ\n\n📍 தொலைவு: {dist} கி.மீ', 'decision_wait_banner': '### 🟡 காத்திருக்கவும் (WAIT)\n\nவிலை உயரக்கூடும் என கணிக்கப்பட்டுள்ளது.\n\n🔮 கணிக்கப்பட்ட விலை: ₹{price}/கிலோ\n\n📈 நல்ல விலை கிடைக்கும் வரை காத்திருப்பது நல்லது.', 'demo_otp_banner': '📲 **[டெமோ SMS]** உங்கள் உள்நுழைவு OTP: **{otp}** (5 நிமிடங்கள் செல்லுபடியாகும்)', 'disclaimer_1': '📌 இந்த பரிந்துரை சமீபத்திய சந்தை விலைகள், தூரம், நிகர லாபம் மற்றும் ML விலை கணிப்பின் அடிப்படையில் அமைந்துள்ளது.', 'disclaimer_2': '⚠️ விலை கணிப்புகள் மதிப்பீடுகள் மட்டுமே. தேவை, விநியோகம் மற்றும் வானிலைக்கு ஏற்ப உண்மையான விலைகள் மாறுபடலாம்.', 'dist_approx_km': '~{dist:.1f} கி.மீ (சாலை)', 'err_name_required': 'தயவுசெய்து உங்கள் பெயரை உள்ளிடவும்.', 'err_otp_expired': '⏱️ OTP காலாவதியானது. மீண்டும் அனுப்பவும் கிளிக் செய்யவும்.', 'err_otp_invalid': '❌ தவறான OTP. சரியான 6 இலக்க குறியீட்டை உள்ளிடவும்.', 'err_otp_required': 'தயவுசெய்து 6 இலக்க OTP ஐ உள்ளிடவும்.', 'err_phone_invalid': 'சரியான 10 இலக்க கைபேசி எண்ணை உள்ளிடவும்.', 'expected_harvest': '📅 அறுவடை தேதி', 'farmer_location': '📍 உங்கள் இருப்பிடம்', 'farmer_name_label': '👤 விவசாயி பெயர்', 'farmer_name_placeholder': 'எ.கா: முருகன் / உங்கள் பெயரை உள்ளிடவும்', 'farmer_phone_help': 'சந்தை விலை அறிவிப்புகள் மற்றும் விவரங்களுக்கு', 'farmer_phone_label': '📱 கைபேசி எண்', 'farmer_phone_placeholder': '10 இலக்க மொபைல் எண்ணை உள்ளிடவும்', 'glance_title': 'சுருக்கமான முடிவு', 'init_ai_intel': '### 🤖 AI நுண்ணறிவு\n\n- எதிர்கால விலை கணிப்பு\n- விலை வரம்பு & நம்பகத்தன்மை\n- விற்கவா அல்லது காத்திருக்கவா?\n- முடிவு மதிப்பெண்கள்\n- உழவர் வழிகாட்டுதல்', 'init_fin_intel': '### 💰 நிதி பகுப்பாய்வு\n\n- மொத்த வருவாய்\n- போக்குவரத்து செலவு\n- கையாளுதல் செலவு\n- கையில் கிடைக்கும் நிகர லாபம்', 'init_how_it_works': '### 🚀 இது எவ்வாறு செயல்படுகிறது\n\n**உழவர் தகவல் → சந்தைத் தரவு → ML விலை கணிப்பு → AI முகவர் → லாபப் பகுப்பாய்வு → விற்பனை பரிந்துரை**', 'init_market_intel': '### 🏪 சந்தை நுண்ணறிவு\n\n- தற்போதைய சந்தை விலைகள்\n- சந்தை ஒப்பீடு\n- சிறந்த சந்தை பரிந்துரை\n- சந்தை தொலைவு', 'init_provides': 'இந்த தளம் உங்களுக்கு என்ன வழங்குகிறது', 'initial_info': '👈 பக்கப்பட்டியில் உங்கள் பயிர் விவரங்களை உள்ளிட்டு **🚀 சந்தையை ஆராய்க** பொத்தானை அழுத்தவும்.', 'lbl_ai_decision': 'AI முடிவு', 'lbl_avg_price': 'சராசரி விலை', 'lbl_best_profit': 'அதிகபட்ச நிகர லாபம்', 'lbl_current_best_price': 'தற்போதைய சிறந்த விலை', 'lbl_damage_factors_title': '🔬 அறுவடைக்கு பின் சேத காரணிகள்:', 'lbl_discovered_markets': '{radius} கி.மீ சுற்றளவில் கண்டறியப்பட்ட சந்தைகள் ({count})', 'lbl_distance': '🚚 தொலைவு', 'lbl_distance_km': 'தொலைவு: {dist} கி.மீ', 'lbl_exp_difference': 'எதிர்பார்க்கப்படும் வித்தியாசம்', 'lbl_expected_rev': '3 நாட்கள் கழித்து எதிர்பார்க்கப்படும் வருவாய்', 'lbl_farmer': 'விவசாயி', 'lbl_from_loc': 'புறப்படும் இடம் (உங்கள் இருப்பிடம்)', 'lbl_humidity': 'ஈரப்பதம்', 'lbl_location': '📍 இடம்', 'lbl_lower_est': 'குறைந்தபட்ச மதிப்பீடு', 'lbl_market': 'சந்தை', 'lbl_max_price': 'அதிகபட்ச விலை', 'lbl_min_price': 'குறைந்தபட்ச விலை', 'lbl_model_mae': 'சராசரி பிழை (MAE)', 'lbl_model_r2': 'மாதிரி R² மதிப்பெண்', 'lbl_near_farmer': 'உங்கள் இடத்திற்கு அருகில்', 'lbl_per_km_rate': '₹2.5/கி.மீ வீதம்', 'lbl_pred_3days': 'கணிக்கப்பட்ட விலை (3 நாட்கள்)', 'lbl_price': '💰 விலை', 'lbl_quality': 'தரம்', 'lbl_quantity': 'அளவு', 'lbl_rain_prob': 'மழை வாய்ப்பு', 'lbl_rating': '⭐ கூகிள் மதிப்பீடு', 'lbl_rec_market': 'பரிந்துரைக்கப்பட்ட சந்தை', 'lbl_safe_window': 'பாதுகாப்பான காலம்: ~{days} நாட்கள்', 'lbl_sell_now_rev': 'உடனே விற்றால் வருவாய்', 'lbl_sell_score': 'இப்போதே விற்கும் மதிப்பெண்', 'lbl_shelf_life': 'அதிகபட்ச சேமிப்பு காலம்', 'lbl_spoilage_rate': 'தினசரி இழப்பு விகிதம்', 'lbl_spoilage_risk': 'அழுகும் அபாயம்', 'lbl_temperature': 'வெப்பநிலை', 'lbl_to_mandi': 'சேருமிடம் (இலக்கு சந்தை)', 'lbl_transit_adv': 'போக்குவரத்து நிலை', 'lbl_transit_guide': 'போக்குவரத்து வழிகாட்டல்', 'lbl_transport_cost': 'போக்குவரத்து செலவு', 'lbl_travel_time': 'பயண நேரம்', 'lbl_upper_est': 'அதிகபட்ச மதிப்பீடு', 'lbl_wait_score': 'காத்திருப்பு மதிப்பெண்', 'live_prices_badge': '🟢 நேரடி தினசரி சந்தை விலைகள் (Agmarknet APMC)', 'login_box_title': '🔐 உழவர் சுயவிவரம் / உள்நுழைவு', 'login_btn': '🚀 தொடரவும்', 'login_hero_desc': 'விவசாயிகளுக்காக வடிவமைக்கப்பட்ட ஸ்மார்ட் தளம். உங்கள் உழைப்பிற்கு சிறந்த விலை பெறுங்கள்.', 'login_hero_title': '👨\u200d🌾 உழவர் சந்தை நுண்ணறிவுக்கு நல்வரவு!', 'maps_caption': '📱 இதைத் தொட்டால் நேரலை ஜிபிஎஸ் மற்றும் போக்குவரத்து விவரங்களுடன் கூகிள் மேப்ஸ் திறக்கும்.', 'metric_best_market': '🏪 சிறந்த சந்தை', 'metric_confidence': '🎯 நம்பகத்தன்மை', 'metric_current_price': '💰 தற்போதைய விலை', 'metric_net_profit': '💵 நிகர லாபம்', 'metric_predicted_price': '🔮 கணிக்கப்பட்ட விலை', 'metric_prediction_range': '📊 விலை வரம்பு', 'metric_r2_score': '📈 R² மதிப்பெண்', 'ml_analysis_title': '🤖 ML விலை கணிப்பு பகுப்பாய்வு', 'ml_caption': '3 நாட்களுக்குப் பின் எதிர்பார்க்கப்படும் விலை: {lower} – {upper}/கிலோ | சராசரி பிழை: {mae}/கிலோ', 'ml_unavailable_msg': '⚠️ இந்த பயிருக்கான ML கணிப்பு விவரங்கள் கிடைக்கவில்லை.', 'otp_box_title': '🔐 மொபைல் OTP சரிபார்ப்பு', 'otp_check_phone_notice': '📩 6 இலக்க OTP குறியீட்டிற்கு உங்கள் மொபைல் SMS செய்திகளைப் பார்க்கவும்.', 'otp_label': '🔢 6 இலக்க OTP ஐ உள்ளிடவும்', 'otp_placeholder': '6 இலக்க OTP உள்ளிடவும் (எ.கா. 582910)', 'otp_resend_success': '✅ புதிய OTP +91 {phone} க்கு அனுப்பப்பட்டது!', 'otp_sent_to': '📲 சரிபார்ப்புக் குறியீடு +91 {phone} க்கு SMS மூலம் அனுப்பப்பட்டது', 'price_date_info': 'சரிபார்க்கப்பட்ட தேதி: {date}', 'price_decrease_msg': '📉 விலை குறைவு எதிர்பார்ப்பு: {diff} ({pct})', 'price_increase_msg': '📈 விலை உயர்வு எதிர்பார்ப்பு: {diff} ({pct})', 'price_stable_msg': '➡️ விலையில் பெரிய மாற்றம் எதிர்பார்க்கப்படவில்லை.', 'quality_advice_grade_a': 'உங்கள் தரம் A பயிருக்கு நல்ல விலை கிடைக்கும். ஈரப்பதம் படாமல் பாதுகாக்கவும்.', 'quality_advice_grade_b': 'நடுத்தர தரம். விற்பனைக்கு முன் பிற சந்தை விலைகளை ஒப்பிட்டுப் பார்க்கவும்.', 'quality_advice_grade_c': 'தரம் மேலும் குறையாமல் இருக்க விரைவாக விற்பது நல்லது.', 'quantity_kg': '⚖️ அளவு (கிலோ / kg)', 'recommended_market_title': '🏪 பரிந்துரைக்கப்பட்ட சந்தை', 'resend_otp_btn': '🔄 மீண்டும் OTP அனுப்பவும்', 'rev_header': 'வருவாய் மதிப்பீடு', 'route_logistics_title': 'வழிசெலுத்தல் மற்றும் போக்குவரத்து வழிகாட்டி', 'select_crop': '🌱 பயிரைத் தேர்ந்தெடுக்கவும்', 'select_price_date': '📅 சந்தை விலை தேதி', 'send_otp_btn': '📲 OTP அனுப்பவும் (Send OTP)', 'shelflife_title': 'பயிர் ஆயுள் மற்றும் சேமிப்பு அபாய பகுப்பாய்வு', 'sidebar_crop_info_header': 'உங்கள் பயிர் தகவல்களை உள்ளிடவும்.', 'sidebar_farmer_details': '👨\u200d🌾 உழவர் விவரங்கள்', 'sidebar_language': '🌐 மொழி மாற்றம்', 'sidebar_logout': '🚪 வெளியேறு', 'sidebar_phone': '📱 {phone}', 'sidebar_welcome': 'வணக்கம், {name}!', 'slider_radius': '📍 தேடல் ஆரம் (கி.மீ)', 'sms_dispatched_toast': '📲 +91 {phone} க்கு SMS மூலம் OTP அனுப்பப்பட்டது!', 'sms_notif_card_sub': 'உங்கள் மொபைல் எண்ணுக்கு 6 இலக்க சரிபார்ப்புக் குறியீடு அனுப்பப்பட்டுள்ளது. தொடர அதை கீழே உள்ளிடவும்.', 'sms_notif_card_title': 'மொபைல் SMS அறிவிப்பு அனுப்பப்பட்டது', 'sync_success': '✅ {date} க்கான புதிய சந்தை விலைகள் பெறப்பட்டன!', 'tab1_chart_title': 'சந்தை விலை விளக்கப்படம்', 'tab1_header': 'சந்தை விலை ஒப்பீடு', 'tab1_no_data': '⚠️ சந்தை ஒப்பீட்டுத் தகவல் இல்லை.', 'tab2_best_profit_banner': '🏆 **அதிக லாபகரமான சந்தை:** {market}\n\n💵 **எதிர்பார்க்கப்படும் நிகர லாபம்:** {profit}', 'tab2_btn_nav': '🧭 {market} சந்தைக்கான மேப்ஸ் வழியைத் திறக்கவும்', 'tab2_chart_title': 'சந்தை வாரியாக நிகர லாபம்', 'tab2_header': 'நிகர லாப பகுப்பாய்வு', 'tab2_transport_caption': '🚚 போக்குவரத்து செலவு சந்தை தூரம் மற்றும் கட்டணத்தின் அடிப்படையில் கணக்கிடப்படுகிறது.', 'tab3_caption': '📌 வரலாற்று விலைகள் சந்தைத் தரவுகளின் அடிப்படையில் கணக்கிடப்படுகின்றன.', 'tab3_decrease': '📉 விலை குறைவு எதிர்பார்ப்பு: {pct}%', 'tab3_header': 'வரலாற்று சந்தை விலை போக்கு', 'tab3_increase': '📈 விலை உயர்வு எதிர்பார்ப்பு: {pct}%', 'tab3_pred_header': 'ML விலை கணிப்பு', 'tab3_range_info': '📊 **3 நாட்களுக்கான எதிர்பார்க்கப்படும் விலை வரம்பு:** {lower} – {upper}/கிலோ', 'tab3_stable': '➡️ பெரிய மாற்றம் எதிர்பார்க்கப்படவில்லை.', 'tab4_advisor_title': 'உழவர் வழிகாட்டுதல்', 'tab4_financial_impact': 'நிதி தாக்கம் & வருமான மதிப்பீடு', 'tab4_header': 'AI உழவர் ஆலோசகர்', 'tab4_logistics_guidance': 'போக்குவரத்து & சந்தை வழிகாட்டல்', 'tab4_quality_guidance': 'தரம் & சேமிப்பு வழிகாட்டல்', 'tab4_rationale_title': 'சந்தை பகுப்பாய்வு & விலை பார்வை', 'tab4_reason_label': 'முக்கிய காரணி', 'tab4_rec_title': 'AI பரிந்துரை', 'tab4_scores_title': 'முடிவு மதிப்பெண்கள்', 'tab4_summary_title': 'விற்பனை சுருக்கம்', 'tab_ai_advisor': '🤖 AI ஆலோசகர்', 'tab_market_comparison': '📊 சந்தை ஒப்பீடு', 'tab_price_trends': '📈 விலை போக்குகள்', 'tab_profit_analysis': '💰 லாபப் பகுப்பாய்வு', 'time_hours_mins': '{h} மணி {m} நிமி', 'time_mins': '{m} நிமிடங்கள்', 'verify_otp_btn': '🚀 OTP சரிபார்த்து தொடரவும்', 'weather_title': 'வானிலை மற்றும் போக்குவரத்து ஆலோசனை', 'transit_heavy_load_note': 'பயண நேரம் கனரக விவசாய போக்குவரத்து (டிராக்டர் / டெம்போ ~24 கி.மீ/மணி) படி கணக்கிடப்படுகிறது. கார் நேரம் குறிப்புக்காக காட்டப்பட்டுள்ளது.', 'lbl_heavy_load': 'கனரக சுமை', 'lbl_car_ref': 'கார்', 'lbl_auto_assessed': 'அறுவடை தேதி அடிப்படையிலான தரம்', 'lbl_days_post_harvest': 'நாட்கள் முன் அறுவடை', 'harvest_date_help': 'அறுவடை தேதியைத் தேர்ந்தெடுக்கவும். புத்துணர்ச்சியே தரத்தை நிர்ணயிக்கிறது.', 'crop_quality_help': 'தரம் A: புதிய/பிரீமியம்; தரம் B: வழக்கமான தரம்; தரம் C: பழைய/குறைந்த தரம்.', 'tab_harvest_quality_title': 'அறுவடை புத்துணர்ச்சி & தரம்', 'quality_fresh_status': 'புதிய அறுவடை', 'quality_basis_note': 'அறுவடை நாட்களின் அடிப்படையில் தரம் தீர்மானிக்கப்படுகிறது', 'tab_freshness_matrix': '🌾 தரம் மற்றும் புத்துணர்ச்சி அணி', 'btn_new_analysis': 'புதிய பகுப்பாய்வு / மீட்டமை', 'matrix_title': 'பல நாள் பயிர் தரம் இழப்பு அணி', 'matrix_subtitle': 'அறுவடை நாட்களின் அடிப்படையில் நேரடி மண்டி தர நிர்ணயம்', 'matrix_caption_photo': 'இந்த அணி ஆறு முக்கிய பயிர்களின் அடுக்கு வாழ்க்கை முறையை விவரிக்கிறது.'}, 'te': {'ai_decision_title': '🤖 AI అమ్మకపు నిర్ణయం', 'analysis_success': '✅ మార్కెట్ విశ్లేషణ విజయవంతంగా పూర్తయింది!', 'analyzing_spinner': '🤖 AI ఏజెంట్ మార్కెట్ పరిస్థితులను విశ్లేషిస్తోంది...', 'api_err_connection': '❌ సర్వర్\u200cకు కనెక్ట్ కాలేకపోతున్నాము.\n\nదయచేసి బ్యాకెండ్ రన్ అవుతుందో లేదో చూడండి:\n\n`uvicorn backend.main:app --reload`', 'api_err_generic': '❌ AI ఏజెంట్ లోపం: {e}', 'api_err_recommendation': '❌ AI సిఫార్సు API లోపం', 'api_err_timeout': '⏱️ AI సిఫార్సు అభ్యర్థన సమయం ముగిసింది.', 'app_hero_desc': 'మార్కెట్ ధరలు పోల్చండి • ధరల అంచనా • రవాణా ఖర్చులు & నికర లాభాలు • అమ్మాలా లేదా వేచి ఉండాలా అనే స్పష్టమైన సలహా', 'app_hero_title': '🌾 పొలం నుండి మంచి మార్కెట్ వరకు — లాభదాయక నిర్ణయాలు', 'app_subtitle': 'రైతులకు సరైన ధర మరియు లాభాన్ని అందించే కృత్రిమ మేధస్సు (AI)', 'app_title': '🌾 రైతు మార్కెట్ ఇంటెలిజెన్స్', 'badge_gps_verified': '📍 GPS ధృవీకరించబడింది ({radius} కి.మీ పరిధి)', 'benefit_1': '📊 సమీపంలోని మార్కెట్లు మరియు మండిలలో తాజా ధరల పోలిక', 'benefit_2': '🚚 రవాణా ఖర్చులు పోను మీకు వచ్చే ఖచ్చితమైన నికర లాభం లెక్క', 'benefit_3': '🤖 AI సలహా: పంటను ఇప్పుడే అమ్మాలా? లేక కొన్ని రోజులు ఆగితే మంచి ధరో తెలుసుకోండి', 'benefits_title': '💡 ఈ యాప్ ద్వారా రైతులకు లభించే ప్రయోజనాలు:', 'btn_analyze': '🚀 మార్కెట్ విశ్లేషించండి', 'btn_navigate_map': '🗺️ రూట్ మ్యాప్', 'btn_start_nav': '🧭 {market} మార్కెట్\u200cకు గూగుల్ మ్యాప్స్ మార్గం ప్రారంభించండి', 'btn_sync_live': '🔄 తాజా మార్కెట్ ధరలను పొందండి', 'change_phone_btn': '✏️ మొబైల్ నంబర్ మార్చండి', 'choose_language': '🌐 మీ భాషను ఎంచుకోండి (Choose Language)', 'col_date': 'తేదీ', 'col_distance': 'రహదారి దూరం (కి.మీ)', 'col_gross_rev': 'మొత్తం రాబడి (₹)', 'col_handling_cost': 'నిర్వహణ ఖర్చు (₹)', 'col_location': 'ప్రాంతం', 'col_market': 'మార్కెట్', 'col_net_profit': 'నికర లాభం (₹)', 'col_price': 'ధర (₹/కిలో)', 'col_rating': 'గూగుల్ రేటింగ్', 'col_transit_cost': 'రవాణా ఖర్చు', 'col_transport_cost': 'రవాణా ఖర్చు (₹)', 'col_travel_time': 'ప్రయాణ సమయం', 'conf_high_msg': '🟢 **అధిక విశ్వసనీయత:** గత మార్కెట్ గణాంకాల ప్రకారం మోడల్ బలమైన ఖచ్చితత్వాన్ని చూపుతోంది.', 'conf_low_msg': '🔴 **తక్కువ విశ్వసనీయత:** మార్కెట్ పరిస్థితులను కూడా పరిశీలించి తుది నిర్ణయం తీసుకోండి.', 'conf_mod_msg': '🟡 **మధ్యస్థ విశ్వసనీయత:** మార్కెట్ పరిస్థితుల వల్ల ధరల్లో కొద్దిపాటి వ్యత్యాసాలు ఉండవచ్చు.', 'confidence_high': 'అధికం (High)', 'confidence_low': 'తక్కువ (Low)', 'confidence_moderate': 'మధ్యస్థం (Moderate)', 'confidence_unavailable': 'అందుబాటులో లేదు', 'crop_quality': '⭐ పంట నాణ్యత', 'dashboard_title': '📊 మీ మార్కెట్ ఇంటెలిజెన్స్ డాష్\u200cబోర్డ్', 'dec_neutral': 'సాధారణం (NEUTRAL)', 'dec_no_data': 'సమాచారం లేదు', 'dec_sell_now': 'ఇప్పుడే అమ్మండి (SELL NOW)', 'dec_wait': 'వేచి ఉండండి (WAIT)', 'decision_nodata_banner': '### ℹ️ సమాచారం లభించలేదు\n\nసిఫార్సు చేయడానికి తగినంత మార్కెట్ సమాచారం లేదు.', 'decision_sell_banner': '### 🟢 ఇప్పుడే అమ్మండి (SELL NOW)\n\n**{market}** ప్రస్తుతం సిఫార్సు చేయబడిన ఉత్తమ మార్కెట్.\n\n💰 ప్రస్తుత ధర: ₹{price}/కిలో\n\n📍 దూరం: {dist} కి.మీ', 'decision_wait_banner': '### 🟡 వేచి ఉండండి (WAIT)\n\nధరలు పెరిగే అవకాశం ఉందని మోడల్ అంచనా వేస్తోంది.\n\n🔮 అంచనా ధర: ₹{price}/కిలో\n\n📈 మెరుగైన ధర కోసం కొద్దిరోజులు వేచి చూడటం మంచిది.', 'demo_otp_banner': '📲 **[డెమో SMS]** మీ రైతు మార్కెట్ AI లాగిన్ ఓటీపీ: **{otp}** (5 నిమిషాలు చెల్లుబాటు)', 'disclaimer_1': '📌 ఈ సిఫార్సు తాజా మార్కెట్ ధరలు, ప్రాంతం, దూరం, నికర లాభాలు మరియు ML ధరల అంచనా ఆధారంగా రూపొందించబడింది.', 'disclaimer_2': '⚠️ ధరల అంచనాలు కేవలం సూచన మాత్రమే. గిరాకీ, సరఫరా, వాతావరణం మరియు రవాణా పరిస్థితులను బట్టి మార్కెట్ ధరలు మారవచ్చు.', 'dist_approx_km': '~{dist:.1f} కి.మీ (రహదారి)', 'err_name_required': 'దయచేసి మీ పేరును నమోదు చేయండి.', 'err_otp_expired': "⏱️ ఓటీపీ సమయం ముగిసింది. దయచేసి 'మళ్ళీ ఓటీపీ పంపండి' క్లిక్ చేయండి.", 'err_otp_invalid': '❌ తప్పు ఓటీపీ. దయచేసి సరైన 6 అంకెల కోడ్\u200cను నమోదు చేయండి.', 'err_otp_required': 'దయచేసి 6 అంకెల ఓటీపీని నమోదు చేయండి.', 'err_phone_invalid': 'దయచేసి సరైన 10 అంకెల మొబైల్ నంబర్\u200cను నమోదు చేయండి.', 'expected_harvest': '📅 పంట కోత / సిద్ధమయ్యే తేదీ', 'farmer_location': '📍 మీ ప్రాంతం / ఊరు', 'farmer_name_label': '👤 రైతు పేరు', 'farmer_name_placeholder': 'ఉదాహరణ: రామయ్య / మీ పేరు నమోదు చేయండి', 'farmer_phone_help': 'మీ పంట మార్కెట్ వివరాలు మరియు ధరల సమాచారం కోసం', 'farmer_phone_label': '📱 మొబైల్ నంబర్', 'farmer_phone_placeholder': '10 అంకెల మొబైల్ నంబర్ నమోదు చేయండి', 'glance_title': 'ఒక్క చూపులో నిర్ణయం', 'init_ai_intel': '### 🤖 AI విశ్లేషణ\n\n- రాబోయే ధరల అంచనా\n- ధరల పరిధి & విశ్వసనీయత\n- అమ్మాలా లేదా వేచి ఉండాలా?\n- నిర్ణయ స్కోర్లు\n- రైతు ప్రత్యేక సలహా', 'init_fin_intel': '### 💰 ఆర్థిక లెక్కలు\n\n- మొత్తం రాబడి\n- రవాణా ఖర్చులు\n- మార్కెట్ ఖర్చులు\n- చేతికి అందే నికర లాభం', 'init_how_it_works': '### 🚀 ఇది ఎలా పనిచేస్తుంది\n\n**రైతు వివరాలు → మార్కెట్ డేటా → ML ధరల అంచనా → AI ఏజెంట్ → లాభాల లెక్క → సరైన అమ్మకపు నిర్ణయం**', 'init_market_intel': '### 🏪 మార్కెట్ సమాచారం\n\n- తాజా మార్కెట్ ధరలు\n- వివిధ మార్కెట్ల పోలిక\n- ఉత్తమ మార్కెట్ సిఫార్సు\n- దూరం & ప్రయాణ సమయం', 'init_provides': 'ఈ వ్యవస్థ మీకు ఏమి అందిస్తుంది', 'initial_info': '👈 ఎడమవైపు సైడ్\u200cబార్\u200cలో మీ పంట వివరాలను నమోదు చేసి **🚀 మార్కెట్ విశ్లేషించండి** పై క్లిక్ చేయండి.', 'lbl_ai_decision': 'AI నిర్ణయం', 'lbl_avg_price': 'సగటు ధర', 'lbl_best_profit': 'గరిష్ట నికర లాభం', 'lbl_current_best_price': 'ప్రస్తుత ఉత్తమ ధర', 'lbl_damage_factors_title': '🔬 పంట కోత అనంతర ప్రధాన నష్ట కారకాలు:', 'lbl_discovered_markets': '{radius} కి.మీ పరిధిలో లభించిన మార్కెట్లు ({count})', 'lbl_distance': '🚚 రహదారి దూరం', 'lbl_distance_km': 'రహదారి దూరం: {dist} కి.మీ', 'lbl_exp_difference': 'ఆశించిన వ్యత్యాసం / లాభం', 'lbl_expected_rev': '3 రోజుల తర్వాత ఆశించిన ఆదాయం', 'lbl_farmer': 'రైతు పేరు', 'lbl_from_loc': 'మీ ప్రాంతం నుండి', 'lbl_humidity': 'తేమ శాతం', 'lbl_location': '📍 ప్రాంతం', 'lbl_lower_est': 'కనిష్ట అంచనా', 'lbl_market': 'మార్కెట్', 'lbl_max_price': 'గరిష్ట ధర', 'lbl_min_price': 'కనిష్ట ధర', 'lbl_model_mae': 'సగటు లోపం (MAE)', 'lbl_model_r2': 'మోడల్ R² స్కోరు', 'lbl_near_farmer': 'మీ ప్రాంతానికి సమీపంలో', 'lbl_per_km_rate': '₹2.5/కి.మీ చొప్పున', 'lbl_pred_3days': '3 రోజుల అంచనా ధర', 'lbl_price': '💰 ధర', 'lbl_quality': 'నాణ్యత', 'lbl_quantity': 'పరిమాణం', 'lbl_rain_prob': 'వర్ష సూచన', 'lbl_rating': '⭐ గూగుల్ రేటింగ్', 'lbl_rec_market': 'సిఫార్సు చేసిన మార్కెట్', 'lbl_safe_window': 'సురక్షిత వ్యవధి: ~{days} రోజులు', 'lbl_sell_now_rev': 'ఇప్పుడే అమ్మితే ఆదాయం', 'lbl_sell_score': 'ఇప్పుడే అమ్మే స్కోరు', 'lbl_shelf_life': 'గరిష్ట నిల్వ కాలం', 'lbl_spoilage_rate': 'రోజువారీ నష్ట శాతం', 'lbl_spoilage_risk': 'పాడయ్యే ప్రమాదం', 'lbl_temperature': 'ఉష్ణోగ్రత', 'lbl_to_mandi': 'చేరాల్సిన మార్కెట్', 'lbl_transit_adv': 'రవాణా అనుకూలత', 'lbl_transit_guide': 'రవాణా మార్గదర్శనం', 'lbl_transport_cost': 'సుమారు రవాణా ఖర్చు', 'lbl_travel_time': 'సుమారు ప్రయాణ సమయం', 'lbl_upper_est': 'గరిష్ట అంచనా', 'lbl_wait_score': 'వేచి ఉండే స్కోరు', 'live_prices_badge': '🟢 ప్రత్యక్ష రోజువారీ మార్కెట్ ధరలు (ఆగ్మార్క్\u200cనెట్ APMC)', 'login_box_title': '🔐 రైతు లాగిన్ / ప్రొఫైల్', 'login_btn': '🚀 డాష్\u200cబోర్డ్\u200cకి కొనసాగండి', 'login_hero_desc': 'రైతన్నల కోసం ప్రత్యేకంగా రూపొందించబడింది. మీ కష్టానికి తగిన గిట్టుబాటు ధర పొందండి.', 'login_hero_title': '👨\u200d🌾 రైతు మార్కెట్ మిత్రకు స్వాగతం!', 'maps_caption': '📱 క్లిక్ చేస్తే గూగుల్ మ్యాప్స్ ద్వారా తాజా ట్రాఫిక్ మరియు అతి తక్కువ సమయం పట్టే మార్గాన్ని చూడవచ్చు.', 'metric_best_market': '🏪 ఉత్తమ మార్కెట్', 'metric_confidence': '🎯 విశ్వసనీయత', 'metric_current_price': '💰 ప్రస్తుత ధర', 'metric_net_profit': '💵 నికర లాభం', 'metric_predicted_price': '🔮 అంచనా ధర', 'metric_prediction_range': '📊 ధరల పరిధి (Range)', 'metric_r2_score': '📈 R² స్కోరు', 'ml_analysis_title': '🤖 ML ధరల అంచనా విశ్లేషణ', 'ml_caption': '3 రోజుల తర్వాత ఆశించిన ధర: {lower} – {upper}/కిలో | సగటు లోపం: {mae}/కిలో', 'ml_unavailable_msg': '⚠️ ఈ పంటకు సంబంధించి ML అంచనా వివరాలు అందుబాటులో లేవు.', 'otp_box_title': '🔐 మొబైల్ ఓటీపీ ధృవీకరణ', 'otp_check_phone_notice': '📩 6 అంకెల ఓటీపీ కోసం మీ మొబైల్ ఫోన్\u200cలోని SMS సందేశాలను చూడండి.', 'otp_label': '🔢 6 అంకెల ఓటీపీని నమోదు చేయండి', 'otp_placeholder': '6 అంకెల ఓటీపీ నమోదు చేయండి (ఉదా: 582910)', 'otp_resend_success': '✅ కొత్త ఓటీపీ +91 {phone} కు విజయవంతంగా పంపబడింది!', 'otp_sent_to': '📲 ధృవీకరణ కోడ్ +91 {phone} కు SMS ద్వారా పంపబడింది', 'price_date_info': 'ధృవీకరించబడిన తేదీ: {date}', 'price_decrease_msg': '📉 ధర తగ్గే అవకాశం: {diff} ({pct})', 'price_increase_msg': '📈 ధర పెరిగే అవకాశం: {diff} ({pct})', 'price_stable_msg': '➡️ ధరలో పెద్దగా మార్పు ఉండకపోవచ్చు.', 'quality_advice_grade_a': 'మీ గ్రేడ్ A పంటకు నాణ్యమైన కొనుగోలుదారుల నుండి మంచి ధర లభిస్తుంది. తడి తగలకుండా జాగ్రత్త పడండి.', 'quality_advice_grade_b': 'మధ్యమ శ్రేణి నాణ్యత. అమ్మకానికి ముందు సమీప మార్కెట్లలో ధరలు సరిపోల్చుకోండి.', 'quality_advice_grade_c': 'పంట నాణ్యత మరింత క్షీణించకుండా త్వరగా విక్రయించడం ప్రయోజనకరం.', 'quantity_kg': '⚖️ పరిమాణం (కిలోలు / kg)', 'recommended_market_title': '🏪 సిఫార్సు చేసిన మార్కెట్', 'resend_otp_btn': '🔄 మళ్ళీ ఓటీపీ పంపండి', 'rev_header': 'ఆదాయ అంచనా', 'route_logistics_title': 'రవాణా & ప్రయాణ మార్గదర్శి', 'select_crop': '🌱 పంటను ఎంచుకోండి', 'select_price_date': '📅 మార్కెట్ ధరల తేదీ', 'send_otp_btn': '📲 ఓటీపీ పంపండి (Send OTP)', 'shelflife_title': 'పంట నిల్వ సామర్థ్యం & నష్ట విశ్లేషణ', 'sidebar_crop_info_header': 'మీ పంట సమాచారాన్ని ఇక్కడ నమోదు చేయండి.', 'sidebar_farmer_details': '👨\u200d🌾 రైతు వివరాలు', 'sidebar_language': '🌐 భాష మార్చండి', 'sidebar_logout': '🚪 లాగౌట్', 'sidebar_phone': '📱 {phone}', 'sidebar_welcome': 'స్వాగతం, {name} గారు!', 'slider_radius': '📍 శోధన పరిధి (కి.మీ)', 'sms_dispatched_toast': '📲 +91 {phone} కు SMS ద్వారా ఓటీపీ పంపబడింది!', 'sms_notif_card_sub': 'మీ మొబైల్ నంబర్\u200cకు 6 అంకెల ధృవీకరణ కోడ్ పంపబడింది. కొనసాగడానికి దానిని క్రింద నమోదు చేయండి.', 'sms_notif_card_title': 'మొబైల్ SMS నోటిఫికేషన్ పంపబడింది', 'sync_success': '✅ {date} నాటి తాజా మార్కెట్ ధరలు విజయవంతంగా లోడ్ చేయబడ్డాయి!', 'tab1_chart_title': 'మార్కెట్ ధరల చార్ట్', 'tab1_header': 'మార్కెట్ ధరల పోలిక', 'tab1_no_data': '⚠️ మార్కెట్ పోలిక సమాచారం అందుబాటులో లేదు.', 'tab2_best_profit_banner': '🏆 **అత్యధిక లాభదాయక మార్కెట్:** {market}\n\n💵 **ఆశించిన నికర లాభం:** {profit}', 'tab2_btn_nav': '🧭 {market} మార్కెట్\u200cకు గూగుల్ మ్యాప్స్ మార్గం', 'tab2_chart_title': 'మార్కెట్ వారీగా నికర లాభం', 'tab2_header': 'స్మార్ట్ నికర లాభాల విశ్లేషణ', 'tab2_transport_caption': '🚚 రవాణా ఖర్చు మార్కెట్ దూరం మరియు వాహన రేటు ఆధారంగా లెక్కించబడింది.', 'tab3_caption': '📌 మునుపటి ధరలు అందుబాటులో ఉన్న మార్కెట్ డేటా ఆధారంగా ఇవ్వబడ్డాయి.', 'tab3_decrease': '📉 ధర తగ్గే అవకాశం: {pct}%', 'tab3_header': 'గత మార్కెట్ ధరల ధోరణి', 'tab3_increase': '📈 ధర పెరిగే అవకాశం: {pct}%', 'tab3_pred_header': 'ML ధరల అంచనా', 'tab3_range_info': '📊 **3 రోజుల అంచనా ధరల పరిధి:** {lower} – {upper}/కిలో', 'tab3_stable': '➡️ పెద్దగా మార్పు ఉండకపోవచ్చు.', 'tab4_advisor_title': 'రైతు సలహా పత్రం', 'tab4_financial_impact': 'ఆర్థిక ప్రభావం & రాబడి అంచనా', 'tab4_header': 'AI రైతు సలహాదారు', 'tab4_logistics_guidance': 'రవాణా & మార్కెట్ చేరే సూచనలు', 'tab4_quality_guidance': 'నాణ్యత & నిల్వ మార్గదర్శనం', 'tab4_rationale_title': 'మార్కెట్ విశ్లేషణ & ధరల దృక్పథం', 'tab4_reason_label': 'ప్రధాన అంశం', 'tab4_rec_title': 'AI సిఫార్సు', 'tab4_scores_title': 'నిర్ణయ స్కోర్లు', 'tab4_summary_title': 'అమ్మకపు సారాంశం', 'tab_ai_advisor': '🤖 AI సలహాదారు', 'tab_market_comparison': '📊 మార్కెట్ల పోలిక', 'tab_price_trends': '📈 ధరల ధోరణి', 'tab_profit_analysis': '💰 లాభాల విశ్లేషణ', 'time_hours_mins': '{h} గం {m} ని', 'time_mins': '{m} నిమిషాలు', 'verify_otp_btn': '🚀 ఓటీపీ ధృవీకరించి కొనసాగండి', 'weather_title': 'వాతావరణం & రవాణా సలహా', 'transit_heavy_load_note': 'రవాణా సమయం భారీ వ్యవసాయ ఉత్పత్తుల లోడింగ్ వాహనం (ట్రాక్టర్-ట్రాలీ / టెంపో ~24 కి.మీ/గం) ప్రకారం లెక్కించబడింది. సాధారణ కారు సమయం సూచనగా చూపబడింది.', 'lbl_heavy_load': 'భారీ లోడ్', 'lbl_car_ref': 'కారు', 'lbl_auto_assessed': 'కోత తేదీ ఆధారంగా నాణ్యత నిర్ధారణ', 'lbl_days_post_harvest': 'రోజుల క్రితం కోత', 'harvest_date_help': 'పంట కోత తేదీని ఎంచుకోండి. తాజాదనమే మార్కెట్ నాణ్యత గ్రేడ్\u200cను నిర్ణయిస్తుంది.', 'crop_quality_help': 'గ్రేడ్ A: తాజాగా కోసిన/ఉత్తమ నాణ్యత; గ్రేడ్ B: సాధారణ మార్కెట్ రకం; గ్రేడ్ C: నిల్వ/తక్కువ నాణ్యత.', 'tab_harvest_quality_title': 'కోత తాజాదనం & నాణ్యత ప్రభావం', 'quality_fresh_status': 'తాజా కోత', 'quality_basis_note': 'కోత తర్వాత గడిచిన రోజుల ఆధారంగా నాణ్యత మారుతుంది', 'tab_freshness_matrix': '🌾 నాణ్యత క్షీణత మ్యాట్రిక్స్', 'btn_new_analysis': 'కొత్త విశ్లేషణ / రీసెట్', 'matrix_title': 'బహుళ-రోజుల నాణ్యత క్షీణత మ్యాట్రిక్స్', 'matrix_subtitle': 'కోత తర్వాత గడిచిన రోజుల ప్రకారం ప్రత్యక్ష మార్కెట్ నాణ్యత గ్రేడింగ్', 'matrix_caption_photo': 'ఈ మ్యాట్రిక్స్ ఆరు ముఖ్యమైన పంటల భౌతిక నిల్వ సామర్థ్యాన్ని చూపుతుంది. టమాటాలు కొద్దిరోజుల్లోనే గ్రేడ్ C కి చేరుకుని భారీ నష్టం కలిగిస్తాయి, అయితే వరి/మొక్కజొన్న వంటి ధాన్యాలు చాలా కాలం పాటు గ్రేడ్ A లో ఉంటాయి.'}}

CROP_CATEGORIES = {
    "all": {
        "en": "All Crops (29)", "te": "అన్ని పంటలు (29)", "hi": "सभी फसलें (29)",
        "ta": "அனைத்து பயிர்கள் (29)", "kn": "ಎಲ್ಲಾ ಬೆಳೆಗಳು (29)", "mr": "सर्व पिके (29)"
    },
    "cereals": {
        "en": "🌾 Cereals & Millets", "te": "🌾 తృణధాన్యాలు & చిరుధాన్యాలు", "hi": "🌾 अनाज और मोटे अनाज",
        "ta": "🌾 தானியங்கள் & சிறுதானியங்கள்", "kn": "🌾 ಧಾನ್ಯಗಳು ಮತ್ತು ಸಿರಿಧಾನ್ಯಗಳು", "mr": "🌾 तृणधान्ये व भरडधान्ये"
    },
    "pulses": {
        "en": "🫘 Pulses (Dal)", "te": "🫘 పప్పుధాన్యాలు", "hi": "🫘 दलहन (दालें)",
        "ta": "🫘 பருப்பு வகைகள்", "kn": "🫘 ಬೇಳೆಕಾಳುಗಳು", "mr": "🫘 कडधान्ये (डाळी)"
    },
    "oilseeds": {
        "en": "🌻 Oilseeds", "te": "🌻 నూనెగింజలు", "hi": "🌻 तिलहन",
        "ta": "🌻 எண்ணெய் வித்துக்கள்", "kn": "🌻 ಎಣ್ಣೆಕಾಳುಗಳು", "mr": "🌻 गळित धान्ये (तेलबिया)"
    },
    "spices_commercial": {
        "en": "🌿 Commercial & Spices", "te": "🌿 వాణిజ్య & సుగంధ ద్రవ్యాలు", "hi": "🌿 वाणिज्यिक व मसाले",
        "ta": "🌿 வணிக & மசாலாப் பயிர்கள்", "kn": "🌿 ವಾಣಿಜ್ಯ ಮತ್ತು ಸಾಂಬಾರ ಬೆಳೆಗಳು", "mr": "🌿 व्यावसायिक व मसाल्यांची पिके"
    },
    "vegetables": {
        "en": "🥬 Vegetables", "te": "🥬 కూరగాయలు", "hi": "🥬 सब्जियां",
        "ta": "🥬 காய்கறிகள்", "kn": "🥬 ತರಕಾರಿಗಳು", "mr": "🥬 भाजीपाला"
    }
}

CROP_CATEGORY_MAP = {
    # Cereals & Millets
    "Rice": "cereals",
    "Maize": "cereals",
    "Jowar": "cereals",
    "Bajra": "cereals",
    "Ragi": "cereals",
    # Pulses
    "Red Gram": "pulses",
    "Bengal Gram": "pulses",
    "Green Gram": "pulses",
    "Black Gram": "pulses",
    # Oilseeds
    "Soybean": "oilseeds",
    "Groundnut": "oilseeds",
    "Sunflower": "oilseeds",
    "Sesame": "oilseeds",
    # Commercial & Spices
    "Cotton": "spices_commercial",
    "Chilli": "spices_commercial",
    "Turmeric": "spices_commercial",
    "Ginger": "spices_commercial",
    "Garlic": "spices_commercial",
    # Vegetables
    "Tomato": "vegetables",
    "Onion": "vegetables",
    "Brinjal": "vegetables",
    "Bhendi": "vegetables",
    "Potato": "vegetables",
    "Bitter Gourd": "vegetables",
    "Bottle Gourd": "vegetables",
    "Pumpkin": "vegetables",
    "Cabbage": "vegetables",
    "Cauliflower": "vegetables",
    "Cucumber": "vegetables"
}

CROPS_DISPLAY = {
    # Existing 6 Crops
    "Tomato": {"en": "🍅 Tomato", "te": "🍅 టమాటా (Tomato)", "hi": "🍅 टमाटर (Tomato)", "ta": "🍅 தக்காளி", "kn": "🍅 ಟೊಮೆಟೊ", "mr": "🍅 टोमॅटो"},
    "Rice": {"en": "🌾 Rice / Paddy", "te": "🌾 వరి / ధాన్యం (Rice)", "hi": "🌾 धान / चावल (Rice)", "ta": "🌾 நெல் / அரிசி", "kn": "🌾 ಭತ್ತ / ಅಕ್ಕಿ", "mr": "🌾 तांदूळ / भात"},
    "Cotton": {"en": "⚪ Cotton", "te": "⚪ పత్తి (Cotton)", "hi": "⚪ कपास (Cotton)", "ta": "⚪ பருத்தி", "kn": "⚪ ಹತ್ತಿ", "mr": "⚪ कापूस"},
    "Chilli": {"en": "🌶️ Chilli", "te": "🌶️ మిర్చి / పచ్చిమిర్చి (Chilli)", "hi": "🌶️ मिर्च (Chilli)", "ta": "🌶️ மிளகாய்", "kn": "🌶️ ಮೆಣಸಿನಕಾಯಿ", "mr": "🌶️ मिरची"},
    "Maize": {"en": "🌽 Maize / Corn", "te": "🌽 మొక్కజొన్న (Maize)", "hi": "🌽 मक्का (Maize)", "ta": "🌽 மக்காச்சோளம்", "kn": "🌽 ಮೆಕ್ಕೆಜೋಳ", "mr": "🌽 मका"},
    "Onion": {"en": "🧅 Onion", "te": "🧅 ఉల్లిపాయ (Onion)", "hi": "🧅 प्याज (Onion)", "ta": "🧅 வெங்காயம்", "kn": "🧅 ಈರುಳ್ಳಿ", "mr": "🧅 कांदा"},

    # Cereals & Millets
    "Jowar": {"en": "🌾 Jowar / Sorghum", "te": "🌾 జొన్నలు (Jowar)", "hi": "🌾 ज्वार (Jowar)", "ta": "🌾 சோளம்", "kn": "🌾 ಜೋಳ", "mr": "🌾 ज्वारी"},
    "Bajra": {"en": "🌾 Bajra / Pearl Millet", "te": "🌾 సజ్జలు (Bajra)", "hi": "🌾 बाजरा (Bajra)", "ta": "🌾 கம்பு", "kn": "🌾 ಸಜ್ಜೆ", "mr": "🌾 बाजरी"},
    "Ragi": {"en": "🌾 Ragi / Finger Millet", "te": "🌾 రాగులు (Ragi)", "hi": "🌾 रागी / मडुआ (Ragi)", "ta": "🌾 கேழ்வரகு", "kn": "🌾 ರಾಗಿ", "mr": "🌾 नाचणी / रागी"},

    # Pulses
    "Red Gram": {"en": "🫘 Red Gram / Tur (Kandi)", "te": "🫘 కందులు / తొగరి (Red Gram)", "hi": "🫘 अरहर / तूर दाल (Red Gram)", "ta": "🫘 துவரை", "kn": "🫘 ತೊಗರಿ", "mr": "🫘 तूर"},
    "Bengal Gram": {"en": "🧆 Bengal Gram / Chickpea (Chana)", "te": "🧆 శనగలు (Bengal Gram)", "hi": "🧆 चना (Bengal Gram)", "ta": "🧆 கொண்டைக்கடலை", "kn": "🧆 ಕಡಲೆ", "mr": "🧆 हरभरा / चणा"},
    "Green Gram": {"en": "🫘 Green Gram / Moong (Pesalu)", "te": "🫘 పెసర్లు (Green Gram)", "hi": "🫘 मूंग (Green Gram)", "ta": "🫘 பாசிப்பயறு", "kn": "🫘 ಹೆಸರುಕಾಳು", "mr": "🫘 मूग"},
    "Black Gram": {"en": "🫘 Black Gram / Urad (Minumu)", "te": "🫘 మినుములు (Black Gram)", "hi": "🫘 उड़द (Black Gram)", "ta": "🫘 உளுந்து", "kn": "🫘 ಉದ್ದು", "mr": "🫘 उडीद"},

    # Oilseeds
    "Soybean": {"en": "🌱 Soybean", "te": "🌱 సోయాబీన్ (Soybean)", "hi": "🌱 सोयाबीन (Soybean)", "ta": "🌱 சோயாபீன்", "kn": "🌱 ಸೋಯಾಬೀನ್", "mr": "🌱 सोयाबीन"},
    "Groundnut": {"en": "🥜 Groundnut / Peanut", "te": "🥜 వేరుశనగ (Groundnut)", "hi": "🥜 मूंगफली (Groundnut)", "ta": "🥜 நிலக்கடலை", "kn": "🥜 ಕಡಲೆಕಾಯಿ", "mr": "🥜 भुईमूग / शेंगदाणा"},
    "Sunflower": {"en": "🌻 Sunflower", "te": "🌻 పొద్దుతిరుగుడు (Sunflower)", "hi": "🌻 सूरजमुखी (Sunflower)", "ta": "🌻 சூரியகாந்தி", "kn": "🌻 ಸೂರ್ಯಕಾಂತಿ", "mr": "🌻 सूर्यफूल"},
    "Sesame": {"en": "🌿 Sesame / Til (Nuvvulu)", "te": "🌿 నువ్వులు (Sesame)", "hi": "🌿 तिल (Sesame)", "ta": "🌿 எள்", "kn": "🌿 ಎಳ್ಳು", "mr": "🌿 तीळ"},

    # Commercial & Spices
    "Turmeric": {"en": "🟡 Turmeric (Pasupu)", "te": "🟡 పసుపు (Turmeric)", "hi": "🟡 हल्दी (Turmeric)", "ta": "🟡 மஞ்சள்", "kn": "🟡 ಅರಿಶಿನ", "mr": "🟡 हळद"},
    "Ginger": {"en": "🫚 Ginger (Allam)", "te": "🫚 అల్లం (Ginger)", "hi": "🫚 अदरक (Ginger)", "ta": "🫚 இஞ்சி", "kn": "🫚 ಶುಂಠಿ", "mr": "🫚 आले / अद्रक"},
    "Garlic": {"en": "🧄 Garlic (Vellulli)", "te": "🧄 వెల్లుల్లి (Garlic)", "hi": "🧄 लहसुन (Garlic)", "ta": "🧄 பூண்டு", "kn": "🧄 ಬೆಳ್ಳುಳ್ಳಿ", "mr": "🧄 लसूण"},

    # Vegetables
    "Brinjal": {"en": "🍆 Brinjal / Eggplant", "te": "🍆 వంకాయ (Brinjal)", "hi": "🍆 बैंगन (Brinjal)", "ta": "🍆 கத்தரிக்காய்", "kn": "🍆 ಬದನೆಕಾಯಿ", "mr": "🍆 वांगी"},
    "Bhendi": {"en": "🌱 Bhendi / Okra (Ladies Finger)", "te": "🌱 బెండకాయ (Bhendi)", "hi": "🌱 भिंडी (Bhendi)", "ta": "🌱 வெண்டைக்காய்", "kn": "🌱 ಬೆಂಡೆಕಾಯಿ", "mr": "🌱 भेंडी"},
    "Potato": {"en": "🥔 Potato (Alu)", "te": "🥔 బంగాళాదుంప / ఆలుగడ్డ (Potato)", "hi": "🥔 आलू (Potato)", "ta": "🥔 உருளைக்கிழங்கு", "kn": "🥔 ಆಲೂಗಡ್ಡೆ", "mr": "🥔 बटाटा"},
    "Bitter Gourd": {"en": "🥒 Bitter Gourd (Karela)", "te": "🥒 కాకరకాయ (Bitter Gourd)", "hi": "🥒 करेला (Bitter Gourd)", "ta": "🥒 பாகற்காய்", "kn": "🥒 ಹಾಗಲಕಾಯಿ", "mr": "🥒 कारले"},
    "Bottle Gourd": {"en": "🍈 Bottle Gourd (Sorakaya)", "te": "🍈 సొరకాయ / ఆనపకాయ (Bottle Gourd)", "hi": "🍈 लौकी (Bottle Gourd)", "ta": "🍈 சுரைக்காய்", "kn": "🍈 ಸೋರೆಕಾಯಿ", "mr": "🍈 दुधी भोपळा"},
    "Pumpkin": {"en": "🎃 Pumpkin (Gummadi)", "te": "🎃 గుమ్మడికాయ (Pumpkin)", "hi": "🎃 कद्दू (Pumpkin)", "ta": "🎃 பூசணிக்காய்", "kn": "🎃 ಕುಂಬಳಕಾಯಿ", "mr": "🎃 लाल भोपळा"},
    "Cabbage": {"en": "🥬 Cabbage", "te": "🥬 క్యాబేజీ (Cabbage)", "hi": "🥬 पत्तागोभी (Cabbage)", "ta": "🥬 முட்டைக்கோஸ்", "kn": "🥬 ಎಲೆಕೋಸು", "mr": "🥬 कोबी"},
    "Cauliflower": {"en": "🥦 Cauliflower", "te": "🥦 కాలీఫ్లవర్ (Cauliflower)", "hi": "🥦 फूलगोभी (Cauliflower)", "ta": "🥦 காலிஃபிளவர்", "kn": "🥦 ಹೂಕೋಸು", "mr": "🥦 फ्लॉवर"},
    "Cucumber": {"en": "🥒 Cucumber (Dosakaya / Kheera)", "te": "🥒 దోసకాయ / కీర (Cucumber)", "hi": "🥒 खीरा / ककड़ी (Cucumber)", "ta": "🥒 வெள்ளரிக்காய்", "kn": "🥒 ಸೌತೆಕಾಯಿ", "mr": "🥒 काकडी"}
}

QUALITY_DISPLAY = {
    "Grade A": {"en": "⭐ Grade A (Fresh / Premium)", "te": "⭐ గ్రేడ్ A (తాజా / ఉత్తమ నాణ్యత)", "hi": "⭐ ग्रेड A (ताज़ा / सर्वोत्तम)", "ta": "⭐ தரம் A (புதிய / பிரீமியம்)", "kn": "⭐ ಗ್ರೇಡ್ A (ತಾಜಾ / ಅತ್ಯುತ್ತಮ)", "mr": "⭐ ग्रेड A (ताजा / उत्तम)"},
    "Grade B": {"en": "⭐ Grade B (Fair / Standard Mandi)", "te": "⭐ గ్రేడ్ B (సాధారణ మార్కెట్ రకం)", "hi": "⭐ ग्रेड B (मानक मंडी ग्रेड)", "ta": "⭐ தரம் B (சராசரி சந்தை தரம்)", "kn": "⭐ ಗ್ರೇಡ್ B (ಸಾಮಾನ್ಯ ಮಾರುಕಟ್ಟೆ)", "mr": "⭐ ग्रेड B (सर्वसाधारण प्रत)"},
    "Grade C": {"en": "⭐ Grade C (Aged / Low Grade)", "te": "⭐ గ్రేడ్ C (నిల్వ / తక్కువ నాణ్యత)", "hi": "⭐ ग्रेड C (कमज़ोर / पुराना)", "ta": "⭐ தரம் C (பழைய / குறைந்த தரம்)", "kn": "⭐ ಗ್ರೇಡ್ C (ಕಡಿಮೆ ಗುಣಮಟ್ಟ)", "mr": "⭐ ग्रेड C (कमी दर्जा)"}
}

EXTRA_TRANSLATIONS = {
    'en': {
        'small_batch_mode_badge': '🛵 Small Batch Mode (≤ 500 kg)',
        'small_batch_mode_help': 'Optimized for smallholder farmers. Recommends nearby Rythu Bazars and local markets to avoid high transport fees from wiping out your profit.',
        'bulk_batch_mode_badge': '🚛 Bulk Commercial Batch (> 500 kg)',
        'small_market_card_title': '🏪 Recommended Small Market / Rythu Bazar (For Small Batches)',
        'small_market_reason': 'Ideal for small batches: No need to hire an expensive truck, 0% commission, and accessible by bike or auto.',
        'btn_navigate_small_market': '🧭 Start Navigation to {market}',
        'lbl_filter_markets': 'Filter Markets:',
        'filter_all_markets': 'All Markets',
        'filter_small_markets': '🏪 Rythu Bazars & Local Markets',
        'filter_wholesale_markets': '🚛 Wholesale APMC Mandis',
        'col_market_category': 'Category',
        'col_commission': 'Commission (₹)',
        'small_market_profit_benefit': '💡 Zero commission & minimal transport overhead: You save ~₹{transit_diff:,.0f} in transport compared to distant wholesale mandis!',
        'quick_start_demo_title': '⚡ Instant Demo Access (No OTP Required)',
        'quick_start_demo_desc': 'Click any sample farmer profile below to explore the dashboard immediately:',
        'demo_farmer_1_name': '🌾 Mallesh (Jangaon)',
        'demo_farmer_1_desc': 'Paddy Farmer • 50 kg (Small Batch)',
        'demo_farmer_2_name': '🍅 Ramulu (Shamshabad)',
        'demo_farmer_2_desc': 'Tomato Grower • 1,200 kg (Bulk Commercial)',
        'demo_farmer_3_name': '🧅 Venkat (Bhongir)',
        'demo_farmer_3_desc': 'Onion Grower • 300 kg (Standard)',
        'quick_scenario_title': '🚀 1-Click Harvest Analysis Presets',
        'quick_scenario_desc': 'Tap any scenario below to instantly run GPS mandi discovery, pricing, and profit comparison:',
        'quick_btn_paddy': '🛵 Small Batch: Paddy 50 kg (Jangaon)',
        'quick_btn_tomato': '🚛 Bulk Commercial: Tomato 1,200 kg (Shamshabad)',
        'quick_btn_onion': '🧅 Standard Lot: Onion 300 kg (Bhongir)',
        'metric_net_cash_title': '💰 Take-Home Net Cash',
        'metric_net_cash_help': 'Actual cash in your hand after transport fuel, mandi fees, and commission.',
        'btn_customize_inputs': '👈 Or customize crop, location & dates in the left sidebar',
        'educational_matrix_title': '📖 Interactive Crop Shelf-Life & Freshness Degradation Matrix',
        'platform_navigation': 'Platform Navigation'
    },
    'te': {
        'small_batch_mode_badge': '🛵 చిన్న పరిమాణం మోడ్ (≤ 500 కిలోలు)',
        'small_batch_mode_help': 'చిన్న రైతులకు అనుకూలమైనది. రవాణా ఖర్చులు మీ లాభాన్ని హరించకుండా సమీప రైతు బజార్లు మరియు స్థానిక మార్కెట్లను సిఫార్సు చేస్తుంది.',
        'bulk_batch_mode_badge': '🚛 భారీ వాణిజ్య పరిమాణం (> 500 కిలోలు)',
        'small_market_card_title': '🏪 చిన్న పరిమాణాలకు సిఫార్సు చేసిన స్థానిక రైతు బజార్ / మార్కెట్',
        'small_market_reason': 'చిన్న పరిమాణాలకు అనువైనది: పెద్ద వాహనం అద్దె అవసరం లేదు, 0% కమీషన్, బైక్ లేదా ఆటో ద్వారా సులభంగా వెళ్లవచ్చు.',
        'btn_navigate_small_market': '🧭 {market} (రైతు బజార్) కి నావిగేషన్ ప్రారంభించండి',
        'lbl_filter_markets': 'మార్కెట్లను ఫిల్టర్ చేయండి:',
        'filter_all_markets': 'అన్ని మార్కెట్లు',
        'filter_small_markets': '🏪 రైతు బజార్లు & స్థానిక మార్కెట్లు',
        'filter_wholesale_markets': '🚛 హోల్‌సేల్ APMC మార్కెట్లు',
        'col_market_category': 'వర్గం',
        'col_commission': 'కమీషన్ (₹)',
        'small_market_profit_benefit': '💡 0% కమీషన్ & అతి తక్కువ రవాణా ఖర్చు: దూరపు హోల్‌సేల్ మార్కెట్లతో పోలిస్తే రవాణాలో ~₹{transit_diff:,.0f} ఆదా అవుతుంది!',
        'quick_start_demo_title': '⚡ తక్షణ డెమో యాక్సెస్ (OTP అవసరం లేదు)',
        'quick_start_demo_desc': 'యాప్‌ను వెంటనే చూడటానికి క్రింది నమూనా రైతు ప్రొఫైల్‌పై క్లిక్ చేయండి:',
        'demo_farmer_1_name': '🌾 మల్లేష్ (జనగాం)',
        'demo_farmer_1_desc': 'వరి రైతు • 50 కిలోలు (చిన్న పరిమాణం)',
        'demo_farmer_2_name': '🍅 రాములు (శంషాబాద్)',
        'demo_farmer_2_desc': 'టమాటా రైతు • 1,200 కిలోలు (భారీ వాణిజ్యం)',
        'demo_farmer_3_name': '🧅 వెంకట్ (భువనగిరి)',
        'demo_farmer_3_desc': 'ఉల్లి రైతు • 300 కిలోలు (సాధారణ)',
        'quick_scenario_title': '🚀 1-క్లిక్ మార్కెట్ విశ్లేషణ ప్రీసెట్లు',
        'quick_scenario_desc': 'మార్కెట్ ధరలు మరియు నికర లాభాన్ని వెంటనే విశ్లేషించడానికి ఒక ఎంపికను నొక్కండి:',
        'quick_btn_paddy': '🛵 చిన్న పరిమాణం: వరి 50 కిలోలు (జనగాం)',
        'quick_btn_tomato': '🚛 భారీ పరిమాణం: టమాటా 1,200 కిలోలు (శంషాబాద్)',
        'quick_btn_onion': '🧅 సాధారణ పరిమాణం: ఉల్లి 300 కిలోలు (భువనగిరి)',
        'metric_net_cash_title': '💰 చేతికి అందే నికర లాభం',
        'metric_net_cash_help': 'రవాణా, మార్కెట్ ఖర్చులు, కమీషన్ మినహాయించిన తర్వాత మీ చేతికి వచ్చే నిజమైన నగదు.',
        'btn_customize_inputs': '👈 లేదా ఎడమ సైడ్‌బార్‌లో పంట, స్థానం, తేదీలను మీ ఇష్టానుసారం మార్చుకోండి',
        'educational_matrix_title': '📖 పంట నిల్వ సామర్థ్యం మరియు నాణ్యత మార్పు పట్టిక',
        'platform_navigation': 'ప్లాట్‌ఫారమ్ నావిగేషన్'
    },
    'hi': {
        'small_batch_mode_badge': '🛵 कम मात्रा मोड (≤ 500 किग्रा)',
        'small_batch_mode_help': 'छोटे किसानों के लिए विशेष। दूर की मंडी जाने में अधिक किराया न लगे, इसलिए पास के रयतू बाज़ार व स्थानीय बाज़ार सुझाए जा रहे हैं।',
        'bulk_batch_mode_badge': '🚛 बड़ी व्यावसायिक मात्रा (> 500 किग्रा)',
        'small_market_card_title': '🏪 कम मात्रा हेतु अनुशंसित स्थानीय रयतू बाज़ार / छोटा बाज़ार',
        'small_market_reason': 'कम मात्रा के लिए उत्तम: बड़ा वाहन किराए पर लेने की आवश्यकता नहीं, 0% आढ़त/कमीशन, बाइक या ऑटो से आसानी से बिक्री।',
        'btn_navigate_small_market': '🧭 {market} (स्थानीय बाज़ार) का रास्ता देखें',
        'lbl_filter_markets': 'मंडियां फ़िल्टर करें:',
        'filter_all_markets': 'सभी मंडियां',
        'filter_small_markets': '🏪 रयतू बाज़ार व स्थानीय बाज़ार',
        'filter_wholesale_markets': '🚛 थोक APMC मंडियां',
        'col_market_category': 'श्रेणी',
        'col_commission': 'आढ़त (₹)',
        'small_market_profit_benefit': '💡 0% आढ़त व कम किराया: दूर की थोक मंडी की तुलना में ढुलाई में ~₹{transit_diff:,.0f} की बचत!',
        'quick_start_demo_title': '⚡ तुरंत डेमो एक्सेस (OTP की आवश्यकता नहीं)',
        'quick_start_demo_desc': 'डैशबोर्ड को तुरंत देखने के लिए नीचे दिए गए किसी भी किसान प्रोफाइल पर क्लिक करें:',
        'demo_farmer_1_name': '🌾 मल्लेश (जनगांव)',
        'demo_farmer_1_desc': 'धान किसान • 50 किग्रा (कम मात्रा)',
        'demo_farmer_2_name': '🍅 रामुलु (शमशाबाद)',
        'demo_farmer_2_desc': 'टमाटर किसान • 1,200 किग्रा (थोक व्यापार)',
        'demo_farmer_3_name': '🧅 वेंकट (भोंगीर)',
        'demo_farmer_3_desc': 'प्याज किसान • 300 किग्रा (मानक)',
        'quick_scenario_title': '🚀 1-क्लिक त्वरित मंडी विश्लेषण',
        'quick_scenario_desc': 'मंडी खोज, भाव और शुद्ध मुनाफे की तत्काल जांच हेतु किसी भी विकल्प पर क्लिक करें:',
        'quick_btn_paddy': '🛵 कम मात्रा: धान 50 किग्रा (जनगांव)',
        'quick_btn_tomato': '🚛 थोक मात्रा: टमाटर 1,200 किग्रा (शमशाबाद)',
        'quick_btn_onion': '🧅 मानक मात्रा: प्याज 300 किग्रा (भोंगीर)',
        'metric_net_cash_title': '💰 हाथ में आने वाली शुद्ध नकदी',
        'metric_net_cash_help': 'भाड़ा, मंडी खर्च और कमीशन काटने के बाद आपकी वास्तविक शुद्ध कमाई।',
        'btn_customize_inputs': '👈 या बाईं ओर के साइडबार से फसल, स्थान और तारीखें बदलें',
        'educational_matrix_title': '📖 फसल की शेल्फ-लाइफ एवं गुणवत्ता गिरावट तालिका',
        'platform_navigation': 'प्लेटफ़ॉर्म नेविगेशन'
    }
}
for _lang, _kvs in EXTRA_TRANSLATIONS.items():
    if _lang in TRANSLATIONS:
        TRANSLATIONS[_lang].update(_kvs)

VOICE_TRANSLATIONS = {
    'en': {
        'voice_assistant_title': '🎙️ Farmer Voice Assistant (Speak in Your Language)',
        'voice_assistant_desc': 'Speak your crop details in your mother tongue (Telugu, Hindi, or English) or tap sample voice phrases below.',
        'voice_btn_speak': '🎙️ Click to Speak (Web Speech)',
        'voice_audio_record_help': 'Or record audio directly with your microphone:',
        'voice_listening': '🎧 Listening to your voice... Please speak clearly now!',
        'voice_quick_examples_title': '🗣️ Or Try Common Voice Commands (1-Tap Test):',
        'voice_sample_1': '🌾 "I have 50 kg rice in Jangaon, where to sell?"',
        'voice_sample_2': '🍅 "1200 kg tomato in Shamshabad"',
        'voice_sample_3': '🧅 "300 kg onion in Bhongir"',
        'voice_detected_badge': '🎙️ Spoken Command Recognized',
        'voice_advice_title': '🔊 Listen to Voice Advice in Your Mother Tongue',
        'voice_advice_desc': 'Tap play below to listen to the complete market analysis and recommendation spoken aloud in your mother tongue.',
        'voice_play_btn': '▶️ Play Voice Advice',
        'voice_generating': '🔊 Generating audio advice in your language...',
        'voice_parsed_chip': '🌾 Parsed: Crop: **{crop}** • Quantity: **{qty} kg** • Location: **{loc}**',
    },
    'te': {
        'voice_assistant_title': '🎙️ రైతు వాయిస్ అసిస్టెంట్ (మీ మాతృభాషలో మాట్లాడండి)',
        'voice_assistant_desc': 'మీ పంట వివరాలను మీ మాతృభాషలో (తెలుగు, హిందీ, ఇంగ్లీష్) మాట్లాడండి లేదా కింద ఉన్న నమూనా మాటలను నొక్కండి.',
        'voice_btn_speak': '🎙️ మాట్లాడండి (వాయిస్ కమాండ్)',
        'voice_audio_record_help': 'లేదా మీ మైక్రోఫోన్ ద్వారా మాట్లాడి రికార్డ్ చేయండి:',
        'voice_listening': '🎧 వింటున్నాము... దయచేసి మీ పంట వివరాలు మాట్లాడండి!',
        'voice_quick_examples_title': '🗣️ లేదా సాధారణ వాయిస్ మాటలను ప్రయత్నించండి (1-ట్యాప్):',
        'voice_sample_1': '🌾 "నా దగ్గర 50 కిలోల వరి ఉంది, జనగాంలో ఎక్కడ అమ్మాలి?"',
        'voice_sample_2': '🍅 "1200 కేజీల టమాటా శంషాబాద్ లో అమ్మాలి"',
        'voice_sample_3': '🧅 "300 కిలోల ఉల్లిపాయలు భువనగిరి"',
        'voice_detected_badge': '🎙️ మీ మాటలు గుర్తించబడ్డాయి',
        'voice_advice_title': '🔊 మీ మాతృభాషలో వాయిస్ సలహా వినండి',
        'voice_advice_desc': 'మార్కెట్ సిఫార్సు, ధరలు మరియు రవాణా వివరాలను మీ భాషలో మాటల్లో వినడానికి ప్లే నొక్కండి.',
        'voice_play_btn': '▶️ వాయిస్ సలహా వినండి',
        'voice_generating': '🔊 మీ భాషలో వాయిస్ సలహా రూపొందిస్తున్నాము...',
        'voice_parsed_chip': '🌾 గుర్తించిన వివరాలు: పంట: **{crop}** • పరిమాణం: **{qty} కిలోలు** • స్థానం: **{loc}**',
    },
    'hi': {
        'voice_assistant_title': '🎙️ किसान वॉयस असिस्टेंट (अपनी मातृभाषा में बोलें)',
        'voice_assistant_desc': 'अपनी फसल का विवरण अपनी मातृभाषा (हिन्दी, तेलुगु, अंग्रेज़ी) में बोलें या नीचे दिए गए वॉयस उदाहरणों पर क्लिक करें।',
        'voice_btn_speak': '🎙️ बोलें (वॉयस कमांड)',
        'voice_audio_record_help': 'या अपने माइक्रोफ़ोन से आवाज़ रिकॉर्ड करें:',
        'voice_listening': '🎧 सुन रहे हैं... कृपया अपनी फसल का विवरण बोलें!',
        'voice_quick_examples_title': '🗣️ या सामान्य वॉयस कमांड आज़माएँ (1-क्लिक टेस्ट):',
        'voice_sample_1': '🌾 "मेरे पास 50 किलो धान है, जनगांव में कहाँ बेचूं?"',
        'voice_sample_2': '🍅 "1200 किलो टमाटर शमशाबाद में बेचना है"',
        'voice_sample_3': '🧅 "300 किलो प्याज भोंगीर मंडी"',
        'voice_detected_badge': '🎙️ आपकी आवाज़ पहचानी गई',
        'voice_advice_title': '🔊 अपनी मातृभाषा में वॉयस सलाह सुनें',
        'voice_advice_desc': 'मंडी सिफारिश, भाव और परिवहन विवरण अपनी भाषा में सुनने के लिए नीचे प्ले बटन दबाएं।',
        'voice_play_btn': '▶️ वॉयस सलाह सुनें',
        'voice_generating': '🔊 आपकी भाषा में वॉयस सलाह तैयार हो रही है...',
        'voice_parsed_chip': '🌾 पहचानी गई जानकारी: फसल: **{crop}** • मात्रा: **{qty} किग्रा** • स्थान: **{loc}**',
    },
    'kn': {
        'voice_assistant_title': '🎙️ ರೈತ ವಾಯ್ಸ್ ಸಹಾಯಕ (ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ ಮಾತನಾಡಿ)',
        'voice_assistant_desc': 'ನಿಮ್ಮ ಬೆಳೆ ವಿವರಗಳನ್ನು ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ ಮಾತನಾಡಿ ಅಥವಾ ಕೆಳಗಿನ ಉದಾಹರಣೆಗಳನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ.',
        'voice_btn_speak': '🎙️ ಮಾತನಾಡಿ (ವಾಯ್ಸ್ ಕಮಾಂಡ್)',
        'voice_audio_record_help': 'ಅಥವಾ ಮೈಕ್ರೊಫೋನ್ ಮೂಲಕ ರೆಕಾರ್ಡ್ ಮಾಡಿ:',
        'voice_listening': '🎧 ಆಲಿಸುತ್ತಿದ್ದೇವೆ... ದಯವಿಟ್ಟು ಸ್ಪಷ್ಟವಾಗಿ ಮಾತನಾಡಿ!',
        'voice_quick_examples_title': '🗣️ ಅಥವಾ ವಾಯ್ಸ್ ಉದಾಹರಣೆಗಳನ್ನು ಪ್ರಯತ್ನಿಸಿ:',
        'voice_sample_1': '🌾 "ನನ್ನ ಬಳಿ 50 ಕೆಜಿ ಭತ್ತವಿದೆ, ಜನಗಾಂವ್‌ನಲ್ಲಿ ಎಲ್ಲಿ ಮಾರಾಟ ಮಾಡಬೇಕು?"',
        'voice_sample_2': '🍅 "1200 ಕೆಜಿ ಟೊಮ್ಯಾಟೊ ಶಂಶಾಬಾದ್"',
        'voice_sample_3': '🧅 "300 ಕೆಜಿ ಈರುಳ್ಳಿ ಭೋಂಗೀರ್"',
        'voice_detected_badge': '🎙️ ನಿಮ್ಮ ಧ್ವನಿ ಗುರುತಿಸಲಾಗಿದೆ',
        'voice_advice_title': '🔊 ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ ವಾಯ್ಸ್ ಸಲಹೆ ಕೇಳಿ',
        'voice_advice_desc': 'ಸಂಪೂರ್ಣ ಮಾರುಕಟ್ಟೆ ಶಿಫಾರಸು ಮತ್ತು ವಿಶ್ಲೇಷಣೆಯನ್ನು ಆಡಿಯೊ ಮೂಲಕ ಕೇಳಲು ಪ್ಲೇ ಮಾಡಿ.',
        'voice_play_btn': '▶️ ಸಲಹೆ ಆಲಿಸಿ',
        'voice_generating': '🔊 ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ ಆಡಿಯೋ ಸಿದ್ಧವಾಗುತ್ತಿದೆ...',
        'voice_parsed_chip': '🌾 ಗುರುತಿಸಲಾದ ಮಾಹಿತಿ: ಬೆಳೆ: **{crop}** • ಪ್ರಮಾಣ: **{qty} ಕೆಜಿ** • ಸ್ಥಳ: **{loc}**',
    },
    'ta': {
        'voice_assistant_title': '🎙️ விவசாயி குரல் உதவியாளர் (உங்கள் மொழியில் பேசுங்கள்)',
        'voice_assistant_desc': 'உங்கள் பயிர் விவரங்களை உங்கள் தாய்மொழியில் பேசுங்கள் அல்லது கீழே உள்ள மாதிரிகளை கிளிக் செய்யவும்.',
        'voice_btn_speak': '🎙️ பேசுங்கள் (Voice Command)',
        'voice_audio_record_help': 'அல்லது மைக்ரோஃபோன் மூலம் பதிவு செய்யுங்கள்:',
        'voice_listening': '🎧 கேட்கிறது... தெளிவாக பேசுங்கள்!',
        'voice_quick_examples_title': '🗣️ அல்லது குரல் கட்டளைகளை முயற்சிக்கவும்:',
        'voice_sample_1': '🌾 "என்னிடம் 50 கிலோ நெல் உள்ளது, ஜனகானில் எங்கு விற்பது?"',
        'voice_sample_2': '🍅 "1200 கிலோ தக்காளி ஷம்ஷாபாத்"',
        'voice_sample_3': '🧅 "300 கிலோ வெங்காயம் போங்கிர்"',
        'voice_detected_badge': '🎙️ உங்கள் குரல் அடையாளம் காணப்பட்டது',
        'voice_advice_title': '🔊 உங்கள் தாய்மொழியில் குரல் ஆலோசனையைக் கேளுங்கள்',
        'voice_advice_desc': 'சந்தை பரிந்துரை மற்றும் விவரங்களை ஆடியோவில் கேட்க பிளே செய்யவும்.',
        'voice_play_btn': '▶️ ஆலோசனையைக் கேளுங்கள்',
        'voice_generating': '🔊 உங்கள் மொழியில் ஆடியோ தயாராகிறது...',
        'voice_parsed_chip': '🌾 அடையாளம் காணப்பட்டவை: பயிர்: **{crop}** • அளவு: **{qty} கிலோ** • இடம்: **{loc}**',
    },
    'mr': {
        'voice_assistant_title': '🎙️ शेतकरी व्हॉईस असिस्टंट (आपल्या भाषेत बोला)',
        'voice_assistant_desc': 'आपल्या पिकाची माहिती आपल्या भाषेत सांगा किंवा खालील उदाहरणांवर क्लिक करा.',
        'voice_btn_speak': '🎙️ बोला (व्हॉईस कमांड)',
        'voice_audio_record_help': 'किंवा मायक्रोफोनद्वारे रेकॉर्ड करा:',
        'voice_listening': '🎧 ऐकत आहे... कृपया स्पष्ट बोला!',
        'voice_quick_examples_title': '🗣️ किंवा व्हॉईस उदाहरणे वापरून पहा:',
        'voice_sample_1': '🌾 "माझ्याकडे 50 किलो भात आहे, जनगावमध्ये कुठे विकू?"',
        'voice_sample_2': '🍅 "1200 किलो टोमॅटो शमशाबाद"',
        'voice_sample_3': '🧅 "300 किलो कांदा भोंगीर"',
        'voice_detected_badge': '🎙️ तुमचा आवाज ओळखला गेला',
        'voice_advice_title': '🔊 आपल्या भाषेत ऑडिओ सल्ला ऐका',
        'voice_advice_desc': 'बाजाराची शिफारस आणि विश्लेषण ऑडिओमध्ये ऐकण्यासाठी प्ले करा.',
        'voice_play_btn': '▶️ सल्ला ऐका',
        'voice_generating': '🔊 आपल्या भाषेत ऑडिओ तयार होत आहे...',
        'voice_parsed_chip': '🌾 ओळखलेली माहिती: पीक: **{crop}** • प्रमाण: **{qty} किलो** • ठिकाण: **{loc}**',
    }
}
REDESIGN_TRANSLATIONS = {
    'en': {
        'app_subtitle_redesign': 'Your harvest. Your market. Your decision.',
        'welcome_smart_decision': 'Make smarter decisions for your harvest.',
        'welcome_desc': 'Compare live market prices across nearby APMC mandis, estimate net revenue after transport, and get instant AI guidance on whether to sell now or wait.',
        'btn_analyze_harvest': 'Analyze Market',
        'metric_current_market_price': 'Current Market Price',
        'metric_best_available_market': 'Best Available Market',
        'metric_estimated_revenue': 'Estimated Revenue',
        'metric_distance_to_market': 'Distance to Market',
        'decision_scores_title': 'Decision Support Scores',
        'decision_scores_disclaimer': 'Scores are decision-support indicators based on price forecast, spoilage risk, and transport cost (not guaranteed probabilities).',
        'nav_dashboard': '📊 Dashboard',
        'nav_market_comparison': '🏪 Market Comparison',
        'nav_price_forecast': '📈 Price Forecast',
        'nav_ai_recommendation': '🤖 AI Recommendation',
        'nav_about': 'ℹ️ About Platform',
        'feed_live_indicator': 'Live APMC Feed Active',
        'crop_input_title': '🌾 Enter Harvest Details',
        'crop_input_subtitle': 'Provide your crop, quantity, and location to find the highest-paying mandi',
    },
    'te': {
        'app_subtitle_redesign': 'మీ పంట. మీ మార్కెట్. మీ నిర్ణయం.',
        'welcome_smart_decision': 'మీ పంటకు సరైన మరియు లాభదాయకమైన నిర్ణయం తీసుకోండి.',
        'welcome_desc': 'సమీప మార్కెట్లలో తాజా ధరలను పోల్చండి, రవాణా ఖర్చులు పోను నికర లాభాన్ని లెక్కించండి మరియు వెంటనే అమ్మాలా లేదా వేచి ఉండాలా అనే AI సలహా పొందండి.',
        'btn_analyze_harvest': 'మార్కెట్ విశ్లేషించండి',
        'metric_current_market_price': 'ప్రస్తుత మార్కెట్ ధర',
        'metric_best_available_market': 'అత్యుత్తమ మార్కెట్',
        'metric_estimated_revenue': 'అంచనా మొత్తం ఆదాయం',
        'metric_distance_to_market': 'మార్కెట్ దూరం',
        'decision_scores_title': 'నిర్ణయ సూచిక స్కోర్లు',
        'decision_scores_disclaimer': 'ధరల అంచనా, నిల్వ నష్ట ప్రమాదం మరియు రవాణా ఖర్చులపై ఆధారపడిన నిర్ణయ సూచికలు మాత్రమే (హామీ కాదు).',
        'nav_dashboard': '📊 డ్యాష్‌బోర్డ్',
        'nav_market_comparison': '🏪 మార్కెట్ల పోలిక',
        'nav_price_forecast': '📈 ధరల అంచనా',
        'nav_ai_recommendation': '🤖 AI సిఫార్సు',
        'nav_about': 'ℹ️ ప్లాట్‌ఫారమ్ గురించి',
        'feed_live_indicator': 'లైవ్ APMC ఫీడ్ యాక్టివ్',
        'crop_input_title': '🌾 పంట వివరాలను నమోదు చేయండి',
        'crop_input_subtitle': 'అత్యధిక ధర చెల్లించే మార్కెట్‌ను కనుగొనడానికి మీ పంట, పరిమాణం మరియు స్థానాన్ని ఎంచుకోండి',
    },
    'hi': {
        'app_subtitle_redesign': 'आपकी फसल. आपका बाज़ार. आपका निर्णय.',
        'welcome_smart_decision': 'अपनी फसल के लिए समझदारी भरा और सही निर्णय लें।',
        'welcome_desc': 'आस-पास की मंडियों के ताज़ा भावों की तुलना करें, परिवहन खर्च काटकर शुद्ध मुनाफ़े का हिसाब लगाएं और तुरंत बेचें या प्रतीक्षा करें की सटीक AI सलाह पाएं।',
        'btn_analyze_harvest': 'बाज़ार का विश्लेषण करें',
        'metric_current_market_price': 'वर्तमान बाज़ार भाव',
        'metric_best_available_market': 'सर्वोत्तम उपलब्ध मंडी',
        'metric_estimated_revenue': 'अनुमानित कुल आय',
        'metric_distance_to_market': 'मंडी की दूरी',
        'decision_scores_title': 'निर्णय समर्थन स्कोर',
        'decision_scores_disclaimer': 'यह स्कोर मूल्य पूर्वानुमान, फसल खराब होने के जोखिम और परिवहन खर्च पर आधारित निर्णय-सहायक संकेतक हैं (गारंटी नहीं)।',
        'nav_dashboard': '📊 डैशबोर्ड',
        'nav_market_comparison': '🏪 मंडी तुलना',
        'nav_price_forecast': '📈 मूल्य पूर्वानुमान',
        'nav_ai_recommendation': '🤖 AI अनुशंसा',
        'nav_about': 'ℹ️ पोर्टल के बारे में',
        'feed_live_indicator': 'लाइव APMC फीड सक्रिय',
        'crop_input_title': '🌾 फसल विवरण दर्ज करें',
        'crop_input_subtitle': 'सबसे अधिक भाव देने वाली मंडी खोजने के लिए फसल, मात्रा और स्थान दर्ज करें',
    },
    'ta': {
        'btn_analyze_harvest': 'சந்தையை ஆராய்க',
    },
    'kn': {
        'btn_analyze_harvest': 'ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಿಸಿ',
    },
    'mr': {
        'btn_analyze_harvest': 'बाजार विश्लेषण करा',
    }
}
for _rlang, _rkvs in REDESIGN_TRANSLATIONS.items():
    if _rlang in TRANSLATIONS:
        TRANSLATIONS[_rlang].update(_rkvs)
    elif 'en' in TRANSLATIONS:
        TRANSLATIONS['en'].update(_rkvs)

for _vlang, _vkvs in VOICE_TRANSLATIONS.items():
    if _vlang in TRANSLATIONS:
        TRANSLATIONS[_vlang].update(_vkvs)
    elif 'en' in TRANSLATIONS:
        TRANSLATIONS['en'].update(_vkvs)

EXPANSION_TRANSLATIONS = {
    'en': {
        'spot_advisory_title': 'APMC Mandi Spot Rate Advisory',
        'spot_advisory_desc': 'Selling and routing decisions for this crop are grounded in verified daily APMC mandi spot prices from regional Telangana agricultural markets. Continuous 3-day machine-learning forecasting will activate as seasonal time-series records accumulate.',
        'filter_by_category': 'Filter by Crop Category',
        'lbl_crop_category': 'Crop Category',
        'select_crop_placeholder': '🌱 Choose your crop...',
        'farmer_loc_placeholder': 'Enter village, town, or mandal (e.g. Warangal, Jangaon)',
        'quantity_placeholder': 'e.g. 500',
        'err_crop_required': 'Please select a crop to analyze market prices.',
        'err_qty_required': 'Please enter harvest quantity in kilograms.',
        'err_loc_required': 'Please enter your location or nearest market town.',
        'lbl_freshness_pending': '🌱 Select a crop and harvest date above to view automated mandi auction grading & freshness.',
    },
    'te': {
        'spot_advisory_title': 'APMC మార్కెట్ స్పాట్ ధర సలహా',
        'spot_advisory_desc': 'ఈ పంటకు అమ్మకం మరియు మార్కెట్ నిర్ణయాలు తెలంగాణ ప్రాంతీయ మార్కెట్ల నుండి ధృవీకరించబడిన రోజువారీ APMC స్పాట్ ధరలపై ఆధారపడి ఉన్నాయి. తగినంత చారిత్రక డేటా లభ్యం కాగానే 3-రోజుల ML ధర అంచనా ప్రారంభమవుతుంది.',
        'filter_by_category': 'పంట వర్గం ప్రకారం ఫిల్టర్ చేయండి',
        'lbl_crop_category': 'పంట వర్గం',
        'select_crop_placeholder': '🌱 మీ పంటను ఎంచుకోండి...',
        'farmer_loc_placeholder': 'గ్రామం, పట్టణం లేదా మండలం నమోదు చేయండి (ఉదా: వరంగల్, జనగాం)',
        'quantity_placeholder': 'ఉదా: 500',
        'err_crop_required': 'మార్కెట్ ధరలను విశ్లేషించడానికి దయచేసి పంటను ఎంచుకోండి.',
        'err_qty_required': 'దయచేసి పంట పరిమాణాన్ని (కిలోలలో) నమోదు చేయండి.',
        'err_loc_required': 'దయచేసి మీ ప్రాంతం లేదా సమీప మార్కెట్ పట్టణం పేరు నమోదు చేయండి.',
        'lbl_freshness_pending': '🌱 నాణ్యత మరియు గ్రేడింగ్ వివరాలు చూడటానికి పైన పంటను ఎంచుకోండి.',
    },
    'hi': {
        'spot_advisory_title': 'APMC मंडी हाजिर भाव परामर्श',
        'spot_advisory_desc': 'इस फसल के लिए बिक्री और मंडी चयन निर्णय तेलंगाना की क्षेत्रीय मंडियों के प्रमाणित दैनिक हाजिर भावों पर आधारित हैं। पर्याप्त मौसमी डेटा उपलब्ध होते ही 3-दिवसीय ML मूल्य भविष्यवाणी सक्रिय हो जाएगी।',
        'filter_by_category': 'फसल श्रेणी अनुसार चुनें',
        'lbl_crop_category': 'फसल श्रेणी',
        'select_crop_placeholder': '🌱 अपनी फसल चुनें...',
        'farmer_loc_placeholder': 'अपना गाँव, कस्बा या तहसील दर्ज करें (उदा. वारंगल, जनगांव)',
        'quantity_placeholder': 'उदा. 500',
        'err_crop_required': 'मंडी भावों का विश्लेषण करने के लिए कृपया एक फसल चुनें।',
        'err_qty_required': 'कृपया फसल की सही मात्रा (किलो में) दर्ज करें।',
        'err_loc_required': 'कृपया अपना स्थान या निकटतम मंडी शहर दर्ज करें।',
        'lbl_freshness_pending': '🌱 गुणवत्ता और ग्रेडिंग देखने के लिए कृपया ऊपर एक फसल चुनें।',
    },
    'ta': {
        'spot_advisory_title': 'APMC சந்தை நேரடி விலை வழிகாட்டுதல்',
        'spot_advisory_desc': 'இந்த பயிருக்கான விற்பனை மற்றும் சந்தை முடிவுகள் தெலுங்கானாவின் ஒழுங்குமுறை விற்பனைக்கூடங்களின் தினசரி நேரடி விலைகளை அடிப்படையாகக் கொண்டவை. போதிய வரலாற்றுத் தரவுகள் சேர்ந்ததும் 3-நாள் ML விலை முன்னறிவிப்பு செயல்படுத்தப்படும்.',
        'filter_by_category': 'பயிர் வகை வாரியாக வடிகட்டவும்',
        'lbl_crop_category': 'பயிர் வகை',
        'select_crop_placeholder': '🌱 உங்கள் பயிரைத் தேர்ந்தெடுக்கவும்...',
        'farmer_loc_placeholder': 'கிராமம், நகரம் அல்லது வட்டத்தை உள்ளிடவும் (எ.கா: வாரங்கல்)',
        'quantity_placeholder': 'எ.கா. 500',
        'err_crop_required': 'சந்தை விலைகளை பகுப்பாய்வு செய்ய ஒரு பயிரைத் தேர்ந்தெடுக்கவும்.',
        'err_qty_required': 'பயிர் அளவை (கிலோவில்) உள்ளிடவும்.',
        'err_loc_required': 'உங்கள் இடம் அல்லது அருகிலுள்ள சந்தை நகரத்தை உள்ளிடவும்.',
        'lbl_freshness_pending': '🌱 தரமதிப்பீட்டைக் காண மேலே ஒரு பயிரைத் தேர்ந்தெடுக்கவும்.',
    },
    'kn': {
        'spot_advisory_title': 'APMC ಮಾರುಕಟ್ಟೆ ಪ್ರಸ್ತುತ ದರ ಮಾಹಿತಿ',
        'spot_advisory_desc': 'ಈ ಬೆಳೆಗೆ ಮಾರಾಟ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ನಿರ್ಧಾರಗಳು ತೆಲಂಗಾಣದ ಪ್ರಾದೇಶಿಕ APMC ಮಾರುಕಟ್ಟೆಗಳ ದೈನಂದಿನ ನೈಜ ದರಗಳನ್ನು ಆಧರಿಸಿವೆ. ಸಾಕಷ್ಟು ಹಿಂದಿನ ದರಗಳ ಮಾಹಿತಿ ಲಭ್ಯವಾದಾಗ 3-ದಿನಗಳ ML ಬೆಲೆ ಮುನ್ಸೂಚನೆ ಸಕ್ರಿಯಗೊಳ್ಳುತ್ತದೆ.',
        'filter_by_category': 'ಬೆಳೆ ವರ್ಗದ ಪ್ರಕಾರ ಫಿಲ್ಟರ್ ಮಾಡಿ',
        'lbl_crop_category': 'ಬೆಳೆ ವರ್ಗ',
        'select_crop_placeholder': '🌱 ನಿಮ್ಮ ಬೆಳೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ...',
        'farmer_loc_placeholder': 'ಗ್ರಾಮ, ಪಟ್ಟಣ ಅಥವಾ ತಾಲೂಕನ್ನು ನಮೂದಿಸಿ (ಉದಾ: ವಾರಂಗಲ್)',
        'quantity_placeholder': 'ಉದಾ. 500',
        'err_crop_required': 'ಮಾರುಕಟ್ಟೆ ದರಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಲು ದಯವಿಟ್ಟು ಬೆಳೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.',
        'err_qty_required': 'ದಯವಿಟ್ಟು ಬೆಳೆ ಪ್ರಮಾಣವನ್ನು (ಕೆಜಿಯಲ್ಲಿ) ನಮೂದಿಸಿ.',
        'err_loc_required': 'ದಯವಿಟ್ಟು ನಿಮ್ಮ ಸ್ಥಳ ಅಥವಾ ಹತ್ತಿರದ ಮಾರುಕಟ್ಟೆ ಪಟ್ಟಣವನ್ನು ನಮೂದಿಸಿ.',
        'lbl_freshness_pending': '🌱 ಮಾರುಕಟ್ಟೆ ಗುಣಮಟ್ಟದ ಗ್ರೇಡಿಂಗ್ ನೋಡಲು ಮೇಲೆ ಬೆಳೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.',
    },
    'mr': {
        'spot_advisory_title': 'APMC कृषी उत्पन्न बाजार समिती थेट भाव सल्ला',
        'spot_advisory_desc': 'या पिकासाठी विक्री आणि बाजारपेठ निवड निर्णय तेलंगणातील प्रादेशिक APMC बाजारपेठांमधील प्रमाणित दैनंदिन थेट भावांवर आधारित आहेत. पुरेसा ऐतिहासिक डेटा उपलब्ध होताच 3-दिवसीय ML किंमत अंदाज सुरू होईल.',
        'filter_by_category': 'पिकांच्या प्रकारानुसार निवडा',
        'lbl_crop_category': 'पिकांचा प्रकार',
        'select_crop_placeholder': '🌱 आपले पीक निवडा...',
        'farmer_loc_placeholder': 'गाव, शहर किंवा तालुका प्रविष्ट करा (उदा. वारंगल)',
        'quantity_placeholder': 'उदा. 500',
        'err_crop_required': 'बाजारभावाचे विश्लेषण करण्यासाठी कृपया एक पीक निवडा.',
        'err_qty_required': 'कृपया पिकाचे प्रमाण (किलोमध्ये) प्रविष्ट करा.',
        'err_loc_required': 'कृपया आपले स्थान किंवा जवळचे बाजारपेठ शहर प्रविष्ट करा.',
        'lbl_freshness_pending': '🌱 प्रतवारी व ताजेपणा पाहण्यासाठी कृपया वर पीक निवडा.',
    }
}

for _elang, _ekvs in EXPANSION_TRANSLATIONS.items():
    if _elang in TRANSLATIONS:
        TRANSLATIONS[_elang].update(_ekvs)
    elif 'en' in TRANSLATIONS:
        TRANSLATIONS['en'].update(_ekvs)



def t(key: str, lang: str = "en", **kwargs) -> str:
    """
    Retrieve translated string for a given key and language.
    Falls back to English if key missing in chosen language.
    """
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS.get("en", {}))
    text = lang_dict.get(key)
    if text is None:
        text = TRANSLATIONS.get("en", {}).get(key, key)
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text


def format_crop(crop_name: str, lang: str = "en") -> str:
    """Format crop name for selectbox display while keeping value clean."""
    if crop_name in CROPS_DISPLAY:
        return CROPS_DISPLAY[crop_name].get(lang, CROPS_DISPLAY[crop_name].get("en", crop_name))
    return crop_name


def format_quality(quality_name: str, lang: str = "en") -> str:
    """Format quality grade for selectbox display while keeping value clean."""
    if quality_name in QUALITY_DISPLAY:
        return QUALITY_DISPLAY[quality_name].get(lang, QUALITY_DISPLAY[quality_name].get("en", quality_name))
    return quality_name


WEATHER_CONDITIONS = {
    "Partly Cloudy": {
        "en": "Partly Cloudy", "te": "పాక్షికంగా మేఘావృతం", "hi": "आंशिक रूप से बादल",
        "ta": "பகுதி மேகமூட்டம்", "kn": "ಭಾಗಶಃ ಮೋಡ ಕವಿದ", "mr": "अंशतः ढगाळ"
    },
    "Humid & Partly Cloudy": {
        "en": "Humid & Partly Cloudy", "te": "తేమ & పాక్షికంగా మేఘావృతం", "hi": "आर्द्र और आंशिक रूप से बादल",
        "ta": "ஈரப்பதம் & பகுதி மேகமூட்டம்", "kn": "ಆರ್ದ್ರ ಮತ್ತು ಭಾಗಶಃ ಮೋಡ", "mr": "दमट आणि अंशतः ढगाळ"
    },
    "Hot & Sunny": {
        "en": "Hot & Sunny", "te": "ఎండ & వేడి వాతావరణం", "hi": "गर्म और धूप",
        "ta": "சூடான வெயில்", "kn": "ಬಿಸಿಲು ಮತ್ತು ಸೆಕೆ", "mr": "उष्ण आणि कडक ऊन"
    },
    "Sunny": {
        "en": "Sunny", "te": "ఎండగా ఉంది", "hi": "धूप", "ta": "வெயில்", "kn": "ಬಿಸಿಲು", "mr": "कडक ऊन"
    }
}

WEATHER_ALERTS = {
    "Moderate rot risk for perishable vegetables.": {
        "en": "Moderate rot risk for perishable vegetables.",
        "te": "కూరగాయలు పాడయ్యే మోస్తరు ప్రమాదం ఉంది.",
        "hi": "जल्दी खराब होने वाली सब्जियों के खराब होने का मध्यम जोखिम।",
        "ta": "காய்கறிகள் அழுகும் மிதமான ஆபத்து.",
        "kn": "ತರಕಾರಿಗಳು ಹಾಳಾಗುವ ಮಧ್ಯಮ ಅಪಾಯವಿದೆ.",
        "mr": "नाशवंत भाजीपाल्यासाठी मध्यम नासाडीचा धोका."
    },
    "Moisture loss / weight loss risk.": {
        "en": "Moisture loss / weight loss risk.",
        "te": "తేమ కోల్పోవడం / బరువు తగ్గే ప్రమాదం.",
        "hi": "नमी में कमी / वजन घटने का जोखिम।",
        "ta": "ஈரப்பதம் குறைவு / எடை இழப்பு ஆபத்து.",
        "kn": "ತೇವಾಂಶ ನಷ್ಟ / ತೂಕ ಇಳಿಕೆಯ ಅಪಾಯ.",
        "mr": "ओलावा कमी / वजन घटण्याचा धोका."
    },
    "Good conditions for harvesting and transit.": {
        "en": "Good conditions for harvesting and transit.",
        "te": "కోత మరియు రవాణాకు అనుకూలమైన వాతావరణం.",
        "hi": "कटाई और परिवहन के लिए अनुकूल परिस्थितियां।",
        "ta": "அறுவடை மற்றும் போக்குவரத்துக்கு சாதகமான சூழல்.",
        "kn": "ಕೊಯ್ಲು ಮತ್ತು ಸಾಗಣೆಗೆ ಅನುಕೂಲಕರ ವಾತಾವರಣ.",
        "mr": "कापणी आणि वाहतुकीसाठी अनुकूल हवामान."
    },
    "Favorable": {
        "en": "Favorable",
        "te": "అనుకూలం",
        "hi": "अनुकूल",
        "ta": "சாதகமானது",
        "kn": "ಅನುಕೂಲಕರ",
        "mr": "अनुकूल"
    }
}

TRANSIT_ADVICES = {
    "Elevated humidity: Ensure tarpaulin protection during transit to avoid moisture-induced fungal rot.": {
        "en": "Elevated humidity: Ensure tarpaulin protection during transit to avoid moisture-induced fungal rot.",
        "te": "అధిక తేమ: బూజు పట్టకుండా రవాణా సమయంలో పంటపై టార్పాలిన్ కప్పండి.",
        "hi": "अधिक नमी: फंगस और सड़न से बचने के लिए परिवहन के दौरान तिरपाल से ढकें।",
        "ta": "அதிக ஈரப்பதம்: பூஞ்சை தொற்று தவிர்க்க வாகனத்தில் தார்ப்பாய் கொண்டு மூடவும்.",
        "kn": "ಹೆಚ್ಚಿನ ತೇವಾಂಶ: ಶಿಲೀಂಧ್ರ ಕೊಳೆಯುವಿಕೆಯನ್ನು ತಪ್ಪಿಸಲು ಸಾಗಣೆಯ ಸಮಯದಲ್ಲಿ ಟಾರ್ಪಾಲಿನ್ ಹೊದಿಕೆ ಬಳಸಿ.",
        "mr": "जास्त आर्द्रता: बुरशीपासून वाचवण्यासाठी वाहतुकीदरम्यान ताडपत्रीने झाकून ठेवा."
    },
    "High afternoon heat: Transport produce during early morning (5:00–8:00 AM) to minimize dehydration.": {
        "en": "High afternoon heat: Transport produce during early morning (5:00–8:00 AM) to minimize dehydration.",
        "te": "మధ్యాహ్నపు ఎండ: పంట వాడిపోకుండా ఉండటానికి ఉదయం (5:00–8:00) రవాణా చేయండి.",
        "hi": "दोपहर की तेज धूप: उपज सूखने से बचाने के लिए सुबह जल्दी (5:00–8:00 बजे) परिवहन करें।",
        "ta": "மதிய வெயில்: வாடிப்போவதை தவிர்க்க அதிகாலை (5:00–8:00 AM) போக்குவரத்து செய்யவும்.",
        "kn": "ಮಧ್ಯಾಹ್ನದ ತೀವ್ರ ಬಿಸಿಲು: ಬೆಳೆ ಒಣಗದಂತೆ ಮುಂಜಾನೆ (5:00–8:00 AM) ಸಾಗಾಟ ಮಾಡಿ.",
        "mr": "दुपारचे कडक ऊन: सुकण्यापासून वाचवण्यासाठी पहाटे (5:00–8:00 AM) माल पाठवा."
    },
    "Favorable transit weather: Normal open-bed or covered transport is suitable.": {
        "en": "Favorable transit weather: Normal open-bed or covered transport is suitable.",
        "te": "అనుకూలమైన రవాణా వాతావరణం: సాధారణ లేదా కప్పబడిన రవాణా సరిపోతుంది.",
        "hi": "अनुकूल परिवहन मौसम: सामान्य खुली या ढकी गाड़ी उपयुक्त है।",
        "ta": "சாதகமான வானிலை: வழக்கமான திறந்த அல்லது மூடப்பட்ட வாகனம் போதுமானது.",
        "kn": "ಅನುಕೂಲಕರ ಸಾಗಾಟ ಹವಾಮಾನ: ಸಾಮಾನ್ಯ ಅಥವಾ ಮುಚ್ಚಿದ ವಾಹನ ಸೂಕ್ತವಾಗಿದೆ.",
        "mr": "अनुकूल हवामान: सामान्य उघडी किंवा झाकलेली गाडी योग्य आहे."
    },
    "Favorable transit conditions.": {
        "en": "Favorable transit conditions.",
        "te": "రవాణాకు అనుకూలమైన పరిస్థితులు.",
        "hi": "परिवहन के लिए अनुकूल परिस्थितियां।",
        "ta": "சாதகமான போக்குவரத்து சூழல்.",
        "kn": "ಸಾಗಾಟಕ್ಕೆ ಸೂಕ್ತ ಪರಿಸ್ಥಿತಿ.",
        "mr": "वाहतुकीसाठी अनुकूल परिस्थिती."
    }
}

SHELF_LIFE_MAP = {
    "3 – 5 Days": {"en": "3 – 5 Days", "te": "3 – 5 రోజులు", "hi": "3 – 5 दिन", "ta": "3 – 5 நாட்கள்", "kn": "3 – 5 ದಿನಗಳು", "mr": "3 – 5 दिवस"},
    "4 – 7 Days": {"en": "4 – 7 Days", "te": "4 – 7 రోజులు", "hi": "4 – 7 दिन", "ta": "4 – 7 நாட்கள்", "kn": "4 – 7 ದಿನಗಳು", "mr": "4 – 7 दिवस"},
    "3 – 6 Weeks": {"en": "3 – 6 Weeks", "te": "3 – 6 వారాలు", "hi": "3 – 6 सप्ताह", "ta": "3 – 6 வாரங்கள்", "kn": "3 – 6 ವಾರಗಳು", "mr": "3 – 6 आठवडे"},
    "6 – 12 Months": {"en": "6 – 12 Months", "te": "6 – 12 నెలలు", "hi": "6 – 12 महीने", "ta": "6 – 12 மாதங்கள்", "kn": "6 – 12 ತಿಂಗಳು", "mr": "6 – 12 महिने"},
    "4 – 8 Months": {"en": "4 – 8 Months", "te": "4 – 8 నెలలు", "hi": "4 – 8 महीने", "ta": "4 – 8 மாதங்கள்", "kn": "4 – 8 ತಿಂಗಳು", "mr": "4 – 8 महिने"},
}

PERISHABILITY_MAP = {
    "Very High": {"en": "Very High", "te": "చాలా ఎక్కువ", "hi": "अत्यधिक", "ta": "மிக அதிகம்", "kn": "ಬಹಳ ಹೆಚ್ಚು", "mr": "खूप जास्त"},
    "High": {"en": "High", "te": "ఎక్కువ", "hi": "अधिक", "ta": "அதிகம்", "kn": "ಹೆಚ್ಚು", "mr": "जास्त"},
    "Moderate": {"en": "Moderate", "te": "మోస్తరు", "hi": "मध्यम", "ta": "மிதமானது", "kn": "ಮಧ್ಯಮ", "mr": "मध्यम"},
    "Very Low (Grain)": {"en": "Very Low (Grain)", "te": "చాలా తక్కువ (ధాన్యం)", "hi": "बहुत कम (अनाज)", "ta": "மிகக் குறைவு (தானியம்)", "kn": "ಬಹಳ ಕಡಿಮೆ (ಧಾನ್ಯ)", "mr": "खूप कमी (धान्य)"},
    "Very Low (Fiber)": {"en": "Very Low (Fiber)", "te": "చాలా తక్కువ (పీచు)", "hi": "बहुत कम (फाइबर)", "ta": "மிகக் குறைவு (இழை)", "kn": "ಬಹಳ ಕಡಿಮೆ (ನಾರು)", "mr": "खूप कमी (फायबर)"},
    "Low": {"en": "Low", "te": "తక్కువ", "hi": "कम", "ta": "குறைவு", "kn": "ಕಡಿಮೆ", "mr": "कमी"}
}

DAMAGE_RISK_MAP = {
    "HIGH DAMAGE RISK": {"en": "HIGH DAMAGE RISK", "te": "అధిక నష్టం ప్రమాదం", "hi": "उच्च खराबी का जोखिम", "ta": "அதிக சேத ஆபத்து", "kn": "ಹೆಚ್ಚಿನ ಹಾನಿ ಅಪಾಯ", "mr": "जास्त नुकसानीचा धोका"},
    "MODERATE-HIGH DAMAGE RISK": {"en": "MODERATE-HIGH DAMAGE RISK", "te": "మోస్తరు-అధిక నష్టం ప్రమాదం", "hi": "मध्यम-उच्च खराबी का जोखिम", "ta": "மிதமான-அதிக சேத ஆபத்து", "kn": "ಮಧ್ಯಮ-ಹೆಚ್ಚಿನ ಹಾನಿ ಅಪಾಯ", "mr": "मध्यम-जास्त नुकसानीचा धोका"},
    "LOW-MODERATE DAMAGE RISK": {"en": "LOW-MODERATE DAMAGE RISK", "te": "తక్కువ-మోస్తరు ప్రమాదం", "hi": "कम-मध्यम जोखिम", "ta": "குறைந்த-மிதமான ஆபத்து", "kn": "ಕಡಿಮೆ-ಮಧ್ಯಮ ಅಪಾಯ", "mr": "कमी-मध्यम धोका"},
    "VERY LOW DAMAGE RISK": {"en": "VERY LOW DAMAGE RISK", "te": "చాలా తక్కువ ప్రమాదం", "hi": "अति न्यून जोखिम", "ta": "மிகக் குறைந்த ஆபத்து", "kn": "ಅತ್ಯಂತ ಕಡಿಮೆ ಅಪಾಯ", "mr": "अतिशय कमी धोका"},
    "MODERATE": {"en": "MODERATE", "te": "మోస్తరు ప్రమాదం", "hi": "मध्यम जोखिम", "ta": "மிதமான ஆபத்து", "kn": "ಮಧ್ಯಮ ಅಪಾಯ", "mr": "मध्यम धोका"}
}

SPOILAGE_RATE_MAP = {
    "5% – 8% loss per day without cold storage": {
        "en": "5% – 8% loss per day without cold storage",
        "te": "కోల్డ్ స్టోరేజ్ లేకుండా రోజుకు 5% – 8% నష్టం",
        "hi": "बिना कोल्ड स्टोरेज के 5% – 8% प्रतिदिन नुकसान",
        "ta": "குளிர்சாதன சேமிப்பு இன்றி தினமும் 5% – 8% இழப்பு",
        "kn": "ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್ ಇಲ್ಲದೆ ದಿನಕ್ಕೆ ಶೇ.5 – 8 ನಷ್ಟ",
        "mr": "कोल्ड स्टोरेजशिवाय दररोज 5% – 8% नुकसान"
    },
    "3% – 5% moisture loss per day": {
        "en": "3% – 5% moisture loss per day",
        "te": "రోజుకు 3% – 5% తేమ నష్టం",
        "hi": "3% – 5% प्रतिदिन नमी का नुकसान",
        "ta": "தினமும் 3% – 5% ஈரப்பதம் இழப்பு",
        "kn": "ದಿನಕ್ಕೆ ಶೇ.3 – 5 ತೇವಾಂಶ ನಷ್ಟ",
        "mr": "दररोज 3% – 5% ओलावा घटणे"
    },
    "1% – 2% per week (if dry and aerated)": {
        "en": "1% – 2% per week (if dry and aerated)",
        "te": "వారానికి 1% – 2% (పొడిగా, గాలి ఆడితే)",
        "hi": "1% – 2% प्रति सप्ताह (यदि सूखा व हवादार हो)",
        "ta": "வாரத்திற்கு 1% – 2% (உலர்ந்த, காத்தோட்டமான இடத்தில்)",
        "kn": "ವಾರಕ್ಕೆ ಶೇ.1 – 2 (ಒಣ ಮತ್ತು ಗಾಳಿಯಾಡುವ ಸ್ಥಳದಲ್ಲಿದ್ದರೆ)",
        "mr": "आठवड्याला 1% – 2% (कोरड्या व हवेशीर जागी)"
    },
    "< 0.5% per month in dry bags": {
        "en": "< 0.5% per month in dry bags",
        "te": "నెలకు 0.5% కంటే తక్కువ (పొడి సంచుల్లో)",
        "hi": "सूखी बोरियों में प्रति माह < 0.5%",
        "ta": "உலர்ந்த பைகளில் மாதத்திற்கு < 0.5%",
        "kn": "ಒಣ ಚೀಲಗಳಲ್ಲಿ ತಿಂಗಳಿಗೆ < 0.5%",
        "mr": "कोरड्या गोणीत दरमहा < 0.5%"
    },
    "Negligible if kept dry": {
        "en": "Negligible if kept dry",
        "te": "పొడిగా ఉంచితే నామమాత్రపు నష్టం",
        "hi": "सूखा रखने पर नगण्य नुकसान",
        "ta": "உலர வைத்தால் மிகக் குறைவு",
        "kn": "ಒಣಗಿಸಿಟ್ಟರೆ ನಗಣ್ಯ ನಷ್ಟ",
        "mr": "कोरडे ठेवल्यास नगण्य नुकसान"
    },
    "3-5% daily": {
        "en": "3-5% daily",
        "te": "రోజుకు 3-5%",
        "hi": "प्रतिदिन 3-5%",
        "ta": "தினமும் 3-5%",
        "kn": "ದಿನಕ್ಕೆ ಶೇ.3-5",
        "mr": "दररोज 3-5%"
    }
}

HOLDING_VERDICT_MAP = {
    "⚠️ SELLING TOO LATE CAUSES NET LOSS": {
        "en": "⚠️ SELLING TOO LATE CAUSES NET LOSS",
        "te": "⚠️ ఆలస్యంగా అమ్మితే నికర నష్టం వాటిల్లుతుంది",
        "hi": "⚠️ देर से बेचने पर शुद्ध नुकसान होगा",
        "ta": "⚠️ தாமதமாக விற்றால் நிகர நஷ்டம் ஏற்படும்",
        "kn": "⚠️ ತಡವಾಗಿ ಮಾರಾಟ ಮಾಡಿದರೆ ನಿವ್ವಳ ನಷ್ಟವಾಗುತ್ತದೆ",
        "mr": "⚠️ उशिरा विकल्यास निव्वळ तोटा होईल"
    },
    "⚠️ SHORT WINDOW: Sell within 3-4 days": {
        "en": "⚠️ SHORT WINDOW: Sell within 3-4 days",
        "te": "⚠️ పరిమిత గడువు: 3-4 రోజుల్లో విక్రయించండి",
        "hi": "⚠️ कम समय: 3-4 दिनों के भीतर बेचें",
        "ta": "⚠️ குறுகிய காலம்: 3-4 நாட்களுக்குள் விற்கவும்",
        "kn": "⚠️ ಕಡಿಮೆ ಸಮಯ: 3-4 ದಿನಗಳಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ",
        "mr": "⚠️ कमी वेळ: 3-4 दिवसांत विक्री करा"
    },
    "✅ GOOD PROFIT POTENTIAL: Safe to wait for price rise": {
        "en": "✅ GOOD PROFIT POTENTIAL: Safe to wait for price rise",
        "te": "✅ మంచి లాభావకాశం: ధర పెరుగుదల కోసం ఆగవచ్చు",
        "hi": "✅ अच्छा लाभ अवसर: मूल्य वृद्धि के लिए रुकना सुरक्षित",
        "ta": "✅ நல்ல லாப வாய்ப்பு: விலை உயர்வுக்கு காத்திருக்கலாம்",
        "kn": "✅ ಉತ್ತಮ ಲಾಭದ ಅವಕಾಶ: ದರ ಹೆಚ್ಚಳಕ್ಕೆ ಕಾಯಬಹುದು",
        "mr": "✅ चांगल्या नफ्याची संधी: भाव वाढण्याची वाट पाहणे सुरक्षित"
    },
    "✅ HIGH PROFIT POTENTIAL: Patient selling recommended": {
        "en": "✅ HIGH PROFIT POTENTIAL: Patient selling recommended",
        "te": "✅ అత్యధిక లాభావకాశం: ఓపికగా మంచి ధరకు అమ్మండి",
        "hi": "✅ अत्यधिक लाभ अवसर: धैर्यपूर्वक बेचने की सलाह",
        "ta": "✅ அதிக லாப வாய்ப்பு: பொறுமையாக விற்க பரிந்துரை",
        "kn": "✅ ಗರಿಷ್ಠ ಲಾಭದ ಅವಕಾಶ: ತಾಳ್ಮೆಯಿಂದ ಮಾರಾಟ ಮಾಡಲು ಸಲಹೆ",
        "mr": "✅ उत्तम नफ्याची संधी: संयमाने विक्री करावी"
    },
    "Monitor closely": {
        "en": "Monitor closely",
        "te": "మార్కెట్‌ను నిశితంగా గమనించండి",
        "hi": "सावधानीपूर्वक निगरानी करें",
        "ta": "கவனமாக கண்காணிக்கவும்",
        "kn": "ಎಚ್ಚರಿಕೆಯಿಂದ ಗಮನಿಸಿ",
        "mr": "काळजीपूर्वक निरीक्षण करा"
    }
}

DAMAGE_FACTORS_MAP = {
    "Soft rot and fungal skin breakdown": {
        "en": "Soft rot and fungal skin breakdown",
        "te": "కుళ్ళిపోవడం మరియు బూజు పట్టడం",
        "hi": "सड़न और फफूंद लगना",
        "ta": "அழுகல் மற்றும் பூஞ்சை தொற்று",
        "kn": "ಕೊಳೆತ ಮತ್ತು ಶಿಲೀಂಧ್ರ ಬಾಧೆ",
        "mr": "सडणे आणि बुरशीची लागण"
    },
    "Weight reduction due to transpiration (up to 2% daily)": {
        "en": "Weight reduction due to transpiration (up to 2% daily)",
        "te": "నీటి ఆవిరి వల్ల బరువు తగ్గడం (రోజుకు 2% వరకు)",
        "hi": "नमी सूखने से वजन में कमी (प्रतिदिन 2% तक)",
        "ta": "ஈரப்பதம் இழப்பால் எடை குறைவு (தினமும் 2% வரை)",
        "kn": "ತೇವಾಂಶ ನಷ್ಟದಿಂದ ತೂಕ ಇಳಿಕೆ (ದಿನಕ್ಕೆ 2% ವರೆಗೆ)",
        "mr": "बाष्पीभवनामुळे वजन घटणे (दररोज 2% पर्यंत)"
    },
    "Buyer downgrading from Grade A to Grade C in mandi auctions": {
        "en": "Buyer downgrading from Grade A to Grade C in mandi auctions",
        "te": "మార్కెట్ వేలంలో గ్రేడ్ A నుండి C కి నాణ్యత పడిపోవడం",
        "hi": "मंडी नीलामी में ग्रेड A से ग्रेड C में गिरावट",
        "ta": "சந்தை ஏலத்தில் தரம் A இலிருந்து C ஆக குறைதல்",
        "kn": "ಮಾರುಕಟ್ಟೆ ಹರಾಜಿನಲ್ಲಿ ಗ್ರೇಡ್ A ನಿಂದ C ಗೆ ಇಳಿಕೆ",
        "mr": "बाजार लिलावात ग्रेड A वरून C दर्जा घसरणे"
    },
    "Shriveling and moisture shrinkage": {
        "en": "Shriveling and moisture shrinkage",
        "te": "పంట వాడిపోవడం మరియు ముడతలు పడటం",
        "hi": "सिकुड़ना और नमी की कमी",
        "ta": "சுருங்குதல் மற்றும் ஈரப்பதம் குறைவு",
        "kn": "ಸುಕ್ಕುಗಟ್ಟುವುದು ಮತ್ತು ತೇವಾಂಶ ಇಳಿಕೆ",
        "mr": "सुकणे आणि सुरकुत्या पडणे"
    },
    "Color fading from green to dull reddish": {
        "en": "Color fading from green to dull reddish",
        "te": "రంగు పాలిపోవడం",
        "hi": "रंग फीका पड़ना",
        "ta": "நிறம் மங்குதல்",
        "kn": "ಬಣ್ಣ ಮಸುಕಾಗುವುದು",
        "mr": "रंग फिका पडणे"
    },
    "Stem decay in humid storage": {
        "en": "Stem decay in humid storage",
        "te": "తేమతో కూడిన నిల్వలో తొడిమ కుళ్ళడం",
        "hi": "नमी वाले भंडारण में डंठल सड़ना",
        "ta": "ஈரப்பத சேமிப்பில் தண்டு அழுகுதல்",
        "kn": "ತೇವವಾದ ಶೇಖರಣೆಯಲ್ಲಿ ತೊಟ್ಟು ಕೊಳೆಯುವುದು",
        "mr": "दमट जागेत देठ सडणे"
    },
    "Sprouting if exposed to moisture/humidity": {
        "en": "Sprouting if exposed to moisture/humidity",
        "te": "తేమ తగిలితే మొలకలు రావడం",
        "hi": "नमी लगने पर अंकुरण फूटना",
        "ta": "ஈரப்பதம் பட்டால் முளை கட்டுதல்",
        "kn": "ತೇವಾಂಶ ತಗುಲಿದರೆ ಮೊಳಕೆ ಬರುವುದು",
        "mr": "ओलावा लागल्यास मोड येणे"
    },
    "Black mold if ventilation is restricted": {
        "en": "Black mold if ventilation is restricted",
        "te": "గాలి సరిగా ఆడకపోతే నల్ల బూజు పట్టడం",
        "hi": "हवा न मिलने पर काली फफूंद लगना",
        "ta": "காற்று புகாவிடில் கருப்பு பூஞ்சை உருவாதல்",
        "kn": "ಗಾಳಿ ಆಡದಿದ್ದರೆ ಕಪ್ಪು ಶಿಲೀಂಧ್ರ",
        "mr": "हवा खेळती नसताना काळी बुरशी लागणे"
    },
    "Minor outer skin peeling": {
        "en": "Minor outer skin peeling",
        "te": "పై పొట్టు ఊడిపోవడం",
        "hi": "ऊपरी छिलका निकलना",
        "ta": "மேல் தோல் உரிதல்",
        "kn": "ಮೇಲ್ಭಾಗದ ಸಿಪ್ಪೆ ಸುಲಿಯುವುದು",
        "mr": "वरचे साल सुटणे"
    },
    "Weevil / pest infestation (treat with neem or fumigation)": {
        "en": "Weevil / pest infestation (treat with neem or fumigation)",
        "te": "పురుగులు / ముక్కపురుగుల బెడద (వేప లేదా పొగ వాడండి)",
        "hi": "घुन / कीट लगना (नीम या धूमन का उपयोग करें)",
        "ta": "வண்டு / பூச்சி தாக்குதல் (வேம்பு தெளிக்கவும்)",
        "kn": "ನುಸಿ / ಕೀಟ ಬಾಧೆ (ಬೇವಿನ ಉಪಚಾರ ಮಾಡಿ)",
        "mr": "कीड लागणे (कडुलिंब किंवा धुरीचा वापर करा)"
    },
    "Moisture absorption if bags touch damp floors": {
        "en": "Moisture absorption if bags touch damp floors",
        "te": "తేమ నేల తగిలితే సంచులు తడవడం",
        "hi": "गीले फर्श पर बोरियां रखने से नमी सोखना",
        "ta": "ஈரமான தரையில் பைகள் நனைதல்",
        "kn": "ತೇವ ನೆಲಕ್ಕೆ ಚೀಲಗಳು ತಗುಲಿದರೆ ತೇವಾಂಶ ಹೀರಲ್ಪಡುತ್ತದೆ",
        "mr": "ओल्या जमिनीवर गोणी ठेवल्यास ओलावा पकडणे"
    }
}

CROP_EXPLANATIONS = {
    "tomato": {
        "en": "Tomatoes are highly perishable. Holding beyond 3-5 days leads to rapid softening, skin cracking, and weight loss. Even if the mandi price rises by ₹2/kg, a 15% crop weight and quality loss will result in a net financial deficit. Sell immediately or use cold storage.",
        "te": "టమాటాలు త్వరగా పాడయ్యే పంట. 3-5 రోజుల కంటే ఎక్కువ ఉంచితే మెత్తబడి, పగుళ్లు వచ్చి బరువు తగ్గుతుంది. మార్కెట్ ధర ₹2 పెరిగినా, 15% బరువు మరియు నాణ్యత నష్టం వల్ల నికర నష్టమే మిగులుతుంది. వెంటనే అమ్మడం లేదా కోల్డ్ స్టోరేజ్ ఉపయోగించడం మంచిది.",
        "hi": "टमाटर अत्यधिक संवेदनशील फसल है। 3-5 दिनों से अधिक रोकने पर यह गलने लगता है, छिलका फटता है और वजन घट जाता है। यदि मंडी में दाम ₹2/किग्रा बढ़ भी जाए, तो भी 15% वजन और गुणवत्ता हानि से शुद्ध घाटा ही होगा। तुरंत बेचें या कोल्ड स्टोरेज का उपयोग करें।",
        "ta": "தக்காளி விரைவில் அழுகக்கூடியது. 3-5 நாட்களுக்கு மேல் வைத்திருந்தால் அழுகி எடை குறையும். சந்தை விலை ₹2 கூடினாலும், 15% எடை இழப்பால் நஷ்டமே ஏற்படும். உடனே விற்கவும் அல்லது குளிர்சாதன கிடங்கைப் பயன்படுத்தவும்.",
        "kn": "ಟೊಮ್ಯಾಟೊ ಬೇಗನೆ ಹಾಳಾಗುವ ಬೆಳೆ. 3-5 ದಿನಗಳಿಗಿಂತ ಹೆಚ್ಚು ಇಟ್ಟರೆ ಮೆತ್ತಗಾಗಿ ತೂಕ ಕಡಿಮೆಯಾಗುತ್ತದೆ. ಮಾರುಕಟ್ಟೆ ದರ ₹2 ಹೆಚ್ಚಾದರೂ, ಶೇ.15 ರಷ್ಟು ತೂಕ ಮತ್ತು ಗುಣಮಟ್ಟ ನಷ್ಟದಿಂದ ನಿವ್ವಳ ನಷ್ಟವೇ ಆಗುತ್ತದೆ. ತಕ್ಷಣ ಮಾರಾಟ ಮಾಡಿ ಅಥವಾ ಕೋಲ್ಡ್ ಸ್ಟೋರೇಜ್ ಬಳಸಿ.",
        "mr": "टोमॅटो हे अत्यंत नाशवंत पीक आहे. 3-5 दिवसांपेक्षा जास्त साठवल्यास टोमॅटो मऊ पडतो आणि वजन घटते. बाजारात भाव ₹2 वाढला तरी 15% वजनातील घटीमुळे तोटाच होईल. त्वरित विक्री करा किंवा कोल्ड स्टोरेज वापरा."
    },
    "chilli": {
        "en": "Fresh green chillies lose shine, moisture, and crispness quickly at ambient temperatures. Over-ripening turns them red and lowers mandi commercial grading. Minor price rises rarely compensate for shriveling weight loss.",
        "te": "పచ్చిమిర్చి నిల్వలో మెరుపు, తేమ మరియు గట్టిదనాన్ని త్వరగా కోల్పోతుంది. ఎక్కువ రోజులు ఉంచితే ఎర్రబడి గ్రేడ్ తగ్గుతుంది. చిన్నపాటి ధర పెరుగుదల బరువు నష్టాన్ని పూడ్చలేదు. 3-4 రోజుల్లో అమ్మండి.",
        "hi": "हरी मिर्च अपनी चमक और ताजगी जल्दी खो देती है। ज्यादा देर रखने पर लाल हो जाती है जिससे मंडी में कम दाम मिलता है। 3-4 दिनों में बेचें।",
        "ta": "பச்சை மிளகாய் விரைவில் ஈரப்பதத்தை இழக்கும். அதிக நாட்கள் வைத்தால் பழுத்து தரம் குறையும். 3-4 நாட்களுக்குள் விற்றுவிடுங்கள்.",
        "kn": "ಹಸಿಮೆಣಸಿನಕಾಯಿ ಬೇಗನೆ ತಾಜಾತನ ಮತ್ತು ತೇವಾಂಶವನ್ನು ಕಳೆದುಕೊಳ್ಳುತ್ತದೆ. ಹೆಚ್ಚು ದಿನ ಇಟ್ಟರೆ ಕೆಂಪಾಗಿ ದರ ಕಡಿಮೆಯಾಗುತ್ತದೆ. 3-4 ದಿನಗಳಲ್ಲಿ ಮಾರಿ.",
        "mr": "हिरवी मिरची लवकर सुकते आणि चमक गमावते. जास्त वेळ ठेवल्यास लाल होते आणि भाव कमी मिळतो. 3-4 दिवसांत विक्री करा."
    },
    "onion": {
        "en": "Well-cured onions store well in dry, ventilated storage. If market predictions project an upward trend, waiting 3-7 days poses minimal physical damage risk and can yield higher net profit. Keep away from dampness to prevent premature sprouting.",
        "te": "ఉల్లిపాయలు పొడి, గాలి ఆడే ప్రదేశంలో బాగా నిల్వ ఉంటాయి. మార్కెట్ ధరలు పెరిగే అవకాశం ఉంటే 3-7 రోజులు ఆగడం వల్ల భౌతిక నష్టం తక్కువగా ఉండి మంచి లాభం పొందవచ్చు. తడి తగలకుండా చూసుకోండి.",
        "hi": "सूखे और हवादार स्थान पर प्याज अच्छी तरह टिकता है। यदि बाजार भाव बढ़ने का अनुमान है, तो 3-7 दिन रुकना सुरक्षित है और अच्छा मुनाफा दे सकता है।",
        "ta": "வெங்காயம் உலர்ந்த காத்தோட்டமான இடத்தில் நன்றாக இருக்கும். விலை உயரும் வாய்ப்பு இருந்தால் 3-7 நாட்கள் காத்திருப்பது நல்ல லாபம் தரும்.",
        "kn": "ಈರುಳ್ಳಿ ಒಣ ಮತ್ತು ಗಾಳಿಯಾಡುವ ಸ್ಥಳದಲ್ಲಿ ಚೆನ್ನಾಗಿ ಬಾಳಿಕೆ ಬರುತ್ತದೆ. ದರ ಹೆಚ್ಚಾಗುವ ಸೂಚನೆ ಇದ್ದರೆ 3-7 ದಿನ ಕಾಯುವುದು ಸೂಕ್ತ.",
        "mr": "कांदा कोरड्या आणि हवेशीर जागी चांगला टिकतो. भाव वाढण्याचे संकेत असल्यास 3-7 दिवस थांबणे फायदेशीर ठरेल."
    },
    "rice": {
        "en": "Dry paddy and milled rice do not spoil quickly. Farmers have the financial leverage to hold stock for peak off-season market rates. Zero risk of rot in standard warehouse storage. Holding for higher prices directly maximizes profit.",
        "te": "వరి ధాన్యం త్వరగా పాడవదు. గోదాముల్లో సురక్షితంగా నిల్వ చేసి, మార్కెట్ గరిష్ట ధరలు ఉన్న సమయంలో అమ్ముకోవచ్చు. ఓపికగా మంచి ధరకు అమ్మితే అధిక లాభం వస్తుంది.",
        "hi": "धान और चावल जल्दी खराब नहीं होते। गोदाम में सुरक्षित रखकर ऑफ-सीजन में उच्चतम दरों पर बेचा जा सकता है। धैर्यपूर्वक बेचने से अधिकतम लाभ मिलेगा।",
        "ta": "நெல் தானியம் எளிதில் கெட்டுப்போகாது. சேமிப்புக் கிடங்கில் வைத்து உச்ச விலைக்கு விற்கலாம். பொறுமையாக விற்றால் அதிக லாபம்.",
        "kn": "ಭತ್ತ ಮತ್ತು ಅಕ್ಕಿ ಬೇಗನೆ ಹಾಳಾಗುವುದಿಲ್ಲ. ಗೋದಾಮಿನಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿಟ್ಟು ಗರಿಷ್ಠ ದರ ಬಂದಾಗ ಮಾರಾಟ ಮಾಡಬಹುದು.",
        "mr": "धान्य आणि तांदूळ लवकर खराब होत नाही. गोदामात साठवून योग्य भाव आल्यावर विकल्यास भरपूर नफा मिळतो."
    },
    "cotton": {
        "en": "Raw seed cotton can be safely stored in covered sheds. Waiting for global or regional price spikes is safe if kept dry and clean. Zero spoilage risk in dry covered areas.",
        "te": "పత్తిని షెడ్లలో సురక్షితంగా నిల్వ చేయవచ్చు. ధరలు పెరిగే వరకు నిరీక్షించడం ద్వారా మంచి లాభం పొందవచ్చు. తడి తగలకుండా జాగ్రత్త పడండి.",
        "hi": "कपास को ढके हुए शेड में सुरक्षित रखा जा सकता है। बेहतर भाव मिलने तक इंतजार करना सुरक्षित और लाभदायक है।",
        "ta": "பருத்தியை மூடிய கொட்டகையில் பாதுகாக்கலாம். நல்ல விலை வரும் வரை காத்திருப்பது பாதுகாப்பானது மற்றும் லாபகரமானது.",
        "kn": "ಹತ್ತಿಯನ್ನು ಸುರಕ್ಷಿತ ಶೆಡ್‌ನಲ್ಲಿ ಶೇಖರಿಸಿಡಬಹುದು. ಮಾರುಕಟ್ಟೆ ದರ ಹೆಚ್ಚಾಗುವವರೆಗೆ ಕಾಯುವುದು ಲಾಭದಾಯಕ.",
        "mr": "कापूस शेडमध्ये सुरक्षित ठेवता येतो. चांगला भाव येईपर्यंत थांबणे फायदेशीर ठरेल."
    },
    "maize": {
        "en": "Dried maize grain stores well in aerated bags. Monitor poultry demand and regional feeds before selling. Safe to hold for favorable market pricing.",
        "te": "మొక్కజొన్న గింజలను ఎండబెట్టి నిల్వ చేస్తే పాడవదు. పౌల్ట్రీ మరియు దాణా మార్కెట్లలో డిమాండ్ చూసి సరైన ధరకు విక్రయించండి.",
        "hi": "मक्का के दानों को सुखाकर रखने पर खराब नहीं होता। अच्छी मांग और भाव देखकर बेचें।",
        "ta": "மக்காச்சோளம் நன்கு காயவைத்து சேமித்தால் கெடாது. நல்ல விலை பார்த்து விற்கலாம்.",
        "kn": "ಮೆಕ್ಕೆಜೋಳವನ್ನು ಒಣಗಿಸಿಟ್ಟರೆ ಹಾಳಾಗುವುದಿಲ್ಲ. ಉತ್ತಮ ಬೇಡಿಕೆ ಇರುವಾಗ ಮಾರಾಟ ಮಾಡಿ.",
        "mr": "मका चांगला वाळवून साठवल्यास टिकतो. बाजारात चांगली मागणी असताना विक्री करावी."
    }
}


def format_weather_condition(cond: str, lang: str = "en") -> str:
    if not cond or lang == "en":
        return cond
    for k, v in WEATHER_CONDITIONS.items():
        if k.lower() in cond.lower() or cond.lower() in k.lower():
            return v.get(lang, cond)
    return cond


def format_weather_alert(alert: str, lang: str = "en") -> str:
    if not alert or lang == "en":
        return alert
    for k, v in WEATHER_ALERTS.items():
        if k.lower() in alert.lower() or alert.lower() in k.lower():
            return v.get(lang, alert)
    return alert


def format_transit_advice(advice: str, lang: str = "en") -> str:
    if not advice or lang == "en":
        return advice
    for k, v in TRANSIT_ADVICES.items():
        if k.lower() in advice.lower() or advice.lower() in k.lower():
            return v.get(lang, advice)
    return advice


def format_shelf_life(shelf_life: str, lang: str = "en") -> str:
    if not shelf_life or lang == "en":
        return shelf_life
    for k, v in SHELF_LIFE_MAP.items():
        if k.lower() in shelf_life.lower() or shelf_life.lower() in k.lower():
            return v.get(lang, shelf_life)
    return shelf_life


def format_perishability(perish: str, lang: str = "en") -> str:
    if not perish or lang == "en":
        return perish
    for k, v in PERISHABILITY_MAP.items():
        if k.lower() in perish.lower() or perish.lower() in k.lower():
            return v.get(lang, perish)
    return perish


def format_damage_risk(risk: str, lang: str = "en") -> str:
    if not risk or lang == "en":
        return risk
    for k, v in DAMAGE_RISK_MAP.items():
        if k.lower() in risk.lower() or risk.lower() in k.lower():
            return v.get(lang, risk)
    return risk


def format_spoilage_rate(rate: str, lang: str = "en") -> str:
    if not rate or lang == "en":
        return rate
    for k, v in SPOILAGE_RATE_MAP.items():
        if k.lower() in rate.lower() or rate.lower() in k.lower():
            return v.get(lang, rate)
    return rate


def format_holding_verdict(verdict: str, lang: str = "en") -> str:
    if not verdict or lang == "en":
        return verdict
    for k, v in HOLDING_VERDICT_MAP.items():
        if k.lower() in verdict.lower() or verdict.lower() in k.lower():
            return v.get(lang, verdict)
    return verdict


def format_crop_explanation(crop: str, lang: str = "en", default: str = "") -> str:
    crop_lower = crop.lower().strip() if crop else ""
    if crop_lower in CROP_EXPLANATIONS:
        return CROP_EXPLANATIONS[crop_lower].get(lang, default or CROP_EXPLANATIONS[crop_lower].get("en", default))
    return default


def format_damage_factors(factors: list, lang: str = "en") -> list:
    if not factors or lang == "en":
        return factors
    translated = []
    for f in factors:
        found = False
        for k, v in DAMAGE_FACTORS_MAP.items():
            if k.lower() in f.lower() or f.lower() in k.lower():
                translated.append(v.get(lang, f))
                found = True
                break
        if not found:
            translated.append(f)
    return translated


def get_localized_recommendation(
    crop: str,
    quantity: float,
    best_market: str,
    best_location: str,
    best_distance: float,
    best_price: float,
    predicted_price: float,
    decision: str,
    lang: str = "en"
) -> str:
    diff = abs(predicted_price - best_price)
    disp_crop = format_crop(crop, lang)
    is_rise = predicted_price > best_price
    is_fall = predicted_price < best_price

    if lang == "te":
        if decision == "SELL NOW":
            if is_fall:
                trend_msg = f"(ధర ₹{diff:.2f}/కిలో తగ్గే అవకాశం ఉంది)"
            elif is_rise:
                trend_msg = f"(స్వల్పంగా ₹{diff:.2f}/కిలో పెరిగే అవకాశం ఉన్నప్పటికీ, నిల్వ నష్టాల దృష్ట్యా ఇప్పుడే అమ్మడం మంచిది)"
            else:
                trend_msg = "(ధర స్థిరంగా ఉండే అవకాశం ఉంది)"
            return (
                f"{quantity:g} కిలోల {disp_crop} కోసం సిఫార్సు చేసిన మార్కెట్ {best_market} ({best_location}), "
                f"సుమారు {best_distance:.1f} కి.మీ దూరం. ప్రస్తుత ధర ₹{best_price:.2f}/కిలో. "
                f"3 రోజుల తర్వాత అంచనా ధర ₹{predicted_price:.2f}/కిలో {trend_msg}. "
                f"కాబట్టి గరిష్ట రాబడి కోసం ఇప్పుడే విక్రయించడం ప్రయోజనకరం."
            )
        elif decision == "WAIT":
            return (
                f"{quantity:g} కిలోల {disp_crop} కోసం సిఫార్సు చేసిన మార్కెట్ {best_market} ({best_location}), "
                f"సుమారు {best_distance:.1f} కి.మీ దూరం. ప్రస్తుత ధర ₹{best_price:.2f}/కిలో. "
                f"3 రోజుల తర్వాత అంచనా ధర ₹{predicted_price:.2f}/కిలో (ధర ₹{diff:.2f}/కిలో పెరిగే అవకాశం ఉంది). "
                f"మీ వద్ద సురక్షిత నిల్వ సదుపాయం ఉంటే మెరుగైన ధర కోసం వేచి ఉండవచ్చు."
            )
        else:
            return (
                f"{quantity:g} కిలోల {disp_crop} కోసం సిఫార్సు చేసిన మార్కెట్ {best_market} ({best_location}). "
                f"ప్రస్తుత ధర ₹{best_price:.2f}/కిలో మరియు 3 రోజుల అంచనా ధర ₹{predicted_price:.2f}/కిలో. "
                f"ధరలో పెద్ద మార్పు లేదు. నిల్వ ఖర్చులు, నిల్వ సామర్థ్యం మరియు అత్యవసరతను బట్టి అమ్మకం నిర్ణయం తీసుకోండి."
            )
    elif lang == "hi":
        if decision == "SELL NOW":
            if is_fall:
                trend_msg = f"(भाव ₹{diff:.2f}/किग्रा घटने की संभावना है)"
            elif is_rise:
                trend_msg = f"(भाव ₹{diff:.2f}/किग्रा बढ़ने की संभावना के बावजूद, रख-रखाव जोखिमों के कारण अभी बेचना अधिक सुरक्षित है)"
            else:
                trend_msg = "(भाव स्थिर रहने का अनुमान है)"
            return (
                f"{quantity:g} किग्रा {disp_crop} के लिए अनुशंसित मंडी {best_market} ({best_location}) है, "
                f"लगभग {best_distance:.1f} किमी दूर। वर्तमान भाव ₹{best_price:.2f}/किग्रा है। "
                f"3 दिन बाद अनुमानित भाव ₹{predicted_price:.2f}/किग्रा है {trend_msg}। "
                f"इसलिए बेहतर लाभ के लिए अभी बेचना सबसे उपयुक्त रहेगा।"
            )
        elif decision == "WAIT":
            return (
                f"{quantity:g} किग्रा {disp_crop} के लिए अनुशंसित मंडी {best_market} ({best_location}) है, "
                f"लगभग {best_distance:.1f} किमी दूर। वर्तमान भाव ₹{best_price:.2f}/किग्रा है। "
                f"3 दिन बाद अनुमानित भाव ₹{predicted_price:.2f}/किग्रा है (भाव ₹{diff:.2f}/किग्रा बढ़ने की उम्मीद है)। "
                f"यदि आपके पास सुरक्षित भंडारण है तो बेहतर मूल्य के लिए प्रतीक्षा कर सकते हैं।"
            )
        else:
            return (
                f"{quantity:g} किग्रा {disp_crop} के लिए अनुशंसित मंडी {best_market} ({best_location}) है। "
                f"वर्तमान भाव ₹{best_price:.2f}/किग्रा और 3 दिन बाद अनुमानित भाव ₹{predicted_price:.2f}/किग्रा है। "
                f"भाव में मामूली अंतर है। भंडारण सुविधा और अपनी जरूरत के अनुसार निर्णय लें।"
            )
    elif lang == "ta":
        if decision == "SELL NOW":
            if is_fall:
                trend_msg = f"(விலை ₹{diff:.2f}/கிலோ குறைய வாய்ப்புள்ளது)"
            elif is_rise:
                trend_msg = f"(விலை ₹{diff:.2f}/கிலோ உயர வாய்ப்பிருந்தாலும் சேமிப்பு அபாயங்களால் இப்போதே விற்பது நல்லது)"
            else:
                trend_msg = "(விலை சீராக இருக்கும்)"
            return (
                f"{quantity:g} கிலோ {disp_crop} பயிருக்கு பரிந்துரைக்கப்பட்ட சந்தை {best_market} ({best_location}), "
                f"சுமார் {best_distance:.1f} கி.மீ தொலைவில் உள்ளது. தற்போதைய விலை ₹{best_price:.2f}/கிலோ. "
                f"3 நாட்களுக்குப் பிறகு கணிக்கப்பட்ட விலை ₹{predicted_price:.2f}/கிலோ {trend_msg}. "
                f"எனவே அதிக லாபம் பெற இப்போதே விற்பது நல்லது."
            )
        elif decision == "WAIT":
            return (
                f"{quantity:g} கிலோ {disp_crop} பயிருக்கு பரிந்துரைக்கப்பட்ட சந்தை {best_market} ({best_location}), "
                f"சுமார் {best_distance:.1f} கி.மீ தொலைவில் உள்ளது. தற்போதைய விலை ₹{best_price:.2f}/கிலோ. "
                f"3 நாட்களுக்குப் பிறகு கணிக்கப்பட்ட விலை ₹{predicted_price:.2f}/கிலோ (விலை ₹{diff:.2f}/கிலோ அதிகரிக்க வாய்ப்புள்ளது). "
                f"பாதுகாப்பான சேமிப்பு இருந்தால் காத்திருக்கலாம்."
            )
        else:
            return (
                f"{quantity:g} கிலோ {disp_crop} பயிருக்கு பரிந்துரைக்கப்பட்ட சந்தை {best_market} ({best_location}). "
                f"தற்போதைய விலை ₹{best_price:.2f}/கிலோ, கணிக்கப்பட்ட விலை ₹{predicted_price:.2f}/கிலோ. "
                f"விலை மாற்றம் குறைவு. சேமிப்பு வசதி மற்றும் தேவையை பொறுத்து முடிவு செய்யவும்."
            )
    elif lang == "kn":
        if decision == "SELL NOW":
            if is_fall:
                trend_msg = f"(ದರ ₹{diff:.2f}/ಕೆಜಿ ಇಳಿಕೆಯಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ)"
            elif is_rise:
                trend_msg = f"(ದರ ₹{diff:.2f}/ಕೆಜಿ ಏರಿಕೆಯಾಗುವ ಸಾಧ್ಯತೆಯಿದ್ದರೂ ಶೇಖರಣಾ ಅಪಾಯ ತಪ್ಪಿಸಲು ಈಗಲೇ ಮಾರಾಟ ಸೂಕ್ತ)"
            else:
                trend_msg = "(ದರ ಸ್ಥಿರವಾಗಿರಲಿದೆ)"
            return (
                f"{quantity:g} ಕೆಜಿ {disp_crop} ಗಾಗಿ ಶಿಫಾರಸು ಮಾಡಿದ ಮಾರುಕಟ್ಟೆ {best_market} ({best_location}), "
                f"ಸುಮಾರು {best_distance:.1f} ಕಿ.ಮೀ ದೂರದಲ್ಲಿದೆ. ಪ್ರಸ್ತುತ ದರ ₹{best_price:.2f}/ಕೆಜಿ. "
                f"3 ದಿನಗಳ ನಂತರ ಅಂದಾಜು ದರ ₹{predicted_price:.2f}/ಕೆಜಿ {trend_msg}. "
                f"ಆದ್ದರಿಂದ ಗರಿಷ್ಠ ಲಾಭಕ್ಕಾಗಿ ಈಗಲೇ ಮಾರಾಟ ಮಾಡುವುದು ಸೂಕ್ತ."
            )
        elif decision == "WAIT":
            return (
                f"{quantity:g} ಕೆಜಿ {disp_crop} ಗಾಗಿ ಶಿಫಾರಸು ಮಾಡಿದ ಮಾರುಕಟ್ಟೆ {best_market} ({best_location}), "
                f"ಸುಮಾರು {best_distance:.1f} ಕಿ.ಮೀ ದೂರದಲ್ಲಿದೆ. ಪ್ರಸ್ತುತ ದರ ₹{best_price:.2f}/ಕೆಜಿ. "
                f"3 ದಿನಗಳ ನಂತರ ಅಂದಾಜು ದರ ₹{predicted_price:.2f}/ಕೆಜಿ (ದರ ₹{diff:.2f}/ಕೆಜಿ ಹೆಚ್ಚಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ). "
                f"ಸುರಕ್ಷಿತ ಶೇಖರಣಾ ಸೌಲಭ್ಯವಿದ್ದರೆ ಕಾಯುವುದು ಲಾಭದಾಯಕ."
            )
        else:
            return (
                f"{quantity:g} ಕೆಜಿ {disp_crop} ಗಾಗಿ ಶಿಫಾರಸು ಮಾಡಿದ ಮಾರುಕಟ್ಟೆ {best_market} ({best_location}). "
                f"ಪ್ರಸ್ತುತ ದರ ₹{best_price:.2f}/ಕೆಜಿ, ಅಂದಾಜು ದರ ₹{predicted_price:.2f}/ಕೆಜಿ. "
                f"ದರದಲ್ಲಿ ಹೆಚ್ಚಿನ ವ್ಯತ್ಯಾಸವಿಲ್ಲ. ಶೇಖರಣಾ ವೆಚ್ಚ ಹಾಗೂ ಅಗತ್ಯಕ್ಕೆ ತಕ್ಕಂತೆ ನಿರ್ಧಾರ ಕೈಗೊಳ್ಳಿ."
            )
    elif lang == "mr":
        if decision == "SELL NOW":
            if is_fall:
                trend_msg = f"(किंमत ₹{diff:.2f}/किलो कमी होण्याची शक्यता)"
            elif is_rise:
                trend_msg = f"(किंमत ₹{diff:.2f}/किलो वाढण्याची शक्यता असली तरी साठवणूक जोखीम टाळण्यासाठी आत्ताच विक्री योग्य)"
            else:
                trend_msg = "(किंमत स्थिर राहण्याची शक्यता)"
            return (
                f"{quantity:g} किलो {disp_crop} साठी शिफारस केलेली बाजारपेठ {best_market} ({best_location}) आहे, "
                f"अंदाजे {best_distance:.1f} किमी अंतरावर. सध्याचा दर ₹{best_price:.2f}/किलो आहे. "
                f"3 दिवसांनंतरचा अंदाजित दर ₹{predicted_price:.2f}/किलो आहे {trend_msg}. "
                f"म्हणून चांगल्या परताव्यासाठी आत्ताच विक्री करणे योग्य ठरेल."
            )
        elif decision == "WAIT":
            return (
                f"{quantity:g} किलो {disp_crop} साठी शिफारस केलेली बाजारपेठ {best_market} ({best_location}) आहे, "
                f"अंदाजे {best_distance:.1f} किमी अंतरावर. सध्याचा दर ₹{best_price:.2f}/किलो आहे. "
                f"3 दिवसांनंतरचा अंदाजित दर ₹{predicted_price:.2f}/किलो आहे (किंमत ₹{diff:.2f}/किलो वाढण्याची शक्यता). "
                f"सुरक्षित साठवणूक असल्यास चांगल्या भावासाठी वाट पाहणे फायदेशीर ठरेल."
            )
        else:
            return (
                f"{quantity:g} किलो {disp_crop} साठी शिफारस केलेली बाजारपेठ {best_market} ({best_location}) आहे. "
                f"सध्याचा दर ₹{best_price:.2f}/किलो आणि 3 दिवसांचा अंदाज ₹{predicted_price:.2f}/किलो आहे. "
                f"भावात जास्त फरक नाही. साठवणूक खर्च व गरजेनुसार निर्णय घ्यावा."
            )
    else:
        if decision == "SELL NOW":
            if is_fall:
                trend_msg = f"The model expects the price to decrease by ₹{diff:.2f}/kg."
            elif is_rise:
                trend_msg = f"Although the price may slightly increase by ₹{diff:.2f}/kg, post-harvest holding risks and immediate cash realization make selling now the recommended choice."
            else:
                trend_msg = "The model expects the price to remain stable."
            return (
                f"For {quantity:g} kg of {crop}, the recommended market is {best_market}, "
                f"located in {best_location}, approximately {best_distance:.1f} km away, "
                f"with a current price of ₹{best_price:.2f}/kg. "
                f"The predicted price after 3 days is ₹{predicted_price:.2f}/kg. "
                f"{trend_msg} "
                f"Therefore, selling now may help maximize current returns."
            )
        elif decision == "WAIT":
            return (
                f"For {quantity:g} kg of {crop}, the recommended market is {best_market}, "
                f"located in {best_location}, approximately {best_distance:.1f} km away, "
                f"with a current price of ₹{best_price:.2f}/kg. "
                f"The predicted price after 3 days is ₹{predicted_price:.2f}/kg. "
                f"The model expects the price to increase by ₹{diff:.2f}/kg. "
                f"Therefore, waiting may provide a better selling price."
            )
        else:
            return (
                f"For {quantity:g} kg of {crop}, the recommended market is {best_market}, "
                f"located in {best_location}, approximately {best_distance:.1f} km away, "
                f"with a current price of ₹{best_price:.2f}/kg. "
                f"The predicted price after 3 days is ₹{predicted_price:.2f}/kg. "
                f"The expected price change is small. "
                f"Consider selling based on storage costs, urgency, and local market conditions."
            )


def get_localized_farmer_advice(
    crop: str,
    location: str,
    quantity: float,
    quality: str,
    best_market: str,
    best_market_location: str,
    best_market_distance: float,
    current_price: float,
    predicted_price: float,
    decision: str,
    lang: str = "en"
) -> str:
    disp_crop = format_crop(crop, lang)
    disp_qual = format_quality(quality, lang)
    
    price_diff = predicted_price - current_price
    pct_change = (price_diff / current_price * 100) if current_price > 0 else 0
    current_rev = quantity * current_price
    predicted_rev = quantity * predicted_price
    rev_diff = predicted_rev - current_rev

    if lang == "te":
        if decision == "SELL NOW":
            action_text = f"మీ {disp_crop} పంటను ఇప్పుడే {best_market} మార్కెట్‌లో విక్రయించండి. ప్రస్తుత ధర ₹{current_price:.2f}/కిలో ఆకర్షణీయంగా ఉంది."
            why_text = f"3 రోజుల తర్వాత అంచనా ధర ₹{predicted_price:.2f}/కిలో (ధర తగ్గే సూచన ఉంది), కాబట్టి వేచి ఉండటం వలన ఎలాంటి ప్రయోజనం ఉండకపోవచ్చు."
            dec_text = "ఇప్పుడే అమ్మండి (SELL NOW)"
        elif decision == "WAIT":
            action_text = f"మీ వద్ద సురక్షిత నిల్వ సదుపాయం ఉంటే, మీ {disp_crop} పంటను విక్రయించేందుకు కొన్ని రోజులు వేచి చూడటం మంచిది."
            why_text = f"మార్కెట్ అంచనా ప్రకారం ధర సుమారు {pct_change:.1f}% పెరిగి ₹{predicted_price:.2f}/కిలోకు చేరే అవకాశం ఉంది."
            dec_text = "వేచి ఉండండి (WAIT)"
        else:
            action_text = "అంతిమ అమ్మకం నిర్ణయం తీసుకునే ముందు స్థానిక మార్కెట్ డిమాండ్‌ను గమనించండి."
            why_text = "రాబోయే రోజుల్లో ఆశించిన ధర మార్పు చాలా స్వల్పంగా ఉంది."
            dec_text = "పరిశీలించండి (MONITOR)"

        if quality == "Grade A":
            qual_text = "మీ గ్రేడ్ A నాణ్యమైన పంటకు నాణ్యతను కోరుకునే కొనుగోలుదారుల నుండి ఉత్తమ ధర లభిస్తుంది."
        elif quality == "Grade B":
            qual_text = "విక్రయించే ముందు సమీపంలోని పలు మార్కెట్ల ధరలను సరిపోల్చుకోండి."
        else:
            qual_text = "గ్రేడ్ C పంట నాణ్యత మరింత తగ్గకముందే త్వరగా విక్రయించడం మంచిది."

        return f"""🌾 రైతు సలహాదారు (AI FARMER ADVISOR)
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 పంట: {disp_crop}
📍 రైతు ప్రాంతం: {location}
🏪 సిఫార్సు చేసిన మార్కెట్: {best_market} ({best_market_location})
🚚 మార్కెట్ రహదారి దూరం: {best_market_distance:.1f} కి.మీ (రహదారి)
⚖️ పరిమాణం: {quantity:g} కిలోలు
⭐ పంట నాణ్యత: {disp_qual}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 ప్రస్తుత మార్కెట్ ధర: ₹{current_price:.2f}/కిలో
🔮 అంచనా ధర (3 రోజులు): ₹{predicted_price:.2f}/కిలో
📈 ఆశించిన ధర మార్పు: {pct_change:+.1f}%
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AI అమ్మకం నిర్ణయం: {dec_text}
💡 సిఫార్సు: {action_text}
📊 కారణం / విశ్లేషణ: {why_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 రాబడి అంచనా:
• ఇప్పుడే అమ్మితే: ₹{current_rev:,.2f}
• అంచనా ధరకు అమ్మితే: ₹{predicted_rev:,.2f}
• ఆశించిన తేడా: ₹{rev_diff:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ నాణ్యత నిర్వహణ సలహా:
{qual_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
🚚 రవాణా సూచన:
సిఫార్సు చేసిన మార్కెట్ రహదారి దూరం: {best_market_distance:.1f} కి.మీ. దగ్గరి మార్కెట్లను ఎంచుకోవడం వల్ల రవాణా సమయం మరియు రవాణా ఖర్చులు తగ్గుతాయి.
━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ ముఖ్య గమనిక:
ధరల అంచనాలు అందుబాటులో ఉన్న మార్కెట్ డేటా ఆధారంగా లెక్కించబడ్డాయి. మార్కెట్ డిమాండ్, సరఫరా, వాతావరణం మరియు ఇతర కారణాల వల్ల వాస్తవ ధరలు మారవచ్చు."""

    elif lang == "hi":
        if decision == "SELL NOW":
            action_text = f"अपनी {disp_crop} की फसल अभी {best_market} मंडी में बेचें। वर्तमान मूल्य ₹{current_price:.2f}/किग्रा आकर्षक है।"
            why_text = f"3 दिनों के बाद अनुमानित मूल्य ₹{predicted_price:.2f}/किग्रा है, इसलिए रुकने से लाभ की संभावना कम है।"
            dec_text = "अभी बेचें (SELL NOW)"
        elif decision == "WAIT":
            action_text = f"यदि सुरक्षित भंडारण उपलब्ध है, तो {disp_crop} बेचने के लिए कुछ दिन प्रतीक्षा करने पर विचार करें।"
            why_text = f"अनुमान है कि मूल्य {pct_change:.1f}% बढ़कर लगभग ₹{predicted_price:.2f}/किग्रा तक पहुंच सकता है।"
            dec_text = "प्रतीक्षा करें (WAIT)"
        else:
            action_text = "अंतिम निर्णय लेने से पहले मंडी के रुख और मांग पर नजर रखें।"
            why_text = "मूल्य में अपेक्षित परिवर्तन काफी कम है।"
            dec_text = "निगरानी करें (MONITOR)"

        if quality == "Grade A":
            qual_text = "आपकी ग्रेड A उपज गुणवत्ता-पसंद खरीदारों से बेहतर भाव दिला सकती है।"
        elif quality == "Grade B":
            qual_text = "बेचने से पहले आसपास की कई मंडियों के भावों की तुलना करें।"
        else:
            qual_text = "ग्रेड C उपज की गुणवत्ता और न गिरे, इसके लिए जल्दी बेचना बेहतर है।"

        return f"""🌾 किसान सलाहकार (AI FARMER ADVISOR)
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 फसल: {disp_crop}
📍 किसान का स्थान: {location}
🏪 अनुशंसित मंडी: {best_market} ({best_market_location})
🚚 मंडी की सड़क दूरी: {best_market_distance:.1f} किमी (सड़क मार्ग)
⚖️ मात्रा: {quantity:g} किग्रा
⭐ फसल गुणवत्ता: {disp_qual}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 वर्तमान मंडी भाव: ₹{current_price:.2f}/किग्रा
🔮 अनुमानित भाव (3 दिन): ₹{predicted_price:.2f}/किग्रा
📈 अपेक्षित मूल्य परिवर्तन: {pct_change:+.1f}%
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AI बिक्री निर्णय: {dec_text}
💡 सलाह: {action_text}
📊 कारण / विश्लेषण: {why_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 आय का अनुमान:
• अभी बेचने पर: ₹{current_rev:,.2f}
• अनुमानित भाव पर: ₹{predicted_rev:,.2f}
• अनुमानित अंतर: ₹{rev_diff:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ गुणवत्ता सलाह:
{qual_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
🚚 परिवहन मार्गदर्शन:
अनुशंसित मंडी की दूरी: {best_market_distance:.1f} किमी। नजदीकी मंडी चुनने से यात्रा का समय और भाड़ा बचता है।
━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ महत्वपूर्ण सूचना:
मूल्य पूर्वानुमान उपलब्ध मंडी आंकड़ों पर आधारित अनुमान हैं। वास्तविक भाव मांग, आपूर्ति और मौसम के अनुसार बदल सकते हैं।"""

    elif lang == "ta":
        if decision == "SELL NOW":
            action_text = f"உங்கள் {disp_crop} பயிரை இப்போதே {best_market} சந்தையில் விற்கவும். தற்போதைய விலை ₹{current_price:.2f}/கிலோ சிறந்தது."
            why_text = f"3 நாட்களுக்குப் பிறகு கணிக்கப்பட்ட விலை ₹{predicted_price:.2f}/கிலோ. காத்திருப்பது பெரிய பலனைத் தராது."
            dec_text = "இப்போதே விற்கவும் (SELL NOW)"
        elif decision == "WAIT":
            action_text = f"பாதுகாப்பான சேமிப்பு இருந்தால், {disp_crop} விற்க சில நாட்கள் காத்திருக்கலாம்."
            why_text = f"விலை {pct_change:.1f}% அதிகரித்து ₹{predicted_price:.2f}/கிலோ ஆக வாய்ப்புள்ளது."
            dec_text = "காத்திருக்கவும் (WAIT)"
        else:
            action_text = "விற்பனைக்கு முன் சந்தை நிலவரத்தை கண்காணிக்கவும்."
            why_text = "விலை மாற்றம் குறைவாக உள்ளது."
            dec_text = "கண்காணிக்கவும் (MONITOR)"

        qual_text = "Grade A தரத்திற்கு நல்ல விலை கிடைக்கும்." if quality == "Grade A" else "அருகிலுள்ள சந்தைகளை ஒப்பிடவும்."

        return f"""🌾 உழவர் ஆலோசகர் (AI FARMER ADVISOR)
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 பயிர்: {disp_crop}
📍 இடம்: {location}
🏪 சந்தை: {best_market} ({best_market_location})
🚚 தூரம்: {best_market_distance:.1f} கி.மீ
⚖️ அளவு: {quantity:g} கிலோ
⭐ தரம்: {disp_qual}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 தற்போதைய விலை: ₹{current_price:.2f}/கிலோ
🔮 கணிக்கப்பட்ட விலை: ₹{predicted_price:.2f}/கிலோ
📈 விலை மாற்றம்: {pct_change:+.1f}%
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AI விற்பனை முடிவு: {dec_text}
💡 பரிந்துரை: {action_text}
📊 காரணம்: {why_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 வருமான மதிப்பீடு:
• இப்போது விற்றால்: ₹{current_rev:,.2f}
• கணிக்கப்பட்ட விலையில்: ₹{predicted_rev:,.2f}
• எதிர்பார்க்கப்படும் வித்தியாசம்: ₹{rev_diff:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ தர ஆலோசனை:
{qual_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
🚚 போக்குவரத்து தகவல்:
சந்தை தூரம்: {best_market_distance:.1f} கி.மீ. அருகிலுள்ள சந்தைகள் போக்குவரத்து செலவைக் குறைக்கும்.
━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ முக்கிய அறிவிப்பு:
விலை கணிப்புகள் மதிப்பீடுகள் மட்டுமே. சந்தை தேவைக்கு ஏற்ப மாறக்கூடும்."""

    elif lang == "kn":
        if decision == "SELL NOW":
            action_text = f"ನಿಮ್ಮ {disp_crop} ಬೆಳೆಯನ್ನು ಈಗಲೇ {best_market} ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ. ಪ್ರಸ್ತುತ ದರ ₹{current_price:.2f}/ಕೆಜಿ ಸೂಕ್ತವಾಗಿದೆ."
            why_text = f"3 ದಿನಗಳ ನಂತರ ಅಂದಾಜು ದರ ₹{predicted_price:.2f}/ಕೆಜಿ. ಕಾಯುವುದರಿಂದ ಹೆಚ್ಚಿನ ಪ್ರಯೋಜನವಿಲ್ಲ."
            dec_text = "ಈಗಲೇ ಮಾರಿ (SELL NOW)"
        elif decision == "WAIT":
            action_text = f"ಸುರಕ್ಷಿತ ಶೇಖರಣೆ ಇದ್ದರೆ, {disp_crop} ಮಾರಾಟಕ್ಕೆ ಕೆಲವು ದಿನ ಕಾಯುವುದು ಸೂಕ್ತ."
            why_text = f"ದರ {pct_change:.1f}% ಹೆಚ್ಚಾಗಿ ₹{predicted_price:.2f}/ಕೆಜಿಗೆ ತಲುಪುವ ಸಾಧ್ಯತೆ ಇದೆ."
            dec_text = "ಕಾಯಿರಿ (WAIT)"
        else:
            action_text = "ಅಂತಿಮ ನಿರ್ಧಾರಕ್ಕೆ ಮುನ್ನ ಮಾರುಕಟ್ಟೆ ಬೇಡಿಕೆ ಗಮನಿಸಿ."
            why_text = "ದರ ಬದಲಾವಣೆ ಕಡಿಮೆಯಾಗಿದೆ."
            dec_text = "ಗಮನಿಸಿ (MONITOR)"

        qual_text = "Grade A ಗುಣಮಟ್ಟಕ್ಕೆ ಉತ್ತಮ ದರ ಲಭಿಸುತ್ತದೆ." if quality == "Grade A" else "ಹತ್ತಿರದ ಮಾರುಕಟ್ಟೆಗಳನ್ನು ಹೋಲಿಕೆ ಮಾಡಿ."

        return f"""🌾 ರೈತ ಸಲಹೆಗಾರ (AI FARMER ADVISOR)
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 ಬೆಳೆ: {disp_crop}
📍 ಸ್ಥಳ: {location}
🏪 ಶಿಫಾರಸು ಮಾರುಕಟ್ಟೆ: {best_market} ({best_market_location})
🚚 ಮಾರುಕಟ್ಟೆ ದೂರ: {best_market_distance:.1f} ಕಿ.ಮೀ
⚖️ ಪ್ರಮಾಣ: {quantity:g} ಕೆಜಿ
⭐ ಗುಣಮಟ್ಟ: {disp_qual}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 ಪ್ರಸ್ತುತ ದರ: ₹{current_price:.2f}/ಕೆಜಿ
🔮 ಅಂದಾಜು ದರ: ₹{predicted_price:.2f}/ಕೆಜಿ
📈 ನಿರೀಕ್ಷಿತ ದರ ಬದಲಾವಣೆ: {pct_change:+.1f}%
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AI ಮಾರಾಟ ನಿರ್ಧಾರ: {dec_text}
💡 ಶಿಫಾರಸು: {action_text}
📊 ಕಾರಣ: {why_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 ಆದಾಯ ಅಂದಾಜು:
• ಈಗ ಮಾರಿದರೆ: ₹{current_rev:,.2f}
• ಅಂದಾಜು ದರದಲ್ಲಿ: ₹{predicted_rev:,.2f}
• ನಿರೀಕ್ಷಿತ ವ್ಯತ್ಯಾಸ: ₹{rev_diff:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ ಗುಣಮಟ್ಟ ಸಲಹೆ:
{qual_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
🚚 ಸಾಗಾಟ ಮಾಹಿತಿ:
ಮಾರುಕಟ್ಟೆ ದೂರ: {best_market_distance:.1f} ಕಿ.ಮೀ. ಹತ್ತಿರದ ಮಾರುಕಟ್ಟೆಗಳು ಸಾಗಾಟ ವೆಚ್ಚ ಕಡಿಮೆ ಮಾಡುತ್ತವೆ.
━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ ಪ್ರಮುಖ ಸೂಚನೆ:
ದರ ಮುನ್ಸೂಚನೆಗಳು ಅಂದಾಜುಗಳಾಗಿವೆ. ವಾಸ್ತವ ದರಗಳು ಮಾರುಕಟ್ಟೆ ಪರಿಸ್ಥಿತಿಗೆ ತಕ್ಕಂತೆ ಬದಲಾಗಬಹುದು."""

    elif lang == "mr":
        if decision == "SELL NOW":
            action_text = f"आपले {disp_crop} पीक आत्ताच {best_market} बाजारपेठेत विका. सध्याचा दर ₹{current_price:.2f}/किलो चांगला आहे."
            why_text = f"3 दिवसांनंतरचा अंदाज ₹{predicted_price:.2f}/किलो आहे, त्यामुळे थांबण्यात फायदा नाही."
            dec_text = "आत्ताच विका (SELL NOW)"
        elif decision == "WAIT":
            action_text = f"सुरक्षित साठवणूक असल्यास {disp_crop} विकण्यासाठी काही दिवस थांबणे योग्य ठरेल."
            why_text = f"भाव {pct_change:.1f}% वाढून सुमारे ₹{predicted_price:.2f}/किलो होण्याची शक्यता आहे."
            dec_text = "थांबा (WAIT)"
        else:
            action_text = "अंतिम निर्णय घेण्यापूर्वी बाजारपेठेतील मागणी तपासा."
            why_text = "भावात फारसा बदल अपेक्षित नाही."
            dec_text = "निरीक्षण करा (MONITOR)"

        qual_text = "Grade A दर्जासाठी चांगला भाव मिळतो." if quality == "Grade A" else "जवळपासच्या बाजारांची तुलना करा."

        return f"""🌾 शेतकरी सल्लागार (AI FARMER ADVISOR)
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 पीक: {disp_crop}
📍 शेतकऱ्याचे ठिकाण: {location}
🏪 शिफारस बाजारपेठ: {best_market} ({best_market_location})
🚚 बाजार अंतर: {best_market_distance:.1f} किमी
⚖️ प्रमाण: {quantity:g} किलो
⭐ प्रत / दर्जा: {disp_qual}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 सध्याचा बाजारभाव: ₹{current_price:.2f}/किलो
🔮 अंदाजित भाव: ₹{predicted_price:.2f}/किलो
📈 अपेक्षित भाव बदल: {pct_change:+.1f}%
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AI विक्री निर्णय: {dec_text}
💡 सल्ला: {action_text}
📊 कारण: {why_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 उत्पन्न अंदाज:
• आत्ता विकल्यास: ₹{current_rev:,.2f}
• अंदाजित भावात: ₹{predicted_rev:,.2f}
• अपेक्षित फरक: ₹{rev_diff:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ गुणवत्ता सल्ला:
{qual_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
🚚 वाहतूक माहिती:
बाजार अंतर: {best_market_distance:.1f} किमी. जवळचा बाजार निवडल्यास वाहतूक खर्च व वेळ वाचतो.
━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ महत्त्वाची सूचना:
किंमतीचे अंदाज बाजारातील उपलब्ध आकडेवारीवर आधारित आहेत. प्रत्यक्ष भाव बदलू शकतात."""

    else:
        if decision == "SELL NOW":
            action_text = f"Sell your {crop} now at {best_market}. The current price of ₹{current_price:.2f}/kg is attractive."
            if price_diff < 0:
                why_text = f"The model expects the price to drop by ₹{abs(price_diff):.2f}/kg ({abs(pct_change):.1f}%). Selling now protects against value loss."
            elif price_diff > 0:
                why_text = f"The predicted price is ₹{predicted_price:.2f}/kg. Even with a minor price change of ₹{price_diff:.2f}/kg, holding risks make selling now the safer choice."
            else:
                why_text = f"The predicted price is ₹{predicted_price:.2f}/kg. Price is expected to remain steady, so selling now guarantees current returns."
        elif decision == "WAIT":
            action_text = f"Consider waiting before selling your {crop}, provided you have safe storage and can manage additional holding costs."
            why_text = f"The system predicts the price may increase by {pct_change:.1f}% to approximately ₹{predicted_price:.2f}/kg."
        else:
            action_text = "Monitor the market before making the final selling decision."
            why_text = "The expected price movement is relatively small."

        if quality == "Grade A":
            qual_text = "Your Grade A produce may attract better prices from quality-focused buyers."
        elif quality == "Grade B":
            qual_text = "Compare multiple nearby markets before selling."
        else:
            qual_text = "For Grade C produce, consider selling sooner to reduce quality deterioration."

        return f"""🌾 FARMER ADVISOR
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌱 Crop: {crop}
📍 Farmer Location: {location}
🏪 Recommended Market: {best_market} ({best_market_location})
🚚 Road Distance to Market: {best_market_distance:.1f} km (by road)
⚖️ Quantity: {quantity:g} kg
⭐ Crop Quality: {quality}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 CURRENT MARKET PRICE: ₹{current_price:.2f}/kg
🔮 PREDICTED PRICE: ₹{predicted_price:.2f}/kg
📈 EXPECTED PRICE CHANGE: {pct_change:+.1f}%
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 AI SELLING DECISION: {decision}
💡 RECOMMENDATION: {action_text}
📊 WHY?: {why_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 REVENUE ESTIMATION:
• If sold now: ₹{current_rev:,.2f}
• At predicted price: ₹{predicted_rev:,.2f}
• Expected difference: ₹{rev_diff:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
⭐ QUALITY ADVICE:
{qual_text}
━━━━━━━━━━━━━━━━━━━━━━━━━━
🚚 TRANSPORT INFORMATION:
Recommended market road distance: {best_market_distance:.1f} km (driving distance). Closer markets can reduce transportation time and transportation expenses.
━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ IMPORTANT:
Price predictions are estimates based on available market data. Actual prices may change because of demand, supply, weather, transportation, storage conditions and other market factors."""
