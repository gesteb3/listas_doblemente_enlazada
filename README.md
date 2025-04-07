# Editor de texto con historial

## Descripción

La tarea simula un **Editor de texto** utilizando una **Lista Doblemente Enlazada** para gestionar el historial de ediciones. El editor permite realizar deshacer y rehacer acciones, guardando el estado del texto en cada paso. La interfaz gráfica está construida utilizando la librería `tkinter` junto con `ttkbootstrap` para un diseño atractivo y moderno.

## Funcionalidades

- **Deshacer**: Permite revertir el último cambio realizado en el texto.
- **Rehacer**: Permite rehacer un cambio previamente deshecho.
- **Historial de Cambios**: El estado del texto se guarda en una lista doblemente enlazada, permitiendo navegar entre versiones anteriores y posteriores del texto.
- **Interfaz Gráfica**: Utiliza `tkinter` para proporcionar una interfaz sencilla y amigable.

## Estructura del Proyecto

### **Clase `DoublyNode`**

Representa un nodo en una lista doblemente enlazada. Cada nodo contiene el valor del texto y referencias a los nodos anterior y siguiente en la lista.

#### Atributos:
- `value`: Contenido del texto.
- `prev`: Referencia al nodo anterior.
- `next`: Referencia al nodo siguiente.

### **Clase `DoublyLinkedList`**

Gestiona la lista doblemente enlazada para almacenar y manejar los estados del texto.

#### Métodos:
- **`append(value: str)`**: Agrega un nuevo nodo con el contenido del texto al final de la lista.
- **`move_backward()`**: Mueve el puntero al nodo anterior (deshacer).
- **`move_forward()`**: Mueve el puntero al nodo siguiente (rehacer).
- **`current()`**: Devuelve el contenido del nodo actual.

### **Clase `TextEditorApp`**

Gestiona la interfaz gráfica del editor de texto utilizando `tkinter` y `ttkbootstrap`.

#### Métodos:
- **`save_state()`**: Guarda el estado actual del texto en el historial. Esta acción agrega el texto del área de texto a la lista doblemente enlazada.
- **`undo()`**: Realiza la acción de deshacer, moviendo el puntero de la lista hacia el nodo anterior y actualizando el área de texto.
- **`redo()`**: Realiza la acción de rehacer, moviendo el puntero de la lista hacia el nodo siguiente y actualizando el área de texto.
- **`update_text_area()`**: Actualiza el área de texto con el estado actual, mostrando el texto guardado en el nodo actual de la lista.
- **`update_buttons_state()`**: Habilita o deshabilita los botones de deshacer y rehacer dependiendo del estado actual del historial.

