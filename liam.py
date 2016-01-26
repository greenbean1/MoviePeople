import soup_info_functions
import soup_operations_functions
import string_functions
import actor_relationships


#neverforgetyourroots
LIAM_NEESON_WIKIPEDIA_URL = 'https://en.wikipedia.org/wiki/Liam_Neeson'


def main():
    name = string_functions.get_input_name().lower()
    wiki_url = string_functions.name_to_url(name)
    html_soup = soup_operations_functions.get_html_soup(wiki_url)
    soup_operations_functions.print_roles(html_soup)
    related_actors = actor_relationships.get_related_actors(html_soup)
    actor_relationships.print_related_actors(related_actors)


if __name__ == '__main__':
    main()