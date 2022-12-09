from a1.e1 import Grafo

class Grafo2(Grafo):
    def __niveis_busca_em_largura(self, d):
        niveis = {}
        for k, v in d.items():
            if v in niveis:
                niveis[v].append(k)
            else:
                niveis[v] = [k]
        
        imprime_nivel = lambda n, v: print(f"{n}: {','.join(v)}")
        for k, v in niveis.items():
            imprime_nivel(k, v)

    def busca_em_largura(self, s, imprimir_niveis=True):
        c, d, a = {}, {}, {}

        d[s] = 0
        c[s] = True

        fila = []
        fila.append(s)

        while len(fila) > 0:
            u = fila.pop()

            for v in self.busca_vizinhos(u):
                if v not in c:
                    c[v] = True
                    d[v] = d[u] + 1
                    a[v] = u
                    fila.append(v)
        
        if imprimir_niveis:
            self.__niveis_busca_em_largura(d)

        return d, a

    def busca_em_profundidade(self, s):
        c, t, a = {}, {}, {}
        c[s] = True

        tempo = 0
        pilha = []
        pilha.append(s)

        while len(pilha) > 0:
            tempo += 1
            u = pilha.pop(0)
            t[u] = tempo

            for v in self.busca_vizinhos(u):
                if v not in c:
                    c[v] = True
                    a[v] = u
                    pilha.append(v)

        return c, t, a

    def busca_vizinhos(self, v):
        vizinhos = []
        conexoes = self.arestas if self.arestas else self.arcos

        for x in conexoes:
            if v == x[0]:
                vizinhos.append(x[1])
            elif self.arestas and v == x[1]:
                vizinhos.append(x[0])
        return vizinhos

if __name__ == '__main__':
    g = Grafo2('entrada_a1.txt')
    g.busca_em_largura('1')
    print(g.busca_em_profundidade('1'))