from library import Library
from book import Book
from member import Member

# Créer une nouvelle bibliothèque
library = Library()

while True:
    # Afficher le menu
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Ajouter un abonné")
    print("4. Supprimer un abonné")
    print("5. Lister les livres empruntés")
    print("6. Quitter")
    print("7. Emprunter un livre")
    print("8. Rendre un livre")

    choice = input("Votre choix : ")

    if choice == "1":
        # Ajouter un livre
        id = input("ID du livre : ")
        isbn = input("ISBN du livre : ")
        title = input("Titre du livre : ")
        author = input("Auteur du livre : ")
        library.add_book(Book(id, isbn, title, author))
    elif choice == "2":
        # Supprimer un livre
        id = input("ID du livre : ")
        library.remove_book(id)

    elif choice == "3":
        # Ajouter un abonné
        num = input("Numéro de l'abonné : ")
        nom = input("Nom de l'abonné : ")
        prenom = input("Prénom de l'abonné : ")
        library.add_member(Member(num, nom, prenom))

    elif choice == "4":
        # Supprimer un abonné
        num = input("Numéro de l'abonné : ")
        library.remove_member(num)
    elif choice == "5":
        # Lister les livres empruntés
        check_outs = library.list_check_outs()
        for check_out in check_outs:
            book = check_out["Book"]
            member = check_out["Member"]
            print(f"{book.title} (ID {book.id}) est emprunté par {member.prenom} {member.nom} (numéro {member.num})")
    elif choice == "6":
        # Quitter
        break
    elif choice == "7":
        # Emprunter un livre
        id = input("ID du livre : ")
        num = input("Numéro de l'abonné : ")
        library.check_out_book(id, num)
    elif choice == "8":
        # Rendre un livre
        id = input("ID du livre : ")
        num = input("Numéro de l'abonné : ")
        library.return_book(id, num)
    else:
        print("Choix non valide")
