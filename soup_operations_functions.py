#Functions that give operational support to BeautifulSoup stuff

import soup_info_functions


def write_html(soup, output_file_name):
    pretty_html = soup.prettify()
    with open(output_file_name, 'w+') as file:
        file.write(pretty_html)

#improve to include a/an, male/female
def print_roles(soup):
    name = soup_info_functions.get_person(soup)
    print('Actor: ' + str(soup_info_functions.is_an_actor(soup)))
    print('Director: ' + str(soup_info_functions.is_a_director(soup)))
    print('Composer: ' + str(soup_info_functions.is_a_composer(soup)))