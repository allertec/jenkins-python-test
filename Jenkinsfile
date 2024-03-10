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
    stage('Upload to ECR') {
      steps{
          withCredentials([[$class: "AmazonWebServicesCredentialsBinding", credentialsId: 'aws-credentials']]) {
            sh """
              aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 161192472568.dkr.ecr.us-east-1.amazonaws.com
              docker tag ${imagename} 161192472568.dkr.ecr.us-east-1.amazonaws.com/${imagename}
              docker push 161192472568.dkr.ecr.us-east-1.amazonaws.com/${imagename}
            """
          }
        }
    }
    stage('Run image') {
      steps {
          sh("""docker run --name py-script ${imagename}
             ls -l
             cat artifact
             docker rm -f py-script
             docker rmi -f ${imagename}""")
      }
    }
    stage('Upload S3'){
      steps {
        withCredentials([[$class: "AmazonWebServicesCredentialsBinding", credentialsId: 'aws-credentials']]) {
          sh """
             aws s3 mv artifact-${currentBuild.number} s3://andrzejb
          """
       }
      }
    }
  }
}
