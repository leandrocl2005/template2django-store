# Template2Django: Store

Make a Django web app from a template. This time we choose the following:

- https://www.tooplate.com/view/2062-clothing

## How to use this project

```bash
git clone https://github.com/leandrocl2005/template2django-store.git
cd template2django-store
python3 -m venv myvenv
. myvenv/Scripts/activate
pip install django
pip install pillow
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

After all, create some data and enjoy.

## To do

- The cart logic

## Thanks

- https://www.tooplate.com/
- https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
- https://stackoverflow.com/questions/901115/how-can-i-get-query-string-values-in-javascript
