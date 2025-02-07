import re

#it matches the regular expresion where word start with a and ends with c in between zero or more instance of b 
a = re.findall('ab*c','abbcd')
print(a)

# ignorecase is required otherwise it match case too
b = re.findall('ab*c','ABC',re.IGNORECASE)
print(b)

# Single characters between two
c = re.findall('a.c','abbc')
print(c)

# any numbers of character between two instance
d = re.findall('a.*c','ahelloworldc')
print(d)


# Search
a = re.search('ab*c','abc')
a.group()
print(a)

# replace
sentence = "Hello <World>"
a = re.sub('<.*>','Duniyaa',sentence)
print(a)

# Multiple replace using ?
sentence = "Hello <replace>\nGood Morning <tags>!!\nYou are <newone>"
a = re.sub('<.*?>',"World",sentence)
print(a)