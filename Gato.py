from random import randrange, choice
preguntas = [
    # Faciles
    {
        "1+2":3,
        "2+3":5,
        "4+3":7
    },
    # Medio
    {
        "1*2":2,
        "2*3":6,
        "1*1*1*1*2":2
    },
    # Dificiles
    {
        "1*2*3":6,
        "2*3*4":24
    }
]

# Posiciones del juego
p = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


print("#### Bienvenido al gato educativo ####")
print("Nombre del primer jugador (x): ")
# El espacio en blanco ayudan a que si son nombres iguales, no de errores en los ifs para
# sacar el nombre actual del jugador. (Linea 71, 76, 111)
nombreJugador1 = " "+input()+" "

print("Nombre del segundo jugador (o): ")
nombreJugador2 = input()

print('\nElije el nivel de dificultad: ')
print("1-Facil     2-Medio    1-Dificil")
dificultad = int(input())-1

# El jugador que empieza
jugadorEnTurno = nombreJugador1


def preguntar():
    pregunta, respuesta = choice(list(preguntas[dificultad].items()))
    print("Digita la respuesta de "+pregunta+" : ")
    respuestaJugador = int(input())
    if respuestaJugador == respuesta:
        return True
    else:    
        return False

def dibujarGato():
    print(f'''          x1   x2   x3
       y1 {p[0][0]} |  {p[0][1]}  | {p[0][2]}
         -------------
       y2 {p[1][0]} |  {p[1][1]}  | {p[1][2]}
         -------------
       y3 {p[2][0]} |  {p[2][1]}  | {p[2][2]}
        ''')

def pedirPosicion():
    while True:     
        print("¿Qué posición desea? : ejemplo: x y")
        posicion = list(map(int, input().split(' ')))
        
        # Ajusta la posicion para la lista 
        for x in range(2): posicion[x] = posicion[x]-1 

        if p[posicion[1]][posicion[0]] == ' ':
            return True, posicion
        else:
            print("Posicion ocupada, reintentelo porfavor")


def guardarPosicion(posicionNueva):
    jugador = 'x' if (nombreJugador1 == jugadorEnTurno) else 'o'
    p[posicionNueva[1]][posicionNueva[0]] = jugador
    return p

def comprobarEstadoJuego():
    jugador = 'x' if (nombreJugador1 == jugadorEnTurno) else 'o'
    if (p[0][0] == jugador and p[0][1] == jugador and p[0][2] == jugador and jugador) or (p[1][0] == jugador and p[1][1] == jugador and p[1][2] == jugador and jugador) or (p[2][0] == jugador and p[2][1] == jugador and p[2][2] == jugador and jugador) or (p[0][0] == jugador and p[1][0] == jugador and p[2][0] == jugador and jugador) or (p[0][1] == jugador and p[1][1] == jugador and p[2][1] == jugador and jugador) or (p[0][2] == jugador and p[1][2] == jugador and p[2][2] == jugador and jugador) or (p[0][0] == jugador and p[1][1] == jugador and p[2][2] == jugador and jugador) or (p[0][2] == jugador and p[1][1] == jugador and p[2][0] == jugador and jugador):
        return 'ganador'
    else :
        posicionesDisponibles = False
        for y in range(3):
            for x in range(3):
                if p[x][y] == ' ':
                    posicionesDisponibles = True
        if not posicionesDisponibles:
            return 'finalizado'
         
if __name__ == "__main__":
    while True:
        print("----- TURNO DE "+jugadorEnTurno+"-----")
        respuesta = preguntar()
        if respuesta:
            print("Respuesta correcta.")
            dibujarGato()
            posicionValida, posicionJugador = pedirPosicion()
            if posicionValida:
                    guardarPosicion(posicionJugador)
                    estado = comprobarEstadoJuego()
                    if estado == 'ganador':
                        print("*** JUEGO TERMINADO ***")
                        dibujarGato()
                        print(jugadorEnTurno+" ES EL JUGADOR GANADOR.")
                        break
                    elif estado == 'finalizado':
                        dibujarGato()
                        print("Juego terminado, ya no hay posiciones disponibles ninguno gana.")
                        break
        else:
            print("Respuesta incorrecta, pierdes tu turno")
        
        jugadorEnTurno = nombreJugador2 if (jugadorEnTurno == nombreJugador1) else nombreJugador1


    