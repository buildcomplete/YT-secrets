FROM python:3-alpine
RUN apk update
RUN pip install flask
RUN pip install flask-unittest
RUN pip install pytest
RUN pip install gunicorn
RUN pip install cryptography

# Create main folder for attached storage
RUN mkdir /storage
RUN mkdir /storage/secrets
WORKDIR /App
ENV PYTHONPATH=/App
#CMD ["flask","--app", "code/SecretController",  "run", "-h", "0.0.0.0", "-p", "5000"]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "code.wsgi:app"]