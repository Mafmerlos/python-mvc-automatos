from views.view import View
from controllers.controller import Controller

def main():
    view = View()
    controller = Controller(view)
    view.iniciar_loop()

if __name__ == "__main__":
    main()