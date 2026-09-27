# Cinema Fullstack

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

## Task:

You already have Backend and Frontend implemented.
You need to connect them together, and make sure all functionality of Cinema Shop works.

NOTE: Attach screenshots of all pages from the correctly connected frontend. Better to make them with opened developer tool, where will be shown requests to the API.

## Run the backend with Docker

Start Docker Desktop. From the project root:

```powershell
Copy-Item .env.sample .env  # First run only; keep an existing .env.
docker compose up --build -d
docker compose exec app python manage.py createsuperuser
```

The admin is at http://localhost:8080/admin/ and API docs are
at http://localhost:8080/api/doc/swagger/.

The Dockerfile installs and runs only the Python backend. PostgreSQL runs
in a separate Compose service. Run the frontend separately as shown below.
Additional Django routes support the frontend's `movies-ID`,
`movie_sessions-ID` and `movies-ID-upload-image` URLs. Frontend source
changes only add trailing slashes to API URLs.

Create a genre, actor, hall, movie with a poster, and a session for today
through the admin or frontend. Then select the session and book a seat.
PostgreSQL data is kept in a Docker volume; uploaded images are in
`backend/media/`. This is a local development setup using Django runserver.

```powershell
docker compose exec app python manage.py test
docker compose logs --tail=50 app
docker compose stop
```

After stopping, start again with `docker compose up -d`.
Rebuild with `docker compose up --build -d` after changing backend dependencies
or the Dockerfile.

## Run the frontend separately

In a separate PowerShell terminal, from the project root:

```powershell
cd frontend
npm.cmd install
$env:VITE_API_URL = "http://localhost:8080"
npm.cmd run dev -- --port 5173 --strictPort
```

Open http://localhost:5173/#/sign-in and use the superuser email and password.
Django allows browser API requests from this origin through CORS.

Known limitation of the supplied frontend: the poster upload uses a relative
`/api/cinema/movies-ID-upload-image/` URL and ignores `VITE_API_URL`. When
running separately, that request goes to Vite and needs an API proxy or an
upload URL correction before poster uploads work. Frontend configuration
and logic have been left unchanged as requested.

## Screenshots

Open browser DevTools (F12), select Network and Fetch/XHR, then visit a page
or submit its form. Capture the page alongside the request URL and status
or response preview. Use Preserve log for sign-in and registration; keep
passwords and tokens out of screenshots.

Include registration, sign-in, movies and movie details, movie creation,
sessions and session creation, seat selection and successful booking,
orders, profile, halls, genres and actors (including their creation forms).
Save images in `screenshots/` and attach them to the pull request.
