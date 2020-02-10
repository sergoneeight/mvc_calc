from controller.calc_controller import CalcController
from model.calc_model import CalcModel
from view.calc_view import CalcView

if __name__ == '__main__':
    calc_model = CalcModel()
    calc = CalcView()
    controller = CalcController(calc, calc_model)
    calc.add_controller(controller)
    calc.mainloop()
