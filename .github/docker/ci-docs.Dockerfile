FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        make \
        graphviz \
        libenchant-2-2 \
        latexmk \
        texlive-latex-base \
        texlive-fonts-recommended \
        texlive-fonts-extra \
        texlive-latex-extra \
        texlive-xetex \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
