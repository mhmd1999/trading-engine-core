from django.apps import AppConfig

class UsersConfig(AppConfig):
    """
    تنظیمات مربوط به اپلیکیشن کاربران.
    در اینجا نام کامل اپلیکیشن (Path) رو مشخص می‌کنیم تا جنگو 
    بتونه موقع Import کردن، دچار سردرگمی نشه.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    
    # این خط خیلی حیاتیه! 
    # چون اپلیکیشن ما داخل پوشه apps هست، باید مسیر کامل رو بنویسیم.
    name = 'apps.users'
    label = 'users' 