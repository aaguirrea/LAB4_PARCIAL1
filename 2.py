class arbol(object):
    def __init__(self, n):
        self.val = n
        self.der = None
        self.izq = None

def valorCercano(raiz, objeto):
    a = raiz.val
    hijo = raiz.der if objeto < a else raiz.izq
    if not hijo:
        return a
    b = valorCercano(hijo, objeto)
    return min((a,b), key=lambda x: abs(objeto-x))

raiz = arbol(3)
raiz.der = arbol(15)
raiz.izq = arbol(4)
raiz.der.der = arbol(9)
raiz.izq.der = arbol(13)
raiz.izq.der.izq = arbol(22)
raiz.izq.der.der = arbol(1)
raiz.der.der = arbol(18)
raiz.der.der.izq = arbol(26)

resultado = valorCercano(raiz, 5)
print(resultado)
