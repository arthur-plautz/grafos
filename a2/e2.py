from a2.e1 import Grafo1
import math

class Grafo2(Grafo1):
    def dfs_ot(self, v, c, t, f, tempo, o):
        c[v] = True
        tempo += 1
        t[v] = tempo

        for u in self.busca_vizinhos(v):
            if not c[u]:
                self.dfs_ot(u, c, t, f, tempo, o)
        
        tempo += 1
        f[v] = tempo
        o.append(v)
        return tempo

    def ordenacao_topologica(self):
        c, t, f, a = {}, {}, {}, {}
        for v in self.vertices.keys():
            c[v] = False
            t[v] = math.inf
            f[v] = math.inf
            a[v] = None
        
        tempo = 0
        o = []

        for v in self.vertices.keys():
            if not c[v]:
                tempo = self.dfs_ot(v, c, t, f, tempo, o)
        
        return o

g = Grafo2('entrada_a2.txt')
print(g.ordenacao_topologica())