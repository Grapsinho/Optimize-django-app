# Django Optimization Project

Welcome to the Django Optimization Project! This project focuses on enhancing the performance of a Django application by implementing indexing, caching strategies, and using signals to manage cache invalidation. 

## Features

- **Indexing:** Utilizes Django’s full-text search capabilities and other indexing strategies to speed up search operations and queries.
- **Caching:** Implements various caching strategies to optimize data retrieval and reduce database load. Caching is applied to views and queries for improved performance.
- **Cache Invalidation:** Employs Django signals to automatically invalidate and refresh cached data when updates occur, ensuring data consistency.

## Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/Grapsinho/Optimize-django-app.git
```

2. Navigate to the project directory:

```bash
cd Optimize-django-app
```

3. Create a virtual environment:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

- On macOS and Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

5. Install the dependencies:

```bash
pip install -r requirements.txt
```

6. Run migrations:

```bash
python manage.py migrate
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Access the application at `http://localhost:8000` in your web browser.

## Usage

- **Indexing:** Indexes are automatically created for search fields. For full-text search, use the search functionality provided in the application.
- **Caching:** Views and querysets are cached based on configuration. Cache invalidation is handled via Django signals when related data is updated.
- **Signals:** Signals are used to invalidate caches on model updates. Check the signals.py file in your app for details on signal handlers.

## Configuration

- **Redis:** This project uses Redis as the caching backend. Ensure Redis is installed and running on your system.
- **Django Settings:** Configuration for caching and indexing is set in the settings.py file. Adjust caching timeouts and other parameters as needed.
