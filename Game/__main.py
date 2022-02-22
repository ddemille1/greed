# from game.shared.color import Color


# FRAME_RATE = 12
# MAX_X = 900
# MAX_Y = 600
# CELL_SIZE = 15
# FONT_SIZE = 15
# COLS = 60
# ROWS = 40
# CAPTION = "Greed"
# #DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
# WHITE = Color(255, 255, 255)
# #DEFAULT_ARTIFACTS = 40

# def main():



import pyray

class Game:
    def __init__(self):
        pass

    def run(self):
        # Set up the window
        pyray.init_window(800, 450, "Greed")
        pyray.set_target_fps(60)

        # Main loop
        while not pyray.window_should_close():
            pyray.begin_drawing()
            pyray.clear_background(pyray.RAYWHITE)
            # original: pyray.draw_text("Congrats!  You created your first window!", 190, 200, 20, pyray.BLACK)
            pyray.draw_text("Score: (variable goes here)", 10, 10, 20, pyray.BLACK)

            pyray.end_drawing()

        # clean up
        pyray.close_window()

if __name__ == '__main__':
    game = Game()
    game.run()