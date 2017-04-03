import sys
#Importa as implementações dos módulos CORBA e PortableServer
import CORBA, PortableServer
#Importa os stubs-client e os skeletons-server
import Fortune, Fortune__POA

class Echo_i (Example__POA.Echo):
    def echoString(self, mesg):
        print ("echoString() called with message:", mesg)
        return mesg

#inicializando o orb chamando a função ORB_init onde é passado uma lista de argumentos de
#linhas de comando e um identificador ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
#ativando o objeto de serviço
poa = orb.resolve_initial_references("RootPOA")

#criando uma instância do objeto
ei = Echo_i()
#obtendo a referência retornada do objeto
eo = ei._this()

#
poaManager = poa._get_the_POAManager()
poaManager.activate()

message = "Hello"
result = eo.echoString(message)

print ("I said '%s'. The object said '%s'." % (message,result))