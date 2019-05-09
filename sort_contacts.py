def sort_contacts(dictionary):
    sorted_list = []
    for name,info in sorted(dictionary.items()):
        sorted_list.append((name, info[0],info[1]))
    return sorted_list
