import random
def create_game()->int:
    """Escoge la caja ganadora"""
    print("Un gatito tiene 3 cajas: A, B, C")
    print("Solo una tiene un pescado, las otras tienen pepinos\n")

    cajas = ['A', 'B', 'C']
    pescado = random.choice(cajas) 

    eleccion = input("Elige una caja (A, B, C): ").upper()

    if eleccion not in cajas:
        print("Elección inválida")
        return

    posibles = [c for c in cajas if c != eleccion and c != pescado]
    caja_abierta = random.choice(posibles)

    print(f"\nSe abre la caja  {caja_abierta} y es un pepino.")


    decision = input("¿Quieres cambiar de caja? (si/no): ").lower()

    if decision == "si":
        
        restantes = [c for c in cajas if c != eleccion and c != caja_abierta]
        eleccion = restantes[0]
        print(f"Cambias a la caja {eleccion}")
    else:
        print(f"Te quedas con la caja {eleccion}")

  
    if eleccion == pescado:
        print("¡El gatito encontró el pescado!")
    else:
        print(f"Había un pepino. El pescado estaba en la caja {pescado}")

create_game()

def play_change(n:int = 1000) -> float:
    """
    Juega monty-hall con la estrategia de cambiar la puerta
    Regresa la tasa de éxito
    """
    victorias = 0
    
    for _ in range(n):
        victorias += simular_juego(cambiar=True)
    
    return victorias / n
    
def play_stay(n: int = 1000) -> float:
    victorias = 0
    
    for _ in range(n):
        victorias += simular_juego(cambiar=False)
    
    return victorias / n

def main():
    success_change = play_change()
    success_stay   = play_stay()
    print(f"{success_change=} {success_stay=}")


if "__name__" == "__main__":
    main()
