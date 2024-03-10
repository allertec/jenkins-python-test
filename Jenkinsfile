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
    stage('Setup docker.sock permissions') {
      sh("""chmod 777 /var/run/docker.sock""")
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
