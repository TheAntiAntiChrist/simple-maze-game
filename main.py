import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])

Done = False
clock = pygame.time.Clock()

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,0,1],
    [1,0,1,1,0,1,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,0,1,1,1,0,1],
    [1,0,1,0,0,1,0,0,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

def drawMaze():
    for x, rows in enumerate(maze):
        for y, columns in enumerate(rows):
            pygame.draw.rect(screen, [255-columns*255,255-columns*255,255-columns*255],[y*60,x*60,60,60],0)

def canMove(direc):
    if direc == 0: #0 is north
        if maze[curPos[1]-1][curPos[0]] == 0:
            return True
        else:
            return False
    if direc == 1: #1 is east
        if maze[curPos[1]][curPos[0]-1] == 0:
            return True
        else:
            return False
    if direc == 2: #2 is south
        if maze[curPos[1]+1][curPos[0]] == 0:
            return True
        else:
            return False
    if direc == 3: #3 is west
        if maze[curPos[1]][curPos[0]+1] == 0:
            return True
        else:
            return False

curPos = [1,1] #inverted y ([1,1] means top left)
destPos = [8,8] #inverted y - bottom right
mazeDrawn = False
while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Done = True
            if event.key == pygame.K_DOWN and canMove(2):
                curPos[1] += 1
            if event.key == pygame.K_UP and canMove(0):
                curPos[1] -= 1
            if event.key == pygame.K_LEFT and canMove(1):
                curPos[0] -= 1
            if event.key == pygame.K_RIGHT and canMove(3):
                curPos[0] += 1

        #if not mazeDrawn:
        #    drawMaze()
        #    mazeDrawn = True

        drawMaze()
        pygame.draw.rect(screen,[0,(255/10)*curPos[0],(255/10)*curPos[1]],[curPos[0]*60,curPos[1]*60,60,60],0)

        #print(maze[curPos[1]][curPos[0]])

        if curPos == destPos:
            print("""
            Maze Complete...
            """)
            Done = True

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
