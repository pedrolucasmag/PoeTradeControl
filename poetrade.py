import logging
import requests

logger = logging.getLogger(__name__)


from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()


class PoeControl:
    def poetrade_on(self):
        if requests.get("http://control.poe.xyz.is/isikodusamikon"):
            logger.warning("Turning online poe.trade")
            requests.post("http://control.poe.xyz.is/isikodusamikon")
            
    def poetrade_off(self):
            logger.info("Turning offline poe.trade")
            requests.post("http://control.poe.xyz.is/isikodusamikon" + "/offline")
            logger.warning("Poe.Trade Status set to offline")        
            
    def steam_status(self):
            steamstatus = requests.get("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=F0980E8BC5B9D2B09FA73D068AD98EDE&format=json&steamids=76561198046989859").json()
            inpoe = steamstatus.get('response').get('players')[0].get('gameextrainfo')
            if inpoe == "Path of Exile":
                p.poetrade_on()
            else:
                p.poetrade_off()
                


                    

    
        
p = PoeControl()

# seconds can be replaced with minutes, hours, or days
sched.add_job(p.steam_status, 'interval', seconds=60)
sched.start()
