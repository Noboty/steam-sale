"""
Looks through Steam's games and writes them all into a txt with json format with their corresponding AppID.
"""
import urllib.request, json

STEAM_GAMES = {}
gamelistUrl = "http://api.steampowered.com/ISteamApps/GetAppList/v2" # Steam's list of games with corresponding AppID
jsonData = json.loads(urllib.request.urlopen(gamelistUrl).read().decode("utf-8")) # open the url and decode it from bytes to string.

for i in jsonData["applist"]["apps"]: # loop through all elements in the array jsonData["applist"]["apps"]
        STEAM_GAMES[i["name"]] = i["appid"] # Adds the data into a dictionary: APP_IDS[name_of_game] = AppID

with open('dictionary.txt', 'w') as game_list:
        json.dump(STEAM_GAMES, game_list) # Writes the dictionary in json format into steam-game-list.txt
