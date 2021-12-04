#Anmeldung
print("Willkommen bei L&D!")
print("Bitte geben Sie Ihre Kundennummer ein:")

x=input()
x=int(x)

if (x>=1) and (x<=99):
    print("Willkommen Premiumkunde", x,"! Fuer Sie kostet eine Stange Mentos nur noch 17,50$." )
else:
    print("Tut uns Leid aber fuer Sie kostet eine Stange Mentos weiterhin 19,00$.")

#Kaufprozess
print("Geben Sie die Menge an Mentosstangen ein die Sie kaufen moechten:")

y=input()
y=int(y)

if (y>=100) and (y<=1000):
    print("Sie erhalten einen Rabatt von 5 Prozent auf Ihren Einkauf von", y,"Mentosstangen.")
else: 
    if (y>=1000):
        print("Sie erhalten einen Rabatt von 20 Prozent auf Ihren generoesen Einkauf von", y,"Mentostangen.")
    else:
        print("Sie erhalten keinen Mengenrabatt auf Ihren laecherlichen Einkauf von", y,"Mentosstangen.")


