import pyray as pr

WINDOW_WIDTH, WINDOW_HEIGHT = (1280, 720)
FPS = 60

COLOR_HEIGHT = (int) (WINDOW_HEIGHT / 6)

pr.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Happy Pride Month!")
pr.set_target_fps(FPS)

while not pr.window_should_close():
    pr.begin_drawing()

    pr.clear_background(pr.BLACK)

    pr.draw_rectangle(0, COLOR_HEIGHT * 0, WINDOW_WIDTH, COLOR_HEIGHT, pr.RED)
    pr.draw_rectangle(0, COLOR_HEIGHT * 1, WINDOW_WIDTH, COLOR_HEIGHT, pr.ORANGE)
    pr.draw_rectangle(0, COLOR_HEIGHT * 2, WINDOW_WIDTH, COLOR_HEIGHT, pr.YELLOW)
    pr.draw_rectangle(0, COLOR_HEIGHT * 3, WINDOW_WIDTH, COLOR_HEIGHT, pr.GREEN)
    pr.draw_rectangle(0, COLOR_HEIGHT * 4, WINDOW_WIDTH, COLOR_HEIGHT, pr.BLUE)
    pr.draw_rectangle(0, COLOR_HEIGHT * 5, WINDOW_WIDTH, COLOR_HEIGHT, pr.VIOLET)

    pr.end_drawing()
pr.close_window()