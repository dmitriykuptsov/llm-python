cd /opt/llm-agent
source venv/bin/activate

venv/bin/uvicorn app:app \
    --host 0.0.0.0 \
    --port 8000
