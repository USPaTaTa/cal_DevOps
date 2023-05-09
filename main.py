import fatsecret
import os

print(type(os.environ.get("PRENOM")))
print(type(os.environ.get("NOM")))
print(type(os.environ.get("TAILLE")))
print(type(os.environ.get("POIDS")))
print(type(os.environ.get("SEXE")))
print(type(os.environ.get("OBJECTIFPOIDS")))
print(type(os.environ.get("OBJECTIFPRECEDENT")))

objectifseance = fatsecret.fatsecret(os.environ.get("PRENOM"), os.environ.get("NOM"), os.environ.get("TAILLE"), os.environ.get("POIDS"), os.environ.get("SEXE"), os.environ.get("OBJECTIFPOIDS"), os.environ.get("OBJECTIFPRECEDENT"))



objectifseance.exec()