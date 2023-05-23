FROM tensorflow/tensorflow:2.4.1-gpu

WORKDIR /app/api

COPY . .
RUN pip --version
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["python", "main.py"]