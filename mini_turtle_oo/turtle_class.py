class Totuga:
    """
    Simula una 'tortuga' de dibujo simple que puede moverse hacia adelante
    (derecha) y dibujar segmentos horizontales y verticales.
    """

    def __init__(self) -> None:
        """
        Inicializa la posición horizontal de la tortuga a 0.
        """
        # El estado 'posicion_x' se inicializa como un atributo de instancia.
        self.posicion_x = 0

    def adelante(self, pasos: int) -> None:
        """
        Mueve la 'tortuga' hacia la derecha y dibuja un tramo horizontal.

        :param pasos: La cantidad de pasos a moverse (longitud del tramo).
        """
        if pasos <= 0:
            return

        # Dibujar el tramo horizontal en la posición actual
        # Usa self.posicion_x para obtener el estado actual
        linea = " " * self.posicion_x + "_" * pasos
        print(linea)

        # Actualizar la posición horizontal
        # Usa self.posicion_x para modificar el estado
        self.posicion_x += pasos

    def abajo(self, pasos: int) -> None:
        """
        Dibuja un poste vertical en la columna actual (self.posicion_x).

        :param pasos: La cantidad de líneas verticales a dibujar.
        """
        if pasos <= 0:
            return

        for _ in range(pasos):
            # Usa self.posicion_x para obtener el estado actual
            linea = " " * self.posicion_x + "|"
            print(linea)

        # Nota: 'abajo' no cambia la posición horizontal (self.posicion_x)

    def reiniciar(self) -> None:
        """
        Reinicia la posición horizontal de la tortuga a 0.
        """
        # Usa self.posicion_x para resetear el estado
        self.posicion_x = 0