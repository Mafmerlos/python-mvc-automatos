from models.model import Model
from views.view_tk import View
from controllers.controller import Controller

def main():
    model = Model() 
    view = View()
    controller = Controller(model, view)
    view.set_controller(controller)
    view.main()

if __name__ == "__main__":
    main()