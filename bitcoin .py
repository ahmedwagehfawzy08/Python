from urllib import response
import requests
import time


# متغيرات
# بتحصل عليه من موقع CoinMarketCap
api_key = '1a918c7b-3971-4bb0-a251-7d572012291d'
# بتحصل عليه من التليجرام من ال bot father
bot_key = '5129956986:AAFCoUXcObVMi_ec8tMqw3ZOJVK8BFW6DFM'
chat_id = '5399890380'
limit = 40537  # ده الحد الي لو سعر البيتكوين وصل ليه يبعت انذار
time_interval = 60*10  # كل خمس دقايق البرنامج هيعمل سيرش عن سغر البيتكوين


def get_price():  # دي الداله الي هتجبلي السعر من الموقع
    # url='https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {
        'start': '1',
        'limit': '50',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price


def send_update(chat_id, msg):  # الداله الي هتبعت الرساله
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
    


def main():
    while True:
        price = get_price()
        
        if price < limit:
            send_update(chat_id, f"سعر البيتكوين بيقل :{price}")
        time.sleep(time_interval)
       


main()
