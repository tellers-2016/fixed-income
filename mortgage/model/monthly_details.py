class MonthlyDetails:
    def __init__(self,
                 month,
                 monthly_payment,
                 monthly_principal,
                 monthly_interest,
                 principal_balance,
                 cumulative_interest=0,
                 cumulative_principal=0,
                 cumulative_payment=0):
        self.month = month
        self.payment = monthly_payment
        self.principal = monthly_principal
        self.interest = monthly_interest
        self.principal_balance = principal_balance
        self.cumulative_interest = cumulative_interest
        self.cumulative_principal = cumulative_principal
        self.cumulative_payment = cumulative_payment

    def __str__(self):
        return ("Monthly Principal: {}, Monthly Interest: {}, Monthly Payment: {}, Principal balance: {}, Cumulative Principal: {}, Cumulative Interest: {}, Cumulative Payment: {}  for month: {}"
                .format(self.principal,
                        self.interest,
                        self.payment,
                        self.principal_balance,
                        self.cumulative_principal,
                        self.cumulative_interest,
                        self.cumulative_payment,
                        self.month))
