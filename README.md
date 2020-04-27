# Blog website django
pip3 install django
django-admin --version 
django-admin startproject mysite
python manage.py runserver 

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
MESSAGE_TAGS = {
    messages.ERROR:"danger"
}
