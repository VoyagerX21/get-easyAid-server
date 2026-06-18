# Get-Easyaid Server

Flask API server for generating personalized financial aid requests for Coursera courses.

## What This Project Does

This service keeps a local catalog of courses, scrapes Coursera pages on demand, stores course and specialization data in the database, and generates AI-backed financial aid responses from a saved request payload. The service uses NVIDIA NIM (Qwen3.5-122B) to generate personalized financial aid responses based on course metadata and user-provided information.

## Architecture Overview

The project now uses a blueprint-based Flask layout:

- `app/__init__.py` creates the Flask app, enables CORS, registers blueprints, and wires the database and migrations.
- `app/routes/` contains the HTTP layer for course lookup, scraping, prompt generation, regeneration, and job status.
- `app/controllers/` contains the request handlers behind each route.
- `app/services/` handles the AI request flow and prompt construction.
- `app/models/` defines the persisted entities for courses, specializations, and AI jobs.
- `app/utils/scrapepage.py` caches scraped Coursera HTML in `static/scraps/` so repeated requests do not re-download the same pages.

The main job flow is asynchronous: `/GetPrompt` creates an `Aidrequest` record, starts a background thread, and `/job/<jobid>` is used to check completion or retry generation.

## Core Features

- Cached Coursera scraping for faster repeated lookups
- Course search by title or organization
- Course and specialization tracking in the database
- Background AI generation for financial aid responses
- Retry support for failed or partial generation jobs
- Database-backed caching of scraped course metadata to avoid repeated Coursera requests

## Tech Stack

```
   Backend:
   - Flask
   - SQLAlchemy
   - Flask-Migrate
   - Gunicorn

   Database:
   - SQLite

   AI:
   - NVIDIA NIM (Qwen3.5-122B)

   Data Collection:
   - BeautifulSoup

   Deployment:
   - Docker
   - Docker Compose
   - Azure VM
```

## API Endpoints

- `GET /` - Health check that returns `{"msg": "API running"}`
- `GET /getAllCourses/` - Return all stored courses
- `GET /search/?query=...` - Search courses by title or organization
- `POST /submit/` - Submit a course payload and scrape the Coursera page
- `POST /GetPrompt/` - Create an AI generation job from a payload
- `POST /regenerate/` - Regenerate one response box from a saved payload
- `GET /job/<jobid>` - Check job status and fetch results when complete
- `POST /job/retry/<jobid>/<num>` - Retry generation for box 1, 2, or both

## Data Model

- `Course` stores course metadata, cache state, and specialization metadata.
- `Spec` stores specialization course names linked to a parent course.
- `Aidrequest` stores the prompt payload, generation status, answers, and timestamps.

## Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with the values used by the current config:
   ```
   KEY=your_ai_api_key
   SQLITE_URI=your_database_uri
   ```

3. Run database migrations if needed:
   ```bash
   flask db upgrade
   ```

4. Start the server:
   ```bash
   python run.py
   ```

## Project Notes

- Scraped HTML is cached under `static/scraps/`.
- The app uses Flask-SQLAlchemy and Flask-Migrate.
- CORS is enabled for the API.
- AI responses are generated through the service configured in `app/config/config.py`.

## Docker

### Build and Run

```bash
docker compose up --build
```

The application will be available at:

```text
http://localhost:5000
```

### Run in Detached Mode

```bash
docker compose up -d
```

### Stop Containers

```bash
docker compose down
```

### View Logs

```bash
docker compose logs -f
```

### Database Persistence

SQLite data is stored using a Docker volume, ensuring course data and generated requests persist across container restarts.

### Container Features

* Gunicorn-based production server
* Automatic database migrations on startup
* Persistent SQLite storage via Docker volumes
* Environment-based configuration support
* Multi-container orchestration with Docker Compose

## Live Server

API Server: [Visit server here](https://geteasyserver.khakse.dev/)
