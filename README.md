# Createdictionnaryletters
Créer un dictionnaire avec les lettres de l' alphabet
Dans cet exercice, nous utilisons la fonction zip, pour construire un dictionnaire comprenant les lettres de l'alphabet et leur position dans l'alphabet.

Pour commencer, nous récupérons toutes les lettres de l'alphabet en minuscule, grâce au module string :

    >>> alphabet = string.ascii_lowercase
    >>> print(alphabet)
    'abcdefghijklmnopqrstuvwxyz'

Ensuite, on créé une liste qui contient les nombres de 1 à la longueur de l'alphabet, grâce à la fonction range et la fonction len :

    >>> indices = range(1, len(alphabet) + 1)
    >>> print(indices)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

On ajoute 1 à la longueur de l'alphabet car notre liste commence à 1 et non 0.

On utilise ensuite la fonction zip, qui permet de créer une liste de tuples à partir de deux listes (la liste de nombres et les lettres de l'alphabet) :

    >>> liste_zip = zip(indices, alphabet)
    >>> print(list(liste_zip))
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j'),
     (11, 'k'), (12, 'l'), (13, 'm'), (14, 'n'), (15, 'o'), (16, 'p'), (17, 'q'), (18, 'r'), (19, 's'),
     (20, 't'), (21, 'u'), (22, 'v'), (23, 'w'), (24, 'x'), (25, 'y'), (26, 'z')

Il ne nous reste plus qu'à utiliser la fonction dict pour convertir cette liste de tuple en dictionnaire.
En effet, vous pouvez passer une liste contenant des tuples contenant deux éléments et la fonction dict va utiliser le premier élément comme clé et le deuxième élément comme valeur :

    >>> resultat = dict(liste_zip)
    >>> print(resultat)
    {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
     13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
     24: 'x', 25: 'y', 26: 'z'}
