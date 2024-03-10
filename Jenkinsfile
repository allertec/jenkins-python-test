pipeline {
  environment {
     imagename = "andrzejb:${currentBuild.number}"
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
             rm -f artifact artifact-latest
             docker rm -f py-script
             docker run -v .:/usr/app/src --name py-script ${imagename}
             cp artifact artifact-${currentBuild.number}
             cp artifact artifact-latest
             docker rm -f py-script""")
      }
    }
    stage('Upload S3'){
      steps {
        withCredentials([[$class: "AmazonWebServicesCredentialsBinding", credentialsId: 'aws-credentials']]) {
          sh """
             aws s3 mv artifact-${currentBuild.number} s3://andrzejb
             aws s3 mv artifact-latest s3://andrzejb
             rm -f artifact-${currentBuild.number} artifact-latest artifact
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
    stage('Test'){
      steps {
        input 'Do you want to run test?'
        withCredentials([[$class: "AmazonWebServicesCredentialsBinding", credentialsId: 'aws-credentials']]) {
          sh """
          aws s3 mv s3://andrzejb/andrzej-latest .
          if [[ -s andrzej-latest ]]; then
            cat andrzej-test
          else
            echo "File andrzej-latest is empty"
          fi
          """
        }
      }
    }
  }
}
