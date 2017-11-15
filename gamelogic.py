# Импорт библиотек и вспомогательных файлов
import pygame,sys,random
from colors import *
from pygame.locals import*

# Переменные для обозначения движения
DOWN=1
UP=2
RIGHT=3
LEFT=4
# Переменные для объявления размеров поля
WIDTH = 16
HEIGHT = 16
# Размер 1 блока
BLOCK_SIZE = 4
# Обозначения размера окна, игровой области и названия окна
window = pygame.display.set_mode((WIDTH*30,HEIGHT*30))
screen = pygame.display.set_mode((WIDTH*30,HEIGHT*30))
pygame.display.set_caption("2048")
# Обозначение 1го блока на игровом поле
BLOCK_SPRITE = pygame.Surface((BLOCK_SIZE*30,BLOCK_SIZE*30))
# Инициализация шрифтов и их описание
pygame.font.init()
pygame.init()
font = pygame.font.SysFont('Clear Sans', 100)
font2 = pygame.font.SysFont('Clear Sans', 50)

def NewBlock(BLOCK):
    k=0
    # Бесконечный цикл, пока не находим пустой блок
    while k!=1:
        x,y=random.randint(0,3),random.randint(0,3)
        if BLOCK[x][y]==0: #Выходим из цикла, если нашли пустой блок
            k=1
    # Записываем в массив случайное значение 2 или 4 и окрашиваем блок в соответствующий цвет    
    if (random.randint(0,1)):
        BLOCK[x][y]= 2
        BLOCK_SPRITE.fill(COLOR2)
    else:
        BLOCK[x][y]= 4
        BLOCK_SPRITE.fill(COLOR4)
    # Отрисовываем блок на игровом поле с учетом размеров окна
    screen.blit(BLOCK_SPRITE,(x*BLOCK_SIZE*30,y*BLOCK_SIZE*30))
    # В переменную Text записываем значение блока
    Text=font2.render(str(BLOCK[x][y]),True,BLACK)
    # И отрисовываем это значение поверх блока
    screen.blit(Text,(x*BLOCK_SIZE*30,y*BLOCK_SIZE*30))

    
def BlocksMoveDown(BLOCK):
    Flag=False
    # Создаем массив 4х4, он нужен нам для отслеживания изменений на игровом поле,
    # например: если 2 клетки с одинаковым значением сложились, то записываем на их координаты
    # в этом массиве единицы и дальше мы их складывать не будем
    CHANGED=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    # Первый цикл нужен для перемещения блоков на игровом поле ("кучкуем" блоки)
    k=0
    while k<3:
        j=0
        while j<=2:
            i=3
            while i>=0:
                # Если блок не равен нулю, а следующий - ноль, выполняется передвижение
                if BLOCK[i][j+1]==0 and BLOCK[i][j]!=0:
                    BLOCK[i][j+1]=BLOCK[i][j]
                    BLOCK[i][j]=0
                    # Пустая клетка заполняется серым
                    BLOCK_SPRITE.fill(GREY)
                    # И отрисовывается на экране
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    # Определяется цвет для новой клетки
                    clr=ColorChoose(BLOCK[i][j+1])
                    # Новая клетка заполняется цветом
                    BLOCK_SPRITE.fill(clr)
                    # И отрисовывается на экране
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,(j+1)*BLOCK_SIZE*30))
                    # Flag становится True, так как изменение на игровом поле произошло
                    Flag=True
                    # Если цвет не серый (клетка не пустая)(это условие нужно чтобы на пустых клетках не отрисовывались нули
                    if clr!=GREY:
                        # В переменную Text записывается значение клетки
                        Text=font2.render(str(BLOCK[i][j+1]),True,BLACK)
                        # И отрисовывается поверх
                        screen.blit(Text,(i*BLOCK_SIZE*30,(j+1)*BLOCK_SIZE*30))
                i-=1
            j+=1
        k+=1
    # Во втором блоке циклов мы складываем соседние блоки с одинаковым значением
    j=2
    while j>=0:
        i=3
        while i>=0:
            # Если соседние блоки одинаковые и не равны нулю и они не складывались до этого
            if BLOCK[i][j+1]==BLOCK[i][j] and BLOCK[i][j]!=0 and CHANGED[i][j+1]==0 and CHANGED[i][j]==0:
                # Складываем их, пустому блоку присваиваем 0
                BLOCK[i][j+1]=BLOCK[i][j]*2
                BLOCK[i][j]=0
                # Пустая клетка заполняется серым
                BLOCK_SPRITE.fill(GREY)
                # И отрисовывается на экране
                screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                # Определяется цвет для новой клетки
                clr=ColorChoose(BLOCK[i][j+1])
                # Новая клетка заполняется цветом
                BLOCK_SPRITE.fill(clr)
                # И отрисовывается на экране
                screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,(j+1)*BLOCK_SIZE*30))
                # Flag становится True, так как изменение на игровом поле произошло
                Flag=True
                # В массив CHANGED записываем 1 на тех позициях, где изменение произошло, дабы исключить последующее складывание
                CHANGED[i][j+1]=CHANGED[i][j]=1
                # Если цвет не серый (клетка не пустая)(это условие нужно чтобы на пустых клетках не отрисовывались нули
                if clr!=GREY:
                    # В переменную Text записывается значение клетки
                    Text=font2.render(str(BLOCK[i][j+1]),True,BLACK)
                    # И отрисовывается поверх
                    screen.blit(Text,(i*BLOCK_SIZE*30,(j+1)*BLOCK_SIZE*30))
            i-=1
        j-=1
    k=0
    # Третий цикл аналогичен 1ому, то есть просто "кучкует" блоки
    while k<3:
        j=0
        while j<=2:
            i=3
            while i>=0:
                if BLOCK[i][j+1]==0 and BLOCK[i][j]!=0:
                    BLOCK[i][j+1]=BLOCK[i][j]
                    BLOCK[i][j]=0
                    BLOCK_SPRITE.fill(GREY)
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    clr=ColorChoose(BLOCK[i][j+1])
                    BLOCK_SPRITE.fill(clr)
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,(j+1)*BLOCK_SIZE*30))
                    Flag=True
                    if clr!=GREY:
                        Text=font2.render(str(BLOCK[i][j+1]),True,BLACK)
                        screen.blit(Text,(i*BLOCK_SIZE*30,(j+1)*BLOCK_SIZE*30))
                i-=1
            j+=1
        k+=1
    #Возвращаем Flag
    return Flag
        
def BlocksMoveUp(BLOCK):
    CHANGED=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    Flag=False
    k=0
    while k<3:
        j=3
        while j>=1:
            i=3
            while i>=0:
                if BLOCK[i][j-1]==0 and BLOCK[i][j]!=0:
                    BLOCK[i][j-1]=BLOCK[i][j]
                    BLOCK[i][j]=0
                    BLOCK_SPRITE.fill(GREY)
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    clr=ColorChoose(BLOCK[i][j-1])
                    BLOCK_SPRITE.fill(clr)
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,(j-1)*BLOCK_SIZE*30))
                    Flag=True
                    if clr!=GREY:
                        Text=font2.render(str(BLOCK[i][j-1]),True,BLACK)
                        screen.blit(Text,(i*BLOCK_SIZE*30,(j-1)*BLOCK_SIZE*30))
                i-=1
            j-=1
        k+=1
    i=0
    while i<=3:
        j=1
        while j<=3:
            if BLOCK[i][j-1]==BLOCK[i][j] and BLOCK[i][j]!=0 and CHANGED[i][j-1]==0 and CHANGED[i][j]==0:
                BLOCK[i][j-1]=BLOCK[i][j]*2
                BLOCK[i][j]=0
                BLOCK_SPRITE.fill(GREY)
                screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                clr=ColorChoose(BLOCK[i][j-1])
                BLOCK_SPRITE.fill(clr)
                screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,(j-1)*BLOCK_SIZE*30))
                Flag=True
                CHANGED[i][j-1]=CHANGED[i][j]=1
                if clr!=GREY:
                    Text=font2.render(str(BLOCK[i][j-1]),True,BLACK)
                    screen.blit(Text,(i*BLOCK_SIZE*30,(j-1)*BLOCK_SIZE*30))
            j+=1
        i+=1
    k=0
    while k<3:
        j=3
        while j>=1:
            i=3
            while i>=0:
                if BLOCK[i][j-1]==0 and BLOCK[i][j]!=0:
                    BLOCK[i][j-1]=BLOCK[i][j]
                    BLOCK[i][j]=0
                    BLOCK_SPRITE.fill(GREY)
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    clr=ColorChoose(BLOCK[i][j-1])
                    BLOCK_SPRITE.fill(clr)
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,(j-1)*BLOCK_SIZE*30))
                    Flag=True
                    if clr!=GREY:
                        Text=font2.render(str(BLOCK[i][j-1]),True,BLACK)
                        screen.blit(Text,(i*BLOCK_SIZE*30,(j-1)*BLOCK_SIZE*30))
                i-=1
            j-=1
        k+=1
    return Flag

def BlocksMoveRight(BLOCK):
    CHANGED=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    Flag=False
    k=0
    while k<3:
        i=2
        while i>=0:
            j=0
            while j<=3:
                if BLOCK[i+1][j]==0 and BLOCK[i][j]!=0:
                    BLOCK[i+1][j]= BLOCK[i][j]
                    BLOCK[i][j]=0
                    BLOCK_SPRITE.fill(GREY)
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    clr=ColorChoose(BLOCK[i+1][j])
                    BLOCK_SPRITE.fill(clr)
                    screen.blit(BLOCK_SPRITE,((i+1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    Flag=True
                    if clr!=GREY:
                        Text=font2.render(str(BLOCK[i+1][j]),True,BLACK)
                        screen.blit(Text,((i+1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                j+=1
            i-=1
        k+=1
    i=2
    while i>=0:
        j=0
        while j<=3:       
            if BLOCK[i+1][j]==BLOCK[i][j] and BLOCK[i][j]!=0 and CHANGED[i+1][j]==0 and CHANGED[i][j]==0:
                BLOCK[i+1][j]=BLOCK[i][j]*2
                BLOCK[i][j]=0
                BLOCK_SPRITE.fill(GREY)
                screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                clr=ColorChoose(BLOCK[i+1][j])
                BLOCK_SPRITE.fill(clr)
                screen.blit(BLOCK_SPRITE,((i+1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                Flag=True
                CHANGED[i+1][j]=CHANGED[i][j]=1
                if clr!=GREY:
                    Text=font2.render(str(BLOCK[i+1][j]),True,BLACK)
                    screen.blit(Text,((i+1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
            j+=1
        i-=1
    k=0
    while k<3:
        i=2
        while i>=0:
            j=0
            while j<=3:
                if BLOCK[i+1][j]==0 and BLOCK[i][j]!=0:
                    BLOCK[i+1][j]= BLOCK[i][j]
                    BLOCK[i][j]=0
                    BLOCK_SPRITE.fill(GREY)
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    clr=ColorChoose(BLOCK[i+1][j])
                    BLOCK_SPRITE.fill(clr)
                    screen.blit(BLOCK_SPRITE,((i+1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    Flag=True
                    if clr!=GREY:
                        Text=font2.render(str(BLOCK[i+1][j]),True,BLACK)
                        screen.blit(Text,((i+1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                j+=1
            i-=1
        k+=1
    return Flag

def BlocksMoveLeft(BLOCK):
    Flag=False
    CHANGED=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    k=0
    while k<3:
        i=1
        while i<=3:
            j=3
            while j>=0:
                if BLOCK[i-1][j]==0 and BLOCK[i][j]!=0:
                    BLOCK[i-1][j]= BLOCK[i][j]
                    BLOCK[i][j]=0
                    BLOCK_SPRITE.fill(GREY)
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    clr=ColorChoose(BLOCK[i-1][j])
                    BLOCK_SPRITE.fill(clr)
                    screen.blit(BLOCK_SPRITE,((i-1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    Flag=True
                    if clr!=GREY:
                        Text=font2.render(str(BLOCK[i-1][j]),True,BLACK)
                        screen.blit(Text,((i-1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                j-=1
            i+=1
        k+=1
    i=1
    while i<=3:
        j=3
        while j>=0:
            if BLOCK[i-1][j]==BLOCK[i][j] and BLOCK[i][j]!=0 and CHANGED[i-1][j]==0 and CHANGED[i][j]==0:
                BLOCK[i-1][j]=BLOCK[i][j]*2
                BLOCK[i][j]=0
                BLOCK_SPRITE.fill(GREY)
                screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                clr=ColorChoose(BLOCK[i-1][j])
                BLOCK_SPRITE.fill(clr)
                screen.blit(BLOCK_SPRITE,((i-1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                Flag=True
                CHANGED[i-1][j]=CHANGED[i][j]=1
                if clr!=GREY:
                    Text=font2.render(str(BLOCK[i-1][j]),True,BLACK)
                    screen.blit(Text,((i-1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
            j-=1
        i+=1
    k=0
    while k<3:
        i=1
        while i<=3:
            j=3
            while j>=0:
                if BLOCK[i-1][j]==0 and BLOCK[i][j]!=0:
                    BLOCK[i-1][j]= BLOCK[i][j]
                    BLOCK[i][j]=0
                    BLOCK_SPRITE.fill(GREY)
                    screen.blit(BLOCK_SPRITE,(i*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    clr=ColorChoose(BLOCK[i-1][j])
                    BLOCK_SPRITE.fill(clr)
                    screen.blit(BLOCK_SPRITE,((i-1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                    Flag=True
                    if clr!=GREY:
                        Text=font2.render(str(BLOCK[i-1][j]),True,BLACK)
                        screen.blit(Text,((i-1)*BLOCK_SIZE*30,j*BLOCK_SIZE*30))
                j-=1
            i+=1
        k+=1
    return Flag

def IsGameOver(BLOCK):
    # Изначально переменная True
    OVER=True
    # В этом блоке циклов проверяем есть ли одинаковые соседние блоки или пустые блоки
    i=0
    while i<3:
        j=0
        while j<3:
            # Если таковые находятся, то переменная становится False
            if BLOCK[i][j]==BLOCK[i][j+1] or BLOCK[i][j]==BLOCK[i+1][j] or BLOCK[i][j]==0:
                OVER=False
            j+=1
        i+=1
    i=0
    # Но проверить все клетки за 1 блок циклов не возможно, так как остаются непроверенными
    # последняя колонка и последняя строка
    # Они и проверяются в последующих циклах
    while i<3:
        if BLOCK[i][3]==BLOCK[i+1][3] or BLOCK[i][j]==0:
            OVER=False
        i+=1
    j=0
    while j<3:
        if BLOCK[3][j]==BLOCK[3][j+1] or BLOCK[i][j]==0:
            OVER=False
        j+=1
    # Если игра все же завершена, то происходит задержка
    if OVER:
        pygame.time.delay(3000)
    return OVER
    
