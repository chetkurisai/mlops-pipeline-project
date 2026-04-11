pipeline {
    agent any

    stages {

        stage('Run Test') {
            steps {
                sh 'python3 test_app.py'
            }
        }

        stage('Run App') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
