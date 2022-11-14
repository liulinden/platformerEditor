"""
game codes: 
200%0%0%0%50%50%6%100%0%50%50%/
545%4%-1505%-1922%292%20%1%-1530%-1133%367%167%1%-1715%-1843%79%40%1%-1907%-1583%103%40%1%-1913%-1413%102%40%1%-1711%-1312%127%40%1%-1918%-1181%99%40%1%-1705%-1090%75%40%1%-1905%-977%73%40%1%-1340%-618%793%107%1%1752%509%199%854%1%1355%476%204%829%2%1537%-118%231%564%0%13%4%50%50%1%-43%69%158%1039%1%404%-36%156%1152%1%795%149%329%120%4%1070%-11%195%20%1%1355%-161%204%749%1%1752%-422%200%999%4%1418%-570%343%20%4%1164%-712%400%20%4%766%-855%546%20%5%1436%-218%50%50%5%1818%-487%50%50%5%-133%-1030%50%50%1%-267%-972%864%209%3%-1182%-656%597%78%1%-608%-723%169%212%1%-1213%-723%79%194%1%-1695%-778%497%267%4%-944%-701%91%20%4%-1890%-845%138%20%1%-2043%-1711%158%898%1%-1658%-1937%168%971%5%-1853%-905%50%50%1%-1231%-2324%165%1358%5%-1587%-1991%50%50%6%-1424%-1194%50%50%1%-1231%-3192%166%987%/
536%4%-1505%-1922%292%20%1%-1530%-1133%367%167%1%-1715%-1843%79%40%1%-1907%-1583%103%40%1%-1913%-1413%102%40%1%-1711%-1312%127%40%1%-1918%-1181%99%40%1%-1705%-1090%75%40%1%-1905%-977%73%40%1%-1340%-618%793%107%1%1752%509%199%854%1%1355%476%204%829%2%1537%-118%231%564%0%21%-37%50%50%1%-43%69%158%1039%1%404%-36%156%1152%1%795%149%329%120%4%1070%-11%195%20%1%1355%-161%204%749%1%1752%-422%200%999%4%1418%-570%343%20%4%1164%-712%400%20%4%766%-855%546%20%5%1436%-218%50%50%5%1818%-487%50%50%5%-133%-1030%50%50%1%-267%-972%864%209%3%-1182%-656%597%78%1%-608%-723%169%212%1%-1213%-723%79%194%1%-1695%-778%497%267%4%-944%-701%91%20%4%-1890%-845%138%20%1%-2043%-1711%158%898%1%-1658%-1937%168%971%5%-1853%-905%50%50%5%-1587%-1991%50%50%6%-1389%-1177%50%50%6%-1350%-1178%50%50%6%-1306%-1178%50%50%6%-1265%-1173%50%50%6%-1419%-1178%50%50%6%-1454%-1178%50%50%6%-1495%-1178%50%50%1%-1271%-3104%105%1881%5%-1404%-1169%50%50%/

editing:
e - switch in/out of editing mode
WASD - scroll screen
up/down arrows - switch platform type
click - (de)select platform
drag - create platform / (when platform selected) move platform
shift drag - create platform
delete/backspace - (when platform selected) delete platform
f - (when platform selected) move platform to front/back
space - (when checkpoint selected) set checkpoint
"""

#import and set up libraries
import pygame, sys
pygame.init()

#colors
playerColor = (245, 66, 66)
brightGreen = (219, 255, 176)
lightGreen = (51, 224, 74)
darkGreen = (14, 191, 67)
water = (5, 70, 170)
lightWater = (5, 120, 160)
brightWater = (165, 235, 242)
wood = (186, 108, 63)
brightWood = (255, 238, 199)
sky = (70, 192, 250)
lava = (230, 60, 30)
lightLava = (250,100,30)
guiColor = (50,50,50)

#set up clock/window/surfaces
c = pygame.time.Clock()
#xDim, yDim = int(input("How wide would you like the screen? ")), int(input("How tall would you like the screen? "))
xDim, yDim = 1000, 700
w = pygame.display.set_mode([xDim, yDim])
pygame.display.set_caption("gamee")
flashAlpha = 0
gameAlpha = 0
flashSurface = pygame.Surface((xDim, yDim))
guiSurface = pygame.Surface((xDim, 100))
gameSurface = pygame.Surface((xDim, yDim))
guiSurface.fill((guiColor))
flashSurface.fill((255,255,255))
gameSurface.fill(lightGreen)
guiSurface.set_alpha(235)
timeSinceWin = 0

#set up text
class EasedFont:
    def __init__(self,text,color,size,x,y):
        font = pygame.font.Font("FredokaOne-Regular.ttf", size)
        self.txt = font.render(text,True, color)
        self.rect = self.txt.get_rect()
        self.rect.center = (x,y)
    def draw(self, surface):
        surface.blit(self.txt,self.rect)
text = [EasedFont("YOU WIN",brightGreen,100,xDim//2,yDim//2)]
#[EasedFont("YOU WIN",darkGreen,100,xDim//2+7,yDim//2-7),EasedFont("YOU WIN",darkGreen,100,xDim//2+7,yDim//2+7),EasedFont("YOU WIN",darkGreen,100,xDim//2-7,yDim//2+7),EasedFont("YOU WIN",darkGreen,100,xDim//2-7,yDim//2-7),EasedFont("YOU WIN",brightGreen,100,xDim//2,yDim//2)]

#platform class
class Platform:

    #initialize platform
    def __init__(self, type, x, y, length, height, selectable=False):
        global scrollX, scrollY

        #create platform
        self.x = x
        self.y = y
        self.type = type
        self.length = length
        self.height = height
        self.selectable = selectable
        if type == "wood":
            self.collisionRect = pygame.Rect(x, y, length, 10)
        elif type == "checkpoint":
            self.collisionRect = pygame.Rect(x, y, playerSize, playerSize)
        else:
            self.collisionRect = pygame.Rect(x, y, length, height)
        self.selected = True

        #visible appearances
        self.drawRects = []

        #ground
        if type == "ground":
            self.drawRects.append([pygame.Rect(x, y, length, height), darkGreen, 0, 0])
            self.drawRects.append([pygame.Rect(x, y, length, 40), lightGreen, 0, 0])
            self.drawRects.append([pygame.Rect(x, y, length, 7), brightGreen, 0, 0])

        #lava
        elif type == "lava":
            self.drawRects.append([pygame.Rect(x, y, length, height), lava, 0, 0])
            self.drawRects.append([pygame.Rect(x, y, length, 20), lightLava, 0, 0])
            self.drawRects.append([pygame.Rect(x, y, length, 5), (255,255,255), 0, 0])
        
        #water
        elif type == "water":
            self.drawRects.append([pygame.Rect(x, y, length, height), water, 0, 0])
            self.drawRects.append([pygame.Rect(x, y, length, 30), lightWater, 0, 0])
            self.drawRects.append([pygame.Rect(x, y, length, 5), brightWater, 0, 0])
        
        #wood
        elif type == "wood":
            self.drawRects.append([pygame.Rect(x, y, length, 10), wood, 0, 0])
            self.drawRects.append([pygame.Rect(x, y, length, 5), lightGreen, 0, 0])
        
        #checkpoint
        elif type == "checkpoint":
            self.drawRects.append([pygame.Rect(x, y, playerSize, playerSize), lightGreen, 0, 0])
        
        #start checkpoint
        elif type == "start":
            self.drawRects.append([pygame.Rect(x, y, playerSize, playerSize), (255, 255, 255), 0, 0])
        
        #end checkpoint
        elif type == "end":
            self.drawRects.append([pygame.Rect(x, y, length, height), (0, 0, 0), 0, 0])

        #update position
        self.updatePosition(scrollX, scrollY)

    #update platform position to scroll position
    def updatePosition(self, scrollx, scrolly):
        
        #update collision rectangle
        self.collisionRect.x = self.x - scrollx
        self.collisionRect.y = self.y - scrolly

        #update appearance position
        for drawRect in self.drawRects:
            drawRect[0].x = self.collisionRect.x + drawRect[2]
            drawRect[0].y = self.collisionRect.y + drawRect[3]

    #draw platform
    def draw(self, window):
        global editing

        #draw platform
        if editing or not (self.type == "checkpoint" or self.type == "start" or self.type == "end"):
            if not self.selectable and self.type == "water":
                s = pygame.Surface((self.collisionRect.width,self.collisionRect.height))
                s.set_alpha(150)
                for rect in self.drawRects:
                    pygame.draw.rect(s, rect[1], pygame.Rect(0,0,rect[0].width,rect[0].height))
                window.blit(s, (self.collisionRect.x,self.collisionRect.y))
            elif not self.selectable and self.type == "checkpoint" or self.type == "start" or self.type == "end":
                s = pygame.Surface((self.collisionRect.width,self.collisionRect.height))
                s.set_alpha(180)
                for rect in self.drawRects:
                    pygame.draw.rect(s, rect[1], pygame.Rect(0,0,rect[0].width,rect[0].height))
                window.blit(s, (self.collisionRect.x,self.collisionRect.y))
            else:
                for rect in self.drawRects:
                    pygame.draw.rect(window, rect[1], rect[0])
        
        #draw selection outline
        if self.selectable:
            if self.selected:
                pygame.draw.rect(window, (255, 255, 255), self.collisionRect, 2)
            else:
                pygame.draw.rect(window, (0, 0, 0), self.collisionRect, 2)
        else:
            if self.selected:
                pygame.draw.rect(window, (255, 255, 255), self.collisionRect, 2)


#platform group class
class PlatformGroup:

    #initialize group
    def __init__(self):
        self.platforms = []

    #add platform to group at top layer
    def add(self, platform):
        self.platforms.append(platform)

    #remove platform from group
    def delete(self, platform):
        if platform.type != "start":
            self.platforms.remove(platform)

    #move a platform to front layer
    def moveToFront(self, platform):
        self.delete(platform)
        self.add(platform)

    #move a platform to back layer
    def moveToBack(self, platform):
        self.delete(platform)
        self.platforms.insert(0, platform)
    
    #move selected platform
    def moveSelected(self, changex, changey):
        global scrollX, scrollY

        #find selected platform
        for platform in self.platforms:
            if platform.selected:

                #move platform
                platform.x += changex
                platform.y += changey
                if platform.type == "start":
                    player.checkpointX, player.checkpointY = platform.x, platform.y
                platform.updatePosition(scrollX, scrollX)

    #update positions of platforms, move/delete selected platforms
    def updatePlatforms(self, scrollx, scrolly):
        global deleteKey, fTap

        #find selected platform
        for platform in self.platforms:
            if platform.selected:
                
                #delete platform
                if deleteKey:
                    self.delete(platform)
                
                #change platform layer
                elif fTap:
                    if self.platforms.index(platform) == len(self.platforms) - 1:
                        self.moveToBack(platform)
                    else:
                        self.moveToFront(platform)
                break
        
        #update platform positions to scroll position
        for platform in self.platforms:
            platform.updatePosition(scrollx, scrolly)
    
    #unselect all platforms
    def unselectAll(self):
        for platform in self.platforms:
            platform.selected = False

#player class
class Player():

    #initialize player
    def __init__(self, x, y, playerSize, color, checkpointx=0, checkpointy=0):
        self.x = x
        self.y = y
        self.checkpointX = checkpointx
        self.checkpointY = checkpointy
        self.selected = False
        self.xspeed = 0
        self.yspeed = 0
        self.color = color
        self.rect = pygame.Rect(x,y,playerSize,playerSize)
    
    #draw player
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
    
    #reset player
    def reset(self, cause="reset"):

        #reset player variables
        self.x = self.checkpointX
        self.y = self.checkpointY
        self.xspeed = 0
        self.yspeed = 0

        #flash screen
        flashScreen(cause)

    #update player rect position
    def updatePosition(self):
        global scrollX, scrollY
        self.rect.x = self.x - scrollX
        self.rect.y = self.y - scrollY

    #check for collisions
    def checkCollisions(self, collisions):
        for platform in collisions:
            if self.rect.colliderect(platform):
                return True
        return False

    #return collision list from string
    def getCollisions(self, collisionType):
        global collisions, platformTypes
        return collisions[platformTypes.index(collisionType)]

    #return coordinates of collided platform
    def getCollisionPos(self, collisions):
        global scrollX, scrollY
        for platform in collisions:
            if self.rect.colliderect(platform):
                return [platform.x + scrollX, platform.y + scrollY]
        return 

    #move player horizontally
    def moveHor(self):

        #steps
        for i in range(round(abs(self.xspeed))):

            #take step
            if self.xspeed > 0:
                self.x += 1
            else:
                self.x -= 1

            #check for collision
            self.updatePosition()
            if self.checkCollisions(self.getCollisions("ground")):

                #take back step
                if self.xspeed > 0:
                    self.x -= 1
                else:
                    self.x += 1
                
                #reset speed
                self.xspeed = 0

                break
    
    #move player vertically
    def moveVert(self, up, down):
        global collisions

        #steps
        for i in range(round(abs(self.yspeed))):

            #take step
            if self.yspeed > 0:
                self.y += 1
            else:
                self.y -= 1
            
            #check for collision
            self.updatePosition()
            if self.checkCollisions(self.getCollisions("ground")):

                #take back step
                if self.yspeed > 0:
                    self.y -= 1

                    if up:

                        #jump
                        self.yspeed = -9
                        break
                else:
                    self.y += 1
                
                #reset speed
                self.yspeed = 0

                break

            #check for alternate collision with wood platform type
            elif self.checkCollisions(self.getCollisions("wood")) and not (down and not up):
                
                #take back step
                if self.yspeed > 0:
                    self.y -= 1

                    #check for continued collision
                    self.updatePosition()
                    if self.checkCollisions(self.getCollisions("wood")):

                        #take step again
                        self.y += 1

                    else:

                        #jump/reset speed
                        if up:
                            self.yspeed = -9
                        else:
                            self.yspeed = 0
                        
                        break
    
    #player physics
    def playerEngine(self, left, right, up, down, gravity, friction, floating):
        global collisions, gameOver, bottomLimit, playerSize

        #death on lava collision
        if self.checkCollisions(self.getCollisions("lava")) or self.y > bottomLimit-(playerSize):
            self.reset("death")
            return()
        
        #checkpoint
        if self.checkCollisions(self.getCollisions("checkpoint")):
            if not [self.checkpointX, self.checkpointY] == self.getCollisionPos(self.getCollisions("checkpoint")):
                self.checkpointX = self.getCollisionPos(self.getCollisions("checkpoint"))[0]
                self.checkpointY = self.getCollisionPos(self.getCollisions("checkpoint"))[1]
                flashScreen("checkpoint")

        #make movements
        self.moveHor()
        self.moveVert(up, down)
        self.updatePosition()

        #check if in water
        if self.checkCollisions(self.getCollisions("water")):

            #water player movements
            if right:
                self.xspeed += 0.1
                self.yspeed -= 0.1
            if left: 
                self.xspeed -= 0.1
                self.yspeed -= 0.1
            if up:
                self.yspeed -= 0.2
            if down:
                self.yspeed += 0.3
            
            #surface water physics
            for i in range(int(playerSize)):
                self.rect.y -= 1
                if not self.checkCollisions(self.getCollisions("water")):
                    break
            self.rect.y += i
            self.yspeed += floating * ((playerSize-(2*(i)))/playerSize)
            
            #water resistance
            self.xspeed *= 0.98
            self.yspeed *= 0.98

        else:

            #player movements
            if right:
                self.xspeed += 0.25
            if left:
                self.xspeed -= 0.25
            
            #gravity/friction
            self.yspeed += gravity
            self.xspeed *= friction
        
        #gameover
        if self.checkCollisions(self.getCollisions("end")):
            gameOver = True

    #dragged move
    def move(self, changex, changey):
        self.x += changex
        self.y += changey
        self.updatePosition()



#update collision rect lists
def updateCollisions(platformlist):
    global collisions, platformTypes
    collisions = []
    for i in range(len(platformTypes)):
        collisions.append([])
        for platform in platformlist:
            if platform.type == platformTypes[i]:
                collisions[i].append(platform.collisionRect)


#save code creator
def createLevelSave(level):
    global allPlatformTypes, bottomLimit
    save = ""

    #add bottom bound to code
    save += str(int(bottomLimit)) + "%"

    #add platforms to code
    for platform in level.platforms:
        save += str(allPlatformTypes.index(platform.type)) + "%" + str(int(platform.x)) + "%" + str(int(platform.y)) + "%" + str(int(platform.length)) + "%" + str(int(platform.height)) + "%"
    save += "/"

    #return code
    return save

#save code converter
def convertSave(code):
    global platforms, allPlatformTypes, bottomLimit

    #convert code  
    platforms.platforms = []
    i = 0
    arg = ""
    while code[i] != '%':
        arg += code[i]
        i += 1
    i += 1
    bottomLimit = int(arg)
    while code[i] != '/':
        args = []
        for j in range(5):
            arg = ""
            while code[i] != '%':
                arg += code[i]
                i+=1
            args.append(arg)
            i += 1
        platforms.add(Platform(allPlatformTypes[int(args[0])], int(args[1]), int(args[2]), int(args[3]), int(args[4])))
        if allPlatformTypes[int(args[0])] == "start":
            player.checkpointX = int(args[1])
            player.checkpointY = int(args[2])
            player.reset()
    platforms.unselectAll()

#gui
def doGui(window):
    global platformTypes, scrollX,scrollY, selecting, selectedType, initx, inity
    guiSurface.fill(guiColor)
    for i in range(len(platformTypes)):
        drawing = Platform(platformTypes[i],scrollX + 10 + (i * 100), scrollY + 10, 80, 80, True)
        if selecting:
            if Platform(platformTypes[i],scrollX + 10 + (i * 100), scrollY + 10 + yDim - 100, 80, 80).collisionRect.collidepoint(initx-scrollX,inity-scrollY):
                selectedType = platformTypes.index(drawing.type)
        if drawing.type != platformTypes[selectedType]:
            drawing.selected = False
        drawing.draw(guiSurface)
    selecting = False
    window.blit(guiSurface,(0,600))

#render screen
def renderScreen(window):
    global flashAlpha, gameAlpha, editing, timeSinceWin, text, darkGreen, sky, lava, bottomLimit

    #clear window
    window.fill(sky)

    if not editing:
        player.draw(window)

    #draw platforms
    for platform in platforms.platforms:
        platform.draw(window)

    #draw editing platform
    for rect in createRect:
        rect.draw(window)
    
    #draw bottom limit
    s = pygame.Surface((xDim, 5))
    s.fill(lava)
    s.set_alpha(150)
    window.blit(s,(0,bottomLimit-scrollY))

    #draw player
    if editing:
        player.draw(window)

    #draw gui
    if editing:
        doGui(window)

    #draw flash
    if flashAlpha > 0:
        flashSurface.set_alpha(flashAlpha)
        window.blit(flashSurface,(0,0))
        flashAlpha -= 2

    #draw game screen
    if gameAlpha > 0 and not editing:
        gameSurface.set_alpha(gameAlpha)
        pygame.draw.rect(gameSurface,darkGreen,pygame.Rect(0,250,1000,200))
        for txt in text:
            txt.draw(gameSurface)
        window.blit(gameSurface,(0,0))
        if timeSinceWin > 200:
            gameAlpha -= 2

    #update screen
    pygame.display.flip()

#screen flash
def flashScreen(cause):
    global flashAlpha
    if cause == "reset":
        flashSurface.fill((255,255,255))
    if cause == "death":
        flashSurface.fill((255,0,0))
    if cause == "checkpoint":
        flashSurface.fill((0,255,0))
    flashAlpha = 120

#set up platform creator
createRect = []
platformTypes = ["ground", "water", "lava", "wood", "checkpoint", "end"]
allPlatformTypes = ["start","ground", "water", "lava", "wood", "checkpoint", "end"]
selectedType = 0

#set up player
playerSize = 50
player = Player(0, 0, playerSize, playerColor)

#scroll position
scrollX = -xDim/2+playerSize/2
scrollY = -yDim/2+playerSize/2

#set up platforms
platforms = PlatformGroup()
platforms.add(Platform("start",0,0,playerSize,playerSize))
platforms.add(Platform("end",100,0,playerSize,playerSize))
platforms.unselectAll()
collisions = [[],[],[]]

#floor of world
bottomLimit = 200
bottomLimitSelected = False

#inputs
shiftKey = False
upKey = False
downKey = False
rightKey = False
leftKey = False
spaceKey = False
wKey = False
aKey = False
sKey = False
dKey = False
deleteKey = False
fTap = False
mouseDown = False

#mouse variables
initx = 0
inity = 0
mousex = 0
mousey = 0

#booleans
editing = True
dragging = False
gameOver = False
selecting = False

#game loop
while True:

    #editor
    if editing:
        
        #get inputs
        fTap = False
        for event in pygame.event.get():
            
            #quit game
            if event.type == pygame.QUIT:
                sys.exit()

            #key down inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shiftKey = True
                if event.key == pygame.K_UP:
                    upKey = True
                    selectedType = (selectedType + 1) % len(platformTypes)
                if event.key == pygame.K_DOWN:
                    downKey = True
                    selectedType = (selectedType - 1) % len(platformTypes)
                if event.key == pygame.K_RIGHT:
                    rightKey = True
                if event.key == pygame.K_SPACE:
                    spaceKey = True
                if event.key == pygame.K_LEFT:
                    leftKey = True
                if event.key == pygame.K_w:
                    wKey = True
                if event.key == pygame.K_a:
                    aKey = True
                if event.key == pygame.K_s:
                    sKey = True
                if event.key == pygame.K_d:
                    dKey = True
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    deleteKey = True
                if event.key == pygame.K_e:
                    gameOver = False
                    gameAlpha = 0
                    timeSinceWin = 0
                    createRect = []
                    dragging = False
                    player.selected = False
                    bottomLimitSelected = False
                    for i in range(len(platforms.platforms) - 1, -1, -1):
                        if platforms.platforms[i].selected == True:
                            platforms.platforms[i].selected = False
                            if platforms.platforms[i].type == "start":
                                player.checkpointX = platforms.platforms[i].x
                                player.checkpointY = platforms.platforms[i].y
                                flashScreen("checkpoint")
                    editing = not editing
                    updateCollisions(platforms.platforms)
                if event.key == pygame.K_f:
                    fTap = True
                if event.key == pygame.K_p:
                    if input("Would you like to input a save code? (y/n) ") == "y":
                        convertSave(input("Input your save code: "))
                if event.key == pygame.K_o:
                    print("Here's your savecode:\n", createLevelSave(platforms))
            
            #key up inputs
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shiftKey = False
                if event.key == pygame.K_UP:
                    upKey = False
                if event.key == pygame.K_DOWN:
                    downKey = False
                if event.key == pygame.K_RIGHT:
                    rightKey = False
                if event.key == pygame.K_LEFT:
                    leftKey = False
                if event.key == pygame.K_w:
                    wKey = False
                if event.key == pygame.K_a:
                    aKey = False
                if event.key == pygame.K_s:
                    sKey = False
                if event.key == pygame.K_d:
                    dKey = False
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    deleteKey = False

            #mouse down
            if event.type == pygame.MOUSEBUTTONDOWN and editing:

                #get mouse position
                initx, inity = pygame.mouse.get_pos()
                initx += scrollX
                inity += scrollY

                #gui
                if pygame.Rect(0, yDim-100, xDim, 100).collidepoint(initx-scrollX, inity-scrollY):
                    selecting = True
                    platforms.unselectAll()
                
                #platform building
                else:
                    #update mouse status
                    mouseDown = True

                    if shiftKey:
                        tv = False
                    else:
                        tv = True
                    tv2 = True

                    #select player
                    if player.rect.collidepoint(initx-scrollX, inity-scrollY):
                        player.selected = True
                        bottomLimitSelected = False
                        tv = False
                    elif pygame.Rect(0,bottomLimit-scrollY,xDim,5).collidepoint(initx-scrollX, inity-scrollY):
                        bottomLimitSelected = True
                        player.selected = False
                        tv = False

                    #select platforms
                    for i in range(len(platforms.platforms) - 1, -1, -1):
                        if platforms.platforms[i].collisionRect.collidepoint(initx-scrollX, inity-scrollY) and tv:
                            platforms.platforms[i].selected = True
                            tv = False
                            player.selected = False
                            bottomLimitSelected = False
                        elif platforms.platforms[i].selected:
                            platforms.platforms[i].selected = False
                            tv2 = False

                    #start drag
                    if tv2 and (tv or shiftKey):
                        dragging = True

            #mouse up
            if event.type == pygame.MOUSEBUTTONUP and editing:
                mouseDown = False

                #end drag
                if dragging:
                    dragging = False

                    #create platform
                    createRect[0].selected = False
                    platforms.add(createRect[0])

        #scroll screen
        if wKey:
            scrollY -= 3
        if sKey:
            scrollY += 3
        if aKey:
            scrollX -= 3
        if dKey:
            scrollX += 3
        
        #set checkpoint
        if spaceKey:
            for i in range(len(platforms.platforms) - 1, -1, -1):
                if platforms.platforms[i].selected == True:
                    if platforms.platforms[i].type == "checkpoint" or platforms.platforms[i].type == "start":
                        player.checkpointX = platforms.platforms[i].x
                        player.checkpointY = platforms.platforms[i].y
                        flashScreen("checkpoint")
        spaceKey = False

        #create image of new platform
        if dragging and editing:

            #get mouse position
            mousex, mousey = pygame.mouse.get_pos()
            mousex += scrollX
            mousey += scrollY

            #image of new platform
            if selectedType == platformTypes.index("wood"):
                createRect = [Platform(platformTypes[selectedType], min(initx,mousex), inity-5, max(abs(mousex - initx), 30), 20)]
            elif selectedType == platformTypes.index("checkpoint"):
                createRect = [Platform(platformTypes[selectedType], mousex-25, mousey-25, playerSize, playerSize)]
            else:
                createRect = [Platform(platformTypes[selectedType], min(initx,mousex), min(inity,mousey), max(abs(mousex - initx), 30), max(abs(mousey - inity), 40))]
        
        #remove new platform image
        elif editing:
            createRect = []

            #move platform
            if mouseDown:

                #get mouse pos
                mousex, mousey = pygame.mouse.get_pos()
                mousex += scrollX
                mousey += scrollY

                #change selected platform position
                platforms.moveSelected(mousex - initx, mousey - inity)
                if player.selected:
                    player.move(mousex - initx, mousey - inity)
                if bottomLimitSelected:
                    bottomLimit += mousey - inity

                initx, inity = mousex, mousey


    #game
    else:
        
        #get inputs
        for event in pygame.event.get():
            
            #quit game
            if event.type == pygame.QUIT:
                sys.exit()

            #key down inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shiftKey = True
                if event.key == pygame.K_UP:
                    upKey = True
                if event.key == pygame.K_DOWN:
                    downKey = True
                if event.key == pygame.K_RIGHT:
                    rightKey = True
                if event.key == pygame.K_LEFT:
                    leftKey = True
                if event.key == pygame.K_w:
                    wKey = True
                if event.key == pygame.K_a:
                    aKey = True
                if event.key == pygame.K_s:
                    sKey = True
                if event.key == pygame.K_d:
                    dKey = True
                if event.key == pygame.K_e:
                    editing = not editing
                if event.key == pygame.K_r:
                    player.reset("reset")
            
            #keyup inputs
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shiftKey = False
                if event.key == pygame.K_UP:
                    upKey = False
                if event.key == pygame.K_DOWN:
                    downKey = False
                if event.key == pygame.K_RIGHT:
                    rightKey = False
                if event.key == pygame.K_LEFT:
                    leftKey = False
                if event.key == pygame.K_w:
                    wKey = False
                if event.key == pygame.K_a:
                    aKey = False
                if event.key == pygame.K_s:
                    sKey = False
                if event.key == pygame.K_d:
                    dKey = False
        
        #player
        player.playerEngine(leftKey,rightKey,upKey,downKey, 0.2, 0.94, 0.1)

        #update scroll position
        scrollX += round((player.x - xDim/2 + playerSize/2 - scrollX) / 30)
        scrollY += round((player.y - yDim/2 + playerSize/2 - scrollY) / 30)

        if player.x - scrollX > xDim - 100:
            scrollX = player.x - xDim + 100
        if player.x - scrollX < 40:
            scrollX = player.x - 40
        if player.y - scrollY > yDim - 100:
            scrollY = player.y - yDim + 100
        if player.y - scrollY < 40:
            scrollY = player.y - 40

        #game over
        if gameOver:
            if timeSinceWin == 0:
                if gameAlpha < 200:
                    gameAlpha += 2
                else:
                    gameAlpha += 1
                if gameAlpha >= 255:
                    gameAlpha = 255
                    timeSinceWin += 1
            else:
                timeSinceWin += 1

    #update screen
    platforms.updatePlatforms(scrollX,scrollY)
    player.updatePosition()
    renderScreen(w)

    #tick clock
    c.tick(120)