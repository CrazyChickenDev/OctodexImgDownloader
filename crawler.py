from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def img_url():
    soup = urlopen('https://octodex.github.com')
    content = BeautifulSoup(soup.read(), 'html.parser')
    img_urls = []
    for link in content.find_all('img'):        
        if link.get('data-src') != None:
            img_urls.append('https://octodex.github.com' + link.get('data-src'))
    return img_urls

def img_name():
    soup = urlopen('https://octodex.github.com')
    content = BeautifulSoup(soup.read(), 'html.parser')
    img_names = []
    for link in content.find_all('a'):
        if link.text != None:
            img_names.append(link.text)
    print(img_names)
    return img_names

def img_download():
        i = 0
#     img_urls = img_url()
#     img_names = img_name()
#     i = 0
#     for url in img_urls:
#         urlretrieve(url, './Octodex/' + img_names[i] + '.jpg')
#         i += 1

if __name__ == '__main__':
#     img_download()
   img_name()
