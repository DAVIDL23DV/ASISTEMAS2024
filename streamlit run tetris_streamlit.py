import pygame
import streamlit as st
import numpy as np
import time

# Configuración del juego
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # Cyan
    (0, 0, 255),    # Blue
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (255, 0, 0),    # Red
    (128, 0, 128)   # Purple
]

# Piezas de Tetris
SHAPES = [
    np.array([[1, 1, 1, 1]]),
    np.array([[1, 1, 1], [0, 1, 0]]),
    np.array([[1, 1], [1, 1]]),
    np.array([[1, 1, 0], [0, 1, 1]]),
    np.array([[0, 1, 1], [1, 1, 0]]),
    np.array([[1, 1, 1], [1, 0, 0]]),
    np.array([[1, 1, 1], [0, 0, 1]])
]

class Tetris:
    def __init__(self):
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
        self.current_piece = self.new_piece()
        self.piece_position = [0, GRID_WIDTH // 2 - 1]
        self.game_over = False

    def new_piece(self):
        return SHAPES[np.random.randint(len(SHAPES))]

    def rotate_piece(self):
        self.current_piece = np.rot90(self.current_piece)

    def check_collision(self, offset=(0, 0)):
        off_y, off_x = offset
        piece_h, piece_w = self.current_piece.shape
        for y in range(piece_h):
            for x in range(piece_w):
                if self.current_piece[y, x]:
                    if (
                        y + self.piece_position[0] + off_y >= GRID_HEIGHT
                        or x + self.piece_position[1] + off_x < 0
                        or x + self.piece_position[1] + off_x >= GRID_WIDTH
                        or self.grid[y + self.piece_position[0] + off_y, x + self.piece_position[1] + off_x]
                    ):
                        return True
        return False

    def merge_piece(self):
        piece_h, piece_w = self.current_piece.shape
        for y in range(piece_h):
            for x in range(piece_w):
                if self.current_piece[y, x]:
                    self.grid[y + self.piece_position[0], x + self.piece_position[1]] = self.current_piece[y, x]
        self.clear_lines()
        self.current_piece = self.new_piece()
        self.piece_position = [0, GRID_WIDTH // 2 - 1]
        if self.check_collision():
            self.game_over = True

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        if lines_to_clear:
            self.grid = np.delete(self.grid, lines_to_clear, axis=0)
            new_rows = np.zeros((len(lines_to_clear), GRID_WIDTH), dtype=int)
            self.grid = np.vstack((new_rows, self.grid))

    def move_piece(self, direction):
        if not self.check_collision((0, direction)):
            self.piece_position[1] += direction

    def drop_piece(self):
        if not self.check_collision((1, 0)):
            self.piece_position[0] += 1
        else:
            self.merge_piece()

    def hard_drop(self):
        while not self.check_collision((1, 0)):
            self.piece_position[0] += 1
        self.merge_piece()

    def update(self):
        self.drop_piece()

    def render(self, screen):
        screen.fill(BLACK)
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y, x]:
                    pygame.draw.rect(screen, COLORS[self.grid[y, x] - 1], pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        piece_h, piece_w = self.current_piece.shape
        for y in range(piece_h):
            for x in range(piece_w):
                if self.current_piece[y, x]:
                    pygame.draw.rect(screen, COLORS[self.current_piece[y, x] - 1], pygame.Rect((x + self.piece_position[1]) * BLOCK_SIZE, (y + self.piece_position[0]) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def main():
    st.title("Tetris Game")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    tetris = Tetris()

    while not tetris.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tetris.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetris.move_piece(-1)
                elif event.key == pygame.K_RIGHT:
                    tetris.move_piece(1)
                elif event.key == pygame.K_DOWN:
                    tetris.drop_piece()
                elif event.key == pygame.K_UP:
                    tetris.rotate_piece()
                elif event.key == pygame.K_SPACE:
                    tetris.hard_drop()

        tetris.update()
        tetris.render(screen)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    st.write("Game Over!")

if __name__ == "__main__":
    st.button("Start Tetris", on_click=main)
