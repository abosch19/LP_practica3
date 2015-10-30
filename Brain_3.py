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
        self.wumpus = True
        self.robot.move('reset')
    def step(self):
        if not self.robot.getItem('win'):
            self.pilot.setSonar(self.robot.getItem('sonar'))
            if self.pilot.isCrossRoad():
                if self.wumpus:
                    talk = self.robot.move('talk')
                    if not talk == "This thing doesn't speak!":
                        self.actions.push(talk)
                    else:
                        self.actions.moveHead()
                        self.wumpus = False
                        self.backtrace.append(self.inverse[self.pilot.getPrevious()])
                        if self.pilot.moveTo(self.actions.getCurrent()):
                            self.robot.move(self.actions.pop())
                else:
                    self.backtrace.append(self.inverse[self.pilot.getPrevious()])
                    if self.pilot.moveTo(self.actions.getCurrent()):
                        self.robot.move(self.actions.pop())
                        
            else:
                if self.robot.move(self.pilot.nextMove()) == 'gold':
                    self.robot.move('grab')
                    self.backtrace.reverse()
                    for i in self.backtrace:
                        self.actions.push(i)
                    
def INIT(engine):
    return WB('WB', engine)
