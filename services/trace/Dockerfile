# Repository : bigip-icontrol-rce-research
# Path       : services/trace/Dockerfile
# Purpose    : Builds container image for trace and fixture services.
# Layer      : service
# SDLC Phase : release
# ASVS Ref   : V14.2.1
# OWASP Ref  : A06
# Modified   : 2026-04-11
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "server.py"]
