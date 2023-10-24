# Determine the operating system
ifeq ($(OS),Windows_NT)
	# Windows-specific commands
	RM = rmdir /s /q
	ACTIVATE_VENV = env\Scripts\activate
	CREATE_ENV_FILE = echo SECRET_KEY=your_secret_key_here >> leave_management_uiet/.env
else
	# Linux-specific commands
	RM = rm -rf
	ACTIVATE_VENV = source env/bin/activate
	CREATE_ENV_FILE = echo "SECRET_KEY=your_secret_key_here" >> leave_management_uiet/.env 
endif

# Check if Python 3.10.0 is available
python_version_check:
	@python -c "import sys; assert sys.version_info >= (3, 9, 13), 'Python 3.9.13 is required.'"

# Create the virtual environment
create-venv:
	@echo Creating the virtual environment...
	@python -m venv env

# Activate the virtual environment
activate-venv:
	@echo Activate the virtual environment with: $(ACTIVATE_VENV)

# Install project dependencies
install-dependencies:
	@echo Installing project dependencies...
	@$(ACTIVATE_VENV) && pip install -r requirements.txt

# Create .env file
create-env-file:
	@echo Creating .env file in leave_management_uiet/...
	@$(CREATE_ENV_FILE)

# Apply database migrations
apply-migrations:
	@echo Applying database migrations...
	@$(ACTIVATE_VENV) && python manage.py makemigrations
	@$(ACTIVATE_VENV) && python manage.py makemigrations accounts account_status applications leave_types authentication home services
	@$(ACTIVATE_VENV) && python manage.py migrate

# Create a superuser
create-superuser:
	@echo Creating a superuser for admin access...
	@$(ACTIVATE_VENV) && python manage.py createsuperuser

# Start the development server
run:
	@echo Starting the development server...
	@$(ACTIVATE_VENV) && python manage.py runserver

# Local setup target
local-setup: python_version_check create-venv activate-venv install-dependencies create-env-file apply-migrations create-superuser
	@echo -- local setup done --
	@echo Note:- run the development server using `make run`


# Help section
.PHONY: help
help:
	@echo "Leave Management UIET Makefile Commands"
	@echo "--------------------------------------"
	@echo "Commands:"
	@echo "  make create-venv          Create a virtual environment"
	@echo "  make activate-venv        Activate the virtual environment"
	@echo "  make install-dependencies Install project dependencies"
	@echo "  make create-env-file      Create the .env file"
	@echo "  make apply-migrations     Apply database migrations"
	@echo "  make create-superuser     Create a superuser for admin access"
	@echo "  make run                  Start the development server"
	@echo "  make local-setup          Set up the project locally (recommended)"
	@echo "  make clean                Remove pycache files"
	@echo "  make help                 Show this help message"
	@echo "--------------------------------------"