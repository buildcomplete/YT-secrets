FROM python:3-alpine
RUN apk update
RUN pip install flask
RUN pip install flask-unittest
RUN pip install pytest

# Create main folder for attached storage
RUN mkdir /storage
RUN mkdir /storage/secrets
WORKDIR /App
ENV PYTHONPATH=/App
CMD ["flask","--app", "code/SecretController",  "run", "-h", "0.0.0.0", "-p", "5000"]