def split_and_join(line):
    ans = ''
    for i in line:
        if i == ' ':
            i = '-'
            ans = ans + i
        else:
            ans = ans + i

    return ans