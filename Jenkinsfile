pipeline {
    agent any

    environment {
        NAME_MARK = "ui_tests"
        VENV_PATH = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/syrovatskyi-valerii/aqa_courses.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''#!/bin/bash
                    set -e  # stop if errrs exisit

                    # -----------------------------
                    # update package
                    # -----------------------------
                    apt-get update

                    # -----------------------------
                    # install Python + venv + pip
                    # -----------------------------
                    apt-get install -y python3 python3-dev python3-pip python3.11-venv wget

                    # -----------------------------
                    # install Chromium and driver
                    # -----------------------------
                    apt-get install -y chromium chromium-driver

                    # -----------------------------
                    # create venv
                    # -----------------------------
                    rm -rf venv
                    python3 -m venv venv'''
            }
        }
        stage('Install requirements') {
            steps {
                sh '''#!/bin/bash
                    source ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt'''
            }
        }
        stage('Run tests') {
            steps {
                sh '''#!/bin/bash
                    source ${VENV_PATH}/bin/activate
                    pytest -m "${NAME_MARK}" -s -v --alluredir=allure-results'''
            }
        }
    }

    post {
        always {
            // generate Allure-report
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]

            // Send email to valerii.aliens@gmail.com
            emailext (
                subject: "Build #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                body: """
                Build #${env.BUILD_NUMBER} finished with status: ${currentBuild.currentResult}.
                See details: ${env.BUILD_URL}
                """,
                to: "valerii.aliens@gmail.com"
            )
        }
    }
}
