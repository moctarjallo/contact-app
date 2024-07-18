db_path = "./database.txt"
database = "./database.txt"

def create_multi(contacts):
    data = "\n".join(contacts)
    with open(db_path, "w+") as db:
        success = db.write(data)
    return success

def create(args):
    with open(db_path, "a+") as db:
        db.write(f"{args['lastname']},{args['firstname']},{args['address']},{args['phone']}\n")
    return True

def search(string):
    with open(db_path, "r") as db:
        contacts = db.read().split("\n")
    results = [contacts[i] for i in range(len(contacts)) if contacts[i].find(string)!=-1]
    return results

def search_all():
    with open("./database.txt", "r") as db:
        contacts = db.read().strip().split("\n")
    return contacts

def delete(contact):
    with open(db_path, "r") as db:
        contacts = db.read().split("\n")
        contacts.remove(contact)
    return create_multi(contacts)

def save_controller(args):
    return create(args)

def search_controller(string):
    results = search(string)
    if results == []:
        print("Contact non trouve.")
    contact_vals = [result.split(',') for result in results]
    contacts = [{"lastname": vals[0], "firstname": vals[1], "address": vals[2], "phone": vals[3]} for vals in contact_vals]
    return contacts

def delete_controller(contact):
    contact = f"{contact['lastname']},{contact['firstname']},{contact["address"]},{contact["phone"]}"
    return delete(contact)

def afficher_contact(lastname, firstname, address, phone):
    contact_string = f"Nom: {lastname}\nPrenom: {firstname}\nAddresse: {address}\nTelephone: {phone}\n"
    print(contact_string)

def afficher_annuaire():
    print("\nAnnuaire:\n")
    contacts = search_all()
    for contact in contacts:
        afficher_contact(*contact.split(','))

def ajouter_contact(contact=None, save=False):
    if not contact:
        contact = {"lastname": None, "firstname": None, "address": None, "phone": None}
    lastname = input("Nom: ") or contact["lastname"]
    firstname = input("Prenom: ") or contact["firstname"]
    address = input("Addresse: ") or contact["address"]
    phone = input("Telephone: ") or contact["phone"]
    args = {"lastname": lastname, "firstname": firstname, "address": address, "phone": phone}

    #import ipdb ; ipdb.set_trace()

    def click_save(args):
        #ligne de verification 
        
        verification = args["phone"]
        results = search(verification)
        if results != []:
           print("le contact existe déjà")
        else:
            success = save_controller(args)
        
            if success:
                print("Contact successfully added.")
            else:
                print("Contact failed.")
    if save:
        click_save(args)
    else:
        afficher_contact(lastname, firstname, address, phone)

def verifie_contact(contact=None, save=False):
    if not contact:
        contact = {"lastname": None, "firstname": None, "address": None, "phone": None}
    lastname = input("Nom: ") or contact["lastname"]
    firstname = input("Prenom: ") or contact["firstname"]
    address = input("Addresse: ") or contact["address"]
    phone = input("Telephone: ") or contact["phone"]
    args = {"lastname": lastname, "firstname": firstname, "address": address, "phone": phone}

    #import ipdb ; ipdb.set_trace()

    def click_save(args):
        
        success = save_controller(args)
        if success:
            print("Contact successfully added.")
        else:
            print("Contact failed.")
    if save:
        click_save(args)
    else:
        afficher_contact(lastname, firstname, address, phone)

def click_search(string):
    return search_controller(string)


def rechercher_contact():
    string = input("Entrer votre recherche: ")
    contacts = click_search(string)
    for contact in contacts:
        afficher_contact(*contact.values())

    print("Voulez-vous..")
    print("3. Modifier ce contact")
    print("4. Supprimer ce contact")
    print("5. Retourner au menu principal")
    sub_action = int(input())
    if sub_action == 5:
        pass
    elif sub_action == 4:
        supprimer_contact()
    elif sub_action == 3:
        supprimer_contact(modify=True)

def supprimer_contact(modify=False):
    tel = input("Entrer le numero de telephone complet du contact:")
    contacts = click_search(tel)
    afficher_contact(*contacts[0].values())
    success = delete_controller(contact=contacts[0])
    if success and not modify:
        print("Le contact a ete supprime avec succes.")
    elif success and modify:
        ajouter_contact(contact=contacts[0], save=True)

if __name__ == "__main__":
    afficher_annuaire()
    while True:
        print("Entrer votre action parmi les suivantes:")
        print("1. Rechercher un contact")
        print("2. Ajouter un contact")
        print("0. Sortir de l'application")
        action = int(input())
        if action == 1:
            rechercher_contact()
        elif action == 2:

            ajouter_contact(save=True)
        elif action == 3:
            modifier_contact()
        elif action == 0:
            break
        else:
            print("Operation non supportee pour le moment.")
