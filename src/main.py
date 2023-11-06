from render.window import Window
from render.maze import Maze_render
from core.maze import Maze

win = Window(800, 600)
maze = Maze_render(Maze(30, 30),100,5,20,win=win)
win.wait_for_close()
