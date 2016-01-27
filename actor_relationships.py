from urllib.error import HTTPError

import string_functions
import soup_info_functions
import soup_operations_functions


def get_related_actors(soup):
    related_actors = {}
    links = soup.find_all('a')
    for link in links:
        if not link_has_good_href(link):
            continue
        actor_slug = get_actor_slug(link)
        actor_url  = string_functions.to_wiki_url(actor_slug)
        if actor_url in related_actors.values():
            continue
        try:
            actor_soup = soup_operations_functions.get_html_soup(actor_url)
        except HTTPError:
            continue
        if soup_info_functions.is_an_actor(actor_soup):
            actor_name = soup_info_functions.get_person(actor_soup)
            if actor_name == soup_info_functions.get_person(soup):
                continue
            related_actors[actor_name] = actor_url
            print(actor_name)
    return related_actors


def link_has_good_href(link):
    if not link_has_href(link):
        return False
    href_value = get_href_value(link)
    bad_start_values = ['#','//','http','/w/']
    for bad_value in bad_start_values:
        if href_value.startswith(bad_value):
            return False
    if href_value.endswith('film)') or string_functions.has_percentage_sign(href_value) or 'filmography' in href_value.lower() or string_functions.has_best_actor(href_value):
        return False
    return True


def link_has_href(link):
    return string_functions.has_href(link)


def get_href_value(link):
    return link['href']


def get_actor_slug(link):
    href_value = get_href_value(link)
    actor_slug = href_value[6:]
    return actor_slug


def print_related_actors(related_actors):
    print(related_actors)







def link_is_filmography(link):
    if not link_has_title(link):
        return False
    title_value = get_title_value(link)
    if title_value[-11:].lower() == 'filmography':
        print('reached filmography')
        return True

def link_has_title(link):
    return string_functions.has_title(link)
    
def get_title_value(link):
    return link['title']