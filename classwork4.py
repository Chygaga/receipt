class UserClass:
    def __init__(self, name):
        self.name = name
        self.username = name.lower()


newUser = UserClass("Gerald")


print(newUser.username)
