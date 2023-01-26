import socket
import pygame
import sys
import time

WIDTH_WINDOW, HEIGHT_WINDOW = 1000, 600
# СоздаемTCP/IP сокет
'''sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

sock.connect(('localhost', 24001))'''
# Создание окна игры

pygame.init()
screen = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
pygame.display.set_caption('мой футбол')

#clock = pygame.time.Clock()
counter = 90
mins, secs = divmod(counter, 60)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
while True:
    # Обработка событий

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.USEREVENT:
            counter -= 1
            mins, secs = divmod(counter, 60)
        text = '{:02d}:{:02d}'.format(mins, secs) if counter > 0 else 'boom!'

    '''if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        print(pos)'''

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (WIDTH_WINDOW / 2 + 40, 48))
    pygame.display.flip()
#run()
    #Отправляем команду на сервер
    #sock.send('Я хочу прыгать как коза'.encode())

    #Получаем от сервера новое состояние игрового поля
    #data = sock.recv(1024)
    #data = data.decode()


    #рисуем новое состояние поля
    #print(data)
