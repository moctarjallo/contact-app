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
    results = [contacts[i] for i in range(len(contacts)) if contacts[i].lower().find(string.lower())!=-1]
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
        print("Contact non trouve.\n")
        return
    contact_vals = [result.split(',') for result in results]
    contacts = [{"lastname": vals[0], "firstname": vals[1], "address": vals[2], "phone": vals[3]} for vals in contact_vals]
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
    del contacts[0]
    contacts = sorted(contacts, key=None)
    for contact in contacts:
        afficher_contact(*contact.split(','))

# Avoid adding duplicate numbers in the database
def check_duplicate_number(string):
    if string == '':
        return 
    result = search(string)
    for info in result:
        if info.split(',')[-1] == string:
            print('Contact existant')
            return False, info.split(',')
    return True


def ajouter_contact(contact=None, save=False):
    if not contact:
        contact = {"lastname": None, "firstname": None, "address": None, "phone": None}
    lastname = input("Nom: ") or contact["lastname"]
    firstname = input("Prenom: ") or contact["firstname"]
    address = input("Addresse: ") or contact["address"]
    phone = input("Telephone: ") or contact["phone"]
    args = {"lastname": lastname, "firstname": firstname, "address": address, "phone": phone}
   
    if firstname is None:
        print("This field can't be empty")
        args['firstname'] = input("Please enter your firstname: ")
        if args["firstname"] == '':
            print("This field can't be empty")
            return
        
    phone, is_unique = digit_number(phone), False
    if phone is not None:
        is_unique = check_duplicate_number(phone)
        if is_unique is not True:
            print('This number exists already') 
        else:
            if save:
                click_save(args)
            else:
                afficher_contact(lastname, firstname, address, phone)
    else:
        print("This field can't be empty")

def click_save(args):
    success = save_controller(args)
    if success:
        print("Contact successfully added.")
    else:
        print("Contact failed.")

def click_search(string):
    return search_controller(string)

def rechercher_contact():
    string = input("Enter your research or 'quit' to go to menu: ")
    if string.lower() == "quit":
        return
    
    if string.strip() != '':
        contacts = click_search(string)
        if contacts is not None and len(contacts) == 1:
            for contact in contacts:
                afficher_contact(*contact.values())

            print("Voulez-vous..")
            print("3. Modifier ce contact")
            print("4. Supprimer ce contact")
            print("5. Retourner au menu principal")
            sub_action = int(input())
            if sub_action == 5:
                pass
            elif sub_action == 3:
                modifier_contact(contacts[0]['phone'])
            elif sub_action == 4:
                supprimer_contact(contacts[0]['phone'])
        elif contacts is not None and len(contacts) > 1:
            for contact in contacts:
                afficher_contact(*contact.values())
            print('Choose one contact by giving its phone number to continue')
            rechercher_contact()
    else:
        print('No contact found, back to menu\n')

def supprimer_contact(string=None):
    if string is None:
        tel = input("Entrer le numero de telephone complet du contact:")
    else:
        tel = string
    contact = check_duplicate_number(tel)
    if contact is not True:
        afficher_contact(*contact[1])
        confirm = input('Do you want to delete this contact? Enter yes or no: ')
        if confirm.lower() == 'yes':
            delete(",".join(contact[1]))
            print('Contact successfully deleted\n')
        elif confirm.lower() == 'no':
            print('Contact not deleted, back to menu\n')
            return
        else:
            print('You must enter "yes" or "no", back to menu\n')
            return
    else:
        print("Contact not found, back to menu\n")

def delete_multiple():
    to_delete = []
    while True:
        number = input('Enter a phone number you want to delete or "quit" to stop selection: ')
        if number.lower() == 'quit':
            break
        is_unique = check_duplicate_number(number)
        if is_unique:
            to_delete.append(is_unique[1])
        else:
            print('Entry is not valid number')
    print(to_delete)
    database = search_all()
    for entry in to_delete:
        if ','.join(entry) in database:
            database.remove(','.join(entry))            
    create_multi(database)
    print('Contacts deleted')



def modifier_contact(string=None):
    if string is None:
        tel = input("Entrer le numero de telephone complet du contact: ")
    else:
        tel = string
    try:
        is_deplicate = check_duplicate_number(tel)    
        if is_deplicate != True:
            old_contact = is_deplicate[1]
            afficher_contact(*old_contact)
            new_contact = old_contact.copy()
            new_contact[0] = input('Update lastname or tap enter to keep the current one: ') or old_contact[0]
            new_contact[1] = input('Udate  name: or tap enter to keep the current one: ') or old_contact[1]
            new_contact[2] = input('Udate  address: or tap enter to keep the current one: ') or old_contact[2]
            new_contact[3] = input('Udate  phone: or tap enter to keep the current one: ') or old_contact[3]
            
            phone_number = digit_number(new_contact[3])
            if  phone_number is not None:
                new_contact[3] = digit_number(phone_number)
            else:
                return 
            
            afficher_contact(*new_contact)
            database = search_all()
            for i in range(len(database)):
                if database[i] == ','.join(old_contact):
                    database[i] = ','.join(new_contact)
                    break
                
            create_multi(database)
            print("Contact successfully updated\n")
        else:
            print('Invalid entry, back to menu\n')
    except (TypeError, ValueError):
        print('Invalid entry, back to menu\n')

# This function checks if the phone number is number or not
def digit_number(string):
    try:  
        type(int(string))
        return string
    except (TypeError, ValueError):
        print('phone must be a number\n')
        try:
            new_string = input('Udate  phone or tap enter to keep the current one: ')
            type(int(new_string))
            return new_string
        except (TypeError, ValueError):
            print('phone must be a number, back to menu\n')


if __name__ == "__main__":
    afficher_annuaire()
    while True:
        try:
            print("Entrer votre action parmi les suivantes:")
            print("1. Rechercher un contact")
            print("2. Ajouter un contact")
            print("3. Modifier un contact")
            print("4. Supprimer un contact")
            print("5. Afficher tous les contacts")
            print("6. Delete multiple contacts")
            print("0. Sortir de l'application")
            action = int(input())
            if action == 1:
                rechercher_contact()
            elif action == 2:
                ajouter_contact(save=True)
            elif action == 3:
                modifier_contact()
            elif action == 4:
                supprimer_contact()
            elif action == 5: 
                afficher_annuaire()
            elif action == 6:
                delete_multiple()
            elif action == 0:
                break
            else:
                print("Operation non supportee pour le moment.")
        except (TypeError, ValueError):
            print("Une erreur s'est produite, veuillez recommencer")