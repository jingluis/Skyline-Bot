import random


def flatten(l):
    if not l:
        return []
    res = []
    for i in l:
        res.extend(i)
    return res


class Building:
    xmin = 0
    xmax = 0
    height = 0

    def __init__(self, xmin, xmax, alcada):
        assert ((xmin < xmax) and (alcada >= 0))
        self.height = alcada
        self.xmin = xmin
        self.xmax = xmax

    def get_height(self):
        return self.height

    def get_area(self):
        return (self.xmax - self.xmin) * self.height

    def get_xmin(self):
        return self.xmin

    def get_xmax(self):
        return self.xmax

    def move_building(self, n):
        self.xmin += n
        self.xmax += n

    def change_height(self, new_h):
        self.height = new_h

    def print_building(self):
        print("(" +
              str(self.xmin) +
              "," +
              str(self.xmax) +
              "," +
              str(self.height) +
              ")")


def sort_skyline(e):
    return e[0]


class Skyline:
    height = 0
    area = 0
    buildings = []

    def __init__(self, input=None):
        self.buildings = []
        self.height = 0
        self.area = 0
        if input is not None:
            if isinstance(input, list):
                # aleatori
                if isinstance(input[0], int):
                    buildings_list = []
                    # print(str(input[0]))
                    for i in range(0, input[0]):
                        h = random.randint(0, input[1])
                        w = random.randint(1, input[2])
                        start = random.randint(input[3], input[4])
                        end = start + w
                        while end > input[4]:
                            h = random.randint(0, input[1])
                            w = random.randint(1, input[2])
                            start = random.randint(input[3], input[4])
                            end = start + w

                        buildings_list.append([start, end, h])
                    # print(buildings_list)
                    aux_list = self.union(buildings_list)
                    # print(len(aux_list))
                    self.buildings = self.reconstruct(aux_list).get_buildings()
                # llista
                else:
                    aux_list = self.union(input)
                    self.buildings = self.reconstruct(aux_list).get_buildings()

            else:
                # tupla
                self.buildings.append(Building(input[0], input[2], input[1]))
                self.area = 0
                self.height = 0

    '''
    Having the buildings of skylines as strips, we need to reconstruct to buildings
    '''

    def reconstruct(self, aux_list):
        res_list = []
        aux_list = flatten(aux_list)
        i = 0
        while i < len(aux_list) - 3:
            if aux_list[i + 1] != 0:
                res_list.append(Building(
                    aux_list[i], aux_list[i + 2], aux_list[i + 1]))
            i += 2
        return Skyline().assign_buildings(res_list)

    def get_buildings(self):
        return self.buildings

    def union(self, buildings):
        buildings.sort(key=sort_skyline)
        return self.i_union(buildings)

    '''
    Recursively find the union of each half of the list, and then merge it
    '''

    def i_union(self, buildings):
        aux_list = []
        if not buildings:
            return aux_list
        if(len(buildings) == 1):
            l, r, h = buildings[0]
            aux_list = [[l, h], [r, 0]]
            return aux_list
        mid = (len(buildings) + 1) // 2
        left = self.union(buildings[:mid])
        right = self.union(buildings[mid:])
        return self.merge_skylines(left, right)

    '''
    Precondition: needs to have the skyline sorted by xmin
    The idea is similar to merge of merge sort, start from first strips of two skylines,
    compare x coordinates. Pick the strip with smaller x coordinate and add it to result.
    The height of added strip is considered as maximum of current heights from skyline1 and skyline2.
    '''

    def merge_skylines(self, left, right):
        i, j = 0, 0
        h1, h2 = -1, -1
        result = []
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                h1 = left[i][1]
                x = left[i][0]
                i += 1
            elif left[i][0] > right[j][0]:
                h2 = right[j][1]
                x = right[j][0]
                j += 1
            else:
                h1 = left[i][1]
                h2 = right[j][1]
                x = right[j][0]
                i += 1
                j += 1

            new = [x, max(h1, h2)]

            if result == [] or result[-1][1] != new[1]:
                result.append(new)

        while i < len(left):
            if result == [] or result[-1][1] != left[i][1]:
                result.append(left[i][:])
            i += 1
        while j < len(right):
            if result == [] or result[-1][1] != right[j][1]:
                result.append(right[j][:])
            j += 1

        return result

    '''
    If the first building of the first skyline has the smallest xmax,
    it can only intersect xmin of the second skyline.
    After, we can discard the first skyline xmin since it cannot intersect anything else.
    Similary with the other side reasoning
    '''

    def assign_buildings(self, buildings):
        self.buildings = buildings
        return self

    def intersect_skylines(self, skylines):
        skyline_b = skylines.get_buildings()
        result_skyline = []
        i, j = 0, 0
        while i < len(self.buildings) and j < len(skyline_b):
            lo = max(self.buildings[i].get_xmin(), skyline_b[j].get_xmin())
            hi = min(self.buildings[i].get_xmax(), skyline_b[j].get_xmax())
            # print(str(lo) + "  " + str(hi))
            height = min(
                self.buildings[i].get_height(),
                skyline_b[j].get_height())
            if lo < hi:
                result_skyline.append(Building(lo, hi, height))
            if self.buildings[i].get_xmax() < skyline_b[j].get_xmax():
                i += 1
            else:
                j += 1

        return Skyline().assign_buildings(result_skyline)

    def compute_values(self):
        self.area = 0
        self.height = 0
        for elem in self.buildings:
            self.area += elem.get_area()
            self.height = max(self.height, elem.get_height())

    def move_positions(self, n):
        res_list = []
        for i in range(0, len(self.buildings)):
            res_list.append(
                Building(
                    self.buildings[i].get_xmin() + n,
                    self.buildings[i].get_xmax() + n,
                    self.buildings[i].get_height()))
        return Skyline().assign_buildings(res_list)

    '''
    Simple algorithm, having a list to keep the reverse skyline and then replace it
    '''

    def reverse_skyline(self):
        aux_list = []
        i = len(self.buildings) - 1
        dist = 1
        while i >= 0:
            xmin = self.buildings[i].get_xmin()
            xmax = self.buildings[i].get_xmax()
            h = self.buildings[i].get_height()
            if i == len(self.buildings) - 1:
                aux_list.append(Building(dist, dist + (xmax - xmin), h))
                dist += (xmax - xmin)
            else:
                dist += (self.buildings[i + 1].get_xmin() - xmax)
                aux_list.append(Building(dist, dist + (xmax - xmin), h))
                dist += (xmax - xmin)
            i -= 1
        return Skyline().assign_buildings(aux_list)

    def replicate_skyline(self, n):

        if n == 0 or not self.buildings:
            return Skyline()
        elif n == 1:
            return Skyline().assign_buildings(self.buildings)
        res_list = []
        res_list[len(res_list):] = self.buildings
        sz = len(self.buildings)
        dist = self.buildings[-1].get_xmax() - self.buildings[0].get_xmin()
        for i in range(1, n):
            for j in range(0, sz):
                res_list.append(
                    Building(
                        self.buildings[j].get_xmin() + i * dist,
                        self.buildings[j].get_xmax() + i * dist,
                        self.buildings[j].get_height()))
        return Skyline().assign_buildings(res_list)

    def get_values_of_plot(self):
        # print(len(self.buildings))
        x, y, w = [], [], []
        for elem in self.buildings:
            x.append((elem.get_xmax() + elem.get_xmin()) / 2)
            y.append(elem.get_height())
            w.append(elem.get_xmax() - elem.get_xmin())
        return x, y, w

    def get_information(self):
        self.area = 0
        self.height = 0
        for elem in self.buildings:
            self.area += elem.get_area()
            self.height = max(self.height, elem.get_height())
        return self.area, self.height
