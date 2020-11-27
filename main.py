import bithumb

api_key = "d124af259a7df8d6da3c05002038cdfe"

secret_key = "d03c061357ba4edbad7ea0b75cc98"

a = bithumb.BithumbGlobalRestAPI(api_key, secret_key)


#url_Base="https://global-openapi.bithumb.pro/openapi/v1"

#hora_server= url_Base + "/serverTime"  # Da la Hora del server es corea 11hs +

#url_Config = url_Base + "/spot/config" #
#url_Tranfer= url_Base +"/transfer"
#url_ValorPar="https://global-openapi.bithumb.pro/openapi/v1/spot/orderBook?symbol = BTC-USDT"


#b = a.withdraw("BTC",)








b = a.depth("BTC", 1)

print(b)
