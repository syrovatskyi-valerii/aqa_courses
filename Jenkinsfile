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
                    set -e

                    apt-get update
                    apt-get install -y python3 python3-dev python3-pip python3.11-venv wget
                    apt-get install -y chromium chromium-driver
                    rm -rf venv
                    python3 -m venv venv
                '''
            }
        }
        stage('Install requirements') {
            steps {
                sh '''#!/bin/bash
                    source ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run tests') {
            steps {
                sh '''#!/bin/bash
                    source ${VENV_PATH}/bin/activate
                    pytest -m "${NAME_MARK}" -s -v --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            script {
                def allureSummary = sh(
                    script: "cat allure-results/widgets/summary.json || true",
                    returnStdout: true
                ).trim()

                def passed = ""
                def failed = ""
                def broken = ""
                def skipped = ""

                if (allureSummary) {
                    def json = readJSON text: allureSummary
                        passed = json.statistic.passed
                        failed = json.statistic.failed
                        broken = json.statistic.broken
                        skipped = json.statistic.skipped
                }

                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]

                sh """
                    rm -f allure-report.zip || true
                    zip -r allure-report.zip allure-report || true
                """

                emailext(
                    subject: "📌 Build #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                    body: """
                        <h2>🔔 Jenkins Build Notification</h2>
                        <p><b>Job:</b> ${env.JOB_NAME}</p>
                        <p><b>Build #:</b> ${env.BUILD_NUMBER}</p>
                        <p><b>Status:</b> <span style="color:${currentBuild.currentResult == 'SUCCESS' ? 'green' : 'red'}">
                            ${currentBuild.currentResult}
                        </span></p>
                        <hr>
                        <h3>📊 Test Results (Allure)</h3>
                        <ul>
                            <li>✅ Passed: ${passed}</li>
                            <li>❌ Failed: ${failed}</li>
                            <li>⚠️ Broken: ${broken}</li>
                            <li>⏭️ Skipped: ${skipped}</li>
                        </ul>
                        <hr>
                        <p><b>Branch:</b> ${env.GIT_BRANCH}</p>
                        <p><b>Commit:</b> ${env.GIT_COMMIT}</p>
                        <p><b>Started by:</b> ${currentBuild.getBuildCauses()[0].userName ?: 'Auto/SCM Trigger'}</p>
                        <p><b>Build URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                        <p><b>Allure Report:</b> <a href="${env.BUILD_URL}allure">Click here to view in browser</a></p>
                        <p><b>Allure Report File:</b> attached as <i>allure-report.zip</i></p>
                    """,
                    mimeType: 'text/html',
                    to: "valerii.aliens@gmail.com",
                    attachmentsPattern: "allure-report.zip"
                )
            }
        }
    }
}
