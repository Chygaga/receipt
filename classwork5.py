class UserClass:
    def __init__(self, firstname,lastname,yearofbirth,gender):
        currentyear= 2020
        self.fullname = firstname  +  lastname
        self.age = currentyear - yearofbirth
        self.gender = gender

    def myfunc(self):
        print("Hello, my name is" + self.fullname)


newUser = UserClass("Joan", "Moses", 1994, "female")


print(newUser.fullname)
print(newUser.age)
print(newUser.gender)
newUser.myfunc()

