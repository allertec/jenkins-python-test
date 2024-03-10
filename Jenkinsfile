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
      steps {
        sh("""sudo chmod 777 /var/run/docker.sock""")
      }
    }
    stage('Build image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Run image') {
      steps {
          sh("""docker run --name py-script ${imagename}
             ls -l
             cat artifact""")
      }
    }
  }
}
