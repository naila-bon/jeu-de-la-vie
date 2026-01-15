import unittest

from main import JeuDeLaVie

class TestJeuDeLaVie(unittest.TestCase):
    
    def test_initialized_grid(self):
        jeu = JeuDeLaVie()

        grid = jeu.grid

        self.assertEqual(grid, [[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])
        
    def test_initialized_cell(self):
        jeu = JeuDeLaVie()

        jeu.add_cell(0,0)

        
        self.assertEqual(jeu.grid, [[1, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])
        
            
    def test_killed_cell(self):
        jeu = JeuDeLaVie()
        jeu.add_cell(0,0)

        jeu.remove_cell(0,0)

        
        self.assertEqual(jeu.grid, [[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])
        
            
    def test_check_neighbours_are_alived(self):
        jeu = JeuDeLaVie()
        jeu.add_cell(0,0)
        jeu.add_cell(0,1)

        neihbours = jeu.check_neighbours(0,0)
        
        self.assertEqual(neihbours, 1)
        
    def test_cell_die_if_less_than_two_neighbours(self):
        jeu = JeuDeLaVie()
        jeu.add_cell(0,0)

        
        jeu.run()
        
        self.assertEqual(jeu.grid[0][0], 0)

    def test_cell_die_if_more_than_three_neighbours(self):
        jeu = JeuDeLaVie()
        jeu.add_cell(0,0)
        jeu.add_cell(0,1)
        jeu.add_cell(0,2)
        jeu.add_cell(1,0)
        jeu.add_cell(1,1)

        jeu.run()
        
        self.assertEqual(jeu.grid[0][1], 0)

    def test_cell_alive_if_equal_to_three_neighbours(self):
        jeu = JeuDeLaVie()
        jeu.add_cell(0,0)
        jeu.add_cell(0,1)
        jeu.add_cell(2,2)

        jeu.run()
        
        self.assertEqual(jeu.grid[1][1], 1)

if __name__ == "__main__":
    unittest.main()