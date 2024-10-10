pipeline {
    agent any

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'main', credentialsId: 'dharani-git', url: 'https://github.com/dharani-sowndharya/create-api-flask.git'
            }
        }
        stage('Docker Build') {
            steps {
                sh "docker build . -t ${BUILD_NUMBER}"
            }
        }
    }   
}
