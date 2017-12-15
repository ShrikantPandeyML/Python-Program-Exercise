class Father:
    def gradnening(self):
        print("I am programmer")
class Mother:
    def cooking(self):
        print("I love art")

class Child(Father,Mother):
    def sports(self):
        print("i am sport player")


obj = Child()
obj.gradnening()
obj.cooking()
obj.sports()
