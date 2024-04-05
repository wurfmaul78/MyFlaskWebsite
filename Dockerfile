# Verwende ein Python-Basisimage
FROM python:3.8-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Dateien `app.py`, `sources`-Ordner und `requirements.txt` in das Arbeitsverzeichnis im Container
COPY app.py .
COPY sources sources/
COPY requirements.txt .

# Installiere die erforderlichen Python-Abhängigkeiten
RUN apt update
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]