#!/bin/sh

echo "⏳ Postgres kutilyapti..."

until pg_isready -h datadb -p 5432; do
  sleep 1
done

echo "✅ Postgres ishga tushdi"

exec "$@"
