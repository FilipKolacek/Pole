predmety = ["Matematika", "Čeština", "Tělocvik", "AAP", "Dějepis","Chemie"]
print(len(predmety))
for i in predmety:
    print(i)

dalsi_predmet = input("zadejte další předmět: ")
predmety.append(dalsi_predmet)
print(predmety)
predmety.pop(0)
print(predmety)
predmety.sort()
print(predmety)
predmety.reverse()
print(predmety)