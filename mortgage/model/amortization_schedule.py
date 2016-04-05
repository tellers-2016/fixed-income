class AmortizationSchedule:
    """Class that holds details of a mortgage amortization schedule. It will have details of the monthly payments, sum totals of the payments and percentages of the interests"""

    def __init__(self):
        self.payment_schedule = []
        self.totals = {'payments': 0, 'interest': 0, 'principal': 0}
        self.metrics = {'Interest': 0, 'InterestOverPrincipal': 0}

    def __str__(self):
        str_ = ""

        for payment in self.payment_schedule:
            str_ += payment.__str__() + "\n"

        str_ += "\nTotal payments: {},\
              Total Principal Paid: {},\
              Total Interest Paid: {}".format(round(self.totals['payments'], 2),
                                              round(
                                                  self.totals['principal'], 2),
                                              round(self.totals['interest'], 2))

        str_ += "\nInterest Percentage: {}".format(
            round(self.metrics['Interest'], 2))
        str_ += "\nInterest as Percentage of Principal: {}".format(
            round(self.metrics['InterestOverPrincipal'], 2))

        return str_
