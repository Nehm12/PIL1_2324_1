<<<<<<< HEAD

print("Bienvenue sur le site de connexion")
mot_de_passe = "peniel123"
indentifiant = input("Entrez votre identifiant: ")
password = input("Entrez votre mot de passe: ")
if password == mot_de_passe:
    print("Bienvenue {}".format(indentifiant))
else:
    print("Mot de passe incorect {} Réessayer" .format(indentifiant))
