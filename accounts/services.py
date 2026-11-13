import secrets
from datetime import timedelta
from django.contrib.auth.hashers import make_password,check_password
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from .models import OTPVerification

def generate_otp(user):
        otp = str(secrets.randbelow(900000) + 100000)
        OTPVerification.objects.filter(user=user,is_used=False).update(is_used=True)
        OTPVerification.objects.create(
            user=user,
            otp_hash=make_password(otp),
            expires_at=timezone.now()+timedelta(minutes=5)
            
        )
        return otp
def verify_otp(user, otp):
    otp_record = OTPVerification.objects.filter(
        user=user,
        is_used=False
    ).order_by('-created_at').first()

    if not otp_record:
        raise ValidationError("OTP not found")

    if otp_record.expires_at < timezone.now():
        otp_record.is_used = True
        otp_record.save()
        raise ValidationError("OTP expired")

    if otp_record.verification_attempts >= 5:
        otp_record.is_used = True
        otp_record.save()
        raise ValidationError("Maximum attempts reached")

    otp_record.verification_attempts += 1

    if not check_password(otp, otp_record.otp_hash):
        otp_record.save()
        raise ValidationError("Invalid OTP")

    otp_record.is_used = True
    otp_record.save()

    return True


def resend_otp(user):
    latest_otp = OTPVerification.objects.filter(
        user=user
    ).order_by('-created_at').first()

    if latest_otp:
        time_difference = (
            timezone.now() - latest_otp.created_at
        ).total_seconds()

        if time_difference < 60:
            raise ValidationError(
                "Please wait before requesting another OTP"
            )

    return generate_otp(user)
