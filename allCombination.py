def return_substrings(input_string):
    length = len(input_string)
    comb=[input_string[i:j + 1] for i in range(length) for j in range(i, length)]
    print(comb)
    d={'a','e','i','o','u'}
    ajay=0
    raj=0
    for i in comb:
        if i[0] in d:
            ajay+=1
        else:
            raj+=1
    if ajay>raj:
        print('Ajay',ajay)
    if ajay<raj:
        print('Raj',raj)
    if ajay==raj:
        print('Draw')
return_substrings(input())