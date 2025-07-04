#!/bin/bash 
 python manage.py createsuperuser --settings=church_donate_platform.settings.dev
 python manage.py makemigrations --settings=church_donate_platform.settings.prod
 python manage.py migrate --settings=church_donate_platform.settings.dev
 python manage.py runserver --settings=church_donate_platform.settings.dev
 python manage.py generate_blog --settings=church_donate_platform.settings.dev
 python manage.py generate_donate --settings=church_donate_platform.settings.dev
 python manage.py generate_donate_record --settings=church_donate_platform.settings.dev
 python manage.py generate_user --settings=church_donate_platform.settings.dev
python manage.py generate_user_donate --settings=church_donate_platform.settings.dev
 