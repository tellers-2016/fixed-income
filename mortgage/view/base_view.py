import abc


class BaseView(abc.ABC):
    """docstring for BaseView"""

    def __init__(self):
        super(BaseView, self).__init__()

    @abc.abstractmethod
    def display_schedule(self, schedule):
        raise NotImplementedError("Base class function. Not implemented.")
