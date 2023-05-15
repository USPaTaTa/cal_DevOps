# Import de bibliothèque pour se connecter à une base de données MySQL
import mysql.connector
from datetime import datetime

# récupération de la date et de l'heure actuelle


class fatsecret:
  """Objet """
  def __init__(self, prenom=str, nom=str, taille=int, poids=float, sexe=str, objectifpoids=str, objectifprecedent=str):
    self.prenom = str(prenom)
    self.nom = str(nom)
    self.taille = int(taille)
    self.poids = float(poids)
    self.sexe = str(sexe)
    self.objectifpoids = str(objectifpoids)
    self.objectifprecedent = str(objectifprecedent)
    self.IMC()
    self.time = datetime.now()
    self.bdd = mysql.connector.connect(
      host="mysql",
      user="sysadmin",
      password="sysadmin1234"
    ) 
    # self.interpetration_IMC()
    
  def interpetration_IMC(self):
    if self.imc == None:
      raise Exception('Erreur dans la fonction interpetrationIMC')
    if self.imc < 16.5:
      self.interpretationIMC = 'Dénutrition ou famine'
      return 'Dénutrition ou famine'
    elif self.imc >= 16.5 and self.imc < 18.5:
      self.interpetrationIMC = 'Maigreur'
      return 'Maigreur'
    elif self.imc >= 18.5 and self.imc < 25:
      self.interpetrationIMC = 'Corpulence normale'
      return 'Corpulence normale'
    elif self.imc >= 25 and self.imc < 30:
      self.interpetrationIMC = 'Surpoids'
      return 'Surpoids'
    elif self.imc >= 30 and self.imc < 35:
      self.interpetrationIMC = 'Obésité modérée'
      return 'Obésité modérée'
    elif self.imc >= 35 and self.imc < 40:
      self.interpetrationIMC = 'Obésité sévère'
      return 'Obésité sévère'
    elif self.imc >= 40:
      self.interpetrationIMC = 'Obésité morbide ou massive'
      return 'Obésité morbide ou massive'
    else:
      raise Exception('Erreur dans la fonction interpetrationIMC')
  
  def IMC(self):
    taille_m = self.taille / 100
    imc = self.poids / (taille_m ** 2)
    self.imc = round(imc, 2)
    return imc
  
  def exec(self):
    print('---------------------------------')
    print('EXECUTION DU PROGRAMME')
    print(f'Prénom: {self.prenom}')
    print(f'Nom: {self.nom}')
    print(f'Taille: {self.taille}')
    print(f'Poids: {self.poids}')
    print(f'Sexe: {self.sexe}')
    print(f'Objectif poids: {self.objectifpoids}')
    print(f'Objectif précédent: {self.objectifprecedent}')
    print(f'IMC: {self.imc}')
    print(f'Interprétation IMC: {self.interpetration_IMC()}')
    print('---------------------------------')
    if self.sexe == "H":
      if self.objectifprecedent == "Réussi":
        if self.objectifpoids == "40-50":
          if self.imc < 16.5:
            print("Programme proposé: Programme sportif C et Programme alimentaire D ou Programme sportif E et Programme alimentaire B")
          elif self.imc >= 16.5 and self.imc < 18.5:
            print("Programme proposé: Programme sportif B et Programme alimentaire C ou Programme sportif A et Programme alimentaire B")
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif D et Programme alimentaire D ou Programme sportif D et Programme alimentaire E')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire D ou Programme sportif B et Programme alimentaire C')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif E et Programme alimentaire E ou Programme sportif C et Programme alimentaire D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire C ou Programme sportif C et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire C ou Programme sportif B et Programme alimentaire B')
        if self.objectifpoids == "50-60":
          if self.imc < 16.5:
            print("Programme proposé: Programme sportif C et Programme alimentaire D ou Programme sportif E et Programme alimentaire B")
          elif self.imc >= 16.5 and self.imc < 18.5:
            print("Programme proposé: Programme sportif B et Programme alimentaire C ou Programme sportif A et Programme alimentaire B")
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif D et Programme alimentaire D ou Programme sportif D et Programme alimentaire E')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire D ou Programme sportif B et Programme alimentaire C')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif E et Programme alimentaire E ou Programme sportif C et Programme alimentaire D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire C ou Programme sportif C et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire C ou Programme sportif B et Programme alimentaire B')
        if self.objectifpoids == "60-70":
          if self.imc < 16.5:
            print("Programme proposé: Programme sportif C et Programme alimentaire D ou Programme sportif E et Programme alimentaire B")
          elif self.imc >= 16.5 and self.imc < 18.5:
            print("Programme proposé: Programme sportif B et Programme alimentaire C ou Programme sportif A et Programme alimentaire B")
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif D et Programme alimentaire D ou Programme sportif D et Programme alimentaire E')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire D ou Programme sportif B et Programme alimentaire C')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif E et Programme alimentaire E ou Programme sportif C et Programme alimentaire D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire C ou Programme sportif C et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire C ou Programme sportif B et Programme alimentaire B')
      if self.objectifprecedent == "En cours":
        if self.objectifpoids == "40-50":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif C et Programme alimentaire C')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif C et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
        if self.objectifpoids == "50-60":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif C et Programme alimentaire C')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif C et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
        if self.objectifpoids == "60-70":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif C et Programme alimentaire C')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif C et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
      if self.objectifprecedent == "Échoué":
        if self.objectifpoids == "40-50":
          if self.imc < 16.5:
            print('Programme proposé: Programme alimentaire B et Programme sportif B ou Programme sportif A et Programme alimentaire A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme alimentaire D et Programme sportif D ou Programme sportif A et Programme alimentaire A')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme alimentaire C et Programme sportif B ou Programme sportif D et Programme alimentaire E')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme alimentaire C et Programme sportif C ou Programme sportif A et Programme alimentaire B')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme alimentaire C et Programme sportif C ou Programme sportif E et Programme alimentaire A')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme alimentaire E et Programme sportif E ou  Programme sportif A et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme alimentaire B et Programme sportif A ou Programme sportif  et Programme alimentaire C')
        if self.objectifpoids == "50-60":
          if self.imc < 16.5:
            print('Programme proposé: Programme alimentaire B et Programme sportif B ou Programme sportif A et Programme alimentaire A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme alimentaire D et Programme sportif D ou Programme sportif A et Programme alimentaire A')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme alimentaire C et Programme sportif B ou Programme sportif D et Programme alimentaire E')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme alimentaire C et Programme sportif C ou Programme sportif A et Programme alimentaire B')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme alimentaire C et Programme sportif C ou Programme sportif E et Programme alimentaire A')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme alimentaire E et Programme sportif E ou  Programme sportif A et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme alimentaire B et Programme sportif A ou Programme sportif  et Programme alimentaire C')
        if self.objectifpoids == "60-70":
          if self.imc < 16.5:
            print('Programme proposé: Programme alimentaire B et Programme sportif B ou Programme sportif A et Programme alimentaire A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme alimentaire D et Programme sportif D ou Programme sportif A et Programme alimentaire A')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme alimentaire C et Programme sportif B ou Programme sportif D et Programme alimentaire E')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme alimentaire C et Programme sportif C ou Programme sportif A et Programme alimentaire B')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme alimentaire C et Programme sportif C ou Programme sportif E et Programme alimentaire A')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme alimentaire E et Programme sportif E ou  Programme sportif A et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme alimentaire B et Programme sportif A ou Programme sportif  et Programme alimentaire C')
      if self.objectifprecedent == "Nouveau (Pas d'objectif précédent)":
        if self.objectifpoids == "40-50":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif C et Programme alimentaire C')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif C et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
        if self.objectifpoids == "50-60":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif C et Programme alimentaire C')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif C et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
        if self.objectifpoids == "60-70":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif C et Programme alimentaire C')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif C et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
    else:
      if self.objectifprecedent == "Réussi":
        if self.objectifpoids == "40-50":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire C ou Programme sportif A et Programme alimentaire B')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif C et Programme alimentaire D ou Programme sportif E et Programme alimentaire B')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif C et Programme alimentaire A')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire D ou Programme sportif B et Programme alimentaire C')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif D et Programme alimentaire A ou Programme sportif A et Programme alimentaire C')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire D ou Programme sportif E et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire B ou Programme sportif E et Programme alimentaire C')
        if self.objectifpoids == "50-60":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire C ou Programme sportif A et Programme alimentaire B')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif C et Programme alimentaire D ou Programme sportif E et Programme alimentaire B')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif C et Programme alimentaire A')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire D ou Programme sportif B et Programme alimentaire C')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif D et Programme alimentaire A ou Programme sportif A et Programme alimentaire C')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire D ou Programme sportif E et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire B ou Programme sportif E et Programme alimentaire C')
        if self.objectifpoids == "60-70":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire C ou Programme sportif A et Programme alimentaire B')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif C et Programme alimentaire D ou Programme sportif E et Programme alimentaire B')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif C et Programme alimentaire A')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif E et Programme alimentaire D ou Programme sportif B et Programme alimentaire C')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif D et Programme alimentaire A ou Programme sportif A et Programme alimentaire C')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif E et Programme alimentaire D ou Programme sportif E et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif A et Programme alimentaire B ou Programme sportif E et Programme alimentaire C')
      if self.objectifprecedent == "En cours":
        if self.objectifpoids == "40-50":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif A et Programme alimentaire A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif D et Programme alimentaire A')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire D')
        if self.objectifpoids == "50-60":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif A et Programme alimentaire A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif D et Programme alimentaire A')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire D')
        if self.objectifpoids == "60-70":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif A et Programme alimentaire A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif D et Programme alimentaire A')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire D')
      if self.objectifprecedent == "Échoué":
        if self.objectifpoids == "40-50":
          if self.imc < 16.5:
            print('Programme proposé: Programme alimentaire A et Programme sportif A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme alimentaire B et Programme sportif B ou Programme sportif A et Programme alimentaire A')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme alimentaire B et Programme sportif B ou Programme sportif A et Programme alimentaire C')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme alimentaire D et Programme sportif A ou Programme sportif C et Programme alimentaire C')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme alimentaire A et Programme sportif D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme alimentaire D et Programme sportif E ou Programme sportif E et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme alimentaire E et Programme sportif E ou Programme sportif  et Programme alimentaire B')
        if self.objectifpoids == "50-60":
          if self.imc < 16.5:
            print('Programme proposé: Programme alimentaire A et Programme sportif A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme alimentaire B et Programme sportif B ou Programme sportif A et Programme alimentaire A')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme alimentaire B et Programme sportif B ou Programme sportif A et Programme alimentaire C')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme alimentaire D et Programme sportif A ou Programme sportif C et Programme alimentaire C')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme alimentaire A et Programme sportif D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme alimentaire D et Programme sportif E ou Programme sportif E et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme alimentaire E et Programme sportif E ou Programme sportif  et Programme alimentaire B')
        if self.objectifpoids == "60-70":
          if self.imc < 16.5:
            print('Programme proposé: Programme alimentaire A et Programme sportif A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme alimentaire B et Programme sportif B ou Programme sportif A et Programme alimentaire A')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme alimentaire B et Programme sportif B ou Programme sportif A et Programme alimentaire C')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme alimentaire D et Programme sportif A ou Programme sportif C et Programme alimentaire C')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme alimentaire A et Programme sportif D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme alimentaire D et Programme sportif E ou Programme sportif E et Programme alimentaire C')
          elif self.imc >= 40:
            print('Programme proposé: Programme alimentaire E et Programme sportif E ou Programme sportif  et Programme alimentaire B')
      if self.objectifprecedent == "Nouveau (Pas d'objectif précédent)":
        if self.objectifpoids == "40-50":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif A et Programme alimentaire A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif D et Programme alimentaire A')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire D')
        if self.objectifpoids == "50-60":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif A et Programme alimentaire A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif D et Programme alimentaire A')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire D')
        if self.objectifpoids == "60-70":
          if self.imc < 16.5:
            print('Programme proposé: Programme sportif A et Programme alimentaire A')
          elif self.imc >= 16.5 and self.imc < 18.5:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 18.5 and self.imc < 25:
            print('Programme proposé: Programme sportif B et Programme alimentaire B')
          elif self.imc >= 25 and self.imc < 30:
            print('Programme proposé: Programme sportif D et Programme alimentaire A')
          elif self.imc >= 30 and self.imc < 35:
            print('Programme proposé: Programme sportif A et Programme alimentaire D')
          elif self.imc >= 35 and self.imc < 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire E')
          elif self.imc >= 40:
            print('Programme proposé: Programme sportif D et Programme alimentaire D')
    print('---------------------------------')
    
      # Insertion des données dans la base de données
    self.cursor = self.bdd.cursor()
    self.cursor.execute('USE bdd_fatsecret')
    formatted_time = self.time.strftime('%d/%m/%Y à %H:%M:%S')
    self.cursor.execute('''INSERT INTO fatsecret (date_time, nom, prenom, sexe, poids, taille, imc, objectifpoids, objectifprecedent, interpretation_IMC) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (formatted_time,self.nom, self.prenom, self.sexe, str(self.poids), str(self.taille), str(self.imc), self.objectifpoids, self.objectifprecedent, self.interpetrationIMC))
    # Affichage des données insérées
    self.cursor.execute('''SELECT * FROM fatsecret''')
    print(self.cursor.fetchall())