pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/syrovatskyi-valerii/aqa_courses.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''#!/bin/bash
                    set -e  # зупинятися при будь-якій помилці

                    # -----------------------------
                    # Оновлення пакетів
                    # -----------------------------
                    apt-get update

                    # -----------------------------
                    # Встановлюємо Python + venv + pip
                    # -----------------------------
                    apt-get install -y python3 python3-dev python3-pip python3.11-venv wget

                    # -----------------------------
                    # Встановлюємо Chromium та драйвер
                    # -----------------------------
                    apt-get install -y chromium chromium-driver

                    # -----------------------------
                    # Створюємо та активуємо віртуальне оточення
                    # -----------------------------
                    rm -rf venv
                    python3 -m venv venv'''
            }
        }
        stage('Install requirements') {
            steps {
                sh '''#!/bin/bash
                    source venv/bin/activate
                    pip install -r requirements.txt'''
            }
        }
        stage('Run tests') {
            steps {
                sh '''#!/bin/bash
                    source venv/bin/activate
                    pytest -m "${NAME_MARK}" -s -v --alluredir=allure-results'''
            }
        }

    }
    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }

}