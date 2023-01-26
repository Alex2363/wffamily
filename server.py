import socket
import time
# создаемTCP/IP сокет
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(('localhost', 24001))
main_socket.setblocking(0)
main_socket.listen(5)

players_sockets = []
print('создался соккет')
while True:
    try:

        new_socket, addr = main_socket.accept()
        print('Подключился ', addr)
        new_socket.setblocking(0)
        players_sockets.append(new_socket)
    except:
        #print('Нет желающих')
        pass
    for sock in players_sockets:
        try:
            data = sock.recv(1024)
            data = data.decode()
            print('Получил', data)
        except:
            pass


    #отправляем новое состояние игрокам
    for sock in players_sockets:
        try:
            sock.send('Новое состояние игры'. encode())
        except:
            players_sockets.remove(sock)
            sock.close()
    time.sleep(3)





