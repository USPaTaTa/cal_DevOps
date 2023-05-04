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
    stages {
        stage('Printing name') {
            steps {
                script {
                    
                docker.build("jenkins-docker")

                }
            }
        }
   }
}
