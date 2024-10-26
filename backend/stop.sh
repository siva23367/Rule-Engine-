#!/bin/bash

echo "Stopping Backend server"
pkill -f "uvicorn app:app --host 0.0.0.0 --port 8000"
echo "Backend server stopped"

echo "Stopping ARQ server"
pkill -f "arq arq_worker.WorkerSettings"
echo "ARQ server stopped"