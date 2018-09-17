
day = 0

def get_sunday():
    return 'get_sunday'

def get_monday():
    return 'get_monday'

def get_tuesday():
    return 'get_tuesday'

switcher = {
    0 : get_sunday,
    1 : get_monday,
    2 : get_tuesday
}

day_name = switcher.get(day, 'Unkown')()
print(day_name)