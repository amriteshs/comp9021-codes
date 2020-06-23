import os
import subprocess
from collections import defaultdict, deque


class MazeError(Exception):
    def __init__(self, message):
        self.message = message


class Maze:
    def __init__(self, file):
        self.file = file

        maze = []
        with open(self.file) as file:
            ydim = 0
            digit_ctr = set()

            for line in file:
                if not line.isspace():
                    xdim = 0
                    maze_line = []

                    for digit in line:
                        if digit not in (' ', '\n', '\t'):
                            if digit not in ['0', '1', '2', '3']:
                                raise MazeError('Incorrect input.')

                            maze_line.append(int(digit))
                            xdim += 1

                    if xdim not in range(2, 32):
                        raise MazeError('Incorrect input.')

                    maze.append(maze_line)
                    digit_ctr.add(xdim)
                    ydim += 1

            if ydim not in range(2, 42) or len(digit_ctr) > 1:
                raise MazeError('Incorrect input.')

        for i in range(len(maze)):
            if maze[i][len(maze[len(maze) - 1]) - 1] in (1, 3):
                raise MazeError('Input does not represent a maze.')

        for j in range(len(maze[len(maze) - 1])):
            if maze[len(maze) - 1][j] in (2, 3):
                raise MazeError('Input does not represent a maze.')

        self.maze = maze

    def analyse(self):
        ctr_list = [0, 0, 0, 0, 0, 0]

        # calculations for connected points
        connected_points = defaultdict(list)
        visited_points = []

        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 0:
                    connected_points[(i, j)] = []
                elif self.maze[i][j] == 1:
                    connected_points[(i, j)] = [(i, j + 1)]
                elif self.maze[i][j] == 2:
                    connected_points[(i, j)] = [(i + 1, j)]
                elif self.maze[i][j] == 3:
                    connected_points[(i, j)] = [(i, j + 1), (i + 1, j)]

                if j > 0 and self.maze[i][j - 1] in (1, 3):
                    connected_points[(i, j)].append((i, j - 1))

                if i > 0 and self.maze[i - 1][j] in (2, 3):
                    connected_points[(i, j)].append((i - 1, j))

                if i in (0, len(self.maze) - 1) and j < len(self.maze[i]) - 1 and (i, j + 1) not in connected_points[(i, j)]:
                    ctr_list[0] += 1

                if j in (0, len(self.maze[i]) - 1) and i < len(self.maze) - 1 and (i + 1, j) not in connected_points[(i, j)]:
                    ctr_list[0] += 1

                if not connected_points[(i, j)]:
                    visited_points.append((i, j))

        start_pt = []
        flag = False

        for key, val in connected_points.items():
            if key not in visited_points:
                start_pt.append(key)
                ctr_list[1] += 1
                flag = True
                break

        if flag:
            while len(visited_points) < len(connected_points):
                flag1 = False

                for s in start_pt:
                    if s not in visited_points:
                        visited_points.append(s)
                        flag1 = True

                if not flag1:
                    ctr_list[1] += 1

                    for key, val in connected_points.items():
                        if key not in visited_points:
                            start_pt = [key]
                            break
                else:
                    temp = []

                    for s in start_pt:
                        for c in connected_points[s]:
                            if c not in temp:
                                temp.append(c)

                    start_pt = temp

        # calculations for connected areas
        connected_areas = defaultdict(list)
        gate_regions = []
        gates_in_gate_regions = defaultdict(int)

        for i in range(len(self.maze) - 1):
            for j in range(len(self.maze[i]) - 1):
                # (i, j) is top-left coordinate of region
                connected_areas[(i, j)] = []

                if i > 0 and (i, j + 1) not in connected_points[(i, j)]:
                    connected_areas[(i, j)].append((i - 1, j))

                if j > 0 and (i + 1, j) not in connected_points[(i, j)]:
                    connected_areas[(i, j)].append((i, j - 1))

                if i < len(self.maze) - 2 and (i + 1, j + 1) not in connected_points[(i + 1, j)]:
                    connected_areas[(i, j)].append((i + 1, j))

                if j < len(self.maze[0]) - 2 and (i + 1, j + 1) not in connected_points[(i, j + 1)]:
                    connected_areas[(i, j)].append((i, j + 1))

                if i == 0 and (i, j + 1) not in connected_points[(i, j)]:
                    if not gates_in_gate_regions[(i, j)]:
                        gates_in_gate_regions[(i, j)] = 1
                    else:
                        gates_in_gate_regions[(i, j)] += 1

                    if (i, j) not in gate_regions:
                        gate_regions.append((i, j))

                if j == 0 and (i + 1, j) not in connected_points[(i, j)]:
                    if not gates_in_gate_regions[(i, j)]:
                        gates_in_gate_regions[(i, j)] = 1
                    else:
                        gates_in_gate_regions[(i, j)] += 1

                    if (i, j) not in gate_regions:
                        gate_regions.append((i, j))

                if i == len(self.maze) - 2 and (i + 1, j + 1) not in connected_points[(i + 1, j)]:
                    if not gates_in_gate_regions[(i, j)]:
                        gates_in_gate_regions[(i, j)] = 1
                    else:
                        gates_in_gate_regions[(i, j)] += 1

                    if (i, j) not in gate_regions:
                        gate_regions.append((i, j))

                if j == len(self.maze[0]) - 2 and (i + 1, j + 1) not in connected_points[(i, j + 1)]:
                    if not gates_in_gate_regions[(i, j)]:
                        gates_in_gate_regions[(i, j)] = 1
                    else:
                        gates_in_gate_regions[(i, j)] += 1

                    if (i, j) not in gate_regions:
                        gate_regions.append((i, j))

        accessible_regions = []
        visited_regions = deque()
        visited_gate_regions = []

        for i in gate_regions:
            if i not in visited_gate_regions:
                visited_gate_regions.append(i)
                visited_regions.append(i)
                ctr_list[3] += 1

                if i not in accessible_regions:
                    accessible_regions.append(i)
            else:
                continue

            while visited_regions:
                current_region = visited_regions.popleft()

                for c in connected_areas[current_region]:
                    if c not in accessible_regions:
                        accessible_regions.append(c)
                        visited_regions.append(c)

                    if c in gate_regions and c not in visited_gate_regions:
                        visited_gate_regions.append(c)

        ctr_list[2] = ((len(self.maze) - 1) * (len(self.maze[0]) - 1)) - len(accessible_regions)

        cul_de_sacs = []
        visited_cul_de_sacs = [key for key, val in connected_areas.items() if gates_in_gate_regions[key] == 1 and len(val) == 0]
        visited_cul_de_sacs.extend([i for i in accessible_regions if i not in gate_regions and len(connected_areas[i]) == 1])
        possible_cul_de_sacs = deque()

        for i in visited_cul_de_sacs:
            if i not in cul_de_sacs:
                cul_de_sacs.append(i)
                possible_cul_de_sacs.append(i)
            else:
                continue

            while possible_cul_de_sacs:
                current_cul_de_sac = possible_cul_de_sacs.popleft()

                if current_cul_de_sac not in cul_de_sacs:
                    cul_de_sacs.append(current_cul_de_sac)

                for c in connected_areas[current_cul_de_sac]:
                    if c not in cul_de_sacs:
                        if gates_in_gate_regions[c] == 1 and len([k for k in connected_areas[c] if k not in cul_de_sacs]) == 0:
                            cul_de_sacs.append(c)
                            possible_cul_de_sacs.append(c)
                        elif not gates_in_gate_regions[c] and len([k for k in connected_areas[c] if k not in cul_de_sacs]) == 1:
                            cul_de_sacs.append(c)
                            possible_cul_de_sacs.append(c)

        visited_cul_de_sacs = []

        for i in cul_de_sacs:
            if i not in visited_cul_de_sacs:
                visited_cul_de_sacs.append(i)
                ctr_list[4] += 1
            else:
                continue

            connected_cul_de_sacs = deque([j for j in connected_areas[i] if j in cul_de_sacs])

            while connected_cul_de_sacs:
                current_cul_de_sac = connected_cul_de_sacs.popleft()

                if current_cul_de_sac not in visited_cul_de_sacs:
                    visited_cul_de_sacs.append(current_cul_de_sac)

                for j in connected_areas[current_cul_de_sac]:
                    if j in cul_de_sacs and j not in visited_cul_de_sacs:
                        connected_cul_de_sacs.append(j)

        visited_gate_regions = []

        for i in gate_regions:
            if i not in visited_gate_regions and i not in cul_de_sacs:
                visited_gate_regions.append(i)
            else:
                continue

            if gates_in_gate_regions[i] == 2:
                if not connected_areas[i] or all([c in cul_de_sacs for c in connected_areas[i]]):
                    ctr_list[5] += 1
            elif gates_in_gate_regions[i] < 2:
                visited_regions = deque()
                possible_path = []

                visited_regions.append(i)

                while len(visited_regions) == 1:
                    current_region = visited_regions.popleft()
                    possible_path.append(current_region)

                    if current_region in gate_regions and len([j for j in connected_areas[current_region] if j not in possible_path and j not in cul_de_sacs]) == 0 and sum([gates_in_gate_regions[j] for j in possible_path]) == 2:
                        ctr_list[5] += 1
                        visited_gate_regions.append(current_region)

                    for c in connected_areas[current_region]:
                        if c not in possible_path and c not in cul_de_sacs:
                            visited_regions.append(c)

        init_output = 'The maze has '
        rest_output = [
            ['no gate.', 'a single gate.', f'{ctr_list[0]} gates.'],
            ['no wall.', 'walls that are all connected.', f'{ctr_list[1]} sets of walls that are all connected.'],
            ['no inaccessible inner point.', 'a unique inaccessible inner point.', f'{ctr_list[2]} inaccessible inner points.'],
            ['no accessible area.', 'a unique accessible area.', f'{ctr_list[3]} accessible areas.'],
            ['no accessible cul-de-sac.', 'accessible cul-de-sacs that are all connected.', f'{ctr_list[4]} sets of accessible cul-de-sacs that are all connected.'],
            ['no entry-exit path with no intersection not to cul-de-sacs.', 'a unique entry-exit path with no intersection not to cul-de-sacs.', f'{ctr_list[5]} entry-exit paths with no intersections not to cul-de-sacs.']
        ]

        for i in range(len(ctr_list)):
            print(init_output + rest_output[i][ctr_list[i] - ((ctr_list[i] - 2) * (ctr_list[i] > 2))])

    def display(self):
        walls_tex = []
        pillars_tex = []
        cul_de_sacs_tex = []
        entry_exit_paths_tex = []

        # calculations for connected points
        connected_points = defaultdict(list)

        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 0:
                    connected_points[(i, j)] = []
                elif self.maze[i][j] == 1:
                    connected_points[(i, j)] = [(i, j + 1)]
                elif self.maze[i][j] == 2:
                    connected_points[(i, j)] = [(i + 1, j)]
                elif self.maze[i][j] == 3:
                    connected_points[(i, j)] = [(i, j + 1), (i + 1, j)]

                if j > 0 and self.maze[i][j - 1] in (1, 3):
                    connected_points[(i, j)].append((i, j - 1))

                if i > 0 and self.maze[i - 1][j] in (2, 3):
                    connected_points[(i, j)].append((i - 1, j))

                if not connected_points[(i, j)]:
                    pillars_tex.append((i, j))

        for i in range(len(self.maze)):
            flag = False
            init_pt = tuple()

            for j in range(len(self.maze[i])):
                if not flag:
                    if (i, j + 1) in connected_points[(i, j)]:
                        init_pt = (i, j)
                        flag = True
                else:
                    if (i, j + 1) not in connected_points[(i, j)]:
                        walls_tex.append((init_pt, (i, j)))
                        flag = False

        for j in range(len(self.maze[0])):
            flag = False
            init_pt = tuple()

            for i in range(len(self.maze)):
                if not flag:
                    if (i + 1, j) in connected_points[(i, j)]:
                        init_pt = (i, j)
                        flag = True
                else:
                    if (i + 1, j) not in connected_points[(i, j)]:
                        walls_tex.append((init_pt, (i, j)))
                        flag = False

        # calculations for connected areas
        connected_areas = defaultdict(list)
        gate_regions = []
        gates_in_gate_regions = defaultdict(int)

        for i in range(len(self.maze) - 1):
            for j in range(len(self.maze[i]) - 1):
                # (i, j) is top-left coordinate of region
                connected_areas[(i, j)] = []

                if i > 0 and (i, j + 1) not in connected_points[(i, j)]:
                    connected_areas[(i, j)].append((i - 1, j))

                if j > 0 and (i + 1, j) not in connected_points[(i, j)]:
                    connected_areas[(i, j)].append((i, j - 1))

                if i < len(self.maze) - 2 and (i + 1, j + 1) not in connected_points[(i + 1, j)]:
                    connected_areas[(i, j)].append((i + 1, j))

                if j < len(self.maze[0]) - 2 and (i + 1, j + 1) not in connected_points[(i, j + 1)]:
                    connected_areas[(i, j)].append((i, j + 1))

                if i == 0 and (i, j + 1) not in connected_points[(i, j)]:
                    if not gates_in_gate_regions[(i, j)]:
                        gates_in_gate_regions[(i, j)] = 1
                    else:
                        gates_in_gate_regions[(i, j)] += 1

                    if (i, j) not in gate_regions:
                        gate_regions.append((i, j))

                if j == 0 and (i + 1, j) not in connected_points[(i, j)]:
                    if not gates_in_gate_regions[(i, j)]:
                        gates_in_gate_regions[(i, j)] = 1
                    else:
                        gates_in_gate_regions[(i, j)] += 1

                    if (i, j) not in gate_regions:
                        gate_regions.append((i, j))

                if i == len(self.maze) - 2 and (i + 1, j + 1) not in connected_points[(i + 1, j)]:
                    if not gates_in_gate_regions[(i, j)]:
                        gates_in_gate_regions[(i, j)] = 1
                    else:
                        gates_in_gate_regions[(i, j)] += 1

                    if (i, j) not in gate_regions:
                        gate_regions.append((i, j))

                if j == len(self.maze[0]) - 2 and (i + 1, j + 1) not in connected_points[(i, j + 1)]:
                    if not gates_in_gate_regions[(i, j)]:
                        gates_in_gate_regions[(i, j)] = 1
                    else:
                        gates_in_gate_regions[(i, j)] += 1

                    if (i, j) not in gate_regions:
                        gate_regions.append((i, j))

        accessible_regions = []
        visited_regions = deque()
        visited_gate_regions = []

        for i in gate_regions:
            if i not in visited_gate_regions:
                visited_gate_regions.append(i)
                visited_regions.append(i)

                if i not in accessible_regions:
                    accessible_regions.append(i)
            else:
                continue

            while visited_regions:
                current_region = visited_regions.popleft()

                for c in connected_areas[current_region]:
                    if c not in accessible_regions:
                        accessible_regions.append(c)
                        visited_regions.append(c)

                    if c in gate_regions and c not in visited_gate_regions:
                        visited_gate_regions.append(c)

        cul_de_sacs = []
        visited_cul_de_sacs = [key for key, val in connected_areas.items() if gates_in_gate_regions[key] == 1 and len(val) == 0]
        visited_cul_de_sacs.extend([i for i in accessible_regions if i not in gate_regions and len(connected_areas[i]) == 1])
        possible_cul_de_sacs = deque()

        for i in visited_cul_de_sacs:
            if i not in cul_de_sacs:
                cul_de_sacs.append(i)
                possible_cul_de_sacs.append(i)
            else:
                continue

            while possible_cul_de_sacs:
                current_cul_de_sac = possible_cul_de_sacs.popleft()

                if current_cul_de_sac not in cul_de_sacs:
                    cul_de_sacs.append(current_cul_de_sac)

                for c in connected_areas[current_cul_de_sac]:
                    if c not in cul_de_sacs:
                        if gates_in_gate_regions[c] == 1 and len([k for k in connected_areas[c] if k not in cul_de_sacs]) == 0:
                            cul_de_sacs.append(c)
                            possible_cul_de_sacs.append(c)
                        elif not gates_in_gate_regions[c] and len([k for k in connected_areas[c] if k not in cul_de_sacs]) == 1:
                            cul_de_sacs.append(c)
                            possible_cul_de_sacs.append(c)

        cul_de_sacs.sort()
        cul_de_sacs_tex.extend([(i[0] + 0.5, i[1] + 0.5) for i in cul_de_sacs])

        entry_exit_paths = []
        visited_gate_regions = []

        for i in gate_regions:
            if i not in visited_gate_regions and i not in cul_de_sacs:
                visited_gate_regions.append(i)
            else:
                continue

            if gates_in_gate_regions[i] == 2:
                if not connected_areas[i] or all([c in cul_de_sacs for c in connected_areas[i]]):
                    entry_exit_paths.append([i, i])
            elif gates_in_gate_regions[i] < 2:
                visited_regions = deque()
                possible_path = []

                visited_regions.append(i)

                while len(visited_regions) == 1:
                    current_region = visited_regions.popleft()
                    possible_path.append(current_region)

                    if current_region in gate_regions and len([j for j in connected_areas[current_region] if j not in possible_path and j not in cul_de_sacs]) == 0 and sum([gates_in_gate_regions[j] for j in possible_path]) == 2:
                        entry_exit_paths.append(possible_path)
                        visited_gate_regions.append(current_region)

                    for c in connected_areas[current_region]:
                        if c not in possible_path and c not in cul_de_sacs:
                            visited_regions.append(c)

        vertical_paths = []
        horizontal_paths = []

        for i in entry_exit_paths:
            if i[0] == i[len(i) - 1]:
                start_region = tuple()
                end_region = tuple()

                if (i[0][0], i[0][1] + 1) not in connected_points[(i[0][0], i[0][1])] and (i[0][0] - 1, i[0][1]) not in cul_de_sacs:
                    start_region = (i[0][0] - 1, i[0][1])
                elif (i[0][0] + 1, i[0][1]) not in connected_points[(i[0][0], i[0][1])] and (i[0][0], i[0][1] - 1) not in cul_de_sacs:
                    start_region = (i[0][0], i[0][1] - 1)
                elif (i[0][0], i[0][1] + 1) not in connected_points[(i[0][0] + 1, i[0][1] + 1)] and (i[0][0], i[0][1] + 1) not in cul_de_sacs:
                    start_region = (i[0][0], i[0][1] + 1)
                elif (i[0][0] + 1, i[0][1]) not in connected_points[(i[0][0] + 1, i[0][1] + 1)] and (i[0][0] + 1, i[0][1]) not in cul_de_sacs:
                    start_region = (i[0][0] + 1, i[0][1])

                if (i[0][0], i[0][1] + 1) not in connected_points[(i[0][0], i[0][1])] and (i[0][0] - 1, i[0][1]) not in cul_de_sacs and (i[0][0] - 1 != start_region[0] or i[0][1] != start_region[1]):
                    end_region = (i[0][0] - 1, i[0][1])
                elif (i[0][0] + 1, i[0][1]) not in connected_points[(i[0][0], i[0][1])] and (i[0][0], i[0][1] - 1) not in cul_de_sacs and (i[0][0] != start_region[0] or i[0][1] - 1 != start_region[1]):
                    end_region = (i[0][0], i[0][1] - 1)
                elif (i[0][0], i[0][1] + 1) not in connected_points[(i[0][0] + 1, i[0][1] + 1)] and (i[0][0], i[0][1] + 1) not in cul_de_sacs and (i[0][0] != start_region[0] or i[0][1] + 1 != start_region[1]):
                    end_region = (i[0][0], i[0][1] + 1)
                elif (i[0][0] + 1, i[0][1]) not in connected_points[(i[0][0] + 1, i[0][1] + 1)] and (i[0][0] + 1, i[0][1]) not in cul_de_sacs and (i[0][0] + 1 != start_region[0] or i[0][1] != start_region[1]):
                    end_region = (i[0][0] + 1, i[0][1])

                if start_region[0] == end_region[0]:
                    horizontal_paths.append((start_region, end_region))
                elif start_region[1] == end_region[1]:
                    vertical_paths.append((start_region, end_region))
                else:
                    if start_region[0] == i[0][0]:
                        if start_region[1] < i[0][1]:
                            horizontal_paths.append((start_region, i[0]))
                        else:
                            horizontal_paths.append((i[0], start_region))

                        if end_region[0] < i[0][0]:
                            vertical_paths.append((end_region, i[0]))
                        else:
                            vertical_paths.append((i[0], end_region))
                    else:
                        if start_region[0] < i[0][0]:
                            vertical_paths.append((start_region, i[0]))
                        else:
                            vertical_paths.append((i[0], start_region))

                        if end_region[1] < i[0][1]:
                            horizontal_paths.append((end_region, i[0]))
                        else:
                            horizontal_paths.append((i[0], end_region))
            else:
                start_region = tuple()
                end_region = tuple()
                temph = []
                tempv = []
                flag1 = False
                flag2 = False
                p = []

                if i[0][0] == 0 and ((i[0][1] not in (0, len(self.maze[0]) - 2)) or (i[0][1] == 0 and (0, 1) not in connected_points[(0, 0)]) or (i[0][1] == len(self.maze[0]) - 2 and (0, len(self.maze[0]) - 2) not in connected_points[(0, len(self.maze[0]) - 1)])):
                    p = [(-1, i[0][1])]
                elif i[0][0] == len(self.maze) - 2 and ((i[0][1] not in (0, len(self.maze[0]) - 2)) or (i[0][1] == 0 and (len(self.maze) - 1, 1) not in connected_points[(len(self.maze) - 1, 0)]) or (i[0][1] == len(self.maze[0]) - 2 and (len(self.maze) - 1, len(self.maze[0]) - 2) not in connected_points[(len(self.maze) - 1, len(self.maze[0]) - 1)])):
                    p = [(len(self.maze) - 1, i[0][1])]
                elif i[0][1] == 0 and ((i[0][0] not in (0, len(self.maze) - 2)) or (i[0][0] == 0 and (1, 0) not in connected_points[(0, 0)]) or (i[0][0] == len(self.maze) - 2 and (len(self.maze) - 2, 0) not in connected_points[(len(self.maze) - 1, 0)])):
                    p = [(i[0][0], -1)]
                elif i[0][1] == len(self.maze[0]) - 2 and ((i[0][0] not in (0, len(self.maze) - 2)) or (i[0][0] == 0 and (1, len(self.maze[0]) - 1) not in connected_points[(0, len(self.maze[0]) - 1)]) or (i[0][0] == len(self.maze) - 2 and (len(self.maze) - 2, len(self.maze[0]) - 1) not in connected_points[(len(self.maze) - 1, len(self.maze[0]) - 1)])):
                    p = [(i[0][0], len(self.maze[0]) - 1)]

                p.extend(i)

                if i[len(i) - 1][0] == 0 and ((i[len(i) - 1][1] not in (0, len(self.maze[0]) - 2)) or (i[len(i) - 1][1] == 0 and (0, 1) not in connected_points[(0, 0)]) or (i[len(i) - 1][1] == len(self.maze[0]) - 2 and (0, len(self.maze[0]) - 2) not in connected_points[(0, len(self.maze[0]) - 1)])):
                    p.append((-1, i[len(i) - 1][1]))
                elif i[len(i) - 1][0] == len(self.maze) - 2 and ((i[len(i) - 1][1] not in (0, len(self.maze[0]) - 2)) or (i[len(i) - 1][1] == 0 and (len(self.maze) - 1, 1) not in connected_points[(len(self.maze) - 1, 0)]) or (i[len(i) - 1][1] == len(self.maze[0]) - 2 and (len(self.maze) - 1, len(self.maze[0]) - 2) not in connected_points[(len(self.maze) - 1, len(self.maze[0]) - 1)])):
                    p.append((len(self.maze) - 1, i[len(i) - 1][1]))
                elif i[len(i) - 1][1] == 0 and ((i[len(i) - 1][0] not in (0, len(self.maze) - 2)) or (i[len(i) - 1][0] == 0 and (1, 0) not in connected_points[(0, 0)]) or (i[len(i) - 1][0] == len(self.maze) - 2 and (len(self.maze) - 2, 0) not in connected_points[(len(self.maze) - 1, 0)])):
                    p.append((i[len(i) - 1][0], -1))
                elif i[len(i) - 1][1] == len(self.maze[0]) - 2 and ((i[len(i) - 1][0] not in (0, len(self.maze) - 2)) or (i[len(i) - 1][0] == 0 and (1, len(self.maze[0]) - 1) not in connected_points[(0, len(self.maze[0]) - 1)]) or (i[len(i) - 1][0] == len(self.maze) - 2 and (len(self.maze) - 2, len(self.maze[0]) - 1) not in connected_points[(len(self.maze) - 1, len(self.maze[0]) - 1)])):
                    p.append((i[len(i) - 1][0], len(self.maze[0]) - 1))

                for j in range(len(p) - 1):
                    if p[j][0] == p[j + 1][0]:
                        if not flag1:
                            if flag2:
                                if start_region[0] < end_region[0]:
                                    tempv.append((start_region, end_region))
                                else:
                                    tempv.append((end_region, start_region))

                                flag2 = False

                            start_region = p[j]
                            end_region = p[j + 1]
                            flag1 = True
                        else:
                            end_region = p[j + 1]
                    else:
                        if not flag2:
                            if flag1:
                                if start_region[1] < end_region[1]:
                                    temph.append((start_region, end_region))
                                else:
                                    temph.append((end_region, start_region))

                                flag1 = False

                            start_region = p[j]
                            end_region = p[j + 1]
                            flag2 = True
                        else:
                            end_region = p[j + 1]

                if start_region[0] == end_region[0]:
                    if start_region[1] < end_region[1]:
                        temph.append((start_region, end_region))
                    else:
                        temph.append((end_region, start_region))
                else:
                    if start_region[0] < end_region[0]:
                        tempv.append((start_region, end_region))
                    else:
                        tempv.append((end_region, start_region))

                horizontal_paths.extend(temph)
                vertical_paths.extend(tempv)

        horizontal_paths.sort()
        vertical_paths.sort(key=lambda e: (e[0][1], e[0][0], e[1][1], e[1][0]))

        entry_exit_paths_tex.extend([((i[0][0] + 0.5, i[0][1] + 0.5), (i[1][0] + 0.5, i[1][1] + 0.5)) for i in horizontal_paths])
        entry_exit_paths_tex.extend([((i[0][0] + 0.5, i[0][1] + 0.5), (i[1][0] + 0.5, i[1][1] + 0.5)) for i in vertical_paths])

        latex = '\\documentclass[10pt]{article}\n' \
                '\\usepackage{tikz}\n' \
                '\\usetikzlibrary{shapes.misc}\n' \
                '\\usepackage[margin=0cm]{geometry}\n' \
                '\\pagestyle{empty}\n' \
                '\\tikzstyle{every node}=[cross out, draw, red]\n' \
                '\n' \
                '\\begin{document}\n' \
                '\n' \
                '\\vspace*{\\fill}\n' \
                '\\begin{center}\n' \
                '\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n' \
                '% Walls\n'

        for i in walls_tex:
            latex += f'    \\draw ({i[0][1]},{i[0][0]}) -- ({i[1][1]},{i[1][0]});\n'

        latex += '% Pillars\n'

        for i in pillars_tex:
            latex += f'    \\fill[green] ({i[1]},{i[0]}) circle(0.2);\n'

        latex += '% Inner points in accessible cul-de-sacs\n'

        for i in cul_de_sacs_tex:
            latex += f'    \\node at ({i[1]},{i[0]}) '
            latex += '{};\n'

        latex += '% Entry-exit paths without intersections\n'

        for i in entry_exit_paths_tex:
            latex += f'    \\draw[dashed, yellow] ({i[0][1]},{i[0][0]}) -- ({i[1][1]},{i[1][0]});\n'

        latex += '\\end{tikzpicture}\n' \
                 '\\end{center}\n' \
                 '\\vspace*{\\fill}\n' \
                 '\n' \
                 '\\end{document}\n'

        file_path, file_name = self.file.split('/')

        with open(f'{file_path}\\{file_name[:(len(file_name) - 4)]}.tex', 'w') as file:
            file.write(latex)

        commandline = subprocess.Popen(['C:\\Users\\amrit\\AppData\\Local\\Programs\\MiKTeX 2.9\\miktex\\bin\\x64\\pdflatex', '-output-directory', 'assignment02_files', f'{file_path}\\{file_name[:(len(file_name) - 4)]}.tex'])
        commandline.communicate()

        os.unlink(f'{file_path}\\{file_name[:(len(file_name) - 4)]}.aux')
        os.unlink(f'{file_path}\\{file_name[:(len(file_name) - 4)]}.log')


if __name__ == '__main__':
    fpath = 'assignment02_files/'
    files_main = ['maze_1.txt', 'maze_2.txt', 'labyrinth.txt']
    files_test = [f'maze_test{i}.txt' for i in range(1, 19)]

    for f in files_main:
        print(f.upper())
        m = Maze(fpath + f)
        m.display()
        print()

    for f in files_main:
        print(f.upper())
        m = Maze(fpath + f)
        m.analyse()
        print()