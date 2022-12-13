from a3.e1 import Grafo1

class Grafo2(Grafo1):
    def bfs(self, mate, d):
        q = []
        for x in self.X:
            if not mate[x]:
                d[x] = 0
                q.append(x)
            else:
                d[x] = 1e10
        
        d['null'] = 1e10

        while len(q) > 0:
            x = q.pop(0)
            if d[x] < d['null']:
                for y in self.busca_vizinhos(x):
                    m_y = mate[y]
                    if d[m_y] == 1e10:
                        d[m_y] = d[x] + 1
                        q.append(m_y)
        return d['null'] != 1e10
                    

    def dfs(self, mate, x, d):
        if x:
            for y in self.busca_vizinhos(x):
                m_y = mate[y]
                if d[m_y] == d[x] + 1:
                    if self.dfs(mate, m_y, d):
                        mate[y] = x
                        mate[x] = y
                        return True
            
            d[x] = 1e10
            return False
        return True

    def hopcroft_karp(self):
        m = 0
        
        d, mate = {}, {}
        for v in self.vertices.keys():
            d[v] = 1e10
            mate[v] = None

        while self.bfs(mate, d):
            for x in self.X:
                if not mate[x]:
                    if self.dfs(mate, x, d):
                        m += 1
        return m, mate
