# Detect the operating system
ifeq ($(OS),Windows_NT)
	VENV_ACTIVATE := .\env\Scripts\activate
else
	VENV_ACTIVATE := source env/bin/activate
endif

# setup Project
setup:
	@echo Creating a virtual environment.. 
	python -m venv env
	@echo virtual environment created.
	@echo installing required dependencies using requirement.txt..  
	$(VENV_ACTIVATE) && pip install -r .\reqirement.txt
	@echo dependencies succesfully installed.
	@echo migrating...
	$(VENV_ACTIVATE) && make migrate
	@echo setup complete✓

# create admin user
admin:
	@echo creating a admin user O_O
	$(VENV_ACTIVATE) && python manage.py createsuperuser

# makemigration and migrate changes
migrate:
	$(VENV_ACTIVATE) && python manage.py makemigrations
	@echo migrating all the changes to DB
	$(VENV_ACTIVATE) && python manage.py migrate

# Run your application
run:
	@echo running server..
	$(VENV_ACTIVATE) && python manage.py runserver
