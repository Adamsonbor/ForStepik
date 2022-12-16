from math import inf

class Vertex:
    """_links - список связей с другими вершинами графа (список объектов класса Link)."""
    i = 0

    def __init__(self):
        self._id = self.i + 1
        self._links = set()
        self.__class__.i += 1

    @property
    def links(self):
        return self._links

    def __repr__(self):
        return str(self._id)



class Link:
    """_v1, _v2 - ссылки на объекты класса Vertex, которые соединяются данной связью;
       _dist - длина связи (по умолчанию 1); это может быть длина пути, время в пути и др."""

    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist
        v1._links.add(self)
        v2._links.add(self)

    def _is_vertex(self, value):
        if type(value) != Vertex:
            raise ValueError

    def __eq__(self, other):
        return (other.v1, other.v2) == (self.v1, self.v2) or (other.v1, other.v2) == (self.v2, self.v1)

    def __hash__(self):
        return hash((self.v1, self.v2))

    @property
    def v1(self):
        return self._v1

    @v1.setter
    def v1(self, value):
        self._is_vertex(value)
        self._v1 = value

    @property
    def v2(self):
        return self._v2

    @v2.setter
    def v2(self, value):
        self._is_vertex(value)
        self._v2 = value

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._is_vertex(value)
        self._dist = value

    def __repr__(self):
        return f"{self.v1} <-{self.dist}-> {self.v2}"


class LinkedGraph:
    """_links - список из всех связей графа (из объектов класса Link);
       _vertex - список из всех вершин графа (из объектов класса Vertex)."""

    def __init__(self):
        self._links = []
        self._vertex = []

    def _is_vertex(self, value):
        if type(value) != Vertex:
            raise ValueError

    def add_vertex(self, vertex):
        self._is_vertex(vertex)
        if vertex not in self._vertex:
            self._vertex.append(vertex)

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)
            if link.v1 not in self._vertex:
                self._vertex.append(link.v1)
            if link.v2 not in self._vertex:
                self._vertex.append(link.v2)

    def find_path(self, start_v, end_v):
        W = {v:inf for v in self._vertex}
        v = start_v
        S = {v}
        W[v] = 0
        L = {}
        while len(self._vertex) > len(S):
            for link in v.links:
                new_v = link.v2 if link.v2 != v else link.v1
                if new_v not in S:
                    w = W[v] + link.dist
                    if w < W[new_v]:
                        W[new_v] = w
                        L[new_v] = link
            m = inf
            for k, i in W.items():
                if i < m and k not in S:
                    v = k
                    m = i
            S.add(v)
        lout = []
        pout = [end_v]
        l = end_v
        while l != start_v:
            link = L[l]
            l = link.v1 if link.v1 != l else link.v2
            lout.append(link)
            pout.append(l)

        return pout[::-1], lout[::-1]
                    


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    pass


     
map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")
print(Link(v1, v2) == Link(v2, v1))

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))
# print(map_metro._links)

# print(len(map_metro._links))
# print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path)
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7

