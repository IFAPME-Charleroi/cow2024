from pynput.mouse import Listener

def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

def on_click(x, y, button, pressed):
    # Vous pouvez toujours garder cette fonction si vous souhaitez également traiter les clics
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")

# Écoute des mouvements et clics de souris
with Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()
