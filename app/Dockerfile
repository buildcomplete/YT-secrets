FROM python:3-alpine
RUN apk update

# Create main folder for attached storage
RUN mkdir /storage
RUN mkdir /storage/secrets
WORKDIR /App
ENV PYTHONPATH=/App
CMD ["python", "-m", "unittest", "discover", "-v"]