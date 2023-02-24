from app.views import *


#ip_local = socket.gethostbyname(socket.gethostname())
ip_local = 'localhost'

if __name__ == '__main__':
    app.run(debug=True, host=ip_local, port=5000)