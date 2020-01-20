class ConnectFour:

    def __init__(self, board, w, h):
        """Class constructor"""
        # Board data
        self.board = board
        # Board width
        self.w = w
        # Board height
        self.h = h

    def isLineAt(self, x, y, dx, dy):
        """Return True if a line of identical tokens exists starting at (x,y)
           in direction (dx,dy)"""
        token = self.board[y][x]
        last_token = token
        # Horizontal Case
        if dx == 1 and dy == 0:
            acc = 0
            while x < self.w - 1 and last_token == self.board[y][x+1]:
                # Checks if the token horizontally to the right of the starting token is the
                # same as the starting token. If so a accumulator is incremented and the x position is incremented
                # to check the next horizontal position on the board
                if token == self.board[y][x+1]:
                    acc = acc + 1
                    last_token = self.board[y][x + 1]
                    x = x + 1
                else:
                    break
            # removes the amount of spaces to the right that the iterator moved
            x = x - acc
            while x > 0 and last_token == self.board[y][x-1]:
                if token == self.board[y][x-1]:
                    acc = acc + 1
                    last_token == self.board[y][x - 1]
                    x = x - 1
                else:
                    break
            # if the accumulator reaches 3, then there are 4 of the same token in a row and thus a player has
            # won the game
            if acc >= 3:
                return True
        # Vertical Case
        if dx == 0 and dy == 1:
            acc = 0
            while y < self.h - 1 and last_token == self.board[y+1][x]:
                if token == self.board[y+1][x]:
                    acc = acc + 1
                    last_token = self.board[y+1][x]
                    y = y + 1
                else:
                    break
            y = y - acc
            while y > 0 and last_token == self.board[y-1][x]:
                if token == self.board[y-1][x]:
                    acc = acc + 1
                    last_token = self.board[y - 1][x]
                    y = y - 1
                else:
                    break
            if acc >= 3:
                return True
        # Diagonal Up Case
        if dx == 1 and dy == 1:
            acc = 0
            while self.w - 1 > x >= 0 and self.h - 1 > y >= 0 and last_token == self.board[y+1][x+1]:
                if token == self.board[y+1][x+1]:
                    acc = acc + 1
                    last_token = self.board[y+1][x+1]
                    x = x + 1
                    y = y + 1
                else:
                    break
            if acc >= 3:
                return True
        # Diagonal Down Case
        if dx == 1 and dy == -1:
            acc = 0
            while self.w - 1 > x > 0 and self.h - 1 >= y > 0 and last_token == self.board[y - 1][x + 1]:
                if token == self.board[y - 1][x + 1]:
                    acc = acc + 1
                    last_token == self.board[y - 1][x + 1]
                    x = x + 1
                    y = y - 1
                else:
                    break
            if acc >= 3:
                return True
            else:
                return False
        else:
            return False

    def isAnyLineAt(self, x, y):
        """Return True if a line of identical symbols exists starting at (x,y)
           in any direction"""
        return (self.isLineAt(x, y, 1, 0) or # Horizontal
                self.isLineAt(x, y, 0, 1) or # Vertical
                self.isLineAt(x, y, 1, 1) or # Diagonal up
                self.isLineAt(x, y, 1, -1)) # Diagonal down

    def getOutcome(self):
        """Returns the winner of the game: 1 for Player 1, 2 for Player 2, and
           0 for no winner"""
        y = 0
        winner = 0
        # Double for loop checks if each token on the board has a line of the same tokens horizontally, vertically
        # or diagonally
        for line in self.board:
            x = 0
            for token in line:
                if self.isAnyLineAt(x, y) and token > 0:
                    winner = token
                x = x + 1
            y = y + 1
        return winner


    def printOutcome(self):
        """Prints the winner of the game"""
        o = self.getOutcome()
        if o == 0:
            print("No winner")
        else:
            print("Player", o, " won")
