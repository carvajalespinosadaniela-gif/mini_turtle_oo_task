from mini_turtle_oo.turtle_class import Totuga

# Crear los dos objetos Totuga
t1 = Totuga()
t2 = Totuga()

print(f"Posición inicial de t1: {t1.posicion_x}")
print(f"Posición inicial de t2: {t2.posicion_x}")
print("\n" + "="*30 + "\n")

print("### Movimiento de t1 (5 pasos)")
t1.adelante(5)

print("\n--- Verificación de Posiciones ---")
print(f"Posición actual de t1: {t1.posicion_x}")
print(f"Posición actual de t2: {t2.posicion_x}") # Debería ser 0
print("\n" + "="*30 + "\n")


print("### Movimiento de t2 (10 pasos)")
t2.adelante(10)


print("\n--- Verificación de Posiciones ---")
print(f"Posición actual de t1: {t1.posicion_x}") # Debería ser 5
print(f"Posición actual de t2: {t2.posicion_x}") # Debería ser 10
print("\n" + "="*30 + "\n")