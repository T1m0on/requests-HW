import requests
heroes = ['Hulk', 'Captain America', 'Thanos']


def get_smartest(heroes = heroes, url = 'https://akabab.github.io/superhero-api/api/all.json'):
    all_heroes = requests.get(url).json()
    smartest_hero = ''
    int_dict = {}
    for hero in heroes:
        for i in all_heroes:
            if hero in i.values():
                int_dict[hero] = i['powerstats']['intelligence']
                smartest_hero = max(int_dict, key=int_dict.get)
    return (f'Умнейший будет {smartest_hero}')

print(get_smartest())
