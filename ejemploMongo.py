"--disable=C0103"
import pymongo

MONGO_HOST = "localhost"
MONGO_PORT = "27017"
MONGO_TIMEOUT = 1000

MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PORT + "/"

try:
    cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS = MONGO_TIMEOUT)
    cliente.server_info()
    print("Conexion a Mongo exitosa")
    db = cliente['test-database']
    collection = db['test-collection']
    cliente.close()
except pymongo.errors.serverSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Error al conectarse "+ errorConexion) 
