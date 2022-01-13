from pydoc import cli
import sys

#problema com path do python
sys.path.insert(0,sys.path[0] + "/graficos")
import tela_conexao
import client

usuario = tela_conexao.get_user()
print(usuario)
try:
    object_socket = client.connect(usuario)
except:
    print("pau")

try:
    client.play(obj_socket=object_socket)
except:
    print("pau2")