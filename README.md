# 🐢 Ejercicio 2: Versión Orientada a Objetos (POO)

## 📝 Descripción del Proyecto

El objetivo principal es encapsular el estado y el comportamiento de una entidad de dibujo (`Totuga`) para demostrar los principios de **encapsulación** y la **independencia del estado** entre múltiples objetos.

---

## 🏗️ Estructura del Código

El proyecto se centra en una única clase principal:

### `class Totuga`

| Atributo / Método | Propósito |
| :--- | :--- |
| `__init__(self)` | Constructor. Inicializa la posición horizontal de la tortuga (`self.posicion_x`) a 0. |
| `adelante(self, pasos: int)` | Mueve la tortuga hacia la derecha, actualiza `self.posicion_x`, y dibuja un tramo horizontal (`_`). |
| `abajo(self, pasos: int)` | Dibuja un poste vertical (`|`) en la posición `self.posicion_x` actual sin modificar la posición horizontal. |
| `reiniciar(self)` | Resetea la posición `self.posicion_x` a 0. |

---

## ✨ Características Clave

* **POO y Encapsulación:** El estado del dibujo (`posicion_x`) se mantiene de forma privada dentro de cada objeto `Totuga`.
* **Independencia de Objetos:** Permite la creación de múltiples tortugas (e.g., `t1`, `t2`) que operan y mantienen sus propias posiciones de dibujo sin interferir entre sí.

---

## 🚀 Uso Básico

Para usar la clase, simplemente crea una instancia y llama a sus métodos:

```python
# Crear una instancia
t = Totuga()

# Mover y dibujar
t.adelante(8)
t.abajo(3)
t.adelante(4)

# Reiniciar la posición
t.reiniciar()
