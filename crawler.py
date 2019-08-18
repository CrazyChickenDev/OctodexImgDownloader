from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def get_img_url():
    soup = urlopen('https://octodex.github.com')
    content = BeautifulSoup(soup.read(), 'html.parser')
    img_urls = []
    for link in content.find_all('img'):
        if link.get('data-src') != None:
            img_urls.append('https://octodex.github.com' + link.get('data-src'))
    return img_urls

def get_img_name():
    soup = urlopen('https://octodex.github.com')
    content = BeautifulSoup(soup.read(), 'html.parser')
    img_names = []
    for link in content.find_all('a'):
        if link.get('name') != None:
            img_names.append(link.get('name'))
    return img_names

def img_download():
    img_urls = get_img_url()
    img_names = get_img_name()
    i = 0
    for url in img_urls:
        urlretrieve(url, './Octodex/' + img_names[i] + '.jpg')
        i += 1

if __name__ == '__main__':
    img_download()