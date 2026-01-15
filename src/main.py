

class JeuDeLaVie():
    
    def __init__(self):
        self.grid =[[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
        
        self.grid_rows = 3
        self.grid_cols = 3
    
    def add_cell(self, cell_row:int, cell_column: int):
        self.grid[cell_row][cell_column] = 1

    def remove_cell(self, cell_row:int, cell_column: int):
        self.grid[cell_row][cell_column] = 0

    def check_neighbours(self, row:int, column: int):
        neighbours = 0

        for direction_row in (-1, 0, 1):
            for direction_col in (-1, 0, 1):
                if direction_row == 0 and direction_col == 0:
                    continue
                current_row, current_col = row + direction_row, column + direction_col
                if 0 <= current_row < self.grid_rows and 0 <= current_col < self.grid_cols:
                    if self.grid[current_row][current_col]:
                        neighbours+=1


        return neighbours
    
    def run(self):
        cells_to_remove = []
        cells_to_add = []
        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                neighbours = self.check_neighbours(row,col)
                alive = self.grid[row][col] == 1

                if alive:
                    if neighbours < 2 or neighbours > 3:
                        cells_to_remove.append((row,col))
                else:
                    if neighbours == 3:
                        cells_to_add.append((row, col))

        for row, col in cells_to_remove:
            self.remove_cell(row, col)

        for row, col in cells_to_add:
            self.add_cell(row, col)