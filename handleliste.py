import os
item = "A"

def AddState():
    os.system('cls')
    print("-----------------------")
    print("HandleListe Add (A)(R)")
    print("-----------------------")

def RemoveState():
    os.system('cls')
    print("-----------------------")
    print("HandleListe Remove (A)(R)")
    print("-----------------------")



list = []
enterEmpty = False
while(enterEmpty == False):
    Removestate = False
    Addstate = True
    if item.upper() == "A":
        AddState()
        Removestate = False
        Addstate = True
    if item.upper() == "R":
        RemoveState()
        print(list)
        Addstate = False
        Removestate = True

    length = len(list)
    item = input("item: ")
    if item == "":
        enterEmpty = True

    if Removestate:
        if item.upper() not in {"A", "R", ""}:
            i = 0
            while i < len(list):
                if item == list[i]:
                    del list[i]
                else:
                    i += 1

            print("removed item ", item)

    if Addstate:
        if item.upper() not in {"A", "R", ""}:
            list.append(item)

filename = os.path.abspath("handleListe.txt")
print("Filename:", filename)
with open(filename, 'w') as file:
    file.write("-----------HandleListe------------\n")
    file.write("\n")
    for i in range(length):
        file.write(f"{list[i]}\n")

if os.path.exists(filename):
    os.startfile(filename)

else:
    print(f"could not find the file {filename}")
    