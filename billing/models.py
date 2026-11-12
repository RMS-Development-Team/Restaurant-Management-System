from django.db import models
class Bill(models.Model):
    class BillStatus(models.TextChoices):
        PENDING='PENDING','Pending'
        PAID='PAID','Paid'
    bill_id=models.AutoField(primary_key=True)
    order=models.OneToOneField("orders.Order",on_delete=models.PROTECT,related_name='bill')
    subtotal=models.DecimalField(max_digits=10,decimal_places=2)
    discount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=10,choices=BillStatus.choices,default=BillStatus.PENDING)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Bill {self.bill_id}"
    
class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH='CASH','Cash'
        UPI='UPI','UPI'
        CARD='CARD','Card'
    class PaymentStatus(models.TextChoices):
        PENDING='PENDING','Pending'
        COMPLETED='COMPLETED','Completed'
        FAILED='FAILED','Failed'
    payment_id=models.AutoField(primary_key=True)
    bill=models.OneToOneField(Bill,on_delete=models.PROTECT,related_name="payment")
    payment_method=models.CharField(max_length=10,choices=PaymentMethod.choices)
    payment_status=models.CharField(max_length=10,choices=PaymentStatus.choices,default=PaymentStatus.PENDING)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    transaction_id=models.CharField(max_length=100,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Payment {self.payment_id}"