# Code is generated using ChatGPT
import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 85, 96)
TEXT_COLOR = (255, 255, 255)
MESSAGE_BACKGROUND_COLOR = (0, 0, 0)  # Background color of the message
SPACE = 15
PLAYER_X = 'X'
PLAYER_O = 'O'
player = PLAYER_X
board = [['' for _ in range(3)] for _ in range(3)]

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
font = pygame.font.Font(None, 36)

# Draw the game board
def draw_board():
    screen.fill(BOARD_COLOR)
    # Draw the vertical lines
    pygame.draw.line(screen, LINE_COLOR, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), LINE_WIDTH)
    # Draw the horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), LINE_WIDTH)

# Draw X and O on the board
def draw_markers():
    for row in range(3):
        for col in range(3):
            if board[row][col] == PLAYER_X:
                pygame.draw.line(screen, X_COLOR, (col * WIDTH // 3 + SPACE, row * HEIGHT // 3 + SPACE),
                                 ((col + 1) * WIDTH // 3 - SPACE, (row + 1) * HEIGHT // 3 - SPACE), LINE_WIDTH)
                pygame.draw.line(screen, X_COLOR, ((col + 1) * WIDTH // 3 - SPACE, row * HEIGHT // 3 + SPACE),
                                 (col * WIDTH // 3 + SPACE, (row + 1) * HEIGHT // 3 - SPACE), LINE_WIDTH)
            elif board[row][col] == PLAYER_O:
                pygame.draw.circle(screen, O_COLOR, (col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6),
                                   WIDTH // 6 - SPACE, LINE_WIDTH)

# Check for a winner
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

# Check if the board is full
def is_board_full():
    return all(cell != '' for row in board for cell in row)

# Display a message on the screen with a background rectangle
def display_message(message, text_color):
    # Define message dimensions
    text_surface = font.render(message, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    # Draw the background rectangle
    rect_width = text_rect.width + 20
    rect_height = text_rect.height + 20
    rect_x = text_rect.x - 10
    rect_y = text_rect.y - 10
    pygame.draw.rect(screen, MESSAGE_BACKGROUND_COLOR, (rect_x, rect_y, rect_width, rect_height))
    
    # Draw the text
    screen.blit(text_surface, text_rect)

# Main game loop
def main():
    global player
    draw_board()
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                clicked_row = y // (HEIGHT // 3)
                clicked_col = x // (WIDTH // 3)

                if board[clicked_row][clicked_col] == '':
                    board[clicked_row][clicked_col] = player
                    player = PLAYER_O if player == PLAYER_X else PLAYER_X

                draw_board()
                draw_markers()

                winner = check_winner()
                if winner:
                    display_message(f"Player {winner} wins!", X_COLOR if winner == PLAYER_X else O_COLOR)
                    game_over = True
                elif is_board_full():
                    display_message("It's a tie!", TEXT_COLOR)
                    game_over = True

        pygame.display.update()

if __name__ == "__main__":
    main()
