#Functions that give information about a given BeautifulSoup object

import re

def get_first_p_tag(soup):
    return soup.p

def get_first_bold_element_text(soup):
    first_p_tag = get_first_p_tag(soup)
    #print(soup.p.b)
    return soup.p.b
    #return first_p_tag.b.get_text().lower()

def get_first_p_tag_text(soup):
    first_p_tag = get_first_p_tag(soup)
    if first_p_tag is None:
        return ''
    return first_p_tag.get_text().lower()
    
def get_text_before_period(text):
    return text.split('.')[0]

def is_an_actor(soup):
    first_p_tag_text = get_first_p_tag_text(soup)
    p_tag_first_sentence = get_text_before_period(first_p_tag_text)
    #first_bold_tag = get_first_bold_element_text(soup)
    actor_words = 'actor', 'actress'
    for actor_word in actor_words:
        actor_regex = r'\b{actor}\b'.format(actor=actor_word)
        actor_match = re.search(actor_regex, p_tag_first_sentence)
        if actor_match:
            return True
    return False

def is_a_director(soup):
    first_p_tag_text = get_first_p_tag_text(soup)
    p_tag_first_sentence = get_text_before_period(first_p_tag_text)
    director_words = 'director', 'filmmaker'
    for director_word in director_words:
        director_regex = r'\b{director}\b'.format(director=director_word)
        match = re.search(director_regex, p_tag_first_sentence)
        if match:
            return True
    return False


def is_a_composer(soup):
    first_p_tag_text = get_first_p_tag_text(soup)
    p_tag_first_sentence = get_text_before_period(first_p_tag_text)
    composer_words = 'composer',
    for composer_word in composer_words:
        composer_regex = r'\b{composer}\b'.format(composer=composer_word)
        match = re.search(composer_regex, p_tag_first_sentence)
        if(match):
            return True
    return False
    
def get_person(soup):
    title_string = soup.title.string
    endIndex = title_string.index(' - Wikipedia')
    person = title_string[:endIndex]
    #print(person)
    return person

#Not currently used
#Fix edge cases like quotes in bold tags (Babe Ruth) 
#Fix edge cases side panel w/bold (Barack Obama)
#Fix edge cases where full name has quotes (Brad Pitt)
def get_full_name(soup):
    print(soup.b.string)
    return soup.b.string