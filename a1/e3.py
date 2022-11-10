from a1.e2 import Grafo2

class Grafo3(Grafo2):
    def subciclo_euleriano(self, v, c):
        ciclo = [v]
        t = v

        fim = False
        while not fim:
            aresta = None
            vizinhos = self.busca_vizinhos(v)

            for vizinho in vizinhos:
                pass

            if not aresta:
                return (False, None)
            else:
                c[aresta] = True
                u = aresta.replace(v, '')
                v = u
                ciclo += [v]

            fim = (v == t)

        vertices_faltantes = list(set(self.vertices.keys()) - set(ciclo))

        for x in vertices_faltantes:
            r, ciclo_ = self.subciclo_euleriano(x, c)
            print(r)
            if not r:
                return (False, None)
            else:
                i = ciclo.index(x)
                ciclo_a = ciclo[:i]
                ciclo_b = ciclo[i:]
                print(ciclo_a, ciclo_b)
        return (True, ciclo)

    def ciclo_euleriano(self):
        v = list(self.vertices.keys())[0]
        c = [(set(aresta[0], aresta[1]), False) for aresta in self.arestas]

        r, ciclo = self.subciclo_euleriano(v, c)

        if not r:
            print(0)
        else:
            print(1)
            print(ciclo)

        return (r, ciclo)

if __name__ == '__main__':
    g = Grafo3('entrada_a1.txt')
    g.ciclo_euleriano()