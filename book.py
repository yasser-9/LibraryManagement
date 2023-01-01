import csv

class Book:

    def __init__(self, id, isbn, title, author):
        self.id = id
        self.isbn = isbn
        self.title = title
        self.author = author

    
    def add_book(self):
        # Vérifier que tous les champs sont remplis
        if not all([self.id, self.isbn, self.title, self.author]):
            print("Veuillez remplir tous les champs")
            return
        
        # Vérifier que l'ISBN n'est pas déjà utilisé
        books = self.get_all_books()
        #print(books)
        # Ajouter le livre au catalogue
        with open("livres.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["ID", "ISBN_010a", "Titre_200a", "Complement_du_titre_200e", "Auteur_principal_nom_700a", "Auteur_principal_prenom_700b", "Auteur_principal_qualificatif_700c", "Autre_auteur_principal_nom_701a", "Autre_auteur_principal_prenom_702b", "Autre_auteur_principal_qualificatif_702b", "Editeur_210c"], delimiter=";")
            #writer.writeheader()
            writer.writerow({"ID": self.id, "ISBN_010a": self.isbn, "Titre_200a": self.title, "Complement_du_titre_200e": "", "Auteur_principal_nom_700a": self.author, "Auteur_principal_prenom_700b": "", "Auteur_principal_qualificatif_700c": "", "Autre_auteur_principal_nom_701a": "", "Autre_auteur_principal_prenom_702b": "", "Autre_auteur_principal_qualificatif_702b": "", "Editeur_210c": ""})
    
    def remove_book(self):
        # Vérifier que tous les champs sont remplis
        #if not all([self.id, self.isbn, self.title, self.author]):
        #    print("Veuillez remplir tous les champs")
        #    return
        print("id1 -- 1")
        # Vérifier que le livre existe
        book = self.get_book(self.id)
        print(book)
        print("id1 -- 2")
        if not book:
            print("Livre non trouvé")
            return
        
        # Supprimer le livre du catalogue
        books = self.get_all_books()
        books = [b for b in books if b["ID"] != self.id]
        self.write_books_to_csv(books)
    
    def get_all_books(self):
        # Lire le fichier CSV et retourner tous les livres sous forme de liste de dictionnaires
        with open("livres.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=["ID", "ISBN_010a", "Titre_200a", "Complement_du_titre_200e", "Auteur_principal_nom_700a", "Auteur_principal_prenom_700b", "Auteur_principal_qualificatif_700c", "Autre_auteur_principal_nom_701a", "Autre_auteur_principal_prenom_702b", "Autre_auteur_principal_qualificatif_702b", "Editeur_210c"], delimiter=";")
            return list(reader)
    
    def get_book(self, id):
        # Retourner le livre correspondant à l'ID donné s'il existe, sinon retourner None
        books = self.get_all_books()
        #print(books)
        for book in books:
            if book["ID"] == id:
                return book
        return None

    def write_books_to_csv(self, books):
        # Écrire la liste des livres dans le fichier CSV
        with open("livres.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["ID", "ISBN_010a", "Titre_200a", "Complement_du_titre_200e", "Auteur_principal_nom_700a", "Auteur_principal_prenom_700b", "Auteur_principal_qualificatif_700c", "Autre_auteur_principal_nom_701a", "Autre_auteur_principal_prenom_702b", "Autre_auteur_principal_qualificatif_702b", "Editeur_210c"])
            writer.writeheader()
            for book in books:
                writer.writerow(book)
