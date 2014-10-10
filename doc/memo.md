## メモ

```
pip freeze -l > requirements.txt
pip install -r requirements.txt
```

## 新規作成の場合
pip install -r requirements.txt

* django-admin.py startproject blog
* python manage.py migrate
* python manage.py createsuperuser

* python manage.py startapp cms
* python manage.py makemigrations cms
* python manage.py migrate           

* python manage.py runserver
