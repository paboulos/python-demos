class Dog:

    dogInfo = "hey dogs are cool"
    classInfo = "methods need first arg of self \
    , Init to setup a default objects"

    def __init__(self, name="", age=0, furcolor=""):
        self.name = name
        self.age = age
        
    def bark(self,str):
        print("BARK!",str)


mydog = Dog("fido",13)
mydog.bark("Ruff")

print(mydog)
