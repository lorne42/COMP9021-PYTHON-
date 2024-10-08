import math
import sys

import polygons


class PolygonsError(Exception):
    def __init__(self, wrong):
        self.wrong = wrong


class Polygons:
    def __init__(self, file_name):
        self.file=file_name
        with open(file_name) as file:
            lines = file.readlines()
        self.grid = []
        line_len = -1
        for line in lines:
            tmp_line = line.replace("", " ").split()
            if len(tmp_line):
                for i in range(0, len(tmp_line)):
                    if tmp_line[i] == '1' or tmp_line[i] == '0':
                        continue
                    else:
                        raise PolygonsError("Incorrect input.")
            if len(tmp_line) == 0:
                continue
            elif len(tmp_line) < 2 or len(tmp_line) > 50:
                raise PolygonsError("Incorrect input.")
            elif line_len != len(tmp_line) and line_len != -1:
                raise PolygonsError("Incorrect input.")
            else:
                line_len = len(tmp_line)
                self.grid.append(tmp_line)
                continue
        self.dim_x = len(self.grid[0])
        self.dim_y = len(self.grid)
        self.polygons = []
        self.all_vertices=[]
        self.area=[]
        self.depth=[]
        for y in range(self.dim_y):
            for x in range(self.dim_x):
                point = (y, x)
                if self.grid[point[0]][point[1]] == '1':
                    self.polygons.append(self.find_polygons(point))

        for polygon in self.polygons:
            vertices = []
            vertices.append(polygon[0])
            for j in range(len(polygon) - 2):
                if polygon[j + 1][0] - polygon[j][0] != polygon[j + 2][0] - polygon[j + 1][0] or polygon[j + 1][1] - \
                        polygon[j][1] != polygon[j + 2][1] - polygon[j + 1][1]:
                    vertices.append(polygon[j + 1])
                if j == len(polygon) - 3:
                    if polygon[-1][0] - polygon[-2][0] != polygon[0][0] - polygon[-1][0] or polygon[-1][1] - \
                            polygon[-2][1] != polygon[0][1] - polygon[-1][1]:
                        vertices.append(polygon[-1])
            self.all_vertices.append(vertices)
        result = self.count_containing_polygons()
        i = 0
        for polygon in self.polygons:
            vertices = []
            i += 1
            vertices.append(polygon[0])
            for j in range(len(polygon) - 2):
                if polygon[j + 1][0] - polygon[j][0] != polygon[j + 2][0] - polygon[j + 1][0] or polygon[j + 1][1] - \
                        polygon[j][1] != polygon[j + 2][1] - polygon[j + 1][1]:
                    vertices.append(polygon[j + 1])
                if j == len(polygon) - 3:
                    if polygon[-1][0] - polygon[-2][0] != polygon[0][0] - polygon[-1][0] or polygon[-1][1] - \
                            polygon[-2][1] != polygon[0][1] - polygon[-1][1]:
                        vertices.append(polygon[-1])
            prm = cperimeter(vertices)
            area = carea(vertices)
            self.area.append(area)
            self.depth.append(result[i - 1])


    def find_polygons(self, point):
        polygon = []
        polygon.append(point)
        while 1:
            point = self.addpoint(polygon)
            if point is False:
                raise PolygonsError("Cannot get polygons as expected.")
            elif point == polygon[0]:
                break
            else:
                polygon.append(point)

        found_duplicate = False
        for i in range(len(polygon)):
            for j in range(len(polygon)):
                if i != j and polygon[i] == polygon[j]:
                    polygon[i:j] = []
                    found_duplicate = True
                    break
            if found_duplicate:
                break
        for p, q in polygon:
            self.grid[p][q] = '0'
        return polygon

    def addpoint(self, polygon):
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        if len(polygon) == 1:
            dir = (1, 0)
        else:
            dir = (polygon[-1][0] - polygon[-2][0], polygon[-1][1] - polygon[-2][1])
        q = None
        for i in range(len(dirs)):
            if dir == dirs[i]:
                q = i
                break
        for i in range(0, 6):
            dir = dirs[(q - 2 + i) % 8]
            x = polygon[-1][1] + dir[1]
            y = polygon[-1][0] + dir[0]
            if 0 <= x < self.dim_x and 0 <= y < self.dim_y and self.grid[y][x] == '1':
                point = (y, x)
                return point
        return False

    def analyse(self):
        result = self.count_containing_polygons()
        i = 0
        for polygon in self.polygons:
            vertices = []
            i += 1
            vertices.append(polygon[0])
            for j in range(len(polygon) - 2):
                if polygon[j + 1][0] - polygon[j][0] != polygon[j + 2][0] - polygon[j + 1][0] or polygon[j + 1][1] - \
                        polygon[j][1] != polygon[j + 2][1] - polygon[j + 1][1]:
                    vertices.append(polygon[j + 1])
                if j == len(polygon) - 3:
                    if polygon[-1][0] - polygon[-2][0] != polygon[0][0] - polygon[-1][0] or polygon[-1][1] - \
                            polygon[-2][1] != polygon[0][1] - polygon[-1][1]:
                        vertices.append(polygon[-1])
            prm = cperimeter(vertices)
            area = carea(vertices)
            print("Polygon " + str(i) + ":")
            if prm[1] == 0:
                print(f"    Perimeter: {prm[0]:.1f}")
            elif prm[0] == 0 and prm[1] != 0:
                print(f"    Perimeter: {prm[1]}*sqrt(.32)")
            elif prm[0] != 0 and prm[1] != 0:
                print(f"    Perimeter: {prm[0]:.1f} + {prm[1]}*sqrt(.32)")

            print(f"    Area: {area:.2f}")


            print("    Convex:", is_convex(vertices))

            print(f"    Nb of invariant rotations: {nb(vertices)}")

            print(f"    Depth: {result[i-1]}")


    def is_point_inside_polygon(self,y, x,polygon):
        n = len(polygon)
        inside = False
        p1y, p1x = polygon[0]
        for i in range(1, n + 1):
            p2y, p2x = polygon[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                            if p1x == p2x or x <= xinters:
                                inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def count_containing_polygons(self):
        num_contained = [0] * len(self.all_vertices)

        for i, polygon1 in enumerate(self.all_vertices):
            for j, polygon2 in enumerate(self.all_vertices):
                if i != j:
                    is_contained = all(self.is_point_inside_polygon(y, x,polygon2) for y, x in polygon1)

                    if is_contained:
                        num_contained[i] += 1

        return num_contained
    def display(self):

        max=-1.0
        min=sys.maxsize
        for i in range(len(self.all_vertices)):
            if self.area[i]>max:
                max=self.area[i]
            if self.area[i]<min:
                min=self.area[i]
        file=self.file.replace(".txt","1.tex")
        with open(file,"w") as f:
            f.write("\\documentclass[10pt]{article}\n")
            f.write("\\usepackage{tikz}\n")
            f.write("\\usepackage[margin=0cm]{geometry}\n")
            f.write("\\pagestyle{empty}\n")
            f.write("\n")
            f.write("\\begin{document}\n")
            f.write("\n")
            f.write("\\vspace*{\\fill}\n")
            f.write("\\begin{center}\n")
            f.write("\\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]\n")
            f.write(f"\\draw[ultra thick] (0, 0) -- ({self.dim_x-1}, 0) -- ({self.dim_x-1}, {self.dim_y-1}) -- (0, {self.dim_y-1}) -- cycle;\n")
            f.write("\n")
            sorted_depth = sorted(self.depth)
            unique_set = set(sorted_depth)
            unique_list = list(unique_set)
            flag=-1
            for j in range(len(unique_list)):
                for q in range(len(sorted_depth)):
                    if flag!=unique_list[j]:
                        f.write(f"% Depth {unique_list[j]}\n")
                        flag=unique_list[j]
                    if self.depth[q]==unique_list[j]:
                        f.write(f"\\filldraw[fill=orange!{cul(max,min,self.area[q])}!yellow] ")
                        for u in range(len(self.all_vertices[q])):
                            f.write(f"({self.all_vertices[q][u][1]}, {self.all_vertices[q][u][0]}) -- ")
                        f.write(f"cycle;\n")
            f.write("\\end{tikzpicture}\n")
            f.write("\\end{center}\n")
            f.write("\\vspace*{\\fill}\n")
            f.write("\n")
            f.write("\\end{document}\n")

def nb(vertices):
    if len(vertices) % 2 == 1:
        return 1

    center_x = set()
    center_y = set()

    for index in range(0, len(vertices) // 2):
        cur = vertices[index]
        next_point = vertices[index + len(vertices) // 2]

        x = (cur[1] + next_point[1]) / 2
        y = (cur[0] + next_point[0]) / 2

        center_x.add(x)
        center_y.add(y)

    if len(center_y) == 1 and len(center_x) == 1:
        mid_point = (center_y.pop(), center_x.pop())
        flag = True

        for index in range(0, len(vertices) // 4):
            cur = vertices[index]
            next_point = vertices[index + len(vertices) // 4]

            if not (abs(cur[0] - mid_point[0]) == abs(mid_point[1] - next_point[1]) and
                    abs(cur[1] - mid_point[1]) == abs(mid_point[0] - next_point[0])):
                flag = False
                break

        if flag:
            return 4

        return 2
    else:
        return 1


def cperimeter(polygon):
    perimeter = []
    prm_1 = 0
    prm_2 = 0

    for i in range(len(polygon) - 1):
        y1, x1 = polygon[i]
        y2, x2 = polygon[i + 1]
        if y2 - y1 == 0 or x2 - x1 == 0:
            edge_length = math.sqrt(((x2 - x1) * 0.4) ** 2 + ((y2 - y1) * 0.4) ** 2)
            prm_1 += edge_length
        else:
            prm_2 += abs(x2 - x1)

    y1, x1 = polygon[-1]
    y2, x2 = polygon[0]
    if y2 - y1 == 0 or x2 - x1 == 0:
        edge_length = math.sqrt(((x2 - x1) * 0.4) ** 2 + ((y2 - y1) * 0.4) ** 2)
        prm_1 += edge_length
    else:
        prm_2 += abs(x2 - x1)
    perimeter.append(prm_1)
    perimeter.append(prm_2)

    return perimeter


def carea(polygon):
    area = 0

    for i in range(len(polygon) - 1):
        y1, x1 = polygon[i]
        y2, x2 = polygon[i + 1]
        area += (x1 * y2 - x2 * y1) * 0.16

    # Add the last term connecting the last and first vertices
    y1, x1 = polygon[-1]
    y2, x2 = polygon[0]
    area += (x1 * y2 - x2 * y1) * 0.16

    area = 0.5 * abs(area)
    area = round(area, 2)
    return area


def is_convex(polygon):
    det_sign = 0
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        p3 = polygon[(i + 2) % len(polygon)]

        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = (p3[0] - p2[0], p3[1] - p2[1])
        det = v1[0] * v2[1] - v1[1] * v2[0]
        if det != 0:
            det_sign = det / abs(det)
            break
    for i in range(1, len(polygon)):
        p1 = polygon[i - 1]
        p2 = polygon[i]
        p3 = polygon[(i + 1) % len(polygon)]

        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = (p3[0] - p2[0], p3[1] - p2[1])

        det = v1[0] * v2[1] - v1[1] * v2[0]
        current_det_sign = det / abs(det) if det != 0 else 0

        if current_det_sign != det_sign:
            return 'no'
    return 'yes'


def cul(max,min,cur_area):
    if max==min:
        return 0
    else:
        return round((max-float(cur_area))/(max-min)*100)
