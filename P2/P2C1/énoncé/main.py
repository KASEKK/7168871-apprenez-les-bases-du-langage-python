def main():
    # Ecrivez votre code ici !
    
    # Attention tout votre code doit être indenté comme ce commentaire
# 1. Créez deux variables `nombre_a_gauche` et `nombre_a_droite` , 
# et affectez-leur chacune un nombre entier à l'aide d'un input.
# variable = input("chaine de caractères")

    nombre_a_gauche = input("5")
    nombre_a_droite = input("2")

# 2. Créez une variable `operation` pour stocker le symbole d'opération **(+, -, * ou /)**.
# L'opérateur sera aussi demander à l'aide de la fonction `input()`.

    operation = input("+")

# 3. Créez une dernière variable `resultat` initialisée à 0, 
# qui contiendra ensuite le résultat du calcul.

    resultat = 0

# 4. Vérifier les deux nombres entiers et si pas afficher message d'erreur
    
    if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric():
        print('Erreur: les deux nombres doivent être des nombres entiers') 

# Et si c'est possible, convertissez les en nombre entier int

    else: 
        nombre_a_droite = int(nombre_a_droite)
        nombre_a_gauche = int(nombre_a_gauche)

# Vérifiez que le symbole stocké dans la variable `operation` correspond bien à 
# une des 4 opérations autorisées (+, -, * ou /) à l’aide d'une structure `match` 
# et effectuez le calcul correspondant dans chaque cas. 

    match operation:
            case '+':
                resultat = nombre_a_gauche + nombre_a_droite
            case '-':
                resultat = nombre_a_gauche - nombre_a_droite
            case '*':
                resultat = nombre_a_gauche * nombre_a_droite

# Il est impossible de diviser un nombre par 0, 
# Utilisez les conditions if-else pour réaliser cette opération ; 
# s’il y a une division par 0, affichez `Erreur: impossible de diviser par zéro.`

            case '/':
                if nombre_a_droite == 0:
                    print("Erreur: impossible de diviser par zéro.")

# Stockez le résultat dans la variable `resultat`.
               
                else:
                    resultat = nombre_a_gauche / nombre_a_droite

# Si le symbole n'est pas correct, 
# affichez un message d'erreur correspondant, et quittez le programme.

            case _:
                print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
            
# Afficher le résultat

    print(f"Le résultat de l'opération {nombre_a_gauche} {operation} {nombre_a_droite} est {resultat}")


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()