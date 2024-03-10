pipeline {
  environment {
     imagename = "allertec/python-script:${currentBuild.number}"
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
    stage('Run image') {
      steps {
          sh("""
             rm -f artifact
             docker rm -f py-script
             docker run -v .:/usr/app/src --name py-script ${imagename}
             mv artifact artifact-${currentBuild.number}
             docker rm -f py-script""")
      }
    }
    stage('Upload S3'){
      steps {
        withCredentials([[$class: "AmazonWebServicesCredentialsBinding", credentialsId: 'aws-credentials']]) {
          sh """
             aws s3 mv artifact-${currentBuild.number} s3://andrzejb
             rm -f artifact-${currentBuild.number}
          """
       }
      }
    }
    stage('Upload to ECR') {
      steps{
          withCredentials([[$class: "AmazonWebServicesCredentialsBinding", credentialsId: 'aws-credentials']]) {
            sh """
              aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 161192472568.dkr.ecr.us-east-1.amazonaws.com
              docker tag ${imagename} 161192472568.dkr.ecr.us-east-1.amazonaws.com/${imagename}
              docker push 161192472568.dkr.ecr.us-east-1.amazonaws.com/${imagename}
              docker rmi -f 161192472568.dkr.ecr.us-east-1.amazonaws.com/${imagename}
              docker rmi -f ${imagename}
            """
          }
        }
    }
  }
}
