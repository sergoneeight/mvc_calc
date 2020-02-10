class CalcController(object):
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def on_calculate_button_clicked(self):
        try:
            first_num = int(self.view.get_first_number)
            second_num = int(self.view.get_second_number)
            self.view.set_calculation_result(self.model.multiply(first_num, second_num))

        except ValueError:
            self.view.set_error_message('Please enter 2 integers')
