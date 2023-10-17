import requests
from bs4 import BeautifulSoup

url = 'https://quizplease.ru/schedule?QpGameSearch%5BcityId%5D=160&QpGameSearch%5Bdates%5D=&QpGameSearch%5Bstatus%5D%5B%5D=1&QpGameSearch%5Btype%5D%5B%5D=all&QpGameSearch%5Btype%5D%5B%5D=1&QpGameSearch%5Btype%5D%5B%5D=3&QpGameSearch%5Btype%5D%5B%5D=5&QpGameSearch%5Btype%5D%5B%5D=9&QpGameSearch%5Bbars%5D%5B%5D=1231'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
data = soup.css.select(".schedule-block-head.w-inline-block")

games = list(map(lambda x: (x.attrs['href'].rsplit("=")[-1],x.css.select(".h2.h2-game-card.h2-left")[0].string), data))

with open('games.txt', 'rt+') as f:
    lines = f.readlines()
    for game in games:
        if game[0] in lines:
            continue
        print(f"ЗАПИШИСЬ НА ИГРУ БЛЯДЬ\n\t{ game[1]}\n\thttps://quizplease.ru/game-page?id={game[0]}")
        f.writelines(game[0])