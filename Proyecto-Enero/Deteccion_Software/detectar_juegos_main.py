import time
from deteccion_juegos import JuegoDetector
from mongo_db import BaseDatos

def main():
    nombre_usuario = input("Ingrese el nombre de usuario: ")

    juego_detector = JuegoDetector()
    base_datos = BaseDatos()

    while True:
        perifericos_externos = juego_detector.detectar_perifericos_externos()
        if juego_detector.detectar_juego_en_ejecucion():
            print("Juego detectado. Registrando actividad...")
            base_datos.registrar_actividad(nombre_usuario, "ejecucion_juego")
            base_datos.bloquear_usuario(nombre_usuario)
            break
        
        if juego_detector.detectar_programa("pseint.exe", nombre_usuario):
            print("¡PSeInt detectado! bloqueando usuario...")
            base_datos.bloquear_usuario(nombre_usuario)
            break

        time.sleep(juego_detector.tiempo_de_espera)
        base_datos.registrar_perifericos_externos(nombre_usuario, perifericos_externos)

if __name__ == "__main__":
    main()
