def dobrar(list_num = []):
    pos = 0
    while pos < len(list_num):
        list_num[pos] *= 2
        pos += 1

values = [1, 2, 3, 4]
dobrar(values)
print(values)
