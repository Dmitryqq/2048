# Импорт библиотек и вспомогательных файлов
import pygame,sys,random
from colors import *
from gamelogic import *
from pygame.locals import*

# Игровая функция
def gameloop():
    # Создание игрового массива и заполнение его нулями
    BLOCK=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
    Move=0  #Переменная для обозначения движения
    done=True  #Переменная для игрового цикла (игра будет продолжаться, пока значение True)
    Flag=False #Переменная для отслеживания изменения на игровом поле
    OVER=False #Переменная для проверки проиграна игра или нет
    screen.fill(GREY) #Заполнение экрана серым цветом
    # Отрисовка 2х случайных (2 или 4) блоков в случайном месте
    for i in range(2):
        NewBlock(BLOCK)

    # Игровой цикл
    while done:
        # Пока игра не проиграна
        if OVER==False:
            # Обрабатываем нажатие клавиш и закрытия окна
            for e in pygame.event.get():
                # Если нажат крестик или клавиша Esc выход из приложения
                 if e.type==QUIT or (e.type==pygame.KEYDOWN and e.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                # Если нажата стрелка вниз/вверх/влево/вправо передаем переменнов Move направление движения
                 if e.type==pygame.KEYDOWN:
                     if e.key==K_DOWN:
                         Move=DOWN
                     if e.key==K_UP:
                         Move=UP
                     if e.key==K_RIGHT:
                         Move=RIGHT
                     if e.key==K_LEFT:
                         Move=LEFT
            # Исходя из заданного направления движения выполняем функцию передвижения блоков и сложения одинаковых
            if Move==DOWN:
                # Функции передвижения возвращают True или False и записываются в переменную Flag
                Flag=BlocksMoveDown(BLOCK)
                # Сбрасываем направление движения для следующего действия
                Move=0
            # Аналогичные действия с другими вариантами
            elif Move==UP:
                Flag=BlocksMoveUp(BLOCK)
                Move=0
            elif Move==RIGHT:                
                Flag=BlocksMoveRight(BLOCK)
                Move=0
            elif Move==LEFT:                
                Flag=BlocksMoveLeft(BLOCK)
                Move=0
            # Если во время передвижения на игровом поле что-либо изменилось, то отрисовываем новый блок
            if Flag:
                NewBlock(BLOCK)
                # И присваиваем Flag False
                Flag=False
            # Отрисовываем игровое поле в окне
            window.blit(screen,(0,0))
            # Обновляем изображение на экране
            pygame.display.flip()
            # И проверяем проиграна ли игра или нет (ф-я IsGameOver возвращает True или False)
            OVER=IsGameOver(BLOCK)
        # Если игра проиграна
        else:
            # Обрабатываем нажатие клавиш и закрытия окна
            for e in pygame.event.get():
                 if e.type==QUIT or (e.type==pygame.KEYDOWN and e.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                # Если нажата клавиша "R", то игра начинается заново 
                 if e.type==pygame.KEYDOWN:
                     if e.key==K_r:
                         gameloop()
            # Заполняем экран цветом
            screen.fill(GOLD)
            # Записываем в переменную Text текста и выводим надписи на экран
            Text=font.render("GAME OVER",True,BLACK)
            screen.blit(Text,(WIDTH,HEIGHT))
            Text=font2.render('"R" to play again',True,BLACK)
            screen.blit(Text,(WIDTH,HEIGHT+200))
            Text=font2.render('"ESC" to quit',True,BLACK)
            screen.blit(Text,(WIDTH,HEIGHT+270))
            # Отрисовываем игровое поле в окне
            window.blit(screen,(0,0))
            # Обновляем изображение на экране
            pygame.display.flip()
gameloop()
