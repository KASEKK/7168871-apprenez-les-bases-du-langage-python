# Écrivez votre code ici !
adresses = {
    # Dictionnaire = {"key": "value", "key": "value"}
    "sandra": "chatelet",
    "jean": "pont de loup",
    "kevin": "marcinelle"
}
# Dictionnaire["key"] = "value"
# value = dictionnaire["key"]
adresses["laura"] = "mons"

# """3. **Accédez** à la valeur correspondant à la clé `"jean"` et 
# stockez-la dans une variable appelée `adresse_jean`. variable = dict["key"]
adresse_jean = adresses["jean"]

#  4. **Modifiez** la valeur associée à la clé `"sandra"` pour `"gilly"`. dict["key"] = "value"
adresses["sandra"] = "gilly"

# 5. **Supprimez** la clé `"jean"` du dictionnaire `adresse`. del dict["key"]
del adresses["jean"]

# 6. **Affichez** les clés restantes dans le dictionnaire. print(dict.keys())
print(adresses["sandra"])
print(adresses.keys())
print(type(adresses.keys()))

