import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize the board
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Function to draw the board
def draw_board():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw X or O on the board
def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 150)
    text = font.render(symbol, True, LINE_COLOR)
    text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
    screen.blit(text, text_rect)

# Function to check for a winner
def check_winner():
    # Check rows and columns
    for i in range(BOARD_SIZE):
        if all(board[i][j] == 'X' for j in range(BOARD_SIZE)) or all(board[j][i] == 'X' for j in range(BOARD_SIZE)):
            return 'X'
        if all(board[i][j] == 'O' for j in range(BOARD_SIZE)) or all(board[j][i] == 'O' for j in range(BOARD_SIZE)):
            return 'O'

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == 'X' for i in range(BOARD_SIZE)):
        return 'X'
    if all(board[i][i] == 'O' for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == 'O' for i in range(BOARD_SIZE)):
        return 'O'

    return None

# Function to check if the board is full
def is_board_full():
    return all(board[i][j] != ' ' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

# Main game loop
current_player = 'X'
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == ' ':
                board[clicked_row][clicked_col] = current_player

                winner = check_winner()
                if winner:
                    print(f"Player {winner} wins!")
                    game_over = True
                elif is_board_full():
                    print("It's a draw!")
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    screen.fill(WHITE)
    draw_board()

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] != ' ':
                draw_symbol(row, col, board[row][col])

    pygame.display.flip()
