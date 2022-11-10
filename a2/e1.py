from a1.e2 import Grafo2
import math

class Grafo1(Grafo2):
    def dfs_visit(self, v, c, t, a, f, tempo):
        c[v] = True
        tempo += 1
        t[v] = tempo
        for u in self.busca_vizinhos(v):
            if not c[u]:
                a[u] = v
                tempo = self.dfs_visit(u, c, t, a, f, tempo)

        tempo += 1
        f[v] = tempo
        return tempo

    def dfs(self, reverse=False):
        c, t, f, a = {}, {}, {}, {}
        for v in self.vertices.keys():
            c[v] = False
            t[v] = math.inf
            f[v] = math.inf
            a[v] = None
        
        tempo = 0

        vertices = list(self.vertices.keys())
        if reverse: vertices.reverse()


        for v in vertices:
            if not c[v]:
                tempo = self.dfs_visit(v, c, t, a, f, tempo)

        return (c, t, a, f)

    def conectividade(self):
        c, t, a_, f = self.dfs()

        a_t = []
        arcos = self.arcos.copy()

        for arco in self.arcos:
            arco_invertido = (arco[1], arco[0])
            a_t.append(arco_invertido)

        self.arcos = a_t
        c_t, t_t, a_t_, f_t = self.dfs(reverse=True)
        self.arcos = arcos

        return a_t_

g = Grafo1('entrada_a2.txt')
print(g.conectividade())