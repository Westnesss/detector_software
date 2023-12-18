import pymongo
import time

class BaseDatos:
    def __init__(self):
        # Conéctate a la base de datos MongoDB
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["Actividad"]
        self.usuarios_collection = self.db["usuarios"]

    def registrar_actividad(self, usuario, tipo_actividad):
        self.usuarios_collection.update_one(
            {"nombre_usuario": usuario},
            {"$push": {"actividades": {"tipo": tipo_actividad, "timestamp": time.time()}}},
        )

    def bloquear_usuario(self, usuario):
        # Agrega lógica para bloquear al usuario
        pass
    
    def registrar_perifericos_externos(self, usuario, perifericos):
        self.usuarios_collection.update_one(
            {"nombre_usuario": usuario},
            {"$push": {"perifericos_externos": {"info": perifericos, "timestamp": time.time()}}},
        )
