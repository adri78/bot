import requests
import pymysql
import json 

from time import time



url = "https://global-openapi.bithumb.pro/openapi/v1/spot/orderBook?symbol="
 
Pares = ["BTC-USDT", "ETH-USDT", "ETH-BTC", "LTC-USDT", "BCH-USDT", "CRO-USDT", "LTC-BTC", "CRO-BTC", "BCH-BTC","LTC-ETH","CRO-ETH","BCH-ETH"]

SQL = "INSERT INTO `historicos`(`id`, `Fecha`,`BTC_BP`, `BTC_BC`, `BTC_AP`, `BTC_AC`,`ETH_BP`, `ETH_BC`, `ETH_AP`, `ETH_AC`,`ETH_BTC_BP`, `ETH_BTC_BC`, `ETH_BTC_AP`, `ETH_BTC_AC`,`LTC_BP`, `LTC_BC`, `LTC_AP`, `LTC_AC`,`BCH_BP`, `BCH_BC`, `BCH_AP`, `BCH_AC`,`CRO_BP`, `CRO_BC`, `CRO_AP`, `CRO_AC`,`LTC_BTC_BP`, `LTC_BTC_BC`, `LTC_BTC_AP`, `LTC_BTC_AC`,`CRO_BTC_BP`, `CRO_BTC_BC`, `CRO_BTC_AP`, `CRO_BTC_AC`,`BCH_BTC_BP`, `BCH_BTC_BC`, `BCH_BTC_AP`, `BCH_BTC_AC`,`LTC_ETH_BP`, `LTC_ETH_BC`, `LTC_ETH_AP`, `LTC_ETH_AC`,`CRO_ETH_BP`, `CRO_ETH_BC`, `CRO_ETH_AP`, `CRO_ETH_AC`,`BCH_ETH_BP`, `BCH_ETH_BC`, `BCH_ETH_AP`, `BCH_ETH_AC`) VALUES  (NULL, CURRENT_TIMESTAMP,'"


while True:
    tmp = ""
    t1 = time()
    for Par in Pares:
        r = requests.get(url+Par)  # metodo get
        if r.status_code == 200:  # veo el estado
            Data = r.json() # Codifica con json como un dicionario
        #print('\n' +Par + '\n')
            tmp = tmp + Data['data']['b'][0][0] + "','" + Data['data']['b'][0][1] +"','"  \
            + Data['data']['s'][0][0] + "','" + Data['data']['s'][0][1] + "','"

    SQL2= SQL +tmp[:-2] +");"

    conn = pymysql.connect(host="localhost", port=3306,
                       user="root", passwd="", db="bithumb")
    cursor = conn.cursor()
    cursor.execute(SQL2)
    conn.commit()
    conn.close()

    TTotal = time() -t1

    print(TTotal)
    print( " TERMINADO ") 

