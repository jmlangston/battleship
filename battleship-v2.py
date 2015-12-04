from random import randint


class Player(object):

	def __init__(self):

		self.name = None
		self.played_turns = 0


class Game(object):

	def __init__(self):

		self.player = None
		# the following 3 attributes can be changed later
		self.board_size = 10
		self.turns_per_game = 5
		self.num_ships = 1

		self.board = []

		# build the game board
		for x in range(self.board_size):
			self.board.append(["O"] * self.board_size)

	def print_board(self):

		for row in self.board:
			print " ".join(row)
		print ""

	def place_ships(self):
		
		ships = []

		for x in range(self.num_ships):
			ship_column = randint(1, len(self.board))
			ship_row = randint(1, len(self.board))
			ship = tuple([ship_row, ship_column])
			ships.append(ship)

		return ships


	def get_player_guess(self):
		"""Returns a valid guess from the player.
		Non-integer guesses and guesses outside of the board are invalid.
		"""

		guess_row = 0
		guess_column = 0

		while guess_row == 0:
			try:
				input_row = int(raw_input("Row: "))
			except ValueError:
				print "Invalid guess. Please enter again"
				continue
			if input_row > len(self.board) or input_row < 0:
				print "Invalid guess. Please enter again"
				continue
			else:
				guess_row = input_row

		while guess_column == 0:
			try:
				input_column = int(raw_input("Column: "))
			except ValueError:
				print "Invalid guess. Please enter again"
				continue
			if input_column > len(self.board) or input_column < 0:
				print "Invalid guess. Please enter again"
				continue
			else:
				guess_column = input_column

		return tuple([guess_row, guess_column])


	def run_game(self, player):

		ships = self.place_ships()
		
		# for debugging
		# print ships, "\n"

		# while turns are left, player guesses
		while player.played_turns < self.turns_per_game:
			
			self.print_board()

			print "This is turn %d of %d" % (player.played_turns + 1, self.turns_per_game)
			print "Guess the ship's location"

			guess = self.get_player_guess()
			guess_row, guess_column = guess[0], guess[1]

			if guess in ships:
				print "Congratulations! You sunk the battleship!"
				return

			else:
				if self.board[guess_row - 1][guess_column - 1] == "X":
					print "You already guessed that location. Try again."
				else:
					print "You missed! Try again."
					self.board[guess_row - 1][guess_column - 1] = "X"
					player.played_turns += 1

			print "You're out of guesses. Game over."


def run_game():

	print """
	Let's play Battleship!
	"""

	game = Game()
	player = Player()

	game.run_game(player)


def main():
	# later - add option to play again

	run_game()


if __name__ == '__main__':
	main()
