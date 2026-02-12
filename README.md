# Tarawih-Website

This is a website that allows users to check what their masjid will read in the tarawih during ramadan.

## Setup & Running

### With Docker (Recommended)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Run:

```bash
docker-compose up
```

3. Open http://localhost:8000 in your browser

The database will be persisted in a Docker volume and won't be committed to git.

### Without Docker

1. Create and activate virtual environment:

```bash
python -m venv virtual
source virtual/bin/activate  # On Windows: virtual\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations and start server:

```bash
cd tarawih
python manage.py migrate
python manage.py runserver
```

4. Open http://localhost:8000 in your browser
