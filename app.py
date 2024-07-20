db_path = "./database.txt"
database = "./database.txt"

# Fonction pour écrire plusieurs contacts à la fois dans le fichier
def create_multi(contacts):
    data = "\n".join(contacts)  # Joint les contacts avec des sauts de ligne
    with open(db_path, "w+") as db:  # Ouvre le fichier en écriture
        success = db.write(data)  # Écrit les données dans le fichier
    return success  # Retourne le nombre de caractères écrits

# Fonction pour ajouter un contact unique au fichier
def create(args):
    with open(db_path, "a+") as db:  # Ouvre le fichier en mode ajout
        db.write(f"{args['lastname']},{args['firstname']},{args['address']},{args['phone']}\n")
    return True  # Retourne True pour indiquer le succès

# Fonction pour rechercher des contacts contenant une chaîne spécifique
def search(string):
    with open(db_path, "r") as db:  # Ouvre le fichier en lecture
        contacts = db.read().split("\n")  # Lit et sépare les contacts par des sauts de ligne
    results = [contacts[i] for i in range(len(contacts)) if contacts[i].find(string) != -1]
    return results  # Retourne la liste des contacts correspondants

# Fonction pour lire tous les contacts
def search_all():
    with open("./database.txt", "r") as db:  # Ouvre le fichier en lecture
        contacts = db.read().strip().split("\n")  # Lit et sépare les contacts par des sauts de ligne
    return contacts  # Retourne la liste des contacts

# Fonction pour supprimer un contact spécifique
def delete(contact):
    with open(db_path, "r") as db:  # Ouvre le fichier en lecture
        contacts = db.read().split("\n")  # Lit et sépare les contacts par des sauts de ligne
        contacts.remove(contact)  # Supprime le contact spécifié de la liste
    return create_multi(contacts)  # Réécrit les contacts mis à jour dans le fichier

# Contrôleur pour sauvegarder un contact
def save_controller(args):
    return create(args)  # Appelle la fonction create pour ajouter le contact

# Contrôleur pour rechercher des contacts
def search_controller(string):
    results = search(string)  # Recherche les contacts correspondants
    if results == []:
        print("Contact non trouvé.")
    contact_vals = [result.split(',') for result in results]  # Sépare les valeurs des contacts trouvés
    contacts = [{"lastname": vals[0], "firstname": vals[1], "address": vals[2], "phone": vals[3]} for vals in contact_vals]
    return contacts  # Retourne la liste des contacts sous forme de dictionnaires

# Contrôleur pour supprimer un contact
def delete_controller(contact):
    contact = f"{contact['lastname']},{contact['firstname']},{contact['address']},{contact['phone']}"
    return delete(contact)  # Appelle la fonction delete pour supprimer le contact

# Fonction pour afficher un contact
def afficher_contact(lastname, firstname, address, phone):
    contact_string = f"Nom: {lastname}\nPrenom: {firstname}\nAddresse: {address}\nTelephone: {phone}\n"
    print(contact_string)  # Affiche les détails du contact

# Fonction pour afficher tous les contacts
def afficher_annuaire():
    print("\nAnnuaire:\n")
    contacts = search_all()  # Récupère tous les contacts
    for contact in contacts:
        afficher_contact(*contact.split(','))  # Affiche chaque contact

# Fonction pour ajouter un contact
def ajouter_contact(contact=None, save=False):
    if not contact:
        contact = {"lastname": None, "firstname": None, "address": None, "phone": None}
    lastname = input("Nom: ") or contact["lastname"]
    firstname = input("Prenom: ") or contact["firstname"]
    address = input("Addresse: ") or contact["address"]
    phone = input("Telephone: ") or contact["phone"]
    args = {"lastname": lastname, "firstname": firstname, "address": address, "phone": phone}

    # Fonction interne pour sauvegarder le contact
    def click_save(args):
        success = save_controller(args)
        if success:
            print("Contact successfully added.")
        else:
            print("Contact failed.")
    
    if save:
        click_save(args)  # Sauvegarde le contact si nécessaire
    else:
        afficher_contact(lastname, firstname, address, phone)  # Affiche le contact sans sauvegarde

# Fonction pour rechercher des contacts
def click_search(string):
    return search_controller(string)  # Appelle le contrôleur de recherche

# Fonction pour gérer la recherche d'un contact
def rechercher_contact():
    string = input("Entrer votre recherche: ")
    contacts = click_search(string)  # Recherche les contacts correspondants
    for contact in contacts:
        afficher_contact(*contact.values())  # Affiche chaque contact trouvé

    # Menu pour des actions supplémentaires
    print("Voulez-vous..")
    print("3. Modifier ce contact")
    print("4. Supprimer ce contact")
    print("5. Retourner au menu principal")
    sub_action = int(input())
    if sub_action == 5:
        pass  # Retourne au menu principal
    elif sub_action == 4:
        supprimer_contact()  # Supprime le contact
    elif sub_action == 3:
        supprimer_contact(modify=True)  # Modifie le contact

# Fonction pour supprimer un contact
def supprimer_contact(modify=False):
    tel = input("Entrer le numero de telephone complet du contact:")
    contacts = click_search(tel)  # Recherche le contact par numéro de téléphone
    afficher_contact(*contacts[0].values())  # Affiche le contact trouvé
    success = delete_controller(contact=contacts[0])  # Supprime le contact
    if success and not modify:
        print("Le contact a été supprimé avec succès.")
    elif success and modify:
        ajouter_contact(contact=contacts[0], save=True)  # Modifie le contact

# Point d'entrée principal de l'application
if __name__ == "__main__":
    afficher_annuaire()  # Affiche tous les contacts au démarrage
    while True:
        print("Entrer votre action parmi les suivantes:")
        print("1. Rechercher un contact")
        print("2. Ajouter un contact")
        print("0. Sortir de l'application")
        action = int(input())
        if action == 1:
            rechercher_contact()  # Recherche un contact
        elif action == 2:
            ajouter_contact(save=True)  # Ajoute un contact
        elif action == 3:
            supprimer_contact(modify=True)
        elif action == 0:
            break  # Sort de l'application
        else:
            print("Opération non supportée pour le moment.")
