contact = {
"samxal": "051",
"serxan": "055",
"elchin": "077"
}
contact2 = {
"samxal": "051",
"serxan": "055",
"elchin": "077"
}
nom = {
"051": "samxal",
"055": "serxan",
"077": "elchin"
}
menu = """
----- Contact program ------
1. Add  
2. Show All  
3. Remove person
4. Search name
5. Search phone
6.If you want to show the person you deleted, type 6
0. Quit  
"""


def add():
    name = input("Name: ")
    number = input("Phone number: ")
    contact[name] = number
    contact2[name] = number
    nom[number] = name
    print("Done!\n")
    
    

def showAll():
    print(contact)


def remove():
    name = input("Name:")
    phone = input("phone:")
    if name in contact.keys():
            contact.pop(name)
            print("done!")
    
def search():
    name = input("name:")
    for c in contact.keys():
        if name in c:
            print(contact.get(c))

def search2():
    name = input("phone:")
    for c in nom.keys():
        if name in c:
            print(nom.get(c))
def serach3():
    name = input("name:")
    for c in contact2.keys():
        if name in c:
            print(contact2.get(c))
    

while True:
    print(menu)
    x = input("Select: ")

    if x == "1":
        add()
    elif x == "2":
        showAll()
    elif x == "3":
        remove()
    elif x == "4":
        search()
    elif x == "6":
        serach3()
    elif x == "5":
        search2()
    elif x == "0":
        print("\n See you soon :) bye")
        input()
        break
    else:
        print("No proper selection!\n\n")
