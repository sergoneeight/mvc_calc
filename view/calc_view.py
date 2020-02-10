from tkinter import *


class CalcView(Tk):
    def __init__(self, controller=None, **kw):
        super().__init__(**kw)
        self.title("Calc")
        self._controller = controller
        self._first_entry = Entry(self)
        self._second_entry = Entry(self)
        self._result_view = Entry(self)
        self._first_entry.pack()
        self._multiply_sign = Label(self, text='x').pack()
        self._second_entry.pack()
        self._calculate_btn = Button(self, text='Calculate', command=self.on_calculate_button_clicked).pack()
        self._result_view.pack()

    def add_controller(self, controller):
        self._controller = controller

    def on_calculate_button_clicked(self):
        self._controller.on_calculate_button_clicked()

    @property
    def get_first_number(self):
        return self._first_entry.get()

    @property
    def get_second_number(self):
        return self._second_entry.get()

    def set_calculation_result(self, result):
        self._result_view.delete(0, len(self._result_view.get()))
        self._result_view.insert(0, result)

    def set_error_message(self, message):
        self._result_view.delete(0, len(self._result_view.get()))
        self._result_view.insert(0, message)
