import numpy
import Family


def sinx_x(x):
    y = numpy.array(1)
    sin = numpy.sin(x)
    y = numpy.divide(sin, x, where=x != 0) or 1
    return y


def cosx_x(x):
    y = numpy.array(1)
    cos = numpy.cos(x)
    y = numpy.divide(cos, x, where=x != 0) or 1
    return y


def main():
    father_name, father_age = input("insert father name and father age ").split()
    mother_name, mother_age = input("insert mather name and mother age").split()
    num_of_children = int(input("insert num of children"))
    children: dict = dict()
    for i in range(num_of_children):
        child_name, child_age = input("insert child name and child age").split()
        children[child_name] = child_age
    last_name = input("insert last name") or "None"
    mother_details = {"mother_name": mother_name, "mother_age": mother_age}
    father_details = {"father_name": father_name, "father_age": father_age}
    parents = {"father": father_details, "mother": mother_details}
    f1 = Family(parents=parents, children=children, last_name=last_name)
    f1.add_child("ya", 13)
    print(f1.get_children(), f1.get_parents_names())
    #================
    print(sinx_x(0))
    #=============
    t = numpy.arange(-100, 100, 0.01)
    print(t)
    sinx = [sinx_x(x) for x in t]
    cosx = [cosx_x(x) for x in t]
    print(cosx, sinx)
    #==================
    name_list = ["aaa", "bbb", "ccc", "eee", "fff"]
    file_name = input("insert file name")
    file = open(file_name+".txt", "w")
    [file.write(x+"\n") for x in name_list]
    file.close()
    file = open(file_name+".txt", "r")
    lines = file.readlines()
    [print(lines[i]) for i in range(0, len(lines), 2)]
    file.close()


if __name__ == "__main__":
    main()