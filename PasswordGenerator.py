# password generator 

import random

def password(char=4,num=2,capitals=2):
    password = ''
    nums = random.sample([1,2,3,4,5,6,7,8,9],num)
    nums = ''.join(map(str,nums))
    small_list = []
    capital_list = []
    for i in range(1,27):
        small_list.append(i+96)
        capital_list.append(64+i)
    small_letters = random.sample(small_list,char)
    small_letters = ''.join(map(chr,small_letters))
    capital_letters = random.sample(capital_list,capitals)
    capital_letters = ''.join(map(chr,capital_letters))
    res = nums+small_letters+capital_letters
    x = list(res)
    random.shuffle(x)
    res = ''.join(x)
    return res
key = password()

print(key)