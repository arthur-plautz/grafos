import math
import string

class Grafo:
    def __init__(self, arquivo=None, vertices:dict=None, arestas:list=None, arcos:list=None):
        self.vertices = vertices 
        self.arestas = arestas 
        self.arcos = arcos 
        self.arquivo = arquivo
        if arquivo:
            self.ler(arquivo)

    def ler(self, arquivo):
        vertices = {}
        arestas = []
        arcos = []

        with open(arquivo, "r") as conteudo:
            t = None
            n = 1
            for linha in conteudo.readlines():
                linha = linha.replace('\n', '')

                if linha.startswith('*edges'):
                    t = 'arestas'
                    continue
                if linha.startswith('*arcs'):
                    t = 'arcos'
                    continue
                elif linha.startswith('*vertices'):
                    t = 'vertices'
                    continue
                
                l = linha.split(' ')
                if t == 'arestas':
                    l[2] = int(l[2])
                    arestas.append(l)
                    l_ = [l[1], l[0], l[2]]
                    arestas.append(l_)
                elif t == 'arcos':
                    l[2] = int(l[2])
                    arcos.append(l)
                elif t == 'vertices':
                    rotulo = l[1]
                    vertice = l[0]
                    vertices[vertice] = rotulo
            
        self.vertices = vertices
        self.arestas = arestas
        self.arcos = arcos

    def vertice(self, i):
        k = list(self.vertice.keys())
        return k[i]
    
    def rotulo(self, v):
        return self.vertices.get(v)

    def grau(self, v):
        v = str(v)

        grau = 0
        for aresta in self.arestas:
            if aresta[0] == v or aresta[1] == v:
                grau += 1
        return grau

    def qtd_vertices(self):
        return len(self.vertices.keys())
    
    def qtd_arestas(self):
        return len(self.arestas)

    def vizinhos(self, v):
        v = str(v)

        vizinhos = []
        conexoes = self.arestas if self.arestas else self.arcos

        for x in conexoes:
            if v in x:
                if (x[0] != v) and (x[0] not in vizinhos):
                    vizinho = x[0]
                    vizinhos.append(vizinho)
                # elif (x[1] != v) and (x[1] not in vizinhos):
                #     vizinho = x[1]
                #     vizinhos.append(vizinho)

        return vizinhos

    def ha_aresta(self, u, v):
        u, v = str(u), str(v)

        for aresta in self.arestas:
            if u in aresta:
                if v in aresta:
                    return aresta

    def ha_arco(self, u, v):
        u, v = str(u), str(v)

        for arco in self.arcos:
            if arco[0] == u and arco[1] == v:
                return arco

    def peso(self, u, v):
        u, v = str(u), str(v)

        for aresta in self.arestas:
            if u in aresta:
                if v in aresta:
                    return aresta[2]

        return math.inf

if __name__ == '__main__':
    g = Grafo('entrada_a1.txt')
    print(g.grau(2))