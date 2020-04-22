import requests
import time
import datetime



while True:
    try:
        result = requests.get('https://www.shipton-mill.com/queue')
        if "Sorry, we don't have any delivery slots available at this time, please come back later." in result.text:
            print('No slot')
        else:
            print(datetime.datetime.now())
            print(result.text)
            break
    except e:
        pass
    time.sleep(60)

