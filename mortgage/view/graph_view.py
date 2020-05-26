from .base_view import BaseView
import matplotlib.pyplot as plt


class GraphView(BaseView):
    """docstring for GraphView"""

    def __init__(self):
        super(GraphView, self).__init__()

    def display_schedule(self, schedule):
        """Graphs out the details of the schedule using matplotlib"""

        pay_schedule = schedule.payment_schedule

        # Create the series to be graphed out
        interest = []
        principal = []
        payments = []

        for payment in pay_schedule:
            interest.append(payment.cumulative_interest)
            principal.append(payment.principal_balance)
            payments.append(payment.cumulative_payment)

        x_axis = range(0, (len(pay_schedule)))

        plt.style.use('bmh')

        # plt.plot(x_axis, interest, x_axis, principal,
                 # x_axis, payments)

        plt.plot(x_axis, interest, label='Interest')
        plt.plot(x_axis, principal, label='Principal')
        plt.plot(x_axis, payments, label='Payment')
        plt.legend(loc=0)

        plt.xlabel('Months')
        plt.ylabel("Dollars")
        plt.title("Mortgage Payment Schedule")
        plt.text(1, 210000, "Principal borrowed")
        plt.annotate('Max Interest',
                     xy=(360, interest[359]),
                     xytext=(330, 350000),
                     arrowprops=dict(facecolor='black', shrink=0.05))
        plt.annotate('Max Payment',
                     xy=(360, payments[359]),
                     xytext=(250, 475000),
                     arrowprops=dict(facecolor='red', shrink=0.05))

        plt.show()

        plt.pie([schedule.totals['interest'], schedule.totals['principal']],
                labels=["Interest", "Principal"],
                explode=(0, 0.1))
        plt.show()
