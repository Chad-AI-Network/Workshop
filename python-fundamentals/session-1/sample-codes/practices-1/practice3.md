# Intaller un module externe

Pour installer un module, en utilise la commande `install` du gestionnaire de paquets de Python (pip).

```bash
pip install nom_du_paquet
```

Par exemple si on veut installer le module `pyjokes` la commande serait:

```bash
pip install pyjokes
```

On peut l'utiliser comme suit.

```python
# Importer pyjokes
import pyjokes

# Creer une blague en français
joke = pyjokes.get_joke(language="fr", category="all")

# Afficher la blague
print(joke)
```

Ceci n'a pas marché lors de la session car on avait nommé le fichier contenant le code `pyjokes.py` alors que `pyjokes` est le nom du module.

Notons que pour utiliser un module il faut au préalable l'installer. Aussi on ne peut l'utiliser dans notre code sans l'avoir importer.
