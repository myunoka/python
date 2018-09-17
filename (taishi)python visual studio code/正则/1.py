import re

xx = 'A1B279C3D47'

def server(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'
    

cc = re.findall('\d',  xx)
print(cc)