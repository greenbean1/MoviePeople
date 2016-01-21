from bs4 import BeautifulSoup
import urllib.request
import re
import soup_info_functions
import soup_operations_functions
import string_functions

#neverforgetyourroots
LIAM_NEESON_WIKIPEDIA_URL = 'https://en.wikipedia.org/wiki/Liam_Neeson'

#Takes URL and returns a BeautifulSoup object
def get_html_soup(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def main():
    name = string_functions.get_input_name().lower()
    wiki_url = string_functions.name_to_url(name)
    html_soup = get_html_soup(wiki_url)
    full_name = soup_info_functions.get_full_name(html_soup)
    soup_operations_functions.print_roles(html_soup)



if __name__ == '__main__':
    main()





