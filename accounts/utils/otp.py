from django.core.cache import cache
import secrets


OTP_EXPIRE = 60 * 5
RESEND_LIMIT = 3
ATTEMPT_LIMIT = 3


def generate_otp():
    return str(secrets.randbelow(900000) + 100000)


def send_otp(phone: str):

    resend_key = f"otp:resend:{phone}"
    resend_count = cache.get(resend_key, 0)

    if resend_count >= RESEND_LIMIT:
        return {"success": False, "error": "Qayta yuborish limiti tugadi. 5 daqiqa kuting."}


    code = generate_otp()
    print(code)

    cache.set(f"otp:{phone}", code, timeout=OTP_EXPIRE)

    cache.set(resend_key, resend_count + 1, timeout=OTP_EXPIRE)

    cache.delete(f"otp:attempts:{phone}")
    # hullas bu yerda eskiz.uz kerak
    # send_sms(phone, f"UzEvently: tasdiqlash kodingiz {code}")

    return {"success": True}


def verify_otp(phone: str, code: str):

    attempt_key = f"otp:attempts:{phone}"
    attempts = cache.get(attempt_key, 0)

    if attempts >= ATTEMPT_LIMIT:
        return {"success": False, "error": "Urinishlar limiti tugadi. Qayta so'rang."}


    saved_code = cache.get(f"otp:{phone}")

    if not saved_code:
        return {"success": False, "error": "OTP muddati tugagan yoki yuborilmagan."}


    if saved_code != code:
        cache.set(attempt_key, attempts + 1, timeout=OTP_EXPIRE)
        return {"success": False, "error": "Noto'g'ri OTP."}

    cache.delete(f"otp:{phone}")
    cache.delete(attempt_key)
    cache.delete(f"otp:resend:{phone}")

    return {"success": True}

