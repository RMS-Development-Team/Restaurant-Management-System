from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'user_id',
            'name',
            'mobile_number',
            'email',
            'role',
        ]
        read_only_fields=['user_id','role']
    def validate_name(self,value):
            if not value.strip():
                raise serializers.ValidationError("Name is required")
            if len(value.strip())<2:
                raise serializers.ValidationError("Name must be at least 2 characters")
            return value.strip()
    def validate_mobile_number(self,value):
        value=value.strip()
        if not value.isdigit() or len(value)!=10:
                raise serializers.ValidationError("Mobile number must be 10 digits")
        users=User.objects.filter(mobile_number=value)
        if self.instance:
            users=users.exclude(pk=self.instance.pk)
        if users.exists():
            raise serializers.ValidationError("Mobile number already exists")
        return value
          
        
        
class OTPRequestSerializer(serializers.Serializer):
    mobile_number=serializers.CharField(max_length=15)
    def validate_mobile_number(self,value):
        if not value.isdigit() or len(value)!=10:
            raise serializers.ValidationError("Mobile number must be 10 digits")
        if not User.objects.filter(mobile_number=value,is_active=True).exists():
            raise serializers.ValidationError("User not found")
        return value
        
class OTPVerificationSerializer(serializers.Serializer):
    mobile_number=serializers.CharField(max_length=15)
    otp=serializers.CharField(min_length=6,max_length=6)
    def validate_mobile_number(self,value):
        if not value.isdigit() or len(value)!=10:
            raise serializers.ValidationError("Enter a valid mobile number")
        return value
    def validate_otp(self,value):
        if not value.isdigit() or len(value)!=6:
            raise serializers.ValidationError("OTP must contain 6 digits only.")
        return value