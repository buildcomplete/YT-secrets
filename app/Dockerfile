FROM python:3-alpine
RUN apk update

# Create main folder for attached storage
RUN mkdir /storage
WORKDIR /App
CMD ["python", "secret-sharing-app.py"]