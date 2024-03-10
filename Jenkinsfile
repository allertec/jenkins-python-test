pipeline {
  environment {
     imagename = "allertec/python-script"
     ecr_repo = "https://161192472568.dkr.ecr.us-east-1.amazonaws.com"
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
    // stage('Upload to ECR') {
    //   steps{
    //     script {
    //     (docker.withRegistry(${env.ecr_repo}, "ecr:us-east-1:aws-credentials") {
    //       docker.image(${env.imagename}).push()
    //       }) }
    //     }
    // }
    stage('Run image') {
      steps {
          sh("""docker run --name py-script ${imagename}
             ls -l
             cat artifact""")
      }
    }
  }
}
