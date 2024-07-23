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
        db.write(f"{args['lastname']},{args['firstname']},{args['address']},{args['phone']}\n")  #ajout de \n au debut pour commencer d'abord à revenir à la ligne avant d'ajouter le contact
    return True  # Retourne True pour indiquer le succès

# Fonction pour rechercher des contacts contenant une chaîne spécifique
# def search(string):
#     with open(db_path, "r") as db:  # Ouvre le fichier en lecture
#         contacts = db.read().split("\n")  # Lit et sépare les contacts par des sauts de ligne
#     results = [contacts[i] for i in range(len(contacts)) if contacts[i].find(string) != -1] #selectionne tous les contact contenant les mot clé tappé par l'utilisateur (string)
#     return results  # Retourne la liste des contacts correspondants

#   NOUVELLE FONCTION search(string) GENERIQUE ET SPECIFIQUE (générique pour rechercher la chaine dans tous le contact) spécifique (pour rechercher le contact en fonction de son numero de téléphone)
def search(string,by_contact=False):
    """ cette fonction est distinée à rechercher un contact dans le fichier par la chaine string

    Args:
        string (chaine de caractère): mot clé par lequel va se passer la recherche
        by_contact (bool, optional): paramètre qui precise si la recherche doit se passer par contact ou en tenant compte de toute chaine dans le contact. Par défaut il est à False, ce qui signifie que la recherche par défaut porte sur toutes les chaine dans le contact

    Returns:
        list: list de contact(s) qui contiennent la chaine de caratère string (si by_contact=False) et le contact en list (by_contact=True)
    """
    
    try:
        with open(db_path, "r") as db:
            contacts = db.read().split("\n")
        
        if by_contact:
        # Retourne les contacts dont le numéro de téléphone correspond exactement à la chaîne recherchée
            return [contact for contact in contacts if contact.split(',')[-1] == str(string)]
        else:
            #si la recherche n'est pas uniquement par contact, on retourne toutes les occurences contenant la chaine de caractère string
            #la casse est gerée par la conversion en upper() lors de la conversion
            return [contacts[i] for i in range(len(contacts)) if contacts[i].upper().find(str(string).upper()) != -1] 
    except IOError as e:
        print(f"Erreur de lecture du fichier: {e}")
        return []
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
    if results == []: #si search() renvoi une liste vide, c'est qu'aucun contact ne correspond au mot clé saisi
        print("Contact non trouvé.")
    contact_vals = [result.split(',') for result in results]  # Sépare les valeurs des contacts trouvés
    contacts = [{"lastname": vals[0], "firstname": vals[1], "address": vals[2], "phone": vals[3]} for vals in contact_vals]
    return contacts  # Retourne la liste des contacts sous forme de dictionnaires

# Contrôleur pour supprimer un contact
def delete_controller(contact):
    print(f"contact reçu pour supprimer: {contact}")
    contact = f"{contact[0]},{contact[1]},{contact[2]},{contact[3]}"
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
def ajouter_contact(contact=None, save=False):  #le parametre contact est là pour definir si c'est en mode modification ou en mode nouvel ajout (None pour nouvelle ajout, et Contact=!None pour le mode modification)

    if not contact:
        contact = {"lastname": None, "firstname": None, "address": None, "phone": None}
    lastname = input("Nom: ") or contact[0]
    firstname = input("Prenom: ") or contact[1]
    address = input("Addresse: ") or contact[2]
    phone = input("Telephone: ") or contact[3]
    args = {"lastname": lastname, "firstname": firstname, "address": address, "phone": phone}

    # Fonction interne pour sauvegarder le contact
    def click_save(args):
        success = save_controller(args)  #POURQUOI NE PAS DIRECTEMENT RECUPERER create()? PARCE QUE save_controller(args) reçoit tout simplement create(), pourquoi cette intermediation
        if success:
            print("Contact successfully added.")
            #ici on peut personnaliser le message en fonction du status d'ajout,
            #donc à la save_controller->create() on peut controler deja la verification pour eviter les doublons
        else:
            print("Contact failed.")
    
    if save:
        #ICI LA GESETION DE LA DUPLICITE DES CONTACTS
        #véfication de l'existence du contact avant de l'enregistrer
        contact_exist = None if args['phone']==None  else  search(args['phone'],True)
        if contact_exist:
            print("Un Contact Exist dejà avec ce numero")
            pass
        else:
        #si on appelle la fonction ajouter_contact() avec le parametre save=True
            click_save(args)  # Sauvegarde le contact si nécessaire
    else:
        #sinon on affiche tout simplement le contact sans le sauvegarder dans le fichier
        afficher_contact(lastname, firstname, address, phone)  # Affiche le contact sans sauvegarde

# Fonction pour rechercher des contacts
def click_search(string):
    return search_controller(string)  # Appelle le contrôleur de recherche

# Fonction pour gérer la recherche d'un contact
def rechercher_contact():
    string = input("Entrer votre recherche: ")
    contacts = click_search(string)  # Recherche les contacts correspondants
    for contact in contacts:
        afficher_contact(*contact.values())  # Affiche chaque contact trouvé (l'astérisque au debut va permettre devoyer tous les element de contact.values chacun comme un paramettre)

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
        supprimer_contact(modify=True)  # Modifie le contact(appeler la fonction de suppression en mode modification)

# Fonction pour supprimer un contact
def supprimer_contact(modify=False):
    tel = input("Entrer le numero de telephone complet du contact:")
    contacts = search(string=tel,by_contact=True)
    print(f"le contacts trouvé est : {contacts}")
    contact = contacts[0].split(',')
    # Recherche le contact par numéro de téléphone
    afficher_contact(contact[0],contact[1],contact[2],contact[3])  # Affiche le contact trouvé
    success = delete_controller(contact=contact)  # Supprime le contact
    contact_string = contacts[0]
    if success and not modify:
        print(f"Le contact {contact_string} a été supprimé avec succès.")
    elif success and modify:
        ajouter_contact(contact, save=True)  # Modifie le contact

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
