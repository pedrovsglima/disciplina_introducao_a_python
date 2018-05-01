import string
alpha = list(string.ascii_lowercase)

def name_value(mylist):
    new = [x.replace(' ', '') for x in mylist]
    final_list, num = [], 0
    for i, x in enumerate(new):
        for y in x:
            num += alpha.index(y) + 1
        final_list.append(num * (i+1))
        num = 0
    return final_list
