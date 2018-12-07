class Vertice:
    def __init__(self, n):
        self.nombre = n;
        self.vecinos = list()

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Grafo:
    vertices = {}

    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    def agregarArista(self, u, v):
        if u in  self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)

            return True
        else:
            return False

    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice" + key +" Sus vecinos son:  " + str(self.vertices[key].vecinos))



        #se crea un objeto "g" de la clase grafo, el grafo
g = Grafo()
        #se crea un objeto "a" de la clase Vertice, un vertice
a = Vertice('A')
        #se agrega el vertice al grafo
g.agregarVertice(a)

        #esta estructura de repeticon es para agregar
        #todos los vertices, y no hacerlo uno a uno
for i in range(ord('A'),ord('H')):
    g.agregarVertice(Vertice(chr(i)))

        #se declara una lista que contiene las aristas del grafo
    edges = ['AC','AB', 'BF', 'CD', 'DE', 'DH', 'EH', 'FG']

        #Se agregan las aristas del grafo
for edge in edges:
    g.agregarArista(edge[:1], edge[1:])
        #se imprime el grafo, como lista de adyacencia
    g.imprimeGrafo()

