pipeline {
    agent any
    parameters {
        string(name: 'PRENOM', description: 'Renseignez votre prénom')
        string(name: 'NOM', description: 'Renseignez votre nom')
        string(name: 'TAILLE', description: 'Renseignez votre taille')
        string(name: 'POIDS', description: 'Renseignez votre poids')
        choice(name: 'SEXE', choices: ['H', 'F'], description: 'Choisir votre sexe')
        choice(name: 'OBJECTIFPOIDS', choices: ['40-50', '50-60', '70-80'], description: 'Choisir votre objectif de poids')

    }
    environment {
        PRENOM = "${params.PRENOM}"
        NOM = "${params.NOM}"
        TAILLE = "${params.TAILLE}"
        POIDS = "${params.POIDS}"
        SEXE = "${params.SEXE}"
        OBJECTIFPOIDS = "${params.OBJECTIFPOIDS}"
    }
    stages {
        stage('Printing name') {
            steps {
                script {

                sh "docker compose down && docker compose up && docker compose down"

                }
            }
        }
   }
}
