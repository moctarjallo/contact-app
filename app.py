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
    results = [contacts[i] for i in range(len(contacts)) if contacts[i].find(string) != -1]
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
    contacts = [{"lastname": vals[0], "firstname": vals[1], "address": vals[2], "phone": vals[3]} for vals in
                contact_vals]
    return contacts


def delete_controller(contact):
    contact = f"{contact['lastname']},{contact['firstname']},{contact['address']},{contact['phone']}"
    return delete(contact)


def afficher_contact(lastname, firstname, address, phone):
    contact_string = f"Nom: {lastname}\nPrenom: {firstname}\nAddresse: {address}\nTelephone: {phone}\n"
    print(contact_string)


def afficher_annuaire():
    print("\nAnnuaire:\n")
    contacts = search_all()
    for contact in contacts:
        afficher_contact(*contact.split(','))

def valeur_dans_fichier(fichier, num_telephone):
    try:
        with open(fichier, "r") as file:
            fichier_en_list_par_ligne = file.read().split("\n") #["BALDE,ELHADJ IBRAHIMA,CONAKRY,611267387","sylla,Oumar,CONAKRY,611267387","None,None,None,9"]
            for row_contenu in fichier_en_list_par_ligne:
                if row_contenu :
                    new_liste = row_contenu.split(",") #["BALDE","ELHADJ IBRAHIMA","CONAKRY","611267387"]
                    phone_in_list = new_liste[-1]      #611267387 <str>
                    if phone_in_list == num_telephone:
                        print(num_telephone," existe déja dans la base de donnée")
                        return True

    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
        return False
def fonction_convertion(num):

    try:
        numero=int(num)
        return numero
    except:
        return print("")

def verify_number(phone):

    control = True

    while control:
        if isinstance(phone,(int)):
           return True
        else:

            control = False


def ajouter_contact(contact=None, save=False):
    if not contact:
        contact = {"lastname": None, "firstname": None, "address": None, "phone": None}
    lastname = input("Nom: ") or contact["lastname"]
    firstname = input("Prenom: ") or contact["firstname"]
    address = input("Addresse: ") or contact["address"]

    phone =input("Télephone : ") or contact["phone"]
    nb=fonction_convertion(phone)
    while not verify_number(nb):

        phone=input("Veuillez rentré un numéro valide : ")
        nb=fonction_convertion(phone)

    if valeur_dans_fichier(database,phone):
        # print(f"Le numéro {phone} se trouve déja dans le fichier.")
        # phone = input("Telephone: ") or contact["phone"]
        return


    args = {"lastname": lastname, "firstname": firstname, "address": address, "phone": phone}

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

def sup_contact(databases, tel_a_supprimer):
    try:
        with open(databases, "r", encoding='utf-8') as file:
            # Lire toutes les lignes du fichier
            fichier_en_list_par_ligne = file.readlines()  # Liste de toutes les lignes du fichier

        # Filtrer les lignes qui ne contiennent pas le numéro de téléphone à supprimer
        nouvelles_lignes = []
        for row_contenu in fichier_en_list_par_ligne:
            if row_contenu.strip():  # Vérifier que la ligne n'est pas vide
                new_liste = row_contenu.strip().split(",")  # ["BBBBBD", "KKFKF", "KFJ", "88888"]
                phone_in_list = new_liste[-1] # 88888 <str>
                #print(f"Comparaison : {phone_in_list} avec {tel_a_supprimer}")
                if phone_in_list != tel_a_supprimer.strip():
                    nouvelles_lignes.append(row_contenu)  # Ajouter la ligne à la nouvelle liste si le téléphone ne correspond pas

        # Écrire les lignes filtrées dans le fichier
        with open(databases, "w", encoding='utf-8') as file:
            for ligne in nouvelles_lignes:
                file.write(ligne)

        print("Contact supprimé")
        return True

    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
        return False




def rechercher_contact():
    string = input("Entrer votre recherche: ")
    contacts = click_search(string)
    for contact in contacts:
        afficher_contact(*contact.values())

        numero_telphon = contact["phone"]
    if contacts :

        print("Voulez-vous..")
        print("3. Modifier ce contact")
        print("4. Supprimer ce contact")
        print("5. Retourner au menu principal")
        sub_action = ""
        while not verify_number(sub_action):
            actions = input("Veuillez un chiffre : ")
            sub_action = fonction_convertion(actions)
        if sub_action == 5:
            pass
        elif sub_action == 4:
            #supprimer_contact()
            sup_contact(database,numero_telphon)
        elif sub_action == 3:
            supprimer_contact(modify=True)
        else:
            print("Operation non supportee pour le moment.")


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

    while True:
        print("Entrer votre action parmi les suivantes:")
        print("1. Afficher tous les contacts ")
        print("2. Rechercher un contact")
        print("3. Ajouter un contact")
        print("0. Sortir de l'application")

        actions = input()
        action= fonction_convertion(actions)
        while not verify_number(action):
            actions = input("Veuillez un chiffre : ")
            action = fonction_convertion(actions)
        if action == 1:
            afficher_annuaire()
        elif action == 2:
            rechercher_contact()
        elif action == 3:
            ajouter_contact(save=True)

        elif action == 0:
            break
        else:
            print("Operation non supportee pour le moment.")