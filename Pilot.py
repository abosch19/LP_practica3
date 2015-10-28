# -*- coding: latin-1 -*- # Comentari per permetre que s'utilitzin accents i carÃ cters especials als comentaris i les cadenes de text.

class Pilot(object):
    __slots__ = ['__previous', '__sonar', '__inverse', '__culdesac']
    def __init__(self):
        """ Constructor de la clase """
        
        self.__previous = 'right'
        self.__sonar = {}
        self.__inverse = {'left' : 'right', 'right' : 'left', 'up' : 'down', 'down' : 'up'}
        self.__culdesac = False
        
    def getPrevious(self):
        """ Retorna l'ultim moviment fet """
        return self.__previous
    
    def setSonar(self, sonar):
        """ Inserta els valors del sonar """
        self.__sonar = dict(sonar) # Fa una copia del diccionari, no una referÃ¨ncia.

    def isCrossRoad(self):
        """ Retorna si els robot esta en una cruïla"""
        return sum(self.__sonar.values()) > 2
    
    def getCulDeSac(self):
        """ Retorna si hem estat en un cul de sac"""
        return self.__culdesac
    
    def setCulDeSac(self, culdesac):
        """ Modifica la variable __culdesac"""
        self.__culdesac = culdesac
        
    def moveTo(self, action):
        """ Comprova si el robot es pot moure seguint la 'action' """
        try:
            if self.__sonar[action]:
                self.__previous = action
                return action
            else:
                raise Exception
        except Exception:
            print 'Error'
            
    def nextMove(self):
        """ Retorna la direcció que ha de seguir el robot per anar a la següent casella sense tornar enrere """
        aux = dict(self.__sonar)
        aux[self.__inverse[self.__previous]] = False
        if sum(aux.values()) < 1:
            self.setCulDeSac(True)
            self.__previous = self.__inverse[self.__previous]
    
        else:
            for key,value in aux.iteritems():
                if value:
                    self.__previous = key
                    break

        return self.__previous
