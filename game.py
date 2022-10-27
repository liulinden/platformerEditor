"""
game codes: 
lava%214%-1754%30%116%lava%318%-1755%30%116%lava%417%-1755%30%117%ground%2403%-1402%114%40%ground%2394%45%50%844%ground%2089%-41%56%921%water%1832%193%161%672%ground%1073%205%104%666%ground%705%207%113%675%ground%134%306%400%166%lava%-156%-280%30%1178%water%1675%193%313%89%ground%1438%166%240%707%lava%-156%858%2624%40%lava%2343%858%1567%40%ground%2550%-108%270%81%ground%1883%-345%529%88%wood%2505%-236%237%20%wood%1448%-486%519%20%wood%1153%-633%497%20%wood%1526%-780%324%20%wood%1696%-953%678%20%ground%2232%-852%425%140%ground%2404%-1041%97%40%ground%2595%-1126%107%40%ground%2591%-920%89%40%ground%2420%-1244%94%40%ground%2374%-1493%72%565%ground%2653%-1492%69%781%ground%2013%-1555%191%98%ground%1570%-1640%222%91%ground%989%-1681%260%100%wood%-79%-1821%234%20%wood%36%-1987%213%20%ground%525%-2105%30%110%ground%235%-2048%30%113%ground%858%-2149%30%108%ground%-147%-1672%795%175%lava%-156%-2113%30%1853%ground%1117%-2207%922%212%checkpoint%1509%134%88%40%checkpoint%1947%-374%391%40%checkpoint%2372%-876%78%40%checkpoint%2397%-1517%30%40%checkpoint%511%-1700%88%40%checkpoint%1%-1693%166%40%checkpoint%1342%-2233%228%40%/

ground%-164%97%334%180%water%275%190%30%40%water%282%995%30%166%water%284%5806%30%563%water%280%10150%30%563%water%269%13552%30%2123%water%278%87138%30%2426%ground%381%89371%30%40%ground%381%89164%30%57%ground%381%88987%30%54%ground%381%88816%30%54%ground%381%88675%30%60%ground%381%88534%30%69%ground%381%88408%30%75%ground%381%88285%30%63%ground%381%88174%30%57%ground%382%87986%30%57%ground%382%87827%30%84%ground%383%87693%30%57%ground%383%87612%30%45%ground%385%87490%30%45%ground%385%87376%30%48%ground%385%87226%30%81%ground%385%87089%30%72%ground%386%86927%30%75%water%272%474909%30%1223%water%373%476124%30%40%water%392%475961%30%57%water%392%475785%30%66%water%392%475701%30%40%water%392%475497%30%111%water%392%475380%30%63%water%393%475142%30%183%water%393%475004%30%78%water%396%474895%30%54%water%247%504385%34%8971%ground%320%513304%30%51%ground%321%513028%30%234%ground%332%512735%35%245%ground%329%512450%30%212%ground%425%512112%113%233%ground%397%511852%30%148%ground%439%511629%30%110%ground%433%511361%30%139%ground%429%511213%30%91%ground%396%511031%30%119%ground%397%510820%30%104%ground%377%510546%30%201%ground%452%510231%30%168%ground%429%510047%30%102%ground%402%509766%30%191%ground%385%509572%30%108%ground%464%509296%30%125%ground%416%509136%30%95%ground%519%508948%30%88%ground%474%508710%46%112%ground%446%508494%30%122%ground%422%508223%34%163%ground%370%507958%52%173%ground%395%507641%30%227%ground%395%507155%52%396%ground%350%506814%49%237%ground%374%506133%43%568%ground%359%505695%50%333%ground%361%505193%41%383%ground%377%504912%30%173%ground%451%504726%47%111%ground%423%504528%32%117%ground%419%504268%50%162%water%230%546369%91%6906%ground%209%553331%174%40%ground%454%553202%90%40%ground%403%553088%49%40%ground%508%553029%30%40%ground%590%552865%30%40%ground%394%552686%30%40%ground%544%552632%30%40%ground%532%552478%30%40%ground%420%552478%30%40%ground%403%552323%30%40%ground%423%552180%30%40%ground%431%552069%30%40%ground%581%551885%30%40%ground%459%551762%30%40%ground%576%551627%30%40%ground%451%551556%30%42%ground%571%551420%30%45%ground%546%551292%30%40%ground%628%551153%30%40%ground%495%550987%30%42%ground%577%550902%30%45%ground%527%550733%30%40%ground%479%550648%30%40%ground%550%550532%30%40%ground%531%550382%30%42%ground%454%550218%30%40%ground%483%550105%30%42%ground%535%549952%30%40%ground%404%549847%30%48%ground%540%549731%30%42%ground%540%549587%30%48%ground%447%549490%30%40%ground%558%549370%30%42%ground%622%549261%30%48%ground%559%549074%30%40%ground%463%548944%30%42%ground%472%548847%30%40%ground%571%548748%30%42%ground%521%548646%30%51%ground%472%548553%30%48%ground%645%548414%30%42%ground%476%548282%30%54%ground%566%548167%30%40%ground%355%548066%30%45%ground%518%547912%30%42%ground%533%547836%30%40%ground%458%547712%30%40%ground%434%547606%30%54%ground%562%547512%39%40%ground%679%547520%30%40%ground%565%547394%48%48%ground%496%547294%42%42%ground%595%547287%36%40%ground%544%547165%54%54%ground%354%547033%30%40%ground%422%546780%30%40%ground%497%546735%57%40%ground%408%546550%30%40%checkpoint%260%553318%65%40%ground%770%548132%30%40%ground%965%548045%30%40%ground%843%547919%30%40%ground%706%547847%30%40%ground%540%547378%30%40%ground%357%546874%30%40%ground%406%546369%30%40%ground%502%546269%142%146%checkpoint%529%546260%74%40%/
"""

#import and set up libraries
import pygame, sys
pygame.init()

#colors
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

#set up clock/window/surfaces
c = pygame.time.Clock()
xDim, yDim = int(input("How wide would you like the screen? ")), int(input("How tall would you like the screen? "))
w = pygame.display.set_mode([xDim, yDim])
pygame.display.set_caption("Super Michael's World wEEEHEEEEE")
flashAlpha = 0
flashSurface = pygame.Surface((xDim, yDim))
flashSurface.fill((255,255,255))

#platform class
class Platform:

    #initialize platform
    def __init__(self, type, x, y, length, height):
        global scrollX, scrollY

        #create platform
        self.x = x
        self.y = y
        self.type = type
        self.length = length
        self.height = height
        if type == "wood":
            self.collisionRect = pygame.Rect(x, y, length, 10)
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
            self.drawRects.append([pygame.Rect(x, y, length, height), lightGreen, 0, 0, True])

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
        for rect in self.drawRects:
            if editing or not len(rect) == 5:
                pygame.draw.rect(window, rect[1], rect[0])
        
        #draw selection outline
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
    def __init__(self, x, y, playerSize, checkpointx=0, checkpointy=0):
        self.x = x
        self.y = y
        self.checkpointX = checkpointx
        self.checkpointY = checkpointy
        self.xspeed = 0
        self.yspeed = 0
        self.rect = pygame.Rect(x,y,playerSize,playerSize)
    
    #draw player
    def draw(self, window):
        pygame.draw.rect(window, (255,255,255), self.rect)
    
    #reset player
    def reset(self, cause="reset"):
        global flashAlpha

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

    #move player horizontally
    def moveHor(self):
        global collisions

        #steps
        for i in range(round(abs(self.xspeed))):

            #take step
            if self.xspeed > 0:
                self.x += 1
            else:
                self.x -= 1

            #check for collision
            self.updatePosition()
            if self.checkCollisions(collisions[0]):

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
            if self.checkCollisions(collisions[0]):

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
            elif self.checkCollisions(collisions[3]) and not (down and not up):
                
                #take back step
                if self.yspeed > 0:
                    self.y -= 1

                    #check for continued collision
                    self.updatePosition()
                    if self.checkCollisions(collisions[3]):

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
        global collisions, checkpointFlashable

        #death on lava collision
        if self.checkCollisions(collisions[2]):
            self.reset("death")
            return()
        
        if self.checkCollisions(collisions[4]):
            self.checkpointX = self.x
            self.checkpointY = self.y
            if checkpointFlashable:
                checkpointFlashable = False
                flashScreen("checkpoint")
        else:
            checkpointFlashable = True

        #make movements
        self.moveHor()
        self.moveVert(up, down)
        self.updatePosition()

        #check if in water
        if self.checkCollisions(collisions[1]):

            #water player movements
            if right:
                self.xspeed += 0.1
                self.yspeed -= 0.1
            if left: 
                self.xspeed -= 0.1
                self.yspeed -= 0.1
            if up:
                self.yspeed -= 0.2

            #surface water physics
            else:
                self.rect.y -= 30
                if not self.checkCollisions(collisions[1]):
                    self.yspeed += gravity
                else:
                    self.yspeed -= floating
                self.rect.y += 30
            
            if down:
                self.yspeed += 0.3
            
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
    save = ""

    #add platforms to code
    for platform in level.platforms:
        save += platform.type + "%" + str(platform.x) + "%" + str(platform.y) + "%" + str(platform.length) + "%" + str(platform.height) + "%"
    save += "/"

    #return code
    return save

#save code converter
def convertSave(code):
    global platforms
    platforms.platforms = []

    #convert code
    i = 0
    while code[i] != '/':
        args = []
        for j in range(5):
            arg = ""
            while code[i] != '%':
                arg += code[i]
                i+=1
            args.append(arg)
            i += 1
        platforms.platforms.append(Platform(args[0], int(args[1]), int(args[2]), int(args[3]), int(args[4])))

#render screen
def renderScreen(window):
    global flashAlpha

    #clear window
    window.fill(sky)

    #draw platforms
    for platform in platforms.platforms:
        platform.draw(window)

    #draw editing platform
    for rect in createRect:
        rect.draw(window)
    
    #draw player
    player.draw(window)

    #draw flash
    if flashAlpha > 0:
        flashSurface.set_alpha(flashAlpha)
        w.blit(flashSurface,(0,0))
        flashAlpha -= 2

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

#set up platforms
platforms = PlatformGroup()
collisions = [[],[],[]]

#set up platform creator
createRect = []
platformTypes = ["ground", "water", "lava", "wood", "checkpoint"]
selectedType = 0

#set up player
playerSize = 50
player = Player(0, 0, playerSize)

#scroll position
scrollX = -xDim/2+playerSize/2
scrollY = -yDim/2+playerSize/2

#inputs
shiftKey = False
upKey = False
downKey = False
rightKey = False
leftKey = False
wKey = False
aKey = False
sKey = False
dKey = False
deleteKey = False
fTap = False
mouseDown = False

#mouse variables
initx = 0
initx = 0
mousex = 0
mousey = 0

#booleans
editing = True
dragging = False
checkpointFlashable = True


#game loop
while True:

    #editor
    if editing:
        
        #get inputs
        fTap = False
        for event in pygame.event.get():
            
            #quit game
            if event.type == pygame.QUIT:
                #sys.exit()
                pygame.display.set_mode([100,100])

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
                    editing = not editing
                    updateCollisions(platforms.platforms)
                    platforms.unselectAll()
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
            if event.type == pygame.MOUSEBUTTONDOWN:

                #update mouse status
                mouseDown = True

                #get mouse position
                initx, inity = pygame.mouse.get_pos()
                initx += scrollX
                inity += scrollY

                if shiftKey:
                    tv = False
                else:
                    tv = True
                tv2 = True

                #select platforms
                for i in range(len(platforms.platforms) - 1, -1, -1):
                    if platforms.platforms[i].collisionRect.collidepoint(initx-scrollX, inity-scrollY) and tv:
                        platforms.platforms[i].selected = True
                        tv = False
                        mouseTap = False
                    else:
                        if platforms.platforms[i].selected == True:
                            platforms.platforms[i].selected = False
                            tv2 = False

                #start drag
                if tv2 and (tv or shiftKey):
                    dragging = True

            #mouse up
            if event.type == pygame.MOUSEBUTTONUP:
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
        
        #create image of new platform
        if dragging:

            #get mouse position
            mousex, mousey = pygame.mouse.get_pos()
            mousex += scrollX
            mousey += scrollY

            #image of new platform
            if selectedType == platformTypes.index("wood"):
                createRect = [Platform(platformTypes[selectedType], min(initx,mousex), inity, max(abs(mousex - initx), 30), 20)]
            else:
                createRect = [Platform(platformTypes[selectedType], min(initx,mousex), min(inity,mousey), max(abs(mousex - initx), 30), max(abs(mousey - inity), 40))]
        
        #remove new platform image
        else:
            createRect = []

            #move platform
            if mouseDown:

                #get mouse pos
                mousex, mousey = pygame.mouse.get_pos()
                mousex += scrollX
                mousey += scrollY

                #change selected platform position
                platforms.moveSelected(mousex - initx, mousey - inity)

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
        player.playerEngine(leftKey,rightKey,upKey,downKey, 0.2, 0.95, 0.1)

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


    #update screen
    platforms.updatePlatforms(scrollX,scrollY)
    player.updatePosition()
    renderScreen(w)

    #tick clock
    c.tick(120)