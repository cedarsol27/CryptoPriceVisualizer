### This file is the data collector. You must access this file before using the visualization

import requests
import json

class collectData:

    # self becomes the name of the coin

    def __init__(self, coin):
        self.coin = coin

    def getData(self):

        # get a json response from market. User selected coin
        response = requests.get(
            "https://api.coingecko.com/api/v3/coins/"+self+"/market_chart?vs_currency=usd&days=max"
        )
        answer = response.json()
        json_object = json.dumps(answer, indent=4)

        # write market data into file
        with open("crypto_data_"+self+".json", "w") as outfile:
            outfile.write(json_object)

    # ask for coin. Will also display a list of current available coins.
    def askForData(self):
        option = input("Please select the coins you wish to gather data from.\n'list' will print all available coin data.\n")
        if option == 'list':
            getList = requests.get('https://api.coingecko.com/api/v3/coins/list')
            getList = getList.json()
            for item in getList:
                print(item["id"])
        else:
            collectData.getData(option)
            choice = input("Would you like to create another list of coin data?\n")
            while choice == "yes":
                collectData.askForData(option)
                choice = input("Would you like to create another list of coin data?\n")

collectData("").askForData()