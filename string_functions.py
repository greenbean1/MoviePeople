#Basic string or stringish functions
#No dependencies

def get_input_name():
    name = input('Please enter a name (first and last name separated with a space): ')
    print('You entered: ' + name)
    return name

def name_to_url(name):
    spaceIndex = name.index(' ')
    name = name[0].upper() + name[1:spaceIndex] + '_' + name[spaceIndex+1].upper() + name[spaceIndex+2:]
    print(name)
    url = 'https://en.wikipedia.org/wiki/'
    url = url + name
    print(url)
    return url
    
def to_wiki_url(slug):
    url = 'https://en.wikipedia.org/wiki/'
    url = url + slug
    #print('Wikipedia URL: ' + url)
    return url
    
def has_href(tag):
    return tag.has_attr('href')
    
def has_title(tag):
    return tag.has_attr('title')
    
def has_percentage_sign(text):
    return '%' in text
    