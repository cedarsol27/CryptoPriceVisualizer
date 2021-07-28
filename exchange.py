### This is the data visual component. Use collect.py first


import plotly.express as px
import json
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class getCoinData:
    def __init__(self, coin):
        self.coin = coin

    # open file related to coin name. 
    # Coin name must be entered exactly like coin list
    def loadData(self):
        with open("crypto_data_" + self.coin + ".json", "r") as openfile:
            data = json.load(openfile)
            return data

    # convert to readable human time
    def get_timestamp_array(self):
        result = [datetime.fromtimestamp(elem[0] / 1000) 
        for elem in self.loadData()["prices"]]
        return result

    # get prices
    def get_market_prices_array(self):
        result = [elem[1] for elem in self.loadData()["prices"]]
        return result

    # plot Bitcoin data
    def setMainPlots(self):
        timestamp = self.get_timestamp_array()
        market = self.get_market_prices_array()
        fig = px.line(
            x=timestamp,
            y=market,
            title= self.coin + " Price over Time"
        )
        # gives ability to trace additional coins
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(
            go.Scatter(x=timestamp, y=market, name="Bitcoin"), 
            secondary_y=False, 
        )
        print("Bitcoin price is default\n")

        # user choice to select more coin data
        option = input("Would you like to add more crypto data? ('yes' continues, all else ends)\n")
        while option == "yes":

            # userinput identifies name for legend
            # userinout2 gets data
            userinput = input("Select the name of the coin: \n")
            userinput2 = getCoinData(userinput)
            fig.add_scatter(
                x= getCoinData.get_timestamp_array(userinput2),
                y= getCoinData.get_market_prices_array(userinput2),
                name= userinput
            )

            # continues a loop
            option = input("Would you like to add more crypto data? \n")

        # updates layout
        fig.update_layout(
            title="Crypto comparative prices over time",
            xaxis_title="Time",
            yaxis_title="Price",
            legend_title="Coins",
            font=dict(
                family="Times New Roman, monospace",
                size=18,
                color="Purple"
            )
        )

        # once all data is gathered, show in a web browser
        fig.show()

# Bitcoin is default for mapping
getCoinData("bitcoin").setMainPlots()