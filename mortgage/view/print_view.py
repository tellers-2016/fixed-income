from .base_view import BaseView


class PrintView(BaseView):
    """docstring for PrintView"""

    def __init__(self):
        super(PrintView, self).__init__()

    def display_schedule(self, schedule):
        print(schedule)
