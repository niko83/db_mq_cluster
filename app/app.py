import socket


def app():
    output = {
        'hostname': socket.gethostname(),
    }
    return output
