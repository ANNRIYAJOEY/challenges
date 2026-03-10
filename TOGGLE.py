str1=input('enter a string:-')
str2=''
for i in str1:
    if i.islower():
        str2=str2+i.upper()
    else:
        str2=str2+i.lower()
print('toggled string',str2)