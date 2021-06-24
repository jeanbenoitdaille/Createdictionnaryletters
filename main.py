import string
     
alphabet = string.ascii_lowercase
indices = range(1, len(alphabet) + 1)
liste_zip = zip(indices, alphabet)
resultat = dict(liste_zip)
     
print(resultat)