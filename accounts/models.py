from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,mobile_number,password=None,**extra_fields):
        if not mobile_number:
            raise ValueError('Mobile number is required')
        user=self.model(mobile_number=mobile_number,**extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user
    def create_superuser(self,mobile_number,password=None,**extra_fields):
        if not password:
          raise ValueError("Superuser must have a password")
        extra_fields.setdefault("role","admin")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(mobile_number,password,**extra_fields)
class User(AbstractUser):
        username = None
        first_name = None
        last_name = None
        class Role(models.TextChoices):
            ADMIN = "admin", "Admin"
            CUSTOMER = "customer", "Customer"
            WAITER = "waiter", "Waiter"
            COUNTER_STAFF = "counter_staff", "Counter Staff"
            KITCHEN_STAFF = "kitchen_staff", "Kitchen Staff" 
        name=models.CharField(max_length=100)
        user_id = models.AutoField(primary_key=True)
        mobile_number=models.CharField(max_length=15,unique=True)
        email = models.EmailField(max_length=100, blank=True, null=True)
        role = models.CharField(max_length=30,choices=Role.choices,default=Role.CUSTOMER)
        objects=UserManager()
        USERNAME_FIELD='mobile_number'
        REQUIRED_FIELDS=["name"]
        
        def __str__(self):
            return f"{self.name} ({self.mobile_number}) "      
    
           
class OTPVerification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,
    related_name="otp_verifications")
    otp_id = models.AutoField(primary_key=True)
    otp_hash=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    verification_attempts = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField()
    
    def __str__(self):
        return f"OTP for {self.user.mobile_number}"
    
    