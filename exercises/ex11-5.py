def count_es(string):
    if not string:
        return 0
    if string[0] != 'e':
        return count_es(string[1:])
    return 1 + count_es(string[1:])

def min_es(string_list):
    if not string_list:
        return 
    
    cur_str = string_list[0]
    next_str = min_es(string_list[1:])
    if count_es(cur_str) < count_es(next_str) or not next_str:
        return cur_str
    return next_str

if __name__ == '__main__':
    print(min_es(["samwise gamgee", "ent", "eomer"])) #ent
    print(min_es(["isildur", "legolas"])) #isildur
    print(min_es(["Gandalf"])) #Gandalf
    print(min_es(["TREEBEARD", "Celeborn"])) #TREEBEARD

