FROM python:3.11
WORKDIR /
COPY app.py .
CMD ["python3", "app.py"]