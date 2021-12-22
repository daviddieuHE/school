import mysql.connector
import secrets

class school:

    @staticmethod
    def start():
        try:
            connector = mysql.connector.connect(host="localhost", user="root", passwd="", db="school")
            return connector
        except mysql.connector.Error as error:
            print("Impossible de se connecter à la base de données: {}".format(error))

    @staticmethod
    def generate_profile(name, firstname, birthdate):
        email = firstname[0] + "." +name + "@students.ephec.be"
        password = secrets.token_urlsafe(8)
        school.send_to_db(name, firstname, birthdate, email, password)

    def generate_updated_profile(id, name, firstname, birthdate):
        email = firstname[0] + "." +name + "@students.ephec.be"
        password = secrets.token_urlsafe(8)
        school.update_student(id, name, firstname, birthdate, email, password)

    @staticmethod
    def send_to_db(name, firstname, birthdate, email, password):
        conn = school.start()
        cursor = conn.cursor()
        insert_tuple = (name, firstname, birthdate, email, password)
        insert_query = "INSERT INTO students (name, firstname, birthdate, email, password) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(insert_query, insert_tuple)
            conn.commit()
            print("L'étudiant a bien enregistré !")
        except mysql.connector.Error as error:
            print("L'étudiant n'a pas pu être enregistré : {}".format(error))

    @staticmethod
    def show_students_list():
        try:
            conn = school.start()
            cursor = conn.cursor()
            student = cursor.execute("""SELECT * from students """)
            rows = cursor.fetchall()
            for row in rows:
                print("Id = ", row[0])
                print("name = ", row[1])
                print("firstname = ", row[2])
                print("birthdate  = ", row[3])
                print("email  = ", row[4])
                print("--------------------------")
            return rows
        except mysql.connector.Error as error:
            print("Pas d'étudiant : {}".format(error))

    @staticmethod
    def update_student(id, name, firstname, birthdate, email, password):
        conn = school.start()
        cursor = conn.cursor()
        insert_tuple = (name, firstname, birthdate, email, password, id)
        insert_query = """UPDATE students SET name = %s, firstname = %s, birthdate = %s, email = %s, password = %s WHERE id = %s"""
        try:
            insert = cursor.execute(insert_query, insert_tuple)
            conn.commit()
            print("Profil de l'étudiant mis à jour !")
        except mysql.connector.Error as error:
            print("le profil de l'étudiant n'a pas pu être mis à jour : {}".format(error))


    @staticmethod
    def chope_name(id):
        conn = school.start()
        cursor = conn.cursor()
        insert_tuple = (id)
        name_query = """SELECT name from students WHERE Id = %s"""
        try:
            student = cursor.execute(name_query, (insert_tuple,))
            rows = cursor.fetchall()
            for row in rows:
                school.delete_student(row[0], id)
        except mysql.connector.Error as error:
            print("le profil de l'étudiant n'a pas pu être supprimé : {}".format(error))

    @staticmethod
    def delete_student(name,id):
        conn = school.start()
        cursor = conn.cursor()
        delete_tuple = (id)
        delete_query = "DELETE FROM students WHERE Id = %s"

        try:
            delete = cursor.execute(delete_query, (delete_tuple,))
            conn.commit()
            print("{} a bien supprimé de la base de donnée !".format(name))
        except mysql.connector.Error as error:
            print("Le profil d'étudiant n'a pas pu être supprimé : {}".format(error))

    @staticmethod
    def list_command():
        """
            Stock et affiche la liste des commandes
        """
        command = {
            "help": "Affiche toute les commandes",
            "liste": "Liste des étudiants",
            "nouvel étudiant": "Permet de créer une nouveau étudiant",
            "supprimer profil": "Permet de supprimer un étudiant",
            "modifier étudiant": "Permet de modifier un étudiant existant",
            "quit": "Permet de quitter l'application"
        }
        for key, value in command.items():
            print(key, ' : ', value)

    @staticmethod
    def command():
        """
            Permet de répondre au commande de l'utilisateur
        """
        while True:
            user_input = input()
            if user_input == 'help':
                school.list_command()

            elif user_input == 'liste':
                school.show_students_list()

            elif user_input == 'nouvel étudiant':
                new_name = input("nom de l'étudiant : ")
                new_firstname = input("prénom de l'étudiant : ")
                new_birthdate = input("date de naissance de l'étudiant : ")
                school.generate_profile(new_name, new_firstname, new_birthdate)

            elif user_input == 'supprimer profil':
                student_id = input("id de l'étudiant à supprimer : ")
                school.chope_name(student_id)

            elif user_input == 'modifier profil':
                up_id = input("id du profil à modifier : ")
                up_name = input("nom : ")
                up_firstname = input("prénom : ")
                up_birthdate = input("date de naissance")
                school.generate_updated_profile(up_id, up_name, up_firstname, up_birthdate)

            elif user_input == 'quit':
                quit()

            else:
                print("La commande saisi n'existe pas.")