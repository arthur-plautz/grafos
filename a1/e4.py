from a1.e2 import Grafo2
import math

class Grafo4(Grafo2):
    def relaxamento(self, u, v, peso, d, a):
        if v in self.vizinhos(u) and d[v] > float(d[u]) + float(peso):
            d[v] = float(d[u]) + float(peso)
            a[v] = u

    def imprimir_distancias(self, d, a, s):
        for vertice in self.vertices.keys():
            caminho = []
            i = vertice
            while i != s:
                u = a[i]
                caminho.append(i)
                i = u
            
            caminho.append(s)
            caminho.reverse()

            print(f"{vertice}: {','.join(caminho)}; d={int(d[vertice])}")

    def dijkstra(self, s):
        pass

    def bellman_ford(self, s):
        d, a = {}, {}
        for vertice in self.vertices:
            d[vertice] = math.inf
            a[vertice] = None
        
        d[s] = 0

        for i in range(1, self.qtd_vertices()-1):
            for aresta in self.arestas:
                u, v, peso = aresta
                self.relaxamento(u, v, peso, d, a)

        for aresta in self.arestas:
            u, v, peso = aresta
            if d[v] > float(d[u]) + float(peso):
                return (False, None, None)

        self.imprimir_distancias(d, a, s)
        return (True, d, a)

if __name__ == '__main__':
    g = Grafo4('entrada_a1.txt')
    g.bellman_ford('1')