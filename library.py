import csv
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.check_outs = []  
    
    def load_data(self):
        # Charger les livres et les abonnés à partir des fichiers CSV
        self.books = Book.get_all_books()
        self.members = Member.get_all_members()
    
    def add_book(self, book):
        # Ajouter un livre à la bibliothèque
        self.books.append(book)
        book.add_book()
    
    def remove_book(self, book_id):
        # Supprimer un livre de la bibliothèque
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                Book.remove_book(book)
                break
    
    def add_member(self, member):
        # Ajouter un abonné à la bibliothèque
        self.members.append(member)
        member.add_member()
    
    def remove_member(self, member_num):
        # Supprimer un abonné de la bibliothèque
        for member in self.members:
            if member.num == member_num:
                self.members.remove(member)
                Member.remove_member(member)
                break
    
    def check_out_book(self, book_id, member_num):
        # Prêter un livre à un abonné
        book = next((b for b in self.books if b.id == book_id), None)
        member = next((m for m in self.members if m.num == member_num), None)
        if book and member:
            self.books.remove(book)
            self.members.remove(member)
            # Ajouter le livre et l'abonné à la liste des prêts
            self.check_outs.append({"Book": book, "Member": member})
        else:
            print("Le livre ou l'abonné n'ont pas été trouvés")
    
    def return_book(self, book_id, member_num):
        # Retourner un livre prêté
        check_out = next((c for c in self.check_outs if c["Book"].id == book_id and c["Member"].num == member_num), None)
        if check_out:
            self.check_outs.remove(check_out)
            self.books.append(check_out["Book"])
            self.members.append(check_out["Member"])
        else:
            print("Le livre n'a pas été trouvé dans la liste des prêts")
    
    def list_books(self):
        # Lister tous les livres de la bibliothèque
        for book in self.books:
            print(f"ID: {book.id}, Titre: {book.title}, Auteur: {book.author}")

    def list_members(self):
        # Lister tous les abonnés de la bibliothèque
        for member in self.members:
            print(f"Num: {member.num}, Nom: {member.nom}, Prénom: {member.prenom}")
    
    def list_check_outs(self):
        # Lister tous les prêts en cours
        for check_out in self.check_outs:
            book = check_out["Book"]
            member = check_out["Member"]
            print(f"Livre: ID {book.id}, Titre: {book.title}, Auteur: {book.author}; Abonné: Num {member.num}, Nom: {member.nom}, Prénom: {member.prenom}")
