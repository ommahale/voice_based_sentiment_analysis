FROM python:3.11.3

WORKDIR /app/api

COPY . .
RUN pip --version
RUN pip install --upgrade pip
RUN pip install numpy pandas tensorflow uvicorn fastapi python-multipart librosa 

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["python", "main.py", "0.0.0.0", "8000"]