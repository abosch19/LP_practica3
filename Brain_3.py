# -*- coding: latin-1 -*- # Comentari per permetre que s'utilitzin accents i caràcters especials als comentaris i les cadenes de text.

from pyrobot.brain import Brain

import QueueList
reload(QueueList) # 'reload' serveix per forçar que Python carregui l'arxiu QueueList. 
import Pilot
reload(Pilot) # 'reload' serveix per forçar que Python carregui l'arxiu Pilot. 

class WB(Brain):
    def setup(self):
        self.inverse = {'up' : 'down', 'down' : 'up', 'right' : 'left', 'left' : 'right'}
        self.actions = QueueList.QueueList()
        self.pilot = Pilot.Pilot()
        self.backtrace = []
        self.robot.move('reset')
    def step(self):
        pass

def INIT(engine):
    return WB('WB', engine)
