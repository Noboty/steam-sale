import json, urllib.request, urllib.error

with open('dictionary.txt', 'r') as game_list:    # Opens up the dictionary.txt and loads the json up
   games = json.load(game_list)

while True:
    appid = "" 
    try:
        try:
            game_name = input("Please enter a game or q to quit: ") # Prompts user to enter a game and store result in variable game_name
            print()
            if (game_name.lower() == "q"):
                quit()
            else:
                appid = str(games[game_name])
        except KeyError:
            suggestions = []
            for i in games: # loop through all keys in a list
                game = i.lower() # make current game name lowercase and store in game
                for change in ["(TM)", "(R)", u"\u2122", u"\u00AE"]: # Checks if game has one of these in it and replaces it if so.
                    game.replace(change, "")
                    game.replace("  ", " ")
                if (game_name.lower() in game):
                    suggestions.append(i)
            if (len(suggestions) == 1):     
                appid = str(games[suggestions[0]])
            else:
                count = 1
                print("Game not found. Suggestions: ")
                for i in suggestions:
                    print("{}) {}".format(count, i))
                    count += 1
                choice = int(input("Choose suggestion: "))
                while choice not in range(1, count + 1):
                    print("Invalid suggestion. Try again.")
                    choice = int(input("Choose suggestion: "))
                print()
                appid = str(games[suggestions[choice - 1]])

        API_KEY = "4E131660438CBF3C40BFC3E7F7CFE3D7"
        url = "http://store.steampowered.com/api/appdetails/?appids="
        url += appid
        url += "&key=" + API_KEY
        response = urllib.request.urlopen(url).read().decode()
        data = json.loads(response)

        final_price = data[str(appid)]['data']['price_overview']['final'] / 100
        initial_price = data[str(appid)]['data']['price_overview']['initial'] / 100
        discount_percent = data[str(appid)]['data']['price_overview']['discount_percent']
        saved = initial_price - final_price

        print(game_name + ":")                                 # Formats the data retrieved for the user
        print("""Current Discount: {}%
Initial Price: ${}
Price after discount: ${}
$$$ Saved: ${:.2f}""".format(discount_percent, initial_price, final_price, saved))
        print()
    except urllib.error.HTTPError:
        print()
