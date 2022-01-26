def add_friends(name, friend):
    if name in dict_friend:
        dict_friend[name] = dict_friend[name] + friend
    else:
        dict_friend[name] = friend
 
 
def are_friends(name1, name2):
    return name2 in dict_friend[name1]
 
    
def print_friends(name):
    print(*sorted(dict_friend[name]))
 
 
dict_friend = {}
