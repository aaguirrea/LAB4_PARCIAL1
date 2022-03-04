class Arbol(object):
    def __init__(self, x):
        self.val = x
        self.der = None
        self.izq = None

def Bts(raiz):
    apilar = []
    prev = None

    while raiz or apilar:
        while raiz:
            apilar.append(raiz)
            raiz = raiz.izq
        raiz = apilar.pop()
        if prev and raiz.val <= prev.val:
            return False
        prev = raiz
        raiz = raiz.der
    return True

raiz = Arbol(2)
raiz.izq = Arbol(1)
raiz.der = Arbol(3)

resultado = Bts(raiz)
print(resultado)

raiz = Arbol(1)
raiz.izq = Arbol(2)
raiz.der = Arbol(3)

resultado = Bts(raiz)
print(resultado)
