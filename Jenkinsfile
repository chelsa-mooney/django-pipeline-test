pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''#!/bin/bash
pip3 install -r requirements.txt
            '''
      }
    }

    stage('Test') {
      steps {
        sh '''#!/bin/bash
python3 DjangoPipelineTest/manage.py test
            '''
      }
    }

  }
}