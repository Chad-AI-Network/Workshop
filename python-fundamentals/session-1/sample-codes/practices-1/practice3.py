# Importer pyjokes
import pyjokes

# Creer une blague en français
joke = pyjokes.get_joke(language="fr", category="all")

# Afficher la blague
print(joke)
