class arbol(object):
    def __init__(self, n):
        self.val = n
        self.der = None
        self.izq = None

def ordenarAsc(numero):
    if not numero:
        return None
    valor = len(numero)//2
    nodo = arbol(numero[valor])
    nodo.izq = ordenarAsc(numero[:valor])
    nodo.der = ordenarAsc(numero[valor+1:])
    return nodo

def orden(nodo):
    if not nodo:
        return
    print(nodo.val)
    orden(nodo.izq)
    orden(nodo.der)

resultado = ordenarAsc([1,2,3,4,5,6,7,])
orden(resultado)