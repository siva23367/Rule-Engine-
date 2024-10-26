#!/bin/bash

if [ -d "migrations" ]; then
    echo "migrartions exist. Now upgrading ..."
    aerich upgrade
else
    echo "Migrations folder does not exist. Skipping aerich migrate."
fi

echo "Starting FastAPI server"
exec uvicorn app:app --host 0.0.0.0 --port 8000
echo "FastAPI server started"