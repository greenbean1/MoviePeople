#Basic string or stringish functions
#No dependencies

def get_input_name():
    name = input('Please enter a name (first and last name separated with a space): ')
    return name

def name_to_url(name):
    spaceIndex = name.index(' ')
    name = name[0].upper() + name[1:spaceIndex] + '_' + name[spaceIndex+1].upper() + name[spaceIndex+2:]
    print(name)
    url = 'https://en.wikipedia.org/wiki/'
    url = url + name
    print(url)
    return url