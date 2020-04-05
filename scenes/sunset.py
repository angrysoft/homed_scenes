from homedaemon.scenes import BaseAutomation
from datetime import datetime
from urllib import request
import json

class Scene(BaseAutomation):
    def __init__(self,sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'sunset'
        self.add_trigger('report.clock.time.01:00', self.pull)
        self.pull()
    
    def pull(self, *args):
        utcoffset = datetime.now() - datetime.utcnow()
        with request.urlopen('https://api.sunrise-sunset.org/json?lat=52.2319581&lng=21.0067249&formatted=0') as r:
            try:    
                ret = json.loads(r.read().decode())
                if 'results' in  ret:
                    ret = ret['results']
                    sunrise_utc = datetime.fromisoformat(ret.get('sunrise', '')) + utcoffset
                    sunset_utc = datetime.fromisoformat(ret.get('sunset', '')) + utcoffset
                    self.daemon.config['datetime'] = {'sunrise': f'{sunrise_utc.hour:02}:{sunrise_utc.minute:02}'}
                    self.daemon.config['datetime'] = {'sunset': f'{sunset_utc.hour:02}:{sunset_utc.minute:02}'}
                    self.daemon.config['datetime'] = {'update': f'{datetime.now()}'}
            except json.JSONDecodeError:
                pass
       
