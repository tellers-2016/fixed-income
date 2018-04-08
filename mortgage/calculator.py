from model.amortization_schedule import AmortizationSchedule
from model.monthly_details import MonthlyDetails




class Calculator:
    """Mortgage calculation class. Calculates the monthly payment, interest, etc"""

    def __init__(self):
        self.last_value = 0



    @staticmethod
    def convert_rate_to_monthly(rate):
        """Convert the rate from an annual percentage to a monthly fraction."""
        return rate / 12 / 100

    @staticmethod
    def convert_term_to_monthly(term):
        """Convert the term of the mortgage from number of years to number of months"""
        return term * 12

    @staticmethod
    def calculate_monthly_payment(principal, rate, term):
        """Calculate the monthly payment for a given mortgage. This is the main formula"""
        monthly_rate = Calculator.convert_rate_to_monthly(rate)
        monthly_term = Calculator.convert_term_to_monthly(term)

        return (monthly_rate * principal) / (1 - ((1 + monthly_rate) ** (-1 * monthly_term)))

    #@staticmethod
    # def calculate_loan_balance(principal, rate, term, months_elapsed):
    #     """ Calculate for a given mortgage, based on months_elapsed, what is the outstanding
    #     principal balance
    #     :param principal:
    #     :param rate:
    #     :param term:
    #     :param months_elapsed:
    #     :return: The balance of the principal amount yet to be re-paid
    #     """
    #     monthly_rate = Calculator.convert_rate_to_monthly(rate)
    #     monthly_term = Calculator.convert_term_to_monthly(term)
    #
    #     factor = (1 + monthly_rate) ** monthly_term
    #
    #     return (factor - ((1 + monthly_rate) ** months_elapsed)) * principal / (factor - 1)

    @staticmethod
    def calculate_monthly_interest(principal_balance, rate):
        monthly_rate = Calculator.convert_rate_to_monthly(rate)
        return principal_balance * monthly_rate


    @staticmethod
    def calculate_mortgage_metrics(amortization_schedule, totals):
        """ Calculates the metrics for a given amortization schedule.
        :param amortization_schedule: The amortization schedule that has details of the monthly payments of a mortgage
        :param totals: The totals calculated for the payment, interest, etc. that are used to calculate the metrics
        :return: Returns the amortization schedule with the metric values filled in
        """

        metrics = {'Interest': 0, 'InterestOverPrincipal': 0}

        # Once the totals are calculated, calculate the percentage metrics
        metrics['Interest'] = totals['interest'] / totals['payments'] * 100
        metrics['InterestOverPrincipal'] = totals[
            'interest'] / totals['principal'] * 100

        # Fill the calculated values into the amortization_schedule object
        amortization_schedule.totals = totals
        amortization_schedule.metrics = metrics

        return amortization_schedule

    @staticmethod
    def is_time_to_make_early_payment(current_month, early_payment_frequency):
        if early_payment_frequency == 0:
            return False

        return current_month % early_payment_frequency == 0

    @staticmethod
    def calculate_schedule(principal, rate, term, early_payment=0, early_payment_frequency=0):
        """ Calculate the amortization schedule of a mortgage
        :param principal: The Principal borrowed
        :param rate: The annual rate of interest of the mortgage
        :param term: The term of the mortgage in years
        :return:
        """
        monthly_term = Calculator.convert_term_to_monthly(term)
        monthly_payment = round(Calculator.calculate_monthly_payment(principal, rate, term), 2)

        principal_balance = principal
        current_month = 1

        amortization_schedule = AmortizationSchedule()
        totals = amortization_schedule.totals

        while principal_balance > 0:
            if Calculator.is_time_to_make_early_payment(current_month, early_payment_frequency):
                totals['early'] += early_payment
                principal_balance -= early_payment

            # Calculate the monthly principal and interest
            monthly_interest = round(Calculator.calculate_monthly_interest(principal_balance,
                                                                           rate), 2)

            if principal_balance > monthly_payment:
                monthly_principal = round((monthly_payment - monthly_interest), 2)
                principal_balance = round((principal_balance - monthly_principal), 2)
            else:
                # This is typically for the last month when the balance is less than the
                # monthly payment
                monthly_interest = 0
                monthly_principal = principal_balance
                principal_balance = 0
                monthly_payment = monthly_principal

            # Add to the totals
            totals['payments'] += monthly_payment
            totals['interest'] += monthly_interest
            totals['principal'] += monthly_principal

            monthly_details = MonthlyDetails(current_month,
                                             monthly_payment,
                                             monthly_principal,
                                             monthly_interest,
                                             principal_balance,
                                             round(totals['interest'], 2),
                                             round(totals['principal'], 2),
                                             round(totals['payments'], 2)
                                             )

            # Store the monthly payment in the amortization schedule
            amortization_schedule.payment_schedule.append(monthly_details)

            # Increment the month counter
            current_month += 1

        return Calculator.calculate_mortgage_metrics(amortization_schedule, totals)

        # print(amortization_schedule)

        # return amortization_schedule
