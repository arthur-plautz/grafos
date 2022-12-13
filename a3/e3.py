from a3.e2 import Grafo2
from itertools import chain, combinations

class Grafo3(Grafo2):
    @property
    def potencia(self):
        v = self.vertices.keys()
        return list(chain.from_iterable(combinations(v, r) for r in range(len(v)+1)))

    def lawler(self):
        self.arestas = self.arcos
        self.arcos = None

        x = [None] * len(self.potencia)
        x[0] = 0

        for s_ in range(1,len(self.potencia)):
            s = self.potencia[s_]
            x[s_] = 1e10

            vertices = dict.fromkeys(s)
            for v in s:
                vertices[v] = self.vertices.get(v)

            arestas = []
            for a in self.arestas:
                u, v = a[:2]
                if u in s or v in s:
                    arestas.append(a)
            
            g_ = Grafo3(vertices=vertices, arestas=arestas)
            # ... Almost


if __name__ == "__main__":
    g = Grafo3('entrada_a3.txt')
    g.lawler()
