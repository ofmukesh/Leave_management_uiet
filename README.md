# Leave Management UIET

## Description

Leave Management UIET is a Django-based web application that simplifies leave management for the University Institute of Engineering & Technology (UIET). It provides a user-friendly interface for staff and students to request, approve, and manage leave applications.

## Requirements

Before using the Makefile, ensure you have the following prerequisites installed on your system:

- Python 3.9.13
- Virtual environment (optional but recommended)
- Git (for cloning the project repository)

## Usage

To set up the project locally, you can use a single Makefile command:

1. Clone the project repository:

   ```bash
   git clone https://github.com/yourusername/Leave_management_uiet.git
   cd Leave_management_uiet
   ```

2. Run the `local-setup` command to create a virtual environment, install project dependencies, configure environment variables, apply migrations, and create a superuser. This command combines all setup steps:

   ```bash
   make local-setup
   ```

3. After running `local-setup`, you can find a file named `.env.template` in the project directory. This template contains variable names, but you need to provide values.

4. To complete the setup, copy the variables from `.env.template` and paste them into a `.env` file.

   For example, you might have variables like this in your `.env.template`:

   ```dotenv
   SECRET_KEY=your-secret-key-value
   EMAIL_HOST_USER=your-email-host-username
   EMAIL_HOST_PASSWORD=your-email-host-password
   ```

   Create a new file named `.env` and copy these variables to it. Then, replace `your-secret-key-value`, `your-email-host-username`, and `your-email-host-password` with the actual values.

5. Start the development server:

   ```bash
   make run
   ```

Access the application in your web browser by visiting [http://localhost:8000/](http://localhost:8000/).

## Makefile Commands

You can use the following Makefile commands for common project tasks:

- `make create-venv`: Create a virtual environment.
- `make activate-venv`: Activate the virtual environment.
- `make install-dependencies`: Install project dependencies.
- `make create-env-file`: Create the .env file.
- `make apply-migrations`: Apply database migrations.
- `make create-superuser`: Create a superuser for admin access.
- `make run`: Start the development server.


## Contributing

- Fork the repository on GitHub.
- Clone your forked repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your GitHub repository.
- Submit a pull request to the original repository.


## License

This project is open-source and available under the [MIT License](LICENSE).