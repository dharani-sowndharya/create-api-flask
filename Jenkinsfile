pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "dharanisowndharya/flask-api:${BUILD_NUMBER}"
    }

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'main', credentialsId: 'dharani-git', url: 'https://github.com/dharani-sowndharya/create-api-flask.git'
            }
        }
        stage('Docker Build') {
            steps {
                sh "docker build . -t ${DOCKER_IMAGE}"
            }
        }
        stage('Docker push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'PWD', usernameVariable: 'USER')]) {
                    sh """
                    docker login --username ${USER} --password ${PWD}
                    docker push ${DOCKER_IMAGE}
                    """
                }
                
            }
        }
        stage('Deploy to k8s') {
            steps {
                sh "kubectl get pods"
            }
        }
    }   
}
