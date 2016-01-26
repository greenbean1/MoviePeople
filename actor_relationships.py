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
        actor_soup = soup_operations_functions.get_html_soup(actor_url)
        if soup_info_functions.is_an_actor(actor_soup):
            actor_name = soup_info_functions.get_person(actor_soup)
            related_actors[actor_name] = actor_url
    return related_actors


def link_has_good_href(link):
    if not link_has_href(link):
        return False
    href_value = get_href_value(link)
    return href_value[0] != '#'


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


