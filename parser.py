from bs4 import BeautifulSoup
import requests
import csv
import json


url = 'https://www.kinonews.ru/games_top100/'

req = requests.get(url)
# with open('index.html','w')as file:
#     file.write(req.text)
with open('index.html','r')as file:
    read_file = file.read()
bs = BeautifulSoup(read_file,'lxml')
db ={}
big = bs.find('div',class_='bigtext')
# print(len(big.text))
names_games = bs.find_all('div',class_='bigtext')
years_of_games= []
names_of_games= []
for  a in names_games:

    year_game = a.text[-4:]
    name_of_game = a.find('a')
    name_of_game = name_of_game.text
    db[name_of_game]=year_game
    print(f'{name_of_game}| Год выпуска: {year_game[-4:]}')
# db = {names_of_games:years_of_games}   
# with open('dbd.csv','w',encoding='utf-8')as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             ('Название игры','Год выпуска',)
#         ) 
# for a,b in db.items():
#     with open('dbd.csv','a',encoding='utf-8')as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             (a,b)
#         )

with open('db.json','w',encoding='utf-8')as file:
    json.dump(db,file,indent=4,ensure_ascii=False)