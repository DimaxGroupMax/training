import os
import django
from django.core.management import call_command

# Укажите путь к вашим настройкам (как в manage.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

# Записываем файл принудительно в UTF-8
with open('total_dump_fixed.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', exclude=['contenttypes', 'auth.permission'], indent=2, stdout=f)

print("Готово! Теперь файл точно в UTF-8.")