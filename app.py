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
        contacts = db.read().split('\n')
    results = [contacts[i] for i in range(len(contacts)) if contacts[i].find(string) != -1]
    return results


def search_all():
    with open("./database.txt", "r") as db:
        contacts = db.read().strip().split("\n")
    return contacts


def update(contact, chaine):
    with open(db_path, "r") as db:
        db.read()
        delete(chaine)
        with open(db_path, "a+") as db:
            tout = contact.split(',')
            db.write(f"{tout[0]},{tout[1]},{tout[2]},{tout[3]}\n")
        return True


def delete(contact):
    with open(db_path, "r") as db:
        contacts = db.read().split("\n")
        contacts.remove(contact)
    return create_multi(contacts)


def save_controller(args):
    return create(args)


def search_controller(string):
    results = search(string)
    try:
        contact_vals = [result.split(',') for result in results]
        contacts = [{"lastname": vals[0], "firstname": vals[1], "address": vals[2], "phone": vals[3]} for vals in
                    contact_vals if vals[3] == string or vals[0].lower()==string or vals[1]==string or vals[2]==string]
    except:
        pass
    else:
        return contacts


def delete_controller(contact):
    contact = f"{contact['lastname']},{contact['firstname']},{contact['address']},{contact['phone']}"
    return delete(contact)


def update_controller(contact, ancien):
    contact = f"{contact['lastname']},{contact['firstname']},{contact['address']},{contact['phone']}"
    return update(contact, ancien)


def afficher_contact(lastname, firstname, address, phone):
    contact_string = f"Nom: {lastname.upper()}\nPrenom.: {firstname.capitalize()}\nAddresse: {address.capitalize()}\nTelephone: {phone}\n"
    print(contact_string)


def afficher_annuaire():
    print("\nAnnuaire:\n")
    contacts = search_all()
    for n,contact in enumerate(contacts):
        print("N°: ",n),afficher_contact(*contact.split(','))
    print('-------------------------------------------------------')
    print(f"il y'a {n} personne enregistrés dans la base de donnée")
    print('-------------------------------------------------------')
    return n

def nombre():
    contacts = search_all()
    for n, contact in enumerate(contacts):
        print(n), afficher_contact(*contact.split(','))
    print('-------------------------------------------------------')
    print(f"il y'a {n} personne enregistrés dans la base de donnée")
    print('-------------------------------------------------------')
    return n

# fonction pour ajouter les contacts
def ajouter_contact(contact=None, save=False):
    if not contact:
        contact = {"lastname": None, "firstname": None, "address": None, "phone": ''}
    lastname = input("Nom: ").lower() or contact["lastname"]
    firstname = input("Prenom: ").lower() or contact["firstname"]
    address = input("Addresse: ").lower() or contact["address"]
    phone = input("Telephone: ").lower() or contact["phone"]
    args = {"lastname": lastname, "firstname": firstname, "address": address, "phone": phone}

    #import ipdb ; ipdb.set_trace()
    def click_save(args):
        # ligne de verification
        verification = args["phone"]
        results = search(verification)
        final = []  # création d'une liste de liste
        for i in results:
            for j in i.split('\n'):
                argu= j.split(',')
            final.append(argu)
        fatal = [[ligne[-1] for ligne in final] for i in range(1)]  # recuperation des derniers éléments de chaque liste
        try:
            int(verification)
        except:
            print('-------------ERREUR DE SAISIE-----------')
            print("Assurez-vous d'entrer des bonnes valeurs")
            print('----------------------------------------')
        else:
            if verification in fatal[0]:
                print("le contact existe déjà")
            else:
                question = input(
                    "voulez vous vraiment Enregister ce contact ?"
                    " \nsi oui appuyer sur << o >>"
                    "\nsinon appuyer sur n'importe quelle touche pour annuler\n: ")
                if question.lower() == "o":
                    success = save_controller(args)
                    if success:
                        print("Contact successfully added.")
                else:
                    print("Enregistrement annuler .")
    if save:
        click_save(args)
    else:
        afficher_contact(lastname, firstname, address, phone)


def click_search(string):
    return search_controller(string)


def rechercher_contact():
    string = input("Entrer votre recherche: ").lower()
    contacts = click_search(string)
    if contacts:
        try:
            for contact in contacts:
                afficher_contact(*contact.values())
        except (TypeError, IndexError):
            print('Erreur')
        else:
            if len(contacts) > 1:
                id = input('lequel des contacts voulez vous sélectionner ?\nveiller inserer son numero : ')
                contacts = click_search(id)
                try:
                    afficher_contact(*contacts[0].values())
                except (IndexError, TypeError):
                    print('vous avez saisie un mauvais numéro !')
                else:

                    print("Voulez-vous..")
                    print("3. Modifier ce contact")
                    print("4. Supprimer ce contact")
                    print("5. Retourner au menu principal")
                    sub_action = input()
                    if sub_action == str(5):
                        pass
                    elif sub_action == str(4):
                        click_delete(contacts)
                    elif sub_action == str(3):
                        click_modif(contacts)
            else:
                print("Voulez-vous..")
                print("3. Modifier ce contact")
                print("4. Supprimer ce contact")
                print("5. Retourner au menu principal")
            sub_action = input()
            if sub_action == str(5):
                pass
            elif sub_action == str(4):
                click_delete(contacts)
            elif sub_action == str(3):
                click_modif(contacts)
    else:
        print("ce contact n'existe pas")

def supprimer_contact():
    tel = input("Entrer le numéro de telephone complet du contact:")
    contacts = click_search(tel)
    return click_delete(contacts)


def click_delete(contacts, modify=True):
    try:
        afficher_contact(*contacts[0].values())
    except (IndexError, TypeError):
        print('--------------------------------')
        print('Erreur: impossible de le joindre')
        print('--------------------------------')
    else:
        question = input("voulez vous vraiment supprimer ce contact ?"
                         "\nsi oui appuyer sur << o >>"
                         "\nsinon appuyer sur n'importe quelle touche pour annuler\n: ")
        if question.lower() == "o":
            success = delete_controller(contact=contacts[0])
            if success and modify:
                print('--------------------------------------')
                print("Le contact a été supprime avec succès.")
                print('--------------------------------------')
        else:
            print('---------------------')
            print('suppression annuler !')
            print('---------------------')


def modifier_contact():
    tel = input("Entrer le numéro de telephone complet du contact:")
    contacts = click_search(tel)
    return click_modif(contacts)
def click_modif(contacts, contact=None, modify=True):
    try:
        afficher_contact(*contacts[0].values())
    except (IndexError, TypeError):
        print('-----------------------------------------')
        print('impossible de modifier ce contact')
        print('-----------------------------------------')
    else:
        modif = contacts
        ancien = modif[0]
        chaine = ancien['lastname'] + ',' + ancien['firstname'] + ',' + ancien['address'] + ',' + ancien['phone']
        if not contact:
            contact = {"lastname": modif[0]["lastname"], "firstname": modif[0]["firstname"],
                       "address": modif[0]["address"], "phone": modif[0]["phone"]}
        lastname = input("Nom: ").lower() or contact["lastname"]
        firstname = input("Prénom : ").lower() or contact["firstname"]
        address = input("Address: ").lower() or contact["address"]
        phone = input("Telephone: ").lower() or contact["phone"]
        contact = {"lastname": lastname, "firstname": firstname, "address": address, "phone": phone}

        question = input("voulez vous vraiment supprimer ce contact ?"
                         "\nsi oui appuyer sur << o >>"
                         "\nsinon appuyer sur n'importe quelle touche pour annuler\n: ")
        if question.lower() == "o":
            success = update_controller(contact, chaine)
            if success and modify:
                print('-----------Bien-----------------------')
                print("Le contact a été modifier avec succes.")
                print('---------------------------------------')
        else:
            print('Modification annuler !')

def multiple_delete(modify=True):
    tel=''
    while tel.lower() !='q':
        tel = input("Entrer le numéro de telephone complet du contact ou taper << q >> pour quitter :")
        contacts = click_search(tel)
        try:
            afficher_contact(*contacts[0].values())
        except (IndexError, TypeError):
            print('--------------------------------')
            print('Contact non retrouvé')
            print('--------------------------------')
        else:
            question = input("voulez vous vraiment supprimer ce contact ?"
                             "\nsi oui appuyer sur << o >>"
                             "\nsinon appuyer sur n'importe quelle touche pour annuler\n: ")
            if question.lower() == "o":
                success = delete_controller(contact=contacts[0])
                if success and modify:
                    print("Le contact a été supprime avec succès.")
                else:
                    print('suppression annuler !')




if __name__ == "__main__":
    afficher_annuaire()
    while True:
        print("Entrer votre action parmi les suivantes:")
        print("1. Rechercher un contact")
        print("2. Ajouter un contact")
        print("3. Modifier un contact")
        print("4. Supprimer un contact")
        print("5. suppression multiple")
        print("6. nombre d'inscrits")
        print("0. Sortir de l'application")
        action = input()
        if action == str(1):
            rechercher_contact()
        elif action == str(2):
            ajouter_contact(save=True)
        elif action == str(3):
            modifier_contact()
        elif action == str(4):
            supprimer_contact()
        elif action ==str(5):
            multiple_delete()
        elif action==str(6):
            nombre()
        elif action == str(0):
            break
        else:
            print(" ERREUR: Operation non supportée.")
