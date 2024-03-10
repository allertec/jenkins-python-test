pipeline {
  environment {
     imagename = "allertec/python-script"
  }
  agent any
  stages {
    stage('Clone Git') {
      steps {
        git([url: 'https://github.com/allertec/jenkins-python-test.git', branch: 'main'])
 
      }
    }
    stage('Build image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
  }
}
