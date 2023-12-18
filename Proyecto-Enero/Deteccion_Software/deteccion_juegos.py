import psutil

class JuegoDetector:
    def __init__(self):
        # Lista de nombres de procesos de juegos que quieres detectar
        self.juegos_permitidos = ["juego1.exe", "juego2.exe"]
        # Tiempo de espera entre verificaciones (en segundos)
        self.tiempo_de_espera = 10

    def detectar_juego_en_ejecucion(self):
        procesos = [p.name() for p in psutil.process_iter(['pid', 'name'])]

        for juego in self.juegos_permitidos:
            if juego.lower() in procesos:
                return True

        return False
    
    #detectar un programa especifico
    def detectar_programa(self, nombre_programa):
        procesos = [p.info for p in psutil.process_iter(['pid', 'name'])]

        programa_detectado = False

        for proceso in procesos:
            if nombre_programa.lower() in proceso["name"].lower():
                programa_detectado = True
                # Registrar la actividad en la base de datos
                BaseDatos.registrar_actividad(self.nombre_usuario, f"ejecucion_{nombre_programa}")
                # Puedes almacenar más información sobre el programa si es necesario
                BaseDatos.registrar_programa_ejecutado(self.nombre_usuario, nombre_programa, proceso)
        
        return programa_detectado
    
    
    def detectar_perifericos_externos(self):
        # Obtener información sobre periféricos externos (ejemplo: unidades USB)
        dispositivos_externos = psutil.disk_partitions(all=True)

        # Puedes personalizar y ampliar esta lógica según tus necesidades
        return dispositivos_externos
