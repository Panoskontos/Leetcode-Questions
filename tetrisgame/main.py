"""
Implement a Tetris game using Pygame.
"""
import pygame
import random
import time
import sys
import os




def main():
    pygame.init()
    # Define the window size
    window_width = 800
    window_height = 600
    game_board_width = 10
    game_board_height = 20
    block_size = 30
    block_colors = [
    (255, 0, 0), # Red
    (0, 255, 0), # Green
    (0, 0, 255), # Blue
    (255, 255, 0), # Yellow
    (255, 0, 255), # Magenta
    (0, 255, 255), # Cyan
    (255, 255, 255) # White
    ]
    blocks = [
        # I block
        [
            [1, 1, 1, 1]
        ],

        # J block
        [
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 0]
        ],

        # L block
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 1]
        ],

        # O block
        [
            [1, 1],
            [1, 1]
        ],

        # S block
        [
            [0, 1, 1],
            [1, 1, 0]
        ],

        # T block
        [
            [0, 1, 0],
            [1, 1, 1]
        ],

        # Z block
        [
            [1, 1, 0],
            [0, 1, 1]
        ]
    ]
    # Create a new window
    screen = pygame.display.set_mode((window_width, window_height))
    # Set the window title
    pygame.display.set_caption("Tetris")
    # Main game loop
    # Create the game board
    game_board = []
    for row in range(game_board_height):
        game_board.append([0] * game_board_width)

    # Define the current block and its position
    current_block = blocks[0]
    current_block_color = block_colors[0]
    current_block_x = game_board_width // 2 - len(current_block[0]) // 2
    current_block_y = 0

    # Main game loop
    running = True
    clock = pygame.time.Clock()

    fall_time = 0
    fall_speed = 0.5
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the falling time
        fall_time += clock.get_rawtime()
        if fall_time / 1000 >= fall_speed:
            # Move the current block down
            current_block_y += 1
            # Reset the falling time
            fall_time = 0
            # Draw the game board
        for row in range(game_board_height):
            for col in range(game_board_width):
                pygame.draw.rect(screen, (255, 255, 255), (col * block_size, row * block_size, block_size, block_size), 1)
                if game_board[row][col] != 0:
                    pygame.draw.rect(screen, block_colors[game_board[row][col] - 1], (col * block_size, row * block_size, block_size, block_size))

        # Draw the current block
        for row in range(len(current_block)):
            for col in range(len(current_block[0])):
                if current_block[row][col] == 1:
                    pygame.draw.rect(screen, current_block_color, ((current_block_x + col) * block_size, (current_block_y + row) * block_size, block_size, block_size))

        # Update the display
        pygame.display.update()
        # Limit the frame rate
        clock.tick(60)
    # Quit Pygame
    pygame.quit()



if __name__ == "__main__":
    main()

