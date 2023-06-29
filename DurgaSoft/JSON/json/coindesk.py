"""
<class 'dict'>
time ,: {'updated': 'Mar 18, 2023 18:23:00 UTC', 'updatedISO': '2023-03-18T18:23:00+00:00', 'updateduk': 'Mar 18, 2023 at 18:23 GMT'}
disclaimer ,: This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org chartName ,: Bitcoinbpi ,: {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '27,406.1090', 'description': 'United States Dollar', 'rate_float': 27406.109}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '22,900.3254', 'description': 'British Pound Sterling', 'rate_float': 22900.3254}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '26,697.5514', 'description': 'Euro', 'rate_float': 26697.5514}}

"""


import requests,json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bitcoiininfo = response.json()
print(type(bitcoiininfo))#python dict
# print(bitcoiininfo)#python dict

# for k,v in bitcoiininfo.items():
#     print(k,",:",v)

# print("BPI : ",bitcoiininfo["bpi"])
print("BPI : ",bitcoiininfo["time"]["updated"])
print("RATE : ",bitcoiininfo["bpi"]["USD"]["rate"])