from a1.e2 import Grafo2
from copy import deepcopy

class Grafo1(Grafo2):
    def __obter_arcos(self, vertices):
        arcos = []
        for i in range(len(vertices)-1):
            u = vertices[i]
            v = vertices[i+1]
            arco = self.ha_arco(u, v)
            arcos.append(arco)
        return arcos

    def menor_capacidade(self, arcos):
        m = 1e10
        for a in arcos:
            m = min(a[2], m)
        return m
    
    def atualizar_capacidade(self, arcos):
        m = self.menor_capacidade(arcos)
        for a in arcos:
            i = self.arcos.index(a)
            self.arcos[i][2] -= m
        return m

    def edmonds_karp(self, s, t):
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

    def fluxo_maximo(self, s, t):
        _arcos = deepcopy(self.arcos)
        
        f_max = 0
        p = True

        while p:
            p = self.edmonds_karp(s, t)
            if p:
                c = self.__obter_arcos(p)
                f = self.atualizar_capacidade(c)
                f_max += f
        
        self.arcos = _arcos
        print(f"Fluxo máximo: {f_max}")
        return f_max

if __name__ == "__main__":
    g = Grafo1('entrada_a3.txt')
    g.fluxo_maximo('1','6')
