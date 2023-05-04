pipeline {
    agent any
    parameters {
        string(name: 'NAME', description: 'Please tell me your name')
        choice(name: 'BRANCH', choices: ['DEV', 'MASTER'], description: 'Choose the branch')
        text(name: 'DESC', description: 'Describe about the job details')
        booleanParam(name: 'SKIP_TEST', description: 'Want to skip running Test cases?')
        password(name: 'SONAR_SERVER_PWD', description: 'Enter SONAR password')
    }
    stages {
        stage('Printing name') {
            steps {
                script {
                    def name = "${'test'}"
                    def desc = "${params.DESC}"
                    def branch = "${params.BRANCH}"
                    def skip_test = "${params.SKIP_TEST}"
                    def sonar_server_pwd = "${params.SONAR_SERVER_PWD}"

                     echo "$name"
                      echo "$desc"
                       echo "$branch"
                        echo "$skip_test"
                         echo "$sonar_server_pwd"
                    python /var/jenkins_home/python/fatsecret.py
                       


                }
            }
        }
   }
}
