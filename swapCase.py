def swap_case(s):
    answer_str = ''
    alpha = 'qwertyuiopasdfghjklzxcvbnm'
    Alpha = 'QWERTYUIOPASDFGHJKLMNBVCXZ'
    for i in s:
        if i in alpha:
            i = i.upper()
            answer_str = answer_str + i
        elif i in Alpha:
            i = i.lower()
            answer_str = answer_str + i
        else:
            answer_str = answer_str + i





    return answer_str

