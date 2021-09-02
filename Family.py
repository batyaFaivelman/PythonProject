import numpy


class Father(object):
    def __init__(self, father_name="",father_age=None):
        self.father_name = father_name
        self.father_age = father_age

    def set_father_name(self, name):
        self.father_name = name

    def set_father_age(self, age):
        self.father_age = age

    def get_father_name(self):
        return self.father_name

    def get_father_age(self):
        return self.father_age


class Mother(object):
    def __init__(self, mother_name="",mother_age=None):
        self.mother_name = mother_name
        self.mother_age = mother_age

    def set_mother_name(self, name):
        self.mother_name = name

    def set_mother_age(self, age):
        self.mother_age = age

    def get_mother_name(self):
        return self.mother_name

    def get_mother_age(self):
        return self.mother_age


class Child(Mother, Father):
    def __init__(self, child_name="", child_age=None, father=Father(), mother=Mother()):
        self.child_name = child_name
        self.child_age = child_age
        self.father = father
        self.mother = mother

    def set_child_name(self, name):
        self.child_name = name

    def set_child_age(self, age):
        self.child_age = age

    def get_child_name(self):
        return self.child_name

    def get_child_age(self):
        return self.child_age

    def set_father(self, father_name, father_age):
        self.father_name = father_name
        self.father_age = father_age

    def set_mother(self, mother_name, mother_age):
        self.mother_name = mother_name
        self.mother_age = mother_age

    def set_parents(self, father_details, mother_details):
        self.mother_name = mother_details["name"]
        self.mother_age = mother_details["age"]
        self.father_name = father_details["name"]
        self.father_age = father_details["age"]


class Family(Child):
    def __init__(self, parents, children, last_name="")-> None:
        self.parents = dict(parents)
        self.children = dict(children)
        self.last_name = str(last_name)

    def add_child(self, child_name, child_age):
        self.children[child_name]=child_age

    def get_children(self):
        return self.children

    def get_child(self, child_name):
        return self.children[child_name]

    def get_parents_names(self):

        return self.parents["father"]["father_name"]+" and "+self.parents["mother"]["mother_name"]


def sinx_x(x):
    y =numpy.array(1)
    sin = numpy.sin(x)
    print(sin)
    y=numpy.divide(sin, x, where= x!=0 ) or 1
    return y
def cosx_x(x):
    y =numpy.array(1)
    cos = numpy.cos(x)
    print(cos)
    y=numpy.divide(cos, x, where= x!=0 ) or 1
    return y

# def main():
    # father_name, father_age = input("insert father name and father age ").split()
    # mother_name, mother_age = input("insert mather name and mother age").split()
    # num_of_children = int(input("insert num of children"))
    # children: dict = dict()
    # for i in range(num_of_children):
    #     child_name, child_age = input("insert child name and child age").split()
    #     children[child_name] = child_age
    # last_name = input("insert last name") or "None"
    # mother_details = {"mother_name": mother_name, "mother_age": mother_age}
    # father_details = {"father_name": father_name, "father_age": father_age}
    # parents = {"father": father_details, "mother": mother_details}
    # f1 = Family(parents=parents, children=children, last_name=last_name)
    # f1.add_child("ya", 13)
    # print(f1.get_children(), f1.get_parents_names())
    # ================
    # print(sinx_x(0))
    # =============
    # t= numpy.arange(-100,100,0.01)
    # print(t)
    # sinx=[sinx_x(x) for x in t ]
    # cosx=[cosx_x(x) for x in t ]
    # print(cosx)
#
# if __name__=="__main__":
#     main()

# class Mother:
#     def __init__(self, mother_name, mother_age):
#         self.mother_details = {"mother_name": mother_name, "mother_age": mother_age}
#
#     def getMotherDetails(self):
#         return self.mother_details
#
#
# class Father:
#     def __init__(self, father_name, father_age):
#         self.father_details = {"father_name": father_name, "father_age": father_age}
#
#     def getFatherDetails(self):
#         return self.father_details
#
#
# class Child:
#     def __init__(self, child_name, child_age):
#         self.father_details = {"child_name": child_name, "child_age": child_age}
#
#     def getChildDetails(self):
#         return self.child_details
#
#
# class Family(Mother, Father, Child):
#     def __init__(self, father_name, father_age, mother_name, mother_age, children):
#         # self.father_details=father_details
#         # self.mother_details=mother_details
#         # self.children=children
#         super(Father, self).__init__(father_name, father_age)
#         super(Mother, self).__init__(mother_name, mother_age)
#         self.parents = {"father": Father.getFatherDetails(), "mother": Mother.getMotherDetails()}
#         self.children = children
#
#
#
# def main():
#     father_name, father_age = input("insert father name and father age ").split()
#     mother_name, mother_age = input("insert mather name and mother age").split()
#     num_of_children = input("insert num of children")
#     children = dict()
#     for i in range(num_of_children):
#         child_name, child_age = input("insert child name and child age").split()
#         children[child_name] = child_age
#     last_name = input("insert last name") or "None"
#     family = Family(father_name, father_age, mother_name, mother_age, children)
# if __name__=="__main__":
#     main()
