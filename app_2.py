db_path = "./database_2.txt"

def create_multi(contacts):
    data = "\n".join(contacts)
    with open(db_path, "w") as db:
        db.write(data)
    return True

# def create(args):
#     if search(args['phone']):
#         print("ERREUR: ce numéro de téléphone existe déjà.")
#         return False
#     with open(db_path, "a") as db:
#         db.write(f"{args['lastname']},{args['firstname']},{args['address']},{args['phone']}\n")
#     return True

def create(args):
    if search(args['phone'], exact=True):
        print("ERREUR: ce numéro de téléphone existe déjà.")
        return False
    with open(db_path, "a") as db:
        db.write(f"{args['lastname']},{args['firstname']},{args['address']},{args['phone']}\n")
    return True

# def search(string):
#     with open(db_path, "r") as db:
#         contacts = db.read().split("\n")
#     results = [contact for contact in contacts if contact.find(string) != -1]
#     return results

def search(string, exact=False):
    with open(db_path, "r") as db:
        contacts = db.read().split("\n")
    if exact:
        results = [contact for contact in contacts if contact.split(',')[-1] == string]
    else:
        results = [contact for contact in contacts if contact.lower().find(string.lower()) != -1]
    return results

def search_all():
    with open(db_path, "r") as db:
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
    results = search(string,exact=True)
    if not results:
        print("Contact non trouvé.")
        return []
    contact_vals = [result.split(',') for result in results]
    contacts = [{"lastname": vals[0], "firstname": vals[1], "address": vals[2], "phone": vals[3]} for vals in contact_vals]
    return contacts

def delete_controller(contact):
    contact_str = f"{contact['lastname']},{contact['firstname']},{contact['address']},{contact['phone']}"
    return delete(contact_str)

def afficher_contact(lastname, firstname, address, phone):
    contact_string = f"\nNom: {lastname}\nPrénom: {firstname}\nAdresse: {address}\nTéléphone: {phone}\n"
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
    firstname = input("Prénom: ") or contact["firstname"]
    address = input("Adresse: ") or contact["address"]
    phone = input("Téléphone: ") or contact["phone"]
    args = {"lastname": lastname, "firstname": firstname, "address": address, "phone": phone}
    
    def click_save(args):
        success = save_controller(args)
        if success:
            print("Contact ajouté avec succès.")
        else:
            print("Échec de l'ajout du contact.")
    
    if save:
        click_save(args)
    else:
        afficher_contact(lastname, firstname, address, phone)

def rechercher_contact():
    string = input("Entrez votre recherche: ")
    contacts = search_controller(string)
    for contact in contacts:
        afficher_contact(*contact.values())
    if contacts:
        print("Voulez-vous..")
        print("3. Modifier ce contact")
        print("4. Supprimer ce contact")
        print("5. Retourner au menu principal")
        sub_action = int(input())
        if sub_action == 5:
            pass
        elif sub_action == 4:
            supprimer_contact(contact=contacts[0])
        elif sub_action == 3:
            modifier_contact(contact=contacts[0])

def supprimer_contact(contact):
    success = delete_controller(contact)
    if success:
        print("Le contact a été supprimé avec succès.")
    else:
        print("Échec de la suppression du contact.")

def modifier_contact(contact):
    ajouter_contact(contact=contact, save=True)

if __name__ == "__main__":
    afficher_annuaire()
    while True:
        print("Entrez votre action parmi les suivantes:")
        print("1. Rechercher un contact")
        print("2. Ajouter un contact")
        print("0. Sortir de l'application")
        action = int(input())
        if action == 1:
            rechercher_contact()
        elif action == 2:
            ajouter_contact(save=True)
        elif action == 0:
            break
        else:
            print("Opération non supportée pour le moment.")