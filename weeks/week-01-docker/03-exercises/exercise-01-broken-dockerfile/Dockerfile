# BUG 2: wrong base — bloated but works
# BUG 3: copies as root then switches user without chown
# BUG 4: no EXPOSE documented, no HEALTHCHECK
FROM python:3.11

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

USER nobody

CMD python app.py
