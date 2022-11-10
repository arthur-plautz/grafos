from a1.e2 import Grafo2
import math

class Grafo1(Grafo2):
    def busca_edmonds_karp(self, s, t):
        c, a = {}, {}
        for v in self.vertices.keys():
            c[v] = False
            a[v] = None
        
        c[s] = True

        q = []
        q.append(s)

        while len(q) > 0:
            u = q.pop(0)
            for v in self.busca_vizinhos(u):
                arco = self.ha_arco(u, v)
                capacidade = int(arco[2]) if arco else 0
                if not c[v] and capacidade > 0:
                    c[v] = True
                    a[v] = u
                    if v == t:
                        p = [t]
                        w = t
                        while w != s:
                            w = a[w]
                            p = [w] + p
                        return p
                    q.append(v)

    def edmonds_karp(self, s, t):
        f = [(arco[0], arco[1], 0) for arco in self.arcos]

        pass

if __name__ == "__main__":
    g = Grafo1('entrada_a3.txt')
    print(g.busca_edmonds_karp('1','4'))
