FROM python:3.9-slim

WORKDIR /opt/responder

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY CommandResponder.py .
COPY manifest.json .

ENTRYPOINT ["python3", "CommandResponder.py"]

