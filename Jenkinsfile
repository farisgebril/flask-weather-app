pipeline {
    agent any
    environment {
        WEATHER_API_KEY = credentials('weather-api-key')
        DOCKER_HUB_CREDS = credentials('dockerhub-creds')
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/farisgebril/flask-weather-app.git', 
                     branch: 'main'
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
                sh """
                    docker build \
                    --build-arg WEATHER_API_KEY=${WEATHER_API_KEY} \
                    -t farisgebril/flask-weather-app:latest .
                """
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                sh """
                    echo ${DOCKER_HUB_CREDS_PSW} | docker login \
                    -u ${DOCKER_HUB_CREDS_USR} --password-stdin
                    docker push farisgebril/flask-weather-app:latest
                """
            }
        }
        
        stage('Deploy') {
            steps {
                sh """
                    docker stop weather-app || true
                    docker rm weather-app || true
                    docker run -d \
                    --name weather-app \
                    -p 5000:5000 \
                    farisgebril/flask-weather-app:latest
                """
            }
        }
    }
    post {
        always {
            cleanWs()
            script {
                currentBuild.description = "Build ${currentBuild.id}"
            }
        }
        success {
            slackSend channel: '#builds',
                     color: 'good',
                     message: "SUCCESS: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
        }
        failure {
            slackSend channel: '#builds',
                     color: 'danger',
                     message: "FAILED: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
        }
    }
}
