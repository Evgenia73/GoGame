import math

BOARD_BROWN = (173, 111, 105)
BOARD_WIDTH = 800
BOARD_BORDER = 80
STONE_RADIUS = int(math.sqrt(BOARD_WIDTH * BOARD_WIDTH / math.pi) / 20)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURN_POS = (BOARD_BORDER, 0)
SCORE_POS = (BOARD_BORDER, BOARD_WIDTH - BOARD_BORDER + 30)
TIMER_POS = (BOARD_BORDER, 20)
RES_POS = (BOARD_BORDER + 130, 20)
DOT_RADIUS = 4