from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_is_verified_otpverification_is_used_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otpverification',
            old_name='is_verified',
            new_name='is_used',
        ),
        migrations.RenameField(
            model_name='otpverification',
            old_name='attempts',
            new_name='verification_attempts',
        ),
        migrations.RenameField(
            model_name='otpverification',
            old_name='id',
            new_name='otp_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(
                blank=True,
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(
                choices=[
                    ('admin', 'Admin'),
                    ('customer', 'Customer'),
                    ('waiter', 'Waiter'),
                    ('counter_staff', 'Counter Staff'),
                    ('kitchen_staff', 'Kitchen Staff'),
                ],
                default='customer',
                max_length=30,
            ),
        ),
    ]