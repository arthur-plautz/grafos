import math
from a1.e4 import Grafo4

class Grafo5(Grafo4):
    def funcao_w(self):
        m = []
        for u in self.vertices.keys():
            l = []
            for v in self.vertices.keys():
                aresta = self.ha_aresta(u, v)
                if u == v:
                    a = 0
                elif u != v and aresta:
                    a = float(aresta[2])
                else:
                    a = math.inf
                l.append(a)
            m.append(l)
        return m

    def floyd_warshwall(self):
        n = self.qtd_vertices()
        d = [self.funcao_w()]

        for k in range(1, n):
            m = d[0]
            d.append(m)
            for u in range(n):
                for v in range(n):
                    d[k][u][v] = min(d[k-1][u][v], d[k-1][u][k-1] + d[k-1][k-1][v])

        m = d[n-1]
        for i in range(n):
            l = [str(int(c)) for c in m[i]]
            print(f"{i+1}: {','.join(l)}")

        return d[n-1]

g = Grafo5('entrada_a1.txt')
g.floyd_warshwall()