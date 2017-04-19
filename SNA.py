# i couldn't finish this part completely.
import inspect,os
def create_dict():
    sn = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\\" +"sn.txt", "a+")
    d = {}
    for line in sn:
        x = line.split(":")
        a = x[0]
        b = x[1].split()
        c = len(b)
        b = b[0:c]
        d[a] = b
    print d.keys()


def add_user(input_key_1, input_key_2):
    sn = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\\" +"sn.txt", "r")
    relation_dict = {}
    for line in sn:
        x = line.split(":")
        a = x[0]
        b = x[1].split()
        c = len(b)
        b = b[0:c]
        relation_dict[a] = b

    if input_key_1 in relation_dict.keys():
        print "This user already exists!!"
    else:
        if input_key_2 in relation_dict.keys():
            relation_dict[input_key_1] = input_key_2

            with open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\\" +"sn.txt", "a+") as test_file:
                test_file.write("\n" + input_key_1 + ":" + input_key_2)

            print "User " + str(input_key_1) + " has been added and tied to " + str(input_key_2) + " succesfully"
        else:
            print "There is no user named " + input_key_2


def remove_user(input_key_1):
    sn = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\\" +"sn.txt", "r")
    relation_dict = {}
    for line in sn:
        x = line.split(":")
        a = x[0]
        b = x[1].split()
        c = len(b)
        b = b[0:c]
        relation_dict[a] = b

    del relation_dict[input_key_1]


def add_relation(input_key_1, input_key_2):
    sn = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\\" +"sn.txt", "r")
    relation_dict = {}
    for line in sn:
        x = line.split(":")
        a = x[0]
        b = x[1].split()
        c = len(b)
        b = b[0:c]
        relation_dict[a] = b
    relation_dict[input_key_1] = input_key_2
    relation_dict[input_key_2] = input_key_1


def remove_relation(input_key_1, input_key_2):
    sn = open("sn.txt", "r")
    relation_dict = {}
    for line in sn:
        x = line.split(":")
        a = x[0]
        b = x[1].split()
        c = len(b)
        b = b[0:c]
        relation_dict[a] = b


def rank_users(input_key_1):
    print input_key_1


def suggest(input_key_1, input_key_2):
    print input_key_1, input_key_2


def analiz_commands():
    commandstxt = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\\" +"commandsP1.txt", "r")
    commands_read = commandstxt.read()
    commandstxt.close()
    commands = commands_read.splitlines()

    for i in commands:
        command_key = ""
        input_key_1 = ""
        input_key_2 = ""
        count_control = len(i.split(" "))
        if count_control == 1:
            command_key = i
        elif count_control == 2:
            command_key = i.split()[0]
            input_key_1 = i.split()[1]
        elif count_control == 3:
            command_key = i.split()[0]
            input_key_1 = i.split()[1]
            input_key_2 = i.split()[2]

        if command_key == "AU":

            try:
                add_user(input_key_1, input_key_2)
            except IndexError:
                print "Error: Wrong input type for 'AU'!"
        elif command_key == "RU":
            try:
                remove_user(input_key_1)
            except IndexError:
                print "Error: Wrong input type! for 'RU'!"
        elif command_key == "AR":
            try:
                add_relation(input_key_1, input_key_2)
            except IndexError:
                print "Error: Wrong input type! for 'AR'!"
        elif command_key == "RR":
            try:
                remove_relation(input_key_1, input_key_2)
            except IndexError:
                print "Error: Wrong input type! for 'RR'!"
        elif command_key == "PA":
            try:
                rank_users(input_key_1)
            except IndexError:
                print "Error: Wrong input type! for 'PA'!"
        elif command_key == "SA":
            try:
                suggest(input_key_1, input_key_2)
            except IndexError:
                print "Error: Wrong input type! for 'SA'!"


analiz_commands()
