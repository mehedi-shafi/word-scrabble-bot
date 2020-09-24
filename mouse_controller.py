import pyautogui
from const import WINDOW_LOC

def getPath(node1, node2):
    print(f'from {node1.center} to {node2.center}')
    path = []
    if node1.position[0] == node2.position[0] or node1.position[1] == node2.position[1]:
        # horizontal or vertical
        path.append((node2.center[0] - node1.center[0], 0))
        path.append((0, node2.center[1] - node1.center[1]))
    else:
        path.append((node2.center[0] - node1.center[0], node2.center[1] - node1.center[1]))
    return path

def imitateMoveX(path, xp, yp):
    from time import sleep
    
    print(path[0].__repr__())
    pyautogui.moveTo(xp, yp, .02, pyautogui.easeInOutQuad)
    pyautogui.move(path[0].center[0], 0, 0.05,  pyautogui.easeInOutQuad)
    pyautogui.move(0, path[0].center[1], 0.05,  pyautogui.easeInOutQuad)

    pyautogui.mouseDown()

    for i in range(1, len(path)):
        print(path[i].__repr__())
        p = getPath(path[i-1], path[i])
        for (x, y) in p:
            pyautogui.move(x, y, .05, pyautogui.easeInOutQuad)
    
    pyautogui.mouseUp()
    sleep(0.5)

if __name__ == '__main__':
    import pickle
    from scrabble import ScrabbleSolver
    with open('sample_board.dat', 'rb') as file:
        board = pickle.load(file)
    solver = ScrabbleSolver()
    paths = solver.validateByLocation(board, ['TOYEE'])

    from models import Letter
    # a = Letter('a', (0, 0, 50, 50))
    # b = Letter('b', (40, 0, 90, 50))
    # c = Letter('c', (40, 180, 90, 230))
    # d = Letter('d', (0, 180, 50, 230))
    # e = Letter('e', (350, 350, 400, 400))

    # imitateMoveX([a, e, c, d, b], 2653, 137)
    # imitateMoveX([a, b, c, d, e], 2653, 137)


    # imitateMoveX(paths['TOYS'], *WINDOW_LOC['top_left'])
    imitateMoveX(paths['TOYEE'], 2653, 137)
