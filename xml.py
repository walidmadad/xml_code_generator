# Autor: Walid Madad
# Date: 24/09/2024
# Ce module permet de générer des balises XML sous forme de chaîne de caractères.
# L'utilisateur peut spécifier le nom de la balise, son contenu et ses attributs.

def myxml(nom, content='', **attributs):
    """Cette fonction permet de créer une balise XML avec un nom, un contenu et des attributs."""

    result = f"<{nom}" # Ajouter la balise ouvrante

    # Ajoute les attributs s'ils existent
    for cle, valeur in attributs.items():
        result += f' {cle}="{valeur}"'


    result += f">{content}</{nom}>" # Ferme la balise et ajouter le contenu

    # Retourner le code XML
    return result

# Exemples d'utilisation
print(myxml('star'))  # <star></star>
print(myxml('star', 'moon'))  # <star>moon</star>
print(myxml('star', 'moon', a=1, b=2, c=3))  # <star a="1" b="2" c="3">moon</star>