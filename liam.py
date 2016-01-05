from bs4 import BeautifulSoup
import urllib.request


LIAM_NEESON_WIKIPEDIA_URL = 'https://en.wikipedia.org/wiki/Liam_Neeson'


def main():
    html_soup = get_html_soup(url=LIAM_NEESON_WIKIPEDIA_URL)
    # write_html(html_soup, output_file_name='pretty_liam.txt')
    liam_neeson_is_an_actor = is_an_actor(html_soup)
    print('Is Liam Neeson an actor?!?! ' +
          'YES!' if liam_neeson_is_an_actor else 'no...')


def get_html_soup(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def write_html(html, output_file_name):
    pretty_html = soup.prettify()
    with open(output_file_name, 'w+') as file:
        file.write(pretty_html)


def get_first_p_tag(html_soup):
    return html_soup.p


if __name__ == '__main__':
    main()
