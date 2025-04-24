FROM python:3.9-slim
ARG WEATHER_API_KEY
ENV WEATHER_API_KEY=$WEATHER_API_KEY
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
