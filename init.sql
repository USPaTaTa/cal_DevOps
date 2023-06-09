USE `bdd_fatsecret`;

CREATE TABLE fatsecret(
  idfatsecret int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  date_time varchar(255) NOT NULL,
  nom varchar(255) NOT NULL,
  prenom varchar(255) NOT NULL,
  sexe varchar(255) NOT NULL,
  poids varchar(255) NOT NULL,
  taille varchar(255) NOT NULL,
  imc varchar(255) NOT NULL,
  objectifpoids varchar(255) NOT NULL,
  objectifprecedent varchar(255) NOT NULL,
  interpretation_IMC varchar(255) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;