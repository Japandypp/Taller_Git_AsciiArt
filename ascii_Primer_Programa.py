#-----------------------------------------------------------------------------
# Script de Python para probar Git
# Autor: Juan Pacheco <jpachecon1@est.ups.edu.ec>
# Fecha: 04/05/2026
#-----------------------------------------------------------------------------
# Crea un programa que pregunte mi nombre y la edad y luego de un mensaje de bienvenida

def main():
    print("---------------------------------")
    print("Ingresemos los datos juntos")
    print("---------------------------------")
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    edad = int(edad)
    
    print("--------------------")
    print("Tu informacion es: ")
    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Edad: ", edad)
    print("--------------------")

    print("Hola", nombre, "el sistema te da la Bienvenida!!")
    
    # Primer ASCII art
    ascii_art1 = r"""
          .  .
          |\_|\
          | a_a\
          | | "]
      ____| '-\___
     /.----.___.-'\
    //        _    \
   //   .-. (~v~) /|
  |'|  /\:  .--  / \
 // |-/  \_/____/\/~|
|/  \ |  []_|_|_] \ |
| \  | \ |___   _\ ]_}
| |  '-' /   '.'  |
| |     /    /|:  | 
| |     |   / |:  /\
| |     /  /  |  /  \
| |    |  /  /  |    \
\ |    |/\/  |/|/\    \
 \|\ |\|  |  | / /\/\__\
  \ \| | /   | |__
snd    / |   |____)
       |_/ 
"""
    print(ascii_art1)

    # Segundo ASCII art
    ascii_art2 = r"""
          _,     _   _     ,_
      .-'` /     \'-'/     \ `'-.
     /    |      |   |      |    \
    ;      \_  _/     \_  _/      ;
   |         ``         ``         |
   |                               |
    ;    .-.   .-.   .-.   .-.    ;
jgs  \  (   '.'   \ /   '.'   )  /
      '-.;         V         ;.-'
          `                 `
"""
    print(ascii_art2)


if __name__ == "__main__":
    main()

