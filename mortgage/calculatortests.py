import unittest

from model.monthly_details import MonthlyDetails
from model.amortization_schedule import AmortizationSchedule
from calculator import Calculator



class TestCalculator(unittest.TestCase):
    """Test suite for the mortgage calculator"""

    def setUp(self):
        self.rate = 6.5
        self.term = 30
        self.principal = 200000

    def test_calculate_monthly_payment(self):
        monthly_payment = round(Calculator.calculate_monthly_payment(self.principal,
                                                                     self.rate,
                                                                     self.term),
                                2)

        self.assertEqual(1264.14,
                         monthly_payment,
                         "The monthly payment for a principal of {}, rate {} and term {} should be 1264.14"
                         .format(self.principal, self.rate, self.term))

    def test_convert_rate_to_monthly(self):
        self.assertEqual(0.0054, round(Calculator.convert_rate_to_monthly(self.rate), 4),
                         "The monthly rate for 6.5 should be 0.0054")

    def test_convert_term_to_monthly(self):
        self.assertEqual(360, Calculator.convert_term_to_monthly(self.term),
                         "The monthly term for a 30 year term is 360")

    def test_calculate_loan_balance_start(self):
        months_elapsed = 0

        loan_balance = round(Calculator.calculate_loan_balance(self.principal,
                                                               self.rate,
                                                               self.term,
                                                               months_elapsed), 0)
        self.assertEqual(
            loan_balance, self.principal, "The loan balance should be the full principal")

    def test_calculate_loan_balance_end(self):
        months_elapsed = 360

        loan_balance = round(Calculator.calculate_loan_balance(self.principal,
                                                               self.rate,
                                                               self.term,
                                                               months_elapsed), 0)

        self.assertEqual(
            loan_balance, 0, "the loan balance at the end of the mortgage term should be 0")

    def test_calculate_monthly_interest(self):
        monthly_interest = Calculator.calculate_monthly_interest(
            self.principal, self.rate)
        self.assertEqual(round(monthly_interest, 2), 1083.33,
                         "The monthly interest on principal of {} should be {}".
                         format(self.principal, 200))

    def test_calculate_mortgage_metrics(self):
        amortization_schedule = AmortizationSchedule()

        for i in range(5):
            monthly_payment = MonthlyDetails(i, 200, 50, 150, 2000)
            amortization_schedule.payment_schedule.append(monthly_payment)

        Calculator.calculate_mortgage_metrics(amortization_schedule)

        self.assertEqual(
            amortization_schedule.totals['payments'], 1000, "The payments must total 1000")
        self.assertEqual(
            amortization_schedule.totals['interest'], 750, "The interest must total 250")
        self.assertEqual(amortization_schedule.totals[
                          'principal'], 250, "The total principal paid back must be 750")

        self.assertEqual(amortization_schedule.metrics[
                          'Interest'], 75, "The Interest is 75% of the total payments")
        self.assertEqual(amortization_schedule.metrics[
                          'InterestOverPrincipal'], 300, "The Interest is 300% of the principal")

    def __assertMonthlySchedule(self, monthly_schedule, month, payment, principal, interest, balance):
        self.assertEqual(
            monthly_schedule.month, month, "The month must be {}".format(month))
        self.assertEqual(monthly_schedule.principal, principal,
                         "The principal must be {}".format(principal))
        self.assertEqual(monthly_schedule.interest, interest,
                         "The interest must be {}".format(interest))
        self.assertEqual(monthly_schedule.payment, payment,
                         "The monthly payment must be {}".format(payment))
        self.assertEqual(monthly_schedule.principal_balance,
                         balance, "The balance must be {}".format(balance))

    def test_calculate_schedule(self):
        schedule = Calculator.calculate_schedule(
            self.principal, self.rate, self.term)

        # Check the first month
        self.__assertMonthlySchedule(
            schedule.payment_schedule[0], 1, 1264.14, 180.81, 1083.33, 199819.19)

        # Check the last month
        self.__assertMonthlySchedule(
            schedule.payment_schedule[359], 360, 1252.77, 1252.77, 0, 0)

        # Check the totals
        self.assertEqual(round(schedule.totals[
                         'payments'], 2), 455079.03, "The total monthly payments made must be 455079.03")
        self.assertEqual(round(schedule.totals[
                         'interest'], 2), 255079.03, "The total interest paid must be 255079.03")
        self.assertEqual(round(schedule.totals[
                         'principal'], 2), 200000.0, "The total principal repaid must be 200000.0")

        # Check the percentages
        self.assertEqual(round(schedule.metrics[
                         'Interest'], 2), 56.05, "The Interest as a percentage of the total payments must be 56.05")
        self.assertEqual(round(schedule.metrics[
                         'InterestOverPrincipal'], 2), 127.54, "The Interest as a percentage of the principal borrowed must be 127.54")

        # Check the integrity of the data
        last_payment = schedule.payment_schedule[
            len(schedule.payment_schedule) - 1]

        self.assertEqual(last_payment.cumulative_principal, round(schedule.totals[
                         'principal'], 2), "The cumulative principal for the last monthly payment should equal the total principal repaid")
        self.assertEqual(last_payment.cumulative_interest, round(schedule.totals[
                         'interest'], 2), "The cumulative interest for the last monthly payment should equal the total interest paid")
        self.assertEqual(last_payment.cumulative_payment, round(schedule.totals[
                         'payments'], 2), "The cumulative payment for the last monthly payment should equal the total payments made")


if __name__ == '__main__':
    unittest.main()
