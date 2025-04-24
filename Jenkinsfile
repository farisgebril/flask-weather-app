pipeline {
    agent any
    environment {
        WEATHER_API_KEY = credentials('weather-api-key')
        DOCKER_HUB_CREDS = credentials('dockerhub-creds')
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/farisgebril/flask-weather-app.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                    --build-arg WEATHER_API_KEY=${WEATHER_API_KEY} \
                    -t farisgebril/flask-weather-app:latest .
                '''
            }
        }
        stage('Push to Docker Hub') {
            steps {
                sh '''
                    echo ${DOCKER_HUB_CREDS_PSW} | docker login -u ${DOCKER_HUB_CREDS_USR} --password-stdin
                    docker push farisgebril/flask-weather-app:latest
                '''
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
