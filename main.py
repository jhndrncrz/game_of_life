import random


class Cell:
    def __init__(self):
        """
        Creates a dead cell
        """
        self.status = 0

    def set_dead(self):
        """
        Sets a live cell to dead cell
        """
        self.status = 0

    def set_alive(self):
        """
        Sets a dead cell to live cell
        """
        self.status = 1

    def get_status(self):
        """
        Returns whether cell is alive or dead
        """
        return self.status

    def get_character(self):
        """
        Returns a character representing whether the cell is dead or alive
        :return:
        """
        return '█' if self.status else ' '


class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell() for j in range(self.columns)] for i in range(self.rows)]

        self.generate_board_random()

    def draw_board(self):
        """
        Prints the board
        """
        print("NEXT ITERATION")

        for row in self.grid:
            for item in row:
                print(item.get_character(), end='')
            print()

    def generate_board_random(self):
        """
        Create board randomly
        """
        for row in self.grid:
            for item in row:
                if random.randint(0, 1):
                    item.set_alive()

    def check_neighbors(self, cell_row, cell_column):
        """
        Count the number of live neighbors of a cell
        """
        neighbor_min = -1
        neighbor_max = 1

        live_neighbors = []

        for i in range(neighbor_min, neighbor_max + 1):
            for j in range(neighbor_min, neighbor_max + 1):
                neighbor_row = cell_row + i
                neighbor_column = cell_column + j

                is_valid_neighbor = True

                if neighbor_row == cell_row and neighbor_column == cell_column:
                    is_valid_neighbor = False

                if neighbor_row < 0 or neighbor_row >= self.rows:
                    is_valid_neighbor = False

                if neighbor_column < 0 or neighbor_column >= self.columns:
                    is_valid_neighbor = False

                if is_valid_neighbor and self.grid[neighbor_row][neighbor_column].get_status():
                    live_neighbors.append(self.grid[neighbor_row][neighbor_column])

        return live_neighbors

    def update_board(self):
        """
        Update the board
        """
        to_live = []
        to_die = []

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                live_neighbors = self.check_neighbors(i, j)
                center_cell = self.grid[i][j]
                center_cell_status = center_cell.get_status()

                if center_cell_status:
                    if len(live_neighbors) < 2 or len(live_neighbors) > 3:
                        to_die.append(center_cell)
                    if 1 < len(live_neighbors) < 4:
                        to_live.append(center_cell)
                else:
                    if len(live_neighbors) == 3:
                        to_live.append(center_cell)

        for cell in to_live:
            cell.set_alive()

        for cell in to_die:
            cell.set_dead()


def main():
    board_rows = int(input("Enter the number of rows: "))
    board_columns = int(input("Enter the number of columns: "))

    main_board = Board(board_rows, board_columns)

    main_board.draw_board()

    action = ''

    while action != 'q':
        action = input("Press enter to create next generation, press q to exit \n")

        if action == '':
            main_board.update_board()
            main_board.draw_board()


if __name__ == '__main__':
    main()
