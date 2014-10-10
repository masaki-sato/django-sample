## メモ

```
pip freeze -l > requirements.txt
pip install -r requirements.txt
```

## 新規作成の場合

```
pip install -r requirements.txt

django-admin.py startproject blog
python manage.py migrate
python manage.py createsuperuser

python manage.py startapp cms
python manage.py makemigrations cms
python manage.py migrate           

python manage.py runserver
```


## チェックアウトの場合

```
git clone https://github.com/checkpoint/django-sample.git
cd django-sample/
pip install -r requirements.txt
cd blog/
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 参考URL

http://www.sakito.com/2012/09/python-memoryprofiler.html
http://qiita.com/kaki_k/items/511611cadac1d0c69c54
https://docs.djangoproject.com/en/1.7/intro/tutorial01/
