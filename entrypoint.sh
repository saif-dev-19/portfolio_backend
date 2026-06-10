#!/bin/sh

echo "Loading environment..."
# Load local .env if exists (safe version)
if [ -f .env ]; then
  set -a
  . ./.env
  set +a
fi

# Wait for PostgreSQL only if not on Railway
if [ -z "$RAILWAY_ENVIRONMENT" ]; then
  echo "Waiting for local PostgreSQL..."
  until python -c "import psycopg2; import os; psycopg2.connect(os.environ['DATABASE_URL'])" 2>/dev/null; do
    echo "DB not ready yet... retrying in 2s"
    sleep 2
  done
fi

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
gunicorn core.wsgi:application