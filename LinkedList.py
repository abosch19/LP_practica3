class LinkedList(object):
    class Node(object):
        def __init__(self, data, next = None):
            self.data = data
            self.next = next
        def getData(self):
            return self.data
        def getNext(self):
            return self.next
        def setData(self, data):
            self.data = data
        def setNext(self, next):
            self.next = next
        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def getHead(self):
        if self.head == None:
            raise IndexError
        else:
            return self.head.getData()
    def getTail(self):
        if self.tail == None:
            raise IndexError
        else:
            return self.tail.getData()
    def getCurrent(self):
        if self.current == None:
            raise IndexError
        else:
            return self.current.getData()
    def moveNext(self):
        if self.head == None:
            raise IndexError
        elif self.current.getNext() == None:
            raise IndexError
        else:
            aux = self.current.getNext()
            self.current = aux
    def moveHead(self):
        if self.head == None:
            raise IndexError
        else:
            self.current = self.head
    def isEmpty(self):
        return self.size == 0
    def getSize(self):
        return self.size
    def clear(self):
        self.size = 0
        self.current = None
        self.tail = None
        self.head = None
    def insertBefore(self, data):
        if self.head == None:
            aux = self.Node(data)
            self.head = aux
            self.tail = aux
        elif self.current == self.head:
            aux = self.Node(data,self.head)
            self.head = aux
        else:
            iterador = self.head
            for i in range(self.size):
                if iterador.getNext() == self.current:
                    aux = self.Node(data,self.current)
                    iterador.setNext(aux)
                    break
                else:
                    iterador = iterador.getNext()
        self.current = aux
        self.size += 1       
    def insertAfter(self, data):
        if self.head == None:
            aux = self.Node(data)
            self.head = aux
            self.tail = aux
        elif self.current == self.tail:
            aux = self.Node(data)
            self.tail = aux
            self.current.setNext(aux)
        else:
            aux = self.Node(data,self.current.getNext())
            self.current.setNext(aux)
        self.current = aux  
        self.size += 1
    def remove(self):
        if not self.head == None:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.current = None
            elif self.current == self.head:
                self.head = self.current.getNext()
                self.current.setNext(None)
                self.current  = self.head
            elif self.current == self.tail:
                iterador = self.head
                while iterador.getNext() != self.tail:
                    iterador = iterador.getNext()
                iterador.setNext(None)
                self.tail = iterador
                self.current = self.tail
            else:
                aux = self.head
                while aux.getNext() != self.current:
                    aux = aux.getNext()
                aux.setNext(self.current.getNext())
                self.current = aux
            self.size -= 1
        else:
            raise IndexError
        
    def __str__(self):
        aux = self.head
        l = ''
        for i in range(self.size):
            l = l + aux.__str__() + ' '
            aux = aux.getNext()
        return l
