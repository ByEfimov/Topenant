FROM python:3.9
# stdder stddin
ENV PYTHONUNBUFFERED=1
# python dont create .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Dockerfile
ENV OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

WORKDIR /topinant-backend


RUN apt-get update && apt-get install -y \
    libfontconfig1 \
    libxrender1 \
    wget \
    xfonts-75dpi \
    xfonts-base \
    libssl3

RUN apt-get update \
    && apt-get install -y wkhtmltopdf \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . /topinant-backend/