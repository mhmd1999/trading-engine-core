from django.contrib.auth.models import AbstractUser
from django.db import models

# 🚫 خط زیر باید حتماً حذف شود:
# from apps.users.models import User  <-- این قاتل پروژه است!

class User(AbstractUser):
    """
    مدل کاربر سفارشی با رعایت اصول طراحی برای سیستم‌های مالی.
    این مدل پایه و اساس سیستم ترید و مدیریت کاربران است.
    """
    
    # ایمیل منحصر به فرد برای امنیت بالاتر
    email = models.EmailField(
        unique=True, 
        help_text="ایمیل کاربر باید منحصر به فرد باشد."
    )
    
    # استفاده از دقت بسیار بالا (High Precision) برای کریپتو
    # max_digits=32 و decimal_places=18 استاندارد جهانی (مثل اتریوم) است.
    balance = models.DecimalField(
        max_digits=32, 
        decimal_places=18, 
        default=0,
        help_text="موجودی کاربر در مقیاس بسیار دقیق (مناسب برای کریپتو)"
    )
    
    # نقش کاربر برای مدیریت دسترسی‌ها (Role-based Access Control)
    is_trader = models.BooleanField(
        default=False, 
        help_text="اگر کاربر اجازه انجام معامله دارد، فعال شود."
    )

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        # اضافه کردن این برای اطمینان از ایندکس شدن بهتر در دیتابیس
        ordering = ['username'] 

    def __str__(self):
        return f"{self.username} ({self.email})"

    def has_sufficient_balance(self, amount: float) -> bool:
        """
        متد کمکی برای بررسی موجودی (Business Logic Layer).
        به جای اینکه منطق چک کردن موجودی را در View بنویسی، اینجا قرار می‌گیرد.
        """
        return self.balance >= amount
