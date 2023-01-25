# Leave_management_uiet

**Note:- Open terminal and go to project root directory.Note that you must follow same root directory in every steps.**

### Step-1 (venv setup & dependencies install)

1. Create virtual environment and activate [(Read this)](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments).
2. Now install all the dependencies using command `pip install -r requirements.txt`.
3. Make sure all the dependencies is installed successfully.

### Step-2 (secure keys and create superuser)

1. Some secret keys and credentials are not given, so you have to change the configs in `settings.py` file.

```
SECRET_KEY = 'DJANGO_SECURE_SECRET_KEY'
```

2. After these steps you need to apply migrations and migrate using command `python .\manage.py makemigrations` ->> `python .\manage.py migrate`.
3. Run command `python .\manage.py createsuperuser` to create superuser.
4. Fill credentials and press Enter.

**Note:- Now run server using command `python .\manage.py runserver` to verify everything is working or not.**
