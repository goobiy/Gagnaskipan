
def len_str(a_str: str) -> int:
    if not a_str:
        return 0
    
    count = 1

    # minnka strenginn þangað til hann er tómur svo bæta öllu saman
    return count + len_str(a_str[1:])



def linear_search(list: list, val: object) -> bool:

    if not list:
        return False

    if list[0] == val:
        return True
        # minnka listann þangað til list[0] er True eða listinn er tómur þá False
    return linear_search(list[1:], val)



def count_instances(list: list, val: object) -> int:
    if not list:
        return 0
    
    count = 0
    
    if list[0] == val:
        count += 1
    

    return count + count_instances(list[1:],val)


def duplicates(list: list) -> bool:
    if len(list) <= 1:
        return False
    
    if list[0] in list[1:]:
        return True
    # chceks wether the first elem is in the rest of the list then so on
    return duplicates(list[1:])


def remove_duplicates(list: list) -> list:
    if len(list) <= 1:
        return list
    
    rest = remove_duplicates(list[1:])

    if list[0] in rest:
        return rest
    else:
        return [list[0]] + rest
        # Start at the back after rest is finished so if one elem is left line 50 return the single elem
        # then its compared to the first elem when there were two elem in the list, if they are the same we return the rest
        # if not we add it to the rest

