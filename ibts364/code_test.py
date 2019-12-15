old_list = [
    "pname1:pid1:parent1:state1",
    "pname2:pid2:parent2:state2",
    "pname3:pid3:parent3:state3",
]

def filter_old_list():
    for elem in old_list:
        pname, pid, parent, state = elem.split(':')
        yield pname, pid

for pname, pid in filter_old_list():
    print pname, pid
