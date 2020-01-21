class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        # f - calkowity koszt dojscia do tego miejsca
        # g - dystans miedzy obecnym miejscem a poczatkiem labiryntu
        # h - oszacowany dystans miedzy obenym miejscem a koncowym
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    pathway = []
    # Tworzenie poczatku i konca labiryntu
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    # Dodanie startu do open_list
    open_list.append(start_node)

    # Dzialamy dopoki nie znajdziemy konca labiryntu
    while len(open_list) > 0:

        # Wez obecne miejsce w labiryncie
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                print(current_node.position)
                current_node = item
                current_index = index

        # Usun obecne miejsce z open list i dodanie go do closed_list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Znalezienie konca labiryntu
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            print(pathway)
            return path[::-1]  # Trzeba odwrocic sciezke

        # Szukanie po sasiednich miejscach
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Sasiednie miejsca

            # Obecne miejsce na labiryncie
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Upewnij sie, ze jest w zasiegu
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Upewnij sie, ze nie wchodzisz w sciane
            if maze[node_position[0]][node_position[1]] != 1:
                continue

            # Stworz nowe miejsce
            new_node = Node(current_node, node_position)

            # Dolacz nowe miejsce do poszukiwan
            children.append(new_node)

        # Petla idaca przez dzieci
        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Obliczanie wartosci g, h, f
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Sprawdzenie czy wybrana sciezka jest juz na open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Dodanie miejsca do open list
            open_list.append(child)


def main():
    maze = [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0),
            (0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0),
            (0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0), (0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0),
            (0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0),
            (0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0), (0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0),
            (0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0),
            (0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0), (0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]

    start = (1, 1)
    end = (10, 10)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
