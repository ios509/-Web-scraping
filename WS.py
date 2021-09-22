import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(requests.get("https://sa.mostaql.com/projects?keyword=python&budget_max=10000&sort=latest").content, 'lxml')

findTitle = soup.find_all('h2', {'class', 'mrg--bt-reset'})
listTitle = [i.text.strip() for i in findTitle]

findDiscreb = soup.find_all('a', {'class', 'details-url'})
listDiscreb = [i.text.strip() for i in findDiscreb]

links = [i.find('a').attrs['href'] for i in findTitle]
salarys = []

for link in links:
    soup1 = BeautifulSoup(requests.get(link).content, 'lxml')
    salary = soup1.find('span', {'dir': 'rtl'}).text
    salarys.append(salary)

allLists = [listTitle, listDiscreb, salarys, links]
exported = '\n'.join(list(
    map(lambda listTitle, listDiscreb, salarys, links: f'{listTitle}\n{listDiscreb}\n{salarys}\n{links}\n\n\n',
        listTitle, listDiscreb, salarys, links)))

open_file = open('info.txt', 'w')
open_file.write(exported)
open_file.close()