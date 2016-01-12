from bs4 import BeautifulSoup
import urllib.request
import re


LIAM_NEESON_WIKIPEDIA_URL = 'https://en.wikipedia.org/wiki/Liam_Neeson'


def main():
    name = get_input_name().lower()
    wiki_url = name_to_url(name)
    html_soup = get_html_soup(wiki_url)
    full_name = get_full_name(html_soup)
    print_roles(html_soup)

#Takes URL and returns a BeautifulSoup object
def get_html_soup(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def write_html(soup, output_file_name):
    pretty_html = soup.prettify()
    with open(output_file_name, 'w+') as file:
        file.write(pretty_html)


def get_first_p_tag(soup):
    return soup.p
    
def get_first_p_tag_text(soup):
    first_p_tag = get_first_p_tag(soup)
    return first_p_tag.get_text().lower()
    
#Fix via regex to include cases when actor/actress is at end of sentence or in a list (.,) Mel Gibson & John Williams
def is_an_actor(soup):
    text = get_first_p_tag_text(soup)
    match = re.search(r' actor[,\.]', text) #[\,\.]
    if match:
        print('actor')
        return True
    else:
        print('noactor')
        return False
    check1 = re.compile(' actor[,.]')
    x = re.search(re.compile(r' actor[,.]'), ' actor.')
    print(x)
    x = re.search(re.compile(r' actor[,.]'), text)
    print(x)
    #y = check1.search(' actor. hi s')
    val = re.match(check1, text)
    if(val):
        print(val.group())
    #x.group(0)
    print('hi')
    check2 = ' actress '
    #if(check1 in text or check2 in text):
    #    return True
    #else:
    #    return False

def is_a_director(soup):
    text = get_first_p_tag_text(soup)
    check1 = ' director '
    check2 = ' filmmaker '
    if(check1 in text or check2 in text):
        return True
    else:
        return False
        
def is_a_composer(soup):
    text = get_first_p_tag_text(soup)
    check1 = ' composer'
    if(check1 in text):
        return True
    else:
        return False

#improve to include director/composer, a/an, male/female
def print_roles(soup):
    name = get_person(soup)
    print('Actor: ' + str(is_an_actor(soup)))
    print('Director: ' + str(is_a_director(soup)))
    print('Composer: ' + str(is_a_composer(soup)))

def get_person(soup):
    title_string = soup.title.string
    endIndex = title_string.index(' - Wikipedia')
    person = title_string[:endIndex]
    print(person)
    return person
    
#Fix edge cases like quotes in bold tags (Babe Ruth) 
#Fix edge cases side panel w/bold (Barack Obama)
def get_full_name(soup):
    print(soup.b.string)
    return soup.b.string

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

if __name__ == '__main__':
    main()





