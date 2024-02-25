class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None
    
class Arbol:
    def __init__(self):
        self.raiz = None
    
    def vacio(self):
        return self.raiz is None
    
    def buscarNodo(self, nombre):
        return self._buscarNodo(nombre, self.raiz)
    
    def _buscarNodo(self, nombre, nodo_actual):
        if nodo_actual is None or nodo_actual.nombre == nombre:
            return nodo_actual
        elif nombre < nodo_actual.nombre:
            return self._buscarNodo(nombre, nodo_actual.izquierda)
        else:
            return self._buscarNodo(nombre, nodo_actual.derecha)
    
    def insertar(self, nombre):
        nuevo_nodo = Nodo(nombre)
        if self.vacio():
            self.raiz = nuevo_nodo
        else:
            self._insertar(nuevo_nodo, self.raiz)
    
    def _insertar(self, nuevo_nodo, nodo_actual):
        if nuevo_nodo.nombre < nodo_actual.nombre:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nuevo_nodo
            else:
                self._insertar(nuevo_nodo, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nuevo_nodo
            else:
                self._insertar(nuevo_nodo, nodo_actual.derecha)
    
    def imprimirArbol(self):
        self._imprimirArbol(self.raiz)
    
    def _imprimirArbol(self, nodo_actual):
        if nodo_actual is not None:
            self._imprimirArbol(nodo_actual.izquierda)
            print(nodo_actual.nombre)
            self._imprimirArbol(nodo_actual.derecha)
