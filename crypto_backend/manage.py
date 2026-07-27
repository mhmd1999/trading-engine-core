#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

def main():
    """Run administrative tasks."""
    
    # پیدا کردن مسیر اصلی پروژه (همون جایی که manage.py هست)
    # این کار باعث میشه BASE_DIR در settings.py به درستی محاسبه بشه
    BASE_DIR = Path(__file__).resolve().parent

    # اضافه کردن مسیر ریشه پروژه به sys.path
    # این کار باعث میشه وقتی دستوراتی مثل 'python manage.py runserver' رو می‌زنی،
    # پایتون بتونه پوشه 'config' و سایر پوشه‌ها رو پیدا کنه.
    if str(BASE_DIR) not in sys.path:
        sys.path.insert(0, str(BASE_DIR))

    # تنظیم کردن متغیر محیطی برای پیدا کردن تنظیمات (settings)
    # چون تو پوشه تنظیمات رو گذاشتی 'config'، حتما باید این دقیق باشه
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
