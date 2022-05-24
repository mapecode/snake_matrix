import copy

movements = {
    # name: (i operation, j operation)
    'Left' : (0, -1),
    'Right' : (0, +1),
    'Down' : (+1, 0),
    'Up' : (-1, 0)
} 

class Game:
    board : list
    snake : list
    depth : int
    board_matrix : list # board[0] x board[1]
    n_paths : int

    def __init__(self, board : list, snake: list, depth : int) -> None:
        self.board = board
        self.snake = snake
        self.depth = depth
        self.board_matrix = []
        self.n_paths = 0

    def run_board_tests(self):
        # board.length = 2
        assert(len(self.board) == 2)
        # 1 ≤ board[i] ≤ 10
        assert(type(self.board[0]) == int)
        assert(type(self.board[1]) == int)
        assert(self.board[0] >= 1 and self.board[0] <= 10)
        assert(self.board[1] >= 1 and self.board[1] <= 10)
    
    def run_snake_tests(self):
        # 3 ≤ ​snake.length​ ≤ 7
        assert(len(self.snake) >= 3 and len(self.snake) <= 7)
        # snake[i].length​ = 2
        for e in self.snake:
            assert(len(e) == 2)
            assert(type(e[0]) == int and type(e[1]) == int)
        # 0 ≤ ​snake[i][j]​ < ​board[j]​
        for i in range(0, len(self.snake)):
            for j in range(0, len(self.snake[i])):
                assert(type(self.snake[i][j]) == int)
                assert(self.snake[i][j] >= 0 and self.snake[i][j] < self.board[j])

    def run_depth_tests(self):
        # 1 ≤ n ≤ 20
        assert(self.depth >= 1 and self.depth <= 20)

    def create_board_matrix(self):
        self.board_matrix = [0] * self.board[1]
        for x in range (self.board[1]):
            self.board_matrix[x] = [0] * self.board[0]

        n : int = 1

        for position in self.snake:
            self.board_matrix[position[1]][position[0]] = n
            n+=1
        
    def __index_of_pos(self, board_matrix, n):
        for i in range(len(board_matrix)):
            try:
                j = board_matrix[i].index(n)
            except:
                continue

            return (i, j)


    def apply_movement(self, board_matrix, movement_id, head, tail):
        new_board_matrix : list = copy.deepcopy(board_matrix)
        # create head movement
        movement : tuple = (head[0] + movements[movement_id][0], head[1] + movements[movement_id][1])

        # apply head movement
        new_board_matrix[movement[0]][movement[1]] = 1

        # apply tail movement
        new_board_matrix[tail[0]][tail[1]] = 0

        # apply rest movements
        for x in range(1, len(self.snake)):
            index : int = self.__index_of_pos(board_matrix, x)

            new_board_matrix[index[0]][index[1]] = x + 1

        return new_board_matrix

    def check_movement(self, board_matrix, head, movement_index):
        i : int = head[0] + movement_index[0]
        j : int = head[1] + movement_index[1]

        if i>=0 and i < len(board_matrix) and  j>=0 and j < len(board_matrix[i]) and board_matrix[i][j] == 0:
            return True
        else:
            return False

    def search_paths(self, stage=0, board_matrix=None):
        if board_matrix == None:
            assert(len(self.board_matrix) != 0)
            board_matrix = self.board_matrix

        if stage == self.depth:
            self.n_paths += 1
        else:
            for movement_id, movement_index in movements.items():
                if(self.check_movement(board_matrix, self.__index_of_pos(board_matrix, 1), movement_index) == True):
                    new_board_matrix = self.apply_movement(board_matrix=board_matrix, movement_id=movement_id, head=self.__index_of_pos(board_matrix, 1), tail=self.__index_of_pos(board_matrix, len(self.snake)))
                    self.search_paths(board_matrix=new_board_matrix, stage=stage+1)




            
