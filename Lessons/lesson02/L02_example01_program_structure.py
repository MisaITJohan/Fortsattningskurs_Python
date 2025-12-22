# Ett exempel på hur man kan strukturera ett program enligt MVC-strukturen.


# Model class - hanterar logik och data
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# View class - visar data för användaren
class UserView:
    def display_user(self, user):
        print("Namn: ", user.name, ", Ålder: ", user.age, sep="")


# Controller class - kopplar ihop Model och View
class UserController:
    def __init__(self):
        self.view = UserView()


    def create_and_display_user(self, name, age):
        # Skapar ett User-objekt (Model)
        user = User(name, age)

        # Använder View för att visa användaren
        self.view.display_user(user)

# Exempel på användning:
controller = UserController()
controller.create_and_display_user("Johan", 36)