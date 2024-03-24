import requests

f = open('APIKEY', 'r')
APIKEY = f.read()
print(APIKEY)
f.close()
steamQuest = requests.get(APIKEY)


def steam_data_handler(game_json):
    result = ''
    result += game_json['name'] + '\n'
    result += '两周游玩时间: ' + str(game_json['playtime_2weeks']) + '分钟\n'
    result += '总游玩时间: ' + str(game_json['playtime_forever']) + '分钟\n'
    return result


# print(steamQuest.text)
data = steamQuest.json()
data = data['response']['games']
time_total = 0
for i in data:
    time_total += i['playtime_2weeks']
print('两周时长为:', time_total / 60, '小时')
print(data)
for i in data:
    print(steam_data_handler(i))
