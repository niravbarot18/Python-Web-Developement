import requests

url = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin")
mydata = url.json()
print(mydata)

print(type(mydata))

print(mydata.keys())
print(len(mydata))

#accesing data
#inr price
print(mydata["market_data"]["current_price"]["inr"])

#usd price
print(mydata["market_data"]["current_price"]["usd"])

#24 hours change in inr
print(mydata["market_data"]["price_change_24h_in_currency"]["inr"])




#5 Analysis:

#1. 24-Hour Bitcoin Price Analysis (High & Low Prices)
print(mydata["market_data"]["high_24h"]["inr"])
print(mydata["market_data"]["low_24h"]["inr"])

print(mydata["market_data"]["high_24h"]["usd"])
print(mydata["market_data"]["low_24h"]["usd"])


#2. Bitcoin Developer Activity Analysis
print(mydata["developer_data"]["pull_requests_merged"])
print((mydata["developer_data"]["pull_request_contributors"]))


#3. Bitcoin Trading Volume Analysis
print(mydata["market_data"]["total_volume"]["inr"])
print(mydata["market_data"]["total_volume"]["usd"])


#4. Market Capitalization Change Percentage Analysis (24 Hours)
print(mydata["market_data"]["market_cap_change_percentage_24h_in_currency"]["aed"])
print(mydata["market_data"]["market_cap_change_percentage_24h_in_currency"]["inr"])


#5. Data Update & Fetch Time Analysis
print(mydata["last_updated"])
print(mydata["tickers"][0]["last_fetch_at"])