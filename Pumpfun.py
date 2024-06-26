## Spencer Pump.fun discord webhooks
## 5/29/2024
# First application using API's

import requests
from requests.adapters import HTTPAdapter, Retry
import json
import cryptocompare
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

from helius import BalancesAPI


solana_endpoint = 'https://api.mainnet-beta.solana.com'
requests = requests.Session()
retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])

requests.mount('http://', HTTPAdapter(max_retries=retries))


proxyrotate = {'https':'Enter Proxy Here',

'https':'Enter Proxy Here',

'https':'Enter Proxy Here',

'https':'Enter Proxy Here',

'https':'Enter Proxy Here'}


webhook = DiscordWebhook(url="Enter Webhook link Here")



balances_api = BalancesAPI("Enter API key Here")

response = requests.get('https://frontend-api.pump.fun/coins/latest')
addy1 = response.json()['mint']  
addy2 = ''  
addy3 = ''

list = [addy1,addy2,addy3]

embed = DiscordEmbed

while True:

    try:
        
        response = requests.get('https://frontend-api.pump.fun/coins/latest')# , proxies = proxyrotate)
        time.sleep(0.5)
        addy2 = response.json()['mint']
        time.sleep(0.25)

    except:
        addy = 0
    while (addy2 == 0):
        response = requests.get('https://frontend-api.pump.fun/coins/latest')# , proxies = proxyrotate)
        
        addy2 = response.json()['mint']
        time.sleep(0.25)

    if (addy2 in list):
        print(response.status_code)
        nothing = 'nothing'
        
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

        
        try:
            balances = balances_api.get_balances(dev)
            
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
            
            try:
                while (n < sizeoflist):
                    templist = firstfive[n]

                    my_dict[n] = {}
                    tempname = templist.get('name')
                
                    tempmint = templist.get('mint')
                
                    tempmc = templist.get('usd_market_cap')
                
                    complete = templist.get('complete')
                
                    my_dict[n]['name'] = tempname
                
                    my_dict[n]['mint'] = tempmint
                    my_dict[n]['marketcap'] = tempmc
                    my_dict[n]['complete'] = complete
                

                    n = n+1
            except:
                  my_dict = {}
                      
                

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


  
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute(remove_embeds=True)
        my_dict.clear()
        #else:

          

        list.append(addy2)
        list.pop(0)
        
