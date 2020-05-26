from calculator import Calculator
from view.print_view import PrintView
from view.graph_view import GraphView


class Controller(object):
    """The Controller class for the mortgage calculator"""

    def __init__(self):
        super(Controller, self).__init__()
        self.view = GraphView()
        # self.view = PrintView()

    def calculate_mortgage_schedule(self):
        # These could be obtained from user input by the view
        principal = 267500
        rate = 3.875
        term = 30
        early_payment = 0
        frequency = 0

        # Run the calculation
        schedule = Calculator.calculate_schedule(principal, rate, term, early_payment, frequency)

        # Display it
        self.view.display_schedule(schedule)


controller = Controller()
controller.calculate_mortgage_schedule()
