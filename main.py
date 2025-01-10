import tkinter as tk
from sources.window.manager import WindowManager
from sources.program.notepad import Notepad
from sources.program.terminal import Terminal
from sources.program.calc import Calculator


def main():
    root = tk.Tk()

    # We need to create an instance of the WindowManager class
    app = WindowManager(root) # And pass the root window to it

    # Windows with content
    app.create_window(title="Notepad", content=Notepad, size=(800, 50, 200, 300))
    app.create_window(title="Terminal", content=Terminal, size=(275, 50, 500, 300))
    app.create_window(title="Calculator", content=Calculator,
                      size=(50, 200, 500, 300))

    # Finally, start the main loop
    root.mainloop()


if __name__ == "__main__":
    main()
