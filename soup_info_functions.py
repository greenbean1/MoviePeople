#Functions that give information about a given BeautifulSoup object

import re

def get_first_p_tag(soup):
    return soup.p


def get_first_p_tag_text(soup):
    first_p_tag = get_first_p_tag(soup)
    return first_p_tag.get_text().lower()


def is_an_actor(soup):
    text = get_first_p_tag_text(soup)
    actor_words = 'actor', 'actress'
    for actor_word in actor_words:
        actor_regex = r'\b{actor}\b'.format(actor=actor_word)
        match = re.search(actor_regex, text)
        if match:
            return True
    return False


def is_a_director(soup):
    text = get_first_p_tag_text(soup)
    director_words = 'director', 'filmmaker'
    for director_word in director_words:
        director_regex = r'\b{director}\b'.format(director=director_word)
        match = re.search(director_regex, text)
        if match:
            return True
    return False


def is_a_composer(soup):
    text = get_first_p_tag_text(soup)
    composer_words = 'composer',
    for composer_word in composer_words:
        composer_regex = r'\b{composer}\b'.format(composer=composer_word)
        match = re.search(composer_regex, text)
        if(match):
            return True
    return False
    
def get_person(soup):
    title_string = soup.title.string
    endIndex = title_string.index(' - Wikipedia')
    person = title_string[:endIndex]
    print(person)
    return person

#Not currently used
#Fix edge cases like quotes in bold tags (Babe Ruth) 
#Fix edge cases side panel w/bold (Barack Obama)
#Fix edge cases where full name has quotes (Brad Pitt)
def get_full_name(soup):
    print(soup.b.string)
    return soup.b.string