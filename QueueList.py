# -*- coding: latin-1 -*-
# LLenar con NIUs de los integrantes del grupo
# NIU_1: 1361507
# NIU_2:

from LinkedList import *


class QueueList(LinkedList):
    """
    QueueList Class
    """
    def __init__(self):
        """
        Agregar comentarios
        :return: Agregar comentarios
        """
        LinkedList.__init__(self)

    def push(self, data):
        """
        Agregar comentarios
        :param data: Agregar comentarios
        :return: Agregar comentarios
        """
        self.current = self.tail
        self.insertAfter(data)
        

    def pop(self):
        """
        Agregar comentarios
        :return: Agregar comentarios
        """
        self.moveHead()
        aux = self.current
        self.remove()

        return aux.getData()
    
    def queueHead(self):
        """
        Agregar comentarios
        :return: Agregar comentarios
        """
        if self.size > 0:
            return self.getHead()
        else:
            raise IndexError

    def purge(self):
        """
        Agregar comentarios
        :return: Agregar comentarios
        """
        self.clear()

    def __len__(self):
        """
        Agregar comentarios
        :return: Agregar comentarios
        """
        return self.getSize()
