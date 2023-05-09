import fatsecret
import os

objectifseance = fatsecret.fatsecret(os.environ.get("PRENOM"), os.environ.get("NOM"), os.environ.get("TAILLE"), os.environ.get("POIDS"), os.environ.get("SEXE"), os.environ.get("OBJECTIFPOIDS"), os.environ.get("OBJECTIFPRECEDENT"))

objectifseance.exec()