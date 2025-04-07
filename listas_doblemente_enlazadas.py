from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

@dataclass
class DoublyNode:
    value: str
    prev: Optional[DoublyNode] = None
    next: Optional[DoublyNode] = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None
        self.current_node: Optional[DoublyNode] = None

    def append(self, value: str):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = self.tail = self.current_node = new_node
        else:
            if self.current_node and self.current_node.next:
                self._truncate_after(self.current_node)

            new_node.prev = self.current_node
            if self.current_node:
                self.current_node.next = new_node
            self.tail = new_node
            self.current_node = new_node

    def _truncate_after(self, node: DoublyNode):
        node.next = None
        self.tail = node

    def move_backward(self):
        if self.current_node and self.current_node.prev:
            self.current_node = self.current_node.prev

    def move_forward(self):
        if self.current_node and self.current_node.next:
            self.current_node = self.current_node.next

    def current(self) -> str:
        return self.current_node.value if self.current_node else ""

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Historial")
        self.history = DoublyLinkedList()

        self.text_area = tk.Text(root, height=15, width=50, font=("Courier", 12))
        self.text_area.pack(pady=10)

        self.frame = ttk.Frame(root)
        self.frame.pack()

        self.save_btn = ttk.Button(self.frame, text="Guardar estado", command=self.save_state)
        self.save_btn.grid(row=0, column=0, padx=5)

        self.undo_btn = ttk.Button(self.frame, text="Deshacer", command=self.undo)
        self.undo_btn.grid(row=0, column=1, padx=5)

        self.redo_btn = ttk.Button(self.frame, text="Rehacer", command=self.redo)
        self.redo_btn.grid(row=0, column=2, padx=5)

    def save_state(self):
        content = self.text_area.get("1.0", tk.END).strip()
        self.history.append(content)
        print("Guardado:", content)

    def undo(self):
        self.history.move_backward()
        self.update_text_area()
        print("Deshacer")

    def redo(self):
        self.history.move_forward()
        self.update_text_area()
        print("Rehacer")

    def update_text_area(self):
        current_text = self.history.current()
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", current_text)

if __name__ == "__main__":
    app = tb.Window(themename="cosmo")
    editor = TextEditorApp(app)
    app.mainloop()
