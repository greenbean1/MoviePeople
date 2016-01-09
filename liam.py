from bs4 import BeautifulSoup
import urllib.request


LIAM_NEESON_WIKIPEDIA_URL = 'https://en.wikipedia.org/wiki/Liam_Neeson'


def main():
    html_soup = get_html_soup(LIAM_NEESON_WIKIPEDIA_URL)
    full_name = get_full_name(html_soup)
    #write_html(html_soup, output_file_name='pretty_liam.txt')
    print(print_roles(html_soup))
    #liam_neeson_is_an_actor = is_an_actor(html_soup)
    #print('Is Liam Neeson an actor?!?! ' +
    #      'YES!' if liam_neeson_is_an_actor else 'no...')

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
    
def is_an_actor(soup):
    text = get_first_p_tag_text(soup)
    if('actor' in text or 'actress' in text):
        return True
    else:
        return False
        
def is_a_director(soup):
    text = get_first_p_tag_text(soup)
    if('director' in text or 'filmmaker' in text):
        return True
    else:
        return False
        
def is_a_composer(soup):
    text = get_first_p_tag_text(soup)
    if('composer' in text):
        return True
    else:
        return False

#improve to include director/composer, a/an, male/female
def print_roles(soup):
    name = get_person(soup)
    if(is_an_actor(soup)):
        print(name + ' is an actor.')
    else:
        print(name + ' is not an actor.')

def get_person(soup):
    title_string = soup.title.string
    endIndex = title_string.index(' - Wikipedia')
    person = title_string[:endIndex]
    print(person)
    return person
    
#Needs improvement with edge cases like quotes in bold tags (Babe Ruth)   
def get_full_name(soup):
    print(soup.b.string)
    return soup.b.string

if __name__ == '__main__':
    main()

