from django.contrib import admin
from .models import Bill,Payment
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display=('bill_id','order','subtotal','discount','status','total_amount','created_at')
    list_filter=('status','created_at')
    search_fields=('=bill_id',)
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=('payment_id','bill','payment_method','payment_status','amount','transaction_id','created_at')
    list_filter=('payment_method','payment_status','created_at')
    search_fields=('=payment_id','transaction_id')
    
