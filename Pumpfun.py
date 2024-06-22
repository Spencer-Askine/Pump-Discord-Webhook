## Spencer Pump.fun discord webhooks
## 5/29/2024
# First application using API's
#import cProfile
#import pstats
import requests
from requests.adapters import HTTPAdapter, Retry
import json
import cryptocompare
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
#from solana.rpc.api import Client
#from solders.pubkey import Pubkey
#from solathon import Client, PublicKey
from helius import BalancesAPI

#from theblockchainapi import TheBlockchainAPIResource

#MY_API_KEY_ID = RCkovU5Iyb4VEF9
#MY_API_SECRET_KEY = Iu99YrJWAMeXvks





solana_endpoint = 'https://api.mainnet-beta.solana.com'
requests = requests.Session()
retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])
requests.mount('http://', HTTPAdapter(max_retries=retries))


proxyrotate = {'https':'PXY_m1CQlTt5:rjotoinnv_country-us_direct-1@nft.bullproxies.com:12321',

'https':'PXY_m1CQlTt5:rjotoinnv_country-us_state-maryland_direct-1@nft.bullproxies.com:12321',

'https':'PXY_m1CQlTt5:rjotoinnv_country-us_state-virginia_direct-1@nft.bullproxies.com:12321',

'https':'PXY_m1CQlTt5:rjotoinnv_country-us_state-westvirginia_direct-1@nft.bullproxies.com:12321',

'https':'PXY_m1CQlTt5:rjotoinnv_country-us_state-delaware_direct-1@nft.bullproxies.com:12321'}


webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1245561134124105738/hUEMTSz6ONiKgQLrXHl9Cdh9vbXofPZx4_fqsmPSWZ2kRDirM7mzcczeFmwfWP54pz__")



balances_api = BalancesAPI("dc413c72-95b9-420c-8c7b-623fb40ba555")

response = requests.get('https://frontend-api.pump.fun/coins/latest')
addy1 = response.json()['mint']  
addy2 = ''  
addy3 = ''

list = [addy1,addy2,addy3]

embed = DiscordEmbed

#def api_call(addy1,addy2,addy3,embed):
while True:
    url = "https://solana-mainnet.g.alchemy.com/v2/ieeha2K6xgNACghpsuDehHuDRa9g_sJv"
    

    #{"jsonrpc":"2.0","error":{"code":-32602,"message":"`params` should have at least 1 argument(s)"},"id":1}

    try:
        #testresponse = requests.get('https://client-api-2-74b1891ee9f9.herokuapp.com/coins?offset=0&limit=20&sort=created_timestamp&order=desc&includeNsfw=true')
        #print(testresponse.json())
        response = requests.get('https://frontend-api.pump.fun/coins/latest')# , proxies = proxyrotate)
        time.sleep(0.5)
        addy2 = response.json()['mint']
        time.sleep(0.25)
        #print(addy2)
        #payload = {
        #    "id": 1,
        #    "jsonrpc": "2.0",
        #    "method": "getBalance"
        #    "Params": ["33UdRJm2p7FGYivdXEzMSM2qjpP3VcPGNTiDBhtCQybJ"]
#}
        #headers = {
        #    "accept": "application/json",
        #    "content-type": "application/json"
#}
        #response = requests.post(url, json=payload, headers=headers)


    except:
        addy = 0
    while (addy2 == 0):
        response = requests.get('https://frontend-api.pump.fun/coins/latest')# , proxies = proxyrotate)
        
        addy2 = response.json()['mint']
        time.sleep(0.25)

    if (addy2 in list):
        print(response.status_code)
        nothing = 'nothing'

            #api_call(addy1,addy2,addy3,embed)
        
    else:

        solPrice = cryptocompare.get_price(['SOL'],['USD'])
        solPrice = solPrice['SOL']
        solPrice = solPrice['USD']

        

        solMC = response.json()['market_cap']
        name = response.json()['name']
        desc = response.json()['description']
        addy = response.json()['mint']
        dev = response.json()['creator']
        image = response.json()['image_uri']
        twit = response.json()['twitter']
        tele = response.json()['telegram']
        site = response.json()['website']
        supply = response.json()['total_supply']
        symbol = response.json()['symbol']
        devholdings = 0
        pumplink = 'https://pump.fun/' + addy
        dev1 = 'https://pump.fun/profile/' + dev
        photon = 'https://photon-sol.tinyastro.io/en/lp/' + addy




        #your_pubkey = Pubkey.from_string(dev)
        #public_key = PublicKey(your_pubkey)
        #balance = solana_endpoint.get_balance(dev)
        #print(balance)

        #solscan = 'https://pro-api.solscan.io/v1.0/account/tokens?account=' + dev
        #solscan_output = requests.get(solscan,proxies = proxyrotate)
        #print(solscan_output)


        #devwallet = solana_endpoint.rpc.types.Pubkey.from_string(dev)
        #money = solana_endpoint.get_balance(Pubkey(dev))
        #devmoney = money['value']

        #GetBalanceResp { context: RpcResponseContext { slot: 269553824, api_version: Some("1.18.12") }, value: 933762493 }
#Sent
        #{'tokens': [], 'nativeBalance': 1600000000}
        
        try:
            balances = balances_api.get_balances(dev)
            #print(balances)
            for dic in balances:
                solacc = balances['nativeBalance']
                solacc = solacc * 0.000000001
                solacc = round(solacc,2)
        except:
            balance = 'N/A'
        try:
            devtrades = 'https://frontend-api.pump.fun/trades/' +addy+'?limit=10&offset=0'
            trades = requests.get(devtrades)
            devout = trades.json()
            for dictionary in devout:
                if (dictionary.get("user") == dev):
                    devbought = dictionary.get("token_amount")
                    devholdings = ((devbought/supply) * 100)
                    devholdings = round(devholdings,2)
                else:
                    devholdings = 0
        except:
            devholding = 'N/A'
           

        try:
            devcoins = 'https://frontend-api.pump.fun/coins/user-created-coins/' + dev + '?limit=10&offset=0&includeNsfw=true'
            
            devcoinget = requests.get(devcoins)
            devcoinlist = devcoinget.json()
            firstfive = devcoinlist[1:6]
            sizeoflist = len(firstfive)
            my_dict = {}
            n = 0
            print(sizeoflist)
            #print(firstfive[0])
            try:
                while (n < sizeoflist):
                    templist = firstfive[n]

                #my_dict[n].update({'mint':tempmint})
                #tempname = templist.get('name')
                #my_dict[n].update({'name':tempname})
                #tempmc = templist.get('usd_market_cap')
                #my_dict[n].update({'mc':tempmc})
                #tempcomp = templist.get('complete')
                #my_dict[n].update({'complete':tempcomp})
                    my_dict[n] = {}
                    tempname = templist.get('name')
                #print(tempname)
                    tempmint = templist.get('mint')
                #print(tempmint)
                    tempmc = templist.get('usd_market_cap')
                #print(tempmc)
                    complete = templist.get('complete')
                #print(complete)
                    my_dict[n]['name'] = tempname
                #my_dict[n].update({'mint':tempmint})
                    my_dict[n]['mint'] = tempmint
                    my_dict[n]['marketcap'] = tempmc
                    my_dict[n]['complete'] = complete
                

                    n = n+1
            except:
                  my_dict = {}
                      
            #for i in firstfive:
            #    newmint = i.get('mint')
            #    mintname = 'mint{n}'
            #    print(mintname)
            #    my_dict[n] = newmint
            #    n = n+1
                

        except:
            devcoinlist = 'N/A'
            sizeoflist = 0
            print('Dev coins api fried')
            my_dict = {}

        solscan = 'https://solscan.io/account/' + dev

        MC = solMC * solPrice
        MC = round(MC,2)
        Trojan = 'https://t.me/achilles_trojanbot?start=r-curiositynft-' + addy
        Bonk = 'https://t.me/furiosa_bonkbot?start=ref_lz8ym_ca_' + addy
            

        embed = DiscordEmbed(title= f'**{name}**',  url= pumplink, description= f'{desc}\n```{addy}```' , color="FF0000")
        embed.set_thumbnail(url=image)
        embed.set_author(name=f'${symbol}', url="", icon_url="")
        embed.add_embed_field(name="**Socials**", value =f'[Twitter]({twit})\n[Website]({site})\n[Telegram]({tele})')
        embed.add_embed_field(name="**Market Cap**", value=f'${MC:,}')
        embed.add_embed_field("**Dev Owns**", value =f'{devholdings}%' )
        embed.add_embed_field("Quick links", value =f'[Photon]({photon})  |  [Bonk]({Bonk})  |  [Trojan]({Trojan})')

        if sizeoflist == 0:
            embed.add_embed_field("Previous Coins", value =f' None')

        elif sizeoflist == 1:
            coin1name = my_dict[0].get('name')
            coin1addy = my_dict[0].get('mint')
            coin1mc = my_dict[0].get('marketcap')
            coin1comp = my_dict[0].get('complete')

            coin1link =  'https://pump.fun/' + coin1addy
            coin1mc = round(coin1mc)
            if coin1comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,}')
            else:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,}')
            
        
        elif sizeoflist == 2:
            coin1name = my_dict[0].get('name')
            coin1addy = my_dict[0].get('mint')
            coin1mc = my_dict[0].get('marketcap')
            coin1comp = my_dict[0].get('complete')
            coin2name = my_dict[1].get('name')
            coin2addy = my_dict[1].get('mint')
            coin2mc = my_dict[1].get('marketcap')
            coin2comp = my_dict[1].get('complete')
            coin1link =  'https://pump.fun/' + coin1addy
            coin2link =  'https://pump.fun/' + coin2addy
            coin1mc = round(coin1mc)
            coin2mc = round(coin2mc)
            
            if coin1comp == True and coin2comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}')
            elif coin1comp == True and coin2comp == False:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}')
            elif coin1comp == False and coin2comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}')
            else:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}')
            

        elif sizeoflist == 3:
            coin1name = my_dict[0].get('name')
            coin1addy = my_dict[0].get('mint')
            coin1mc = my_dict[0].get('marketcap')
            coin1comp = my_dict[0].get('complete')
            coin2name = my_dict[1].get('name')
            coin2addy = my_dict[1].get('mint')
            coin2mc = my_dict[1].get('marketcap')
            coin2comp = my_dict[1].get('complete')
            coin3name = my_dict[2].get('name')
            coin3addy = my_dict[2].get('mint')
            coin3mc = my_dict[2].get('marketcap')
            coin3comp = my_dict[2].get('complete')
            coin1link =  'https://pump.fun/' + coin1addy
            coin2link =  'https://pump.fun/' + coin2addy
            coin3link = 'https://pump.fun/' + coin3addy
            coin1mc = round(coin1mc)
            coin2mc = round(coin2mc)
            coin3mc = round(coin3mc)
            #
            if coin1comp == True and coin2comp == True and coin3comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}')
            elif coin1comp == True and coin2comp == True and coin3comp == False:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == False:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}')
            elif coin1comp == False and coin2comp == True and coin3comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}')
            elif coin1comp == False and coin2comp == True and coin3comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}')
            elif coin1comp == False and coin2comp == False and coin3comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}')
            else:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}')

        elif sizeoflist == 4:
            coin1name = my_dict[0].get('name')
            coin1addy = my_dict[0].get('mint')
            coin1mc = my_dict[0].get('marketcap')
            coin1comp = my_dict[0].get('complete')
            coin2name = my_dict[1].get('name')
            coin2addy = my_dict[1].get('mint')
            coin2mc = my_dict[1].get('marketcap')
            coin2comp = my_dict[1].get('complete')
            coin3name = my_dict[2].get('name')
            coin3addy = my_dict[2].get('mint')
            coin3mc = my_dict[2].get('marketcap')
            coin3comp = my_dict[2].get('complete')
            coin4name = my_dict[3].get('name')
            coin4addy = my_dict[3].get('mint')
            coin4mc = my_dict[3].get('marketcap')
            coin4comp = my_dict[3].get('complete')
            coin1link =  'https://pump.fun/' + coin1addy
            coin2link =  'https://pump.fun/' + coin2addy
            coin3link = 'https://pump.fun/' + coin3addy
            coin4link = 'https://pump.fun/' + coin4addy
            coin1mc = round(coin1mc)
            coin2mc = round(coin2mc)
            coin3mc = round(coin3mc)
            coin4mc = round(coin4mc)
            if coin1comp == True and coin2comp == True and coin3comp == True and coin4comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}')
            elif coin1comp == True and coin2comp == True and coin3comp == True and coin4comp == False:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}')
            elif coin1comp == True and coin2comp == True and coin3comp == False and coin4comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}')
            elif coin1comp == True and coin2comp == True and coin3comp == False and coin4comp == False:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == True and coin4comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == True and coin4comp == False:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == False and coin4comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == False and coin4comp == False:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}')
            elif coin1comp == False and coin2comp == True and coin3comp == True and coin4comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}')
            elif coin1comp == False and coin2comp == True and coin3comp == True and coin4comp == False:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}')
            elif coin1comp == False and coin2comp == True and coin3comp == False and coin4comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}')
            elif coin1comp == False and coin2comp == True and coin3comp == False and coin4comp == False:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}')
            elif coin1comp == False and coin2comp == False and coin3comp == True and coin4comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}')
            elif coin1comp == False and coin2comp == False and coin3comp == True and coin4comp == False:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}')
            elif coin1comp == False and coin2comp == False and coin3comp == False and coin4comp == True:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}')
            else:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}')



        elif sizeoflist == 5:
            coin1name = my_dict[0].get('name')
            coin1addy = my_dict[0].get('mint')
            coin1mc = my_dict[0].get('marketcap')
            coin1comp = my_dict[0].get('complete')
            coin2name = my_dict[1].get('name')
            coin2addy = my_dict[1].get('mint')
            coin2mc = my_dict[1].get('marketcap')
            coin2comp = my_dict[1].get('complete')
            coin3name = my_dict[2].get('name')
            coin3addy = my_dict[2].get('mint')
            coin3mc = my_dict[2].get('marketcap')
            coin3comp = my_dict[2].get('complete')
            coin4name = my_dict[3].get('name')
            coin4addy = my_dict[3].get('mint')
            coin4mc = my_dict[3].get('marketcap')
            coin4comp = my_dict[3].get('complete')
            coin5name = my_dict[4].get('name')
            coin5addy = my_dict[4].get('mint')
            coin5mc = my_dict[4].get('marketcap')
            coin5comp = my_dict[4].get('complete')
            coin1mc = round(coin1mc)
            coin2mc = round(coin2mc)
            coin3mc = round(coin3mc)
            coin4mc = round(coin4mc)
            coin5mc = round(coin5mc)
            coin1link =  'https://pump.fun/' + coin1addy
            coin2link =  'https://pump.fun/' + coin2addy
            coin3link = 'https://pump.fun/' + coin3addy
            coin4link = 'https://pump.fun/' + coin4addy
            coin5link = 'https://pump.fun/' + coin5addy

            if coin1comp == True and coin2comp == True and coin3comp == True and coin4comp == True and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611>${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}')
            elif coin1comp == True and coin2comp == True and coin3comp == True and coin4comp == True and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}')
            elif coin1comp == True and coin2comp == True and coin3comp == True and coin4comp == False and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}')
            elif coin1comp == True and coin2comp == True and coin3comp == True and coin4comp == False and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}')      
            elif coin1comp == True and coin2comp == True and coin3comp == False and coin4comp == True and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}')
            elif coin1comp == True and coin2comp == True and coin3comp == False and coin4comp == True and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}')
            elif coin1comp == True and coin2comp == True and coin3comp == False and coin4comp == False and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}')
            elif coin1comp == True and coin2comp == True and coin3comp == False and coin4comp == False and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == True and coin4comp == True and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == True and coin4comp == True and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611>${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == True and coin4comp == False and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == True and coin4comp == False and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == False and coin4comp == True and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}')
            elif coin1comp == True and coin2comp == False and coin3comp == False and coin4comp == True and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}')   
            elif coin1comp == True and coin2comp == False and coin3comp == False and coin4comp == False and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | <:radlogo:1247662817788825611> ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == True and coin3comp == True and coin4comp == True and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == True and coin3comp == True and coin4comp == True and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == True and coin3comp == True and coin4comp == False and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == True and coin3comp == True and coin4comp == False and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == True and coin3comp == False and coin4comp == True and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == True and coin3comp == False and coin4comp == True and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == True and coin3comp == False and coin4comp == False and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == True and coin3comp == False and coin4comp == False and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | <:radlogo:1247662817788825611> ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == False and coin3comp == True and coin4comp == True and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == False and coin3comp == True and coin4comp == True and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == False and coin3comp == True and coin4comp == False and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == False and coin3comp == True and coin4comp == False and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | <:radlogo:1247662817788825611> ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == False and coin3comp == False and coin4comp == True and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == False and coin3comp == False and coin4comp == True and coin5comp == False:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | <:radlogo:1247662817788825611> ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}') 
            elif coin1comp == False and coin2comp == False and coin3comp == False and coin4comp == False and coin5comp == True:
                    embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | <:radlogo:1247662817788825611> ${coin5mc:,}') 
            else:
                embed.add_embed_field("Previous Coins", value =f'[{coin1name}]({coin1link}) | ${coin1mc:,} \n [{coin2name}]({coin2link}) | ${coin2mc:,}\n [{coin3name}]({coin3link}) | ${coin3mc:,}\n [{coin4name}]({coin4link}) | ${coin4mc:,}\n [{coin5name}]({coin5link}) | ${coin5mc:,}')
                     
        
        
        
        
        
        
        
        embed.set_footer(text="Made by Curiosity.eth")  


        #if (site == 'None' or twit == 'None'or tele == 'None'):
            #webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1245561134124105738/hUEMTSz6ONiKgQLrXHl9Cdh9vbXofPZx4_fqsmPSWZ2kRDirM7mzcczeFmwfWP54pz__")
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute(remove_embeds=True)
        my_dict.clear()
        #else:

            #webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1247213583503200407/JRyE4GWjofM7BdVMxoGuCUY9JDWS1FNpVsigPXz-SaOaggPF6n0VUHmSgY42C7p3K1_-")
        #    embed.set_timestamp()
        #    webhook2.add_embed(embed)
        #    webhook2.execute(remove_embeds=True)

        list.append(addy2)
        list.pop(0)
        #print("Sent")
            #api_call(addy1,addy2,addy3,embed)

#api_call(addy1,addy2,addy3,embed)
