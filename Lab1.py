try:
    f = open("exemplu2.txt", "r")
except FileNotFoundError:
    print("Fișier inexistent!")

lines = f.read().split("\n")
#print(lines)
label = ""
sigma = set() #va contine cuvintele
states = set() #va contine starile
start_state = []#va contine starea de inceput(sau starile de inceput)
final_states = set() #va contine starile finale
transitions = {} #va contine tranzitiile
cnt = 0

for line in lines:
    cnt += 1
    line = line.lstrip().rstrip()
    comment_ind = line.find("#")

    if comment_ind != -1:
        line = line[0:comment_ind]
        line = line.lstrip().rstrip()


    if line == "":
        continue

    cuvinte = line.split(", ")

    if cuvinte[0].lower() == "end":
        label = "end"
        continue

    if cuvinte[0].lower() == "sigma:":
        label = "sigma"
        continue

    if cuvinte[0].lower() == "states:":
        label = "states"
        continue

    if cuvinte[0].lower() == "transitions:":
        label = "transitions"
        continue

    if label == "sigma":
        sigma.add(cuvinte[0])
        continue

    if label == "states":

        if len(cuvinte) == 1:
            states.add(cuvinte[0])

        elif len(cuvinte) == 2:
            if cuvinte[1].lower() == "s":
                states.add(cuvinte[0])
                start_state.append(cuvinte[0])
            elif cuvinte[1].lower() == "f":
                states.add(cuvinte[0])
                final_states.add(cuvinte[0])

        elif len(cuvinte) == 3:
                states.add(cuvinte[0])
                start_state.append(cuvinte[0])
                final_states.add(cuvinte[0])


        continue

    if label == "transitions":

        if len(cuvinte) == 3:
            transitions[cnt] = tuple(cuvinte)

        continue

print("Simbolurile sunt:", sigma)
print("Starile sunt:", states)
print("Starea de inceput este:", *start_state)
print("Starile finale sunt:", final_states)
print("Tranzitiile sunt:", transitions)

OK = 1
for t in transitions:
    ok = 1

    if transitions[t][0] not in states:
        pozitie_greseala = 0
        ok = 0
        OK = 0

    if transitions[t][2] not in states:
        pozitie_greseala = 2
        ok = 0
        OK = 0

    if transitions[t][1] not in sigma:
        pozitie_greseala = 1
        ok = 0
        OK = 0

    if transitions[t][1] not in sigma:
        pozitie_greseala = 1
        ok = 0
        OK = 0

    if ok == 0:
        print("\nEroare: Tranzitia de la linia", t, "nu este corecta")
        print("Greseala se afla pe pozitia a", pozitie_greseala+1,"a de pe linia", t)

if len(start_state) != 1:
    OK = 0
    print("\nEroare: Are mai mult de o stare initiala!! ->", *start_state)

if len(final_states) == 0:
    OK = 0
    print("\nEroare: Nu are nicio stare finala!! ->", final_states)

if OK == 1:
    print("\nFisierul este valid!")
else:
    print("\nFisierul nu a putut fi validat!")



