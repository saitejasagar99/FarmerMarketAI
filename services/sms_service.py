# -*- coding: utf-8 -*-
"""
SMS Notification Service for FarmerMarketAI
Handles OTP delivery to Indian mobile numbers (+91) via:
1. Fast2SMS (Indian SMS Gateway - route="otp")
2. Twilio SMS
3. Logging Fallback
"""

import os
import re
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("sms_service")
logger.setLevel(logging.INFO)


def clean_phone_number(phone: str) -> str:
    """Normalize phone number to 10 digits without country code or spaces."""
    cleaned = re.sub(r"[^\d]", "", str(phone))
    if len(cleaned) == 12 and cleaned.startswith("91"):
        cleaned = cleaned[2:]
    elif len(cleaned) == 11 and cleaned.startswith("0"):
        cleaned = cleaned[1:]
    return cleaned


def send_otp_via_fast2sms(phone: str, otp: str, api_key: str) -> dict:
    """Send OTP to Indian mobile number via Fast2SMS Quick OTP route."""
    try:
        url = "https://www.fast2sms.com/dev/bulkV2"
        headers = {
            "authorization": api_key,
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache"
        }
        payload = {
            "variables_values": otp,
            "route": "otp",
            "numbers": phone
        }
        response = requests.post(url, data=payload, headers=headers, timeout=10)
        data = response.json()
        
        if data.get("return") is True:
            logger.info(f"Fast2SMS OTP sent successfully to +91 {phone}")
            return {
                "success": True,
                "provider": "fast2sms",
                "message": "SMS dispatched successfully to mobile number"
            }
        else:
            err_msg = data.get("message", ["Unknown Fast2SMS error"])[0] if isinstance(data.get("message"), list) else data.get("message", "Error")
            logger.warning(f"Fast2SMS error: {err_msg}")
            return {
                "success": False,
                "provider": "fast2sms",
                "message": str(err_msg)
            }
    except Exception as e:
        logger.error(f"Fast2SMS request failed: {e}")
        return {
            "success": False,
            "provider": "fast2sms",
            "message": str(e)
        }


def send_otp_via_twilio(phone: str, otp: str, account_sid: str, auth_token: str, from_phone: str) -> dict:
    """Send OTP via Twilio REST API."""
    try:
        url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"
        to_phone = f"+91{phone}"
        body = f"Your FarmerMarketAI login verification code is {otp}. Valid for 5 minutes."
        
        response = requests.post(
            url,
            data={"From": from_phone, "To": to_phone, "Body": body},
            auth=(account_sid, auth_token),
            timeout=10
        )
        data = response.json()
        
        if response.status_code in (200, 201):
            logger.info(f"Twilio SMS sent to {to_phone}")
            return {
                "success": True,
                "provider": "twilio",
                "message": "SMS dispatched successfully via Twilio"
            }
        else:
            err_msg = data.get("message", "Twilio delivery failed")
            logger.warning(f"Twilio error: {err_msg}")
            return {
                "success": False,
                "provider": "twilio",
                "message": str(err_msg)
            }
    except Exception as e:
        logger.error(f"Twilio request failed: {e}")
        return {
            "success": False,
            "provider": "twilio",
            "message": str(e)
        }


def send_otp_sms(phone: str, otp: str) -> dict:
    """
    Main dispatch function to send OTP to a mobile phone.
    Checks environment for FAST2SMS_API_KEY or Twilio credentials.
    """
    cleaned_phone = clean_phone_number(phone)
    if len(cleaned_phone) != 10:
        return {
            "success": False,
            "provider": "validation",
            "message": f"Invalid mobile number format: {phone}"
        }
    
    load_dotenv(override=True)
    fast2sms_key = os.getenv("FAST2SMS_API_KEY", "").strip()
    if "*" in fast2sms_key or len(fast2sms_key) < 25:
        # Key is masked or invalid
        fast2sms_key = ""
    
    twilio_sid = os.getenv("TWILIO_ACCOUNT_SID", "").strip()
    twilio_token = os.getenv("TWILIO_AUTH_TOKEN", "").strip()
    twilio_from = os.getenv("TWILIO_PHONE_NUMBER", "").strip()
    
    # 1. Try Fast2SMS (Preferred in India)
    if fast2sms_key:
        result = send_otp_via_fast2sms(cleaned_phone, otp, fast2sms_key)
        if result["success"]:
            return result
        return {
            "success": False,
            "provider": "fast2sms_pending_kyc",
            "message": result.get("message", "Fast2SMS verification needed"),
            "otp": otp,
            "phone": cleaned_phone
        }
    
    # 2. Try Twilio
    if twilio_sid and twilio_token and twilio_from:
        result = send_otp_via_twilio(cleaned_phone, otp, twilio_sid, twilio_token, twilio_from)
        if result["success"]:
            return result
    
    # 3. Fallback: Log safely to console
    try:
        print("\n" + "="*55)
        print(f"[SMS NOTIFICATION DISPATCHED]")
        print(f"To: +91 {cleaned_phone}")
        print(f"Message: Your FarmerMarketAI OTP code is {otp}")
        print(f"Status: Logged to server (Add FAST2SMS_API_KEY to .env for carrier delivery)")
        print("="*55 + "\n")
    except Exception:
        pass
    
    has_key = bool(fast2sms_key or (twilio_sid and twilio_token))
    return {
        "success": has_key,
        "provider": "unconfigured" if not has_key else "gateway_error",
        "message": "SMS gateway key not configured in .env" if not has_key else "Gateway delivery error",
        "otp": otp,
        "phone": cleaned_phone
    }
