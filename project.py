import tkinter as tk

# Ventana principal
root = tk.Tk()
root.title("AstroCycle")
root.geometry("800x500")
root.config(bg="#0a0a1a") 

# --- FUNCIONES PARA CAMBIAR CONTENIDO ---
def mostrar_inicio():
    limpiar_contenido()
    tk.Label(frame_contenido, text="Bienvenido a AstroCycle", font=("Arial", 18, "bold"), bg="#0a0a1a", fg="#03dffc").pack(pady=30)

def mostrar1():
    limpiar_contenido()
    tk.Label(frame_contenido, text="aca va algo 1", font=("Arial", 18, "bold"), bg="#0a0a1a", fg="#03dffc").pack(pady=30)

def mostrar2():
    limpiar_contenido()
    tk.Label(frame_contenido, text="aca va algo2", font=("Arial", 18, "bold"), bg="#0a0a1a", fg="#03dffc").pack(pady=30)

def limpiar_contenido():
    for widget in frame_contenido.winfo_children():
        widget.destroy()

# --- ESTRUCTURA PRINCIPAL ---
# Frame lateral (izquierda)
frame_menu = tk.Frame(root, bg="#111133", width=200)
frame_menu.pack(side="left", fill="y")

# Frame de contenido (derecha)
frame_contenido = tk.Frame(root, bg="#0a0a1a")
frame_contenido.pack(side="right", expand=True, fill="both")

# --- BOTONES DEL MENÚ ---
botones = [
    ("Inicio", mostrar_inicio),
    ("Pantalla 1", mostrar1),
    ("Pantalla 2", mostrar2),
]

for texto, comando in botones:
    b = tk.Button(
        frame_menu, text=texto, command=comando,
        font=("Arial", 14, "bold"),
        bg="#1a1a3d", fg="#03dffc",
        activebackground="#03dffc", activeforeground="#0a0a1a",
        relief="flat", width=16, pady=10
    )
    b.pack(pady=8)

# Mostrar por defecto la primera pantalla
mostrar_inicio()

root.mainloop()
