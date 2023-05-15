pipeline {
    agent any
    parameters {
        string(name: 'PRENOM', description: 'Renseignez votre prénom')
        string(name: 'NOM', description: 'Renseignez votre nom')
        string(name: 'TAILLE', description: 'Renseignez votre taille')
        string(name: 'POIDS', description: 'Renseignez votre poids')
        choice(name: 'SEXE', choices: ['H', 'F'], description: 'Choisir votre sexe')
        choice(name: 'OBJECTIFPOIDS', choices: ['40-50', '50-60', '60-70'], description: 'Choisir votre objectif de poids')
        choice(name: 'OBJECTIFPRECEDENT', choices: ['Réussi', 'En cours', 'Échoué',"Nouveau (Pas d'objectif précédent)"], description: 'Indiquer le statut de votre objectif précédent')
    }
    environment {
        PRENOM = "${params.PRENOM}"
        NOM = "${params.NOM}"
        TAILLE = "${params.TAILLE}"
        POIDS = "${params.POIDS}"
        SEXE = "${params.SEXE}"
        OBJECTIFPOIDS = "${params.OBJECTIFPOIDS}"
        OBJECTIFPRECEDENT = "${params.OBJECTIFPRECEDENT}"
    }
    stages {
        stage('Printing name') {
            steps {
                script {

                sh "docker compose down && docker rm -f $(docker ps -a -q) && docker volume rm $(docker volume ls -q) && docker rmi -f $(docker image ls -q) && docker compose build --no-cache && docker compose up"

                }
            }
        }
   }
}
