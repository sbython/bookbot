def get_num_words(string):
    return len(string.split())

def sort_char(dic):
    return dic["num"]
def get_num_char(string):
    dic = {}
    string = string.lower()
    for i in string:
        if i.isalpha() == False:
            continue
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    new_dic = [
        {"char": k , "num": v}
        for k, v in dic.items()
    ]
    new_dic.sort(reverse=True, key=sort_char)
    return new_dic

