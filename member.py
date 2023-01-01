import csv

class Member:
    def __init__(self, num=None, nom=None, prenom=None):
        self.num = num
        self.nom = nom
        self.prenom = prenom
    
    def add_member(self):
        # Vérifier que tous les champs sont remplis
        if not all([self.num, self.nom, self.prenom]):
            print("Veuillez remplir tous les champs")
            return
        
        # Vérifier que le numéro d'abonné n'est pas déjà utilisé
        members = self.get_all_members()
        for member in members:
            if member["Num"] == self.num:
                print("Numéro d'abonné déjà utilisé")
                return
        
        # Ajouter l'abonné à la liste
        with open("abonnes.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Num", "Nom", "Prenom"], delimiter=";")
            writer.writerow({"Num": self.num,"Nom": self.nom, "Prenom": self.prenom})
    
    def remove_member(self):
        # Vérifier que tous les champs sont remplis
        if not all([self.num, self.nom, self.prenom]):
            print("Veuillez remplir tous les champs")
            return
        
        # Vérifier que l'abonné existe
        member = self.get_member(self.num)
        if not member:
            print("Abonné non trouvé")
            return
        
        # Supprimer l'abonné de la liste
        members = self.get_all_members()
        members = [m for m in members if m["Num"] != self.num]
        print(members)
        self.write_members_to_csv(members)
    
    def get_all_members(self):
        # Lire le fichier CSV et retourner tous les abonnés sous forme de liste de dictionnaires
        with open("abonnes.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=["Num", "Nom", "Prenom"], delimiter=";")
            members = [member for member in reader]
        return members
    
    def get_member(self, num):
        # Lire le fichier CSV et retourner l'abonné avec le numéro donné, s'il existe
        members = self.get_all_members()
        for member in members:
            if member["Num"] == num:
                return member
        return None
    
    def write_members_to_csv(self, members):
            # Écrire la liste des abonnés dans le fichier CSV
            with open("abonnes.csv", "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=["Num", "Nom", "Prenom"], delimiter=";")
                #writer.writeheader()
                for member in members:
                    writer.writerow(member)

