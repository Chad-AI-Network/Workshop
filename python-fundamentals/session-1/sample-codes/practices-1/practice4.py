# `os` est un module prédefini (built-in) donc on a pas besoin de l'installer.
# Pour en savoir un peut plus sur le module (ses propriétés, fonctions et méthodes),
# on peut faire une recherche sur Google
# Par exemple: Comment afficher le contenu d'un dossirer en utilisant le module os de Python

# Importer le module os
import os

# appelle la fonction listdir de os pour récuper le contenu du dossier
contenue = os.listdir("./")

# Afficher le contenue du dossier
print(contenue)
