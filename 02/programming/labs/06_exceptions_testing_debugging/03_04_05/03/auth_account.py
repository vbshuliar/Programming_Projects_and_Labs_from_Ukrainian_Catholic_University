import auth

auth.authenticator.add_user("vlad", "password")
auth.authorizor.add_permission("add")
auth.authorizor.add_permission("check")
auth.authorizor.permit_user("add", "vlad")
auth.authorizor.permit_user("check", "vlad")


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "register": self.register,
            "login": self.login,
            "add": self.add,
            "check": self.check,
            "quit": self.quit,
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

    def register(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                auth.authenticator.add_user(username, password)
                auth.authorizor.permit_user("add", username)
                auth.authorizor.permit_user("check", username)
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def add(self):
        if self.is_permitted("add"):
            print("Add notes now.")
            print(auth.authenticator.users[self.username].notebook)
            print("Write a message.")
            a = input(">>> ")
            print("Write tags.")
            b = input(">>> ")
            auth.authenticator.users[self.username].notebook.new_note(a, b)

    def check(self):
        if self.is_permitted("check"):
            print("Check notes now.")
            for _ in auth.authenticator.users[self.username].notebook.notes:
                print(
                    f"""
{_}
"""
                )

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print(
                    """
Please enter a command:
    > register
    > login
    > add
    > check
    > quit
"""
                )
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")


Editor().menu()
