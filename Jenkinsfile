pipeline {
    agent any

    stages {

        stage('Setup Python Env') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . venv/bin/activate
                python train.py
                '''
            }
        }

        stage('Run Prediction') {
            steps {
                sh '''
                . venv/bin/activate
                python app.py
                '''
            }
        }
    }
}
