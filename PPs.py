import inspect, os

run_commands = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\\" + "commandsP2.txt",
                    "r")
paths_file = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "\\" + "paths.txt", "r")
commands = run_commands.read()
command_list = commands.split(",")

dictionary = dict()
road_list = list()
key_list = list()
toread = paths_file.read()
toread_list = toread.splitlines()

for line in toread_list:
    x = line.split(":")
    a = x[0]
    b = x[1].split()
    c = len(b)
    b = b[0:c]
    dictionary[a] = b

for i, j in dictionary.iteritems():
    key_list.append(i)
    value_dict = dictionary[i]
    for t in value_dict:
        road_list.append(t)
    for r in road_list:
        if r in dictionary.keys():
            value_dict_2 = dictionary[r]
            for w in value_dict_2:
                road_list.append(w)
    for r in road_list:
        if r in dictionary.keys():
            value_dict_2 = dictionary[r]
            for w in value_dict_2:
                road_list.append(w)
    myset = set(road_list)
    print i, ":", [x for x in iter(myset)]
    road_list = []

for t in command_list:
    if t not in key_list:
        print "City '" + str(t) + "' has no reachable neighbour "

# All reachable neighbour checked from assignment pdf.
