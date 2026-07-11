# Flask on Railway

Flask — lightweight Python web framework served by Gunicorn. Deploy on Railway with one click.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/FLASK_TEMPLATE_CODE)

## Features

- **Minimal and flexible** — Build web apps and APIs with just the pieces you need.
- **Gunicorn production server** — Production-grade WSGI server, not Flask's dev server.
- **Jinja2 templating** — Server-side HTML rendering with Bootstrap 4 styling included.
- **Auto-deploy from GitHub** — Push code, Railway rebuilds and redeploys automatically.
- **Environment variables** — Manage secrets and config through Railway's dashboard.

## How to use

1. Click the **Deploy on Railway** button above.
2. Wait for the build to finish (~30 seconds).
3. Open your Railway domain to see the default landing page.
4. Edit `main.py` to add routes, push to GitHub, and Railway redeploys.

## Adding Routes

```python
@app.route('/api/hello')
def hello():
    return {"message": "Hello, world!"}
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `PORT` | Auto-set by Railway |
| `FLASK_ENV` | Set to `production` for production mode |
| `SECRET_KEY` | App secret key (set in Railway dashboard) |

## Notes

- This template uses Railpack (no Dockerfile) — Railway auto-detects Python from `requirements.txt`.
- Gunicorn serves the app via the `Procfile`: `web: gunicorn main:app`.
- Add Python packages to `requirements.txt` and they'll be installed on the next deploy.
- For database support, add a PostgreSQL plugin in Railway and use `os.environ.get("DATABASE_URL")`.
