pipeline {
  agent any

  stages {
    stage ('Build') {
      steps {
        sh 'docker build -t server-status:preliminary .'
      }
    }
    stage ('Validate') {
      steps {
        sh 'pwd'
      }
    }
    stage ('Tag and Push to Repo') {
      steps {
        sh 'docker tag server-status:preliminary server-status-ui:master'
      }
    }
    stage ('Update infrastructure') {
      steps {
        echo "Deploy to ${BRANCH_NAME}"
      }
    }
  }
}
