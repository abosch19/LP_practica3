# -*- coding: latin-1 -*-

import py_compile
import os
import sys

sum_grades = 0

def comprova_valor_node(QueueList, node, valor):
    naux = QueueList.Node(valor)
    return node is None or type(node) != type(naux) or node.getData() != valor

class MissatgeError(Exception):
    def __init__(self, missatge):
        self._missatge = missatge

def cadena_ordinal(n):
    if n == 0:
        return '1er'
    elif n == 1:
        return '2do'
    elif n == 3:
        return '3ro'
    else:
        return '%drd' % (n + 1)


def comprova_valors_cua(QueueList, cua, valors):
    N = len(valors)
    if len(cua) != N:
        raise MissatgeError, "El método '__len__' no retorna el número correcto de elementos de la cola (retorna '%s' pero deberia  retornar '%d'). Posible error en los métodos '__len__' o 'push'." % (str(len(cua)), N)
    if cua.size != N:
        raise MissatgeError, "La variable 'size' no se actualiza correctamente al hacer un 'push' (deberia de ser '%d' pero es '%s')." % (N, str(cua.size))
    aux = cua.head
    for idx in range(len(valors)):
        if comprova_valor_node(QueueList, aux, valors[idx]):
            raise MissatgeError, "El %s elemento de la cola deberia ser %d pero el nodo tiene otro valor " % (cadena_ordinal(idx), valors[idx])
        aux = aux.getNext()
        if idx < N - 1 and aux == None:
            raise MissatgeError, "Se esperaban más nodos, pero la variable 'next' del nodo apunta a None. La cola termina en el %s elemento" % (cadena_ordinal(idx))
    if aux != None:
        raise MissatgeError, "El último elemento deberia apuntar a None"


"""
--------------------------------------------------------------------------------
Print functions
--------------------------------------------------------------------------------
"""


def comment(s):
    """Formats strings to create VPL comments"""
    print('Comentario :=>> ' + s)


def grade(num):
    """formats a number to create a VPL grade"""
    global sum_grades
    sum_grades = sum_grades + num

def print_grade():
    """formats a number to create a VPL grade"""
    global sum_grades
    print('Puntaje :=>> ' + str(sum_grades) + '/100')


"""
--------------------------------------------------------------------------------
Check if file exists
--------------------------------------------------------------------------------
"""

filename = 'QueueList.py'
if os.path.isfile(filename) and os.access(filename, os.R_OK):
    comment("OK -> El archivo existe")
else:
    comment("FAIL -> El archivo "+filename+ " no esta en esta carpeta o "
            "no tiene permisos de lectura")
    print_grade()
    exit()

"""
--------------------------------------------------------------------------------
Check sintax
--------------------------------------------------------------------------------
"""

try:
    py_compile.compile(filename, doraise=True)
    comment('OK -> Importar '+ filename)
except py_compile.PyCompileError as e:
    comment("FAIL -> Importar "+filename+ "\n " + str(e))
    print_grade()
    exit()

"""
--------------------------------------------------------------------------------
Import QueueList
--------------------------------------------------------------------------------
"""
try:
    from QueueList import QueueList
    comment('OK -> from QueueList import QueueList')
except ImportError as e:
    comment("FAIL -> from QueueList import QueueList\n" + str(e))
    print_grade()
    exit()


"""
--------------------------------------------------------------------------------
Set grades
--------------------------------------------------------------------------------
"""
points = dict(ql_vacia_constructor=5,
              ql_vacia_pop=10,
              ql_vacia_queuehead=10,
              ql_vacia_len=5,
              ql_vacia_purge=5,
              ql_1e_push=10,
              ql_1e_queuehead=10,
              ql_1e_purge=5,
              ql_1e_pop=10,
              ql_me_test1=10,
              ql_me_test2=10,
              ql_me_purge=10)


"""
--------------------------------------------------------------------------------
Check QueueList
--------------------------------------------------------------------------------
"""

# Check empty QueueList - Constructor

test_name = 'QueueList vacia: Constructor'
try:
    q = QueueList()
    if q.head is not None or q.current is not  None or q.tail is not None or q.size != 0:
        comment("FAIL -> " + test_name +"\n El constructor de QueueList no inicializa las variables correctamente")
        grade(0)
    else:
        comment("OK -> " + test_name)
        grade(points['ql_vacia_constructor'])
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)

# Check empty QueueList - pop()

test_name = 'QueueList vacia: pop()'
try:
    q = QueueList()
    try:
        q.pop()
        comment("FAIL -> " + test_name + "\n pop() debe lanzar una excepcion de tipo IndexError cuando la lista esta vacia")
        grade(0)
    except IndexError:
        comment("OK -> " + test_name)
        grade(points['ql_vacia_pop'])
    except:
        e = sys.exc_info()[1]
        comment("FAIL -> " + test_name + "\n" + str(e))
        grade(0)
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)

# Check empty QueueList - queueHead()

test_name = 'QueueList vacia: queueHead()'
try:
    q = QueueList()
    try:
        q.queueHead()
        comment("FAIL -> " + test_name + "\n queueHead() debe lanzar una excepcion de tipo IndexError cuando la lista esta vacia")
        grade(0)
    except IndexError:
        comment("OK -> " + test_name)
        grade(points['ql_vacia_queuehead'])
    except:
        e = sys.exc_info()[1]
        comment("FAIL -> " + test_name + "\n" + str(e))
        grade(0)
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)


# Check empty QueueList - len

test_name = 'QueueList vacia: len()'
try:
    q = QueueList()
    if len(q) != 0:
        comment("FAIL -> " + test_name + "\n __len__() debe retornar un 0 cuando la lista esta vacia")
        grade(0)
    else:
        comment("OK -> " + test_name)
        grade(points['ql_vacia_len'])
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)

# Check empty QueueList - purge

test_name = 'QueueList vacia: purge()'
try:
    q = QueueList()
    q.purge()
    if q.current is not None or q.size != 0:
        comment("FAIL -> " + test_name + " \n purge() no elimina correctamente la lista")
        grade(0)
    else:
        comment("OK -> " + test_name)
        grade(points['ql_vacia_purge'])
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)

# Check one element QueueList - push

test_name = 'QueueList con un elemento: push()'
try:
    q = QueueList()
    q.push(1)
    try:
        comprova_valors_cua(QueueList, q, [1])
        if q.head != q.current or  q.head != q.tail or  q.head.getData() != 1:
            comment("FAIL -> " + test_name + " \n push() no inserta correctamente valores en la lista")
            grade(0)
        else:
            comment("OK -> " + test_name)
            grade(points['ql_1e_push'])
    except MissatgeError, (e):
        comment("FAIL -> " + test_name + "\n" + e._missatge)
        grade(0)
    except:
        e = sys.exc_info()[1]
        comment("FAIL -> " + test_name + "\n" + str(e))
        grade(0)
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)

# Check one element QueueList - queueHead

test_name = 'QueueList con un elemento: queueHead()'
try:
    q = QueueList()
    q.push(1)
    if q.queueHead() != 1:
        comment("FAIL -> " + test_name + " \n queueHead() no retorna correctamente el valor de un unico elemento en la lista")
        grade(0)
    else:
        comment("OK -> " + test_name)
        grade(points['ql_1e_queuehead'])
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)


# Check one element QueueList - purge

test_name = 'QueueList con un elemento: purge()'
try:
    q = QueueList()
    q.push(1)
    q.purge()
    if q.current is not None or q.size != 0:
        comment("FAIL -> " + test_name + " \n purge() no elimina correctamente la lista")
        grade(0)
    else:
        comment("OK -> " + test_name)
        grade(points['ql_1e_purge'])
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)


# Check one element QueueList - pop

test_name = 'QueueList con un elemento: pop()'
try:
    q = QueueList()
    q.push(1)
    if q.pop() != 1:
        comment("FAIL -> " + test_name + " \n pop() no retorna correctamente el valor del elemento en la cola")
        grade(0)
    else:
        if q.current is not None or q.size != 0:
            comment("FAIL -> " + test_name + " \n pop() no actualiza correctamente la lista")
            grade(0)
        else:
            try:
                q.pop()
                comment("FAIL -> " + test_name + " \n pop debe lanzar una excepcion de tipo IndexError cuando la lista esta vacia")
                grade(0)
            except IndexError:
                comment("OK -> " + test_name)
                grade(points['ql_1e_pop'])
            except:
                e = sys.exc_info()[1]
                comment("FAIL -> " + test_name + "\n" + str(e))
                grade(0)
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)


# Check multiples elements QueueList - Prueba #1

test_name = 'QueueList con multiples elementos: Prueba #1'

try:
    pass_test = True
    elements = [20, 17, 7, 19, 23, 17, 5, 8, 9]
    q = QueueList()
    expected_result = []
    for idx in range(len(elements) / 2):
        q.push(elements[idx])
        expected_result.append(elements[idx])
        comprova_valors_cua(QueueList, q, expected_result)
        if q.queueHead() != expected_result[0]:
            comment("FAIL -> " + test_name + " \n El método queueHead() no retorna el valor esperado luego de hacer un push")
            pass_test = False
            grade(0)
    while len(expected_result) > 0:
        if expected_result[0] != q.pop():
            comment("FAIL -> " + test_name + " \n El método pop() no retorna el valor esperado")
            pass_test = False
            grade(0)
        expected_result.pop(0)
        comprova_valors_cua(QueueList, q, expected_result)
        if len(expected_result) > 0:
            if q.queueHead() != expected_result[0]:
                comment("FAIL -> " + test_name + " \n El método queueHead() no retorna el valor esperado luego de hacer un pop")
                pass_test = False
                grade(0)
        else:
            if q.current is not None or q.size != 0:
                comment("FAIL -> " + test_name + " \n Los elementos no fueron eliminados correctamente de la lista")
                pass_test = False
                grade(0)

    if pass_test:
        comment("OK -> " + test_name)
        grade(points['ql_me_test1'])
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)


# Check multiples elements QueueList - Prueba #2

test_name = 'QueueList con multiples elementos: Prueba #2'

try:
    pass_test = True
    elements = [20, 17, 7, 19, 23, 17, 5, 8, 9]
    for idx in range(len(elements) / 2): # AFEGIR LA MEITAT
        q.push(elements[idx])
        expected_result.append(elements[idx])
        comprova_valors_cua(QueueList, q, expected_result)
        if q.queueHead() != expected_result[0]:
            comment("FAIL -> " + test_name + " \n El método queueHead() no retorna el valor esperado luego de hacer un push")
            pass_test = False
            grade(0)
    for idx in range(len(elements) / 3): # TREURE'N UN TERÇ
        if expected_result[0] != q.pop():
            comment("FAIL -> " + test_name + " \n El método pop() no retorna el valor esperado")
            pass_test = False
            grade(0)
        expected_result.pop(0)
        comprova_valors_cua(QueueList, q, expected_result)
        if q.queueHead() != expected_result[0]:
            comment("FAIL -> " + test_name + " \n El método queueHead() no retorna el valor esperado luego de hacer un pop")
            pass_test = False
            grade(0)
    for idx in range(len(elements) / 2, len(elements)): # AFEGIR LA RESTA
        q.push(elements[idx])
        expected_result.append(elements[idx])
        comprova_valors_cua(QueueList, q, expected_result)
        if q.queueHead() != expected_result[0]:
            comment("FAIL -> " + test_name + " \n El método queueHead() no retorna el valor esperado luego de hacer un push")
            pass_test = False
            grade(0)
    while len(expected_result) > 0: # BUIDAR LA CUA FENT POPS
        if expected_result[0] != q.pop():
            comment("FAIL -> " + test_name + " \n El método pop() no retorna el valor esperado")
            pass_test = False
            grade(0)
        expected_result.pop(0)
        comprova_valors_cua(QueueList, q, expected_result)
        if len(expected_result) > 0:
            if q.queueHead() != expected_result[0]:
                comment("FAIL -> " + test_name + " \n El método queueHead() no retorna el valor esperado luego de hacer un pop")
                pass_test = False
                grade(0)
        else:
            if q.current is not  None or q.size != 0:
                comment("FAIL -> " + test_name + " \n Los elementos no fueron eliminados correctamente de la lista")
                pass_test = False
                grade(0)

    if pass_test:
        comment("OK -> " + test_name)
        grade(points['ql_me_test2'])
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)

# Check multiples elements QueueList - Prueba #2

test_name = 'QueueList con multiples elementos: purge()'

try:
    elements = [20, 17, 7, 19, 23, 17, 5, 8, 9]
    expected_result = []
    pass_test = True
    for idx in range(len(elements) / 2): # AFEGIR LA MEITAT
        q.push(elements[idx])
        expected_result.append(elements[idx])
        comprova_valors_cua(QueueList, q, expected_result)
        if q.queueHead() != expected_result[0]:
            comment("FAIL -> " + test_name + " \n El método queueHead() no retorna el valor esperado luego de hacer un push")
            pass_test = False
            grade(0)
    q.purge()
    if q.current is not None or q.size != 0:
        comment("FAIL -> " + test_name + " \n Los elementos no fueron eliminados correctamente de la lista")
        pass_test = False
        grade(0)
    q.purge()
    if q.current is not None or q.size != 0:
        comment("FAIL -> " + test_name + " \n Los elementos no fueron eliminados correctamente de la lista")
        pass_test = False
        grade(0)
    if pass_test:
        comment("OK -> " + test_name)
        grade(points['ql_me_purge'])
except:
    e = sys.exc_info()[1]
    comment("FAIL -> " + test_name + "\n" + str(e))
    grade(0)

"""
--------------------------------------------------------------------------------
Print grades
--------------------------------------------------------------------------------
"""
print_grade()
print "El puntaje final puede cambiar. Esto dependera de una revision del codigo por parte de los profesores del curso."
