# -*- coding: utf-8 -*-
import random as rd
import string as s
import itertools
h = str(s.ascii_letters + s.digits)
key =input("enter your key value:")
hcopy = h
d = []
for char1 in h:
    for char2 in hcopy:

        d.append(char1+char2)

alpha1 = itertools.combinations_with_replacement(h,key)
alpha2 = itertools.permutations(h,key)
alpha3 = itertools.chain(h)
alpha_num = []
result1 = []
result2 = []
result3 = []
for items in alpha1:
    result1.append(''.join(list(items)))

for items in alpha2:
    result2.append(''.join(list(items)))
for items in alpha3:
    result3.append(''.join(list(items)))
#print result
#print len(result)
alpha_num  = result1 + result2 + d

hal = rd.choice(alpha_num)
print hal