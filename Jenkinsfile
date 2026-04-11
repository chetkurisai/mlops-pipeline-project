pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mlops-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run mlops-app'
            }
        }
    }
}
