# Interactive Cancer Analysis Project

## Description

This Django-based web application is designed for visualizing various cancer types and censoring information through interactive charts. It allows users to explore the distribution of different cancer diagnoses and understand the censoring status of patient data.

## Features

- **Cancer Type Visualization**: Displays a pie chart of the distribution of cancer types from the dataset.
- **Censoring Information Visualization**: Illustrates a pie chart showing the proportion of censored and non-censored patient data.

## Installation

To set up the project on your local machine:

1. **Clone the Repository**

    ```
    git clone https://github.com/your-username/cancer-analysis-project.git
    cd cancer-analysis-project
    ```

2. **Create and Activate a Virtual Environment (optional but recommended)**

    For Unix/MacOS:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

    For Windows:

    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. **Install Required Packages**

    ```
    pip install -r requirements.txt
    ```

4. **Initialize the Database**

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the Development Server**

    ```
    python manage.py runserver
    ```

    Access the application at `http://127.0.0.1:8000/`.

## Usage

Once the server is running:

- Navigate to `/cancer-types/` to view the pie chart of cancer types.
- Navigate to `/censoring-data/` to view the censoring information chart.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

