class MortgageCalculator:
    MONTHS_IN_YEAR = 12
    PERCENT = 100

    def __init__(self, principal, annual_interest, years):
        self.principal = principal
        self.annual_interest = annual_interest
        self.years = years

    def calculate_balance(self, number_of_payments_made):
        monthly_interest = self.get_monthly_interest()
        number_of_payments = self.get_number_of_payments()

        balance = self.principal * (pow(1 + monthly_interest, number_of_payments) - pow(1 + monthly_interest, number_of_payments_made)) / (pow(1 + monthly_interest, number_of_payments) - 1)

        return balance

    def calculate_mortgage(self):
        monthly_interest = self.get_monthly_interest()
        number_of_payments = self.get_number_of_payments()

        mortgage = self.principal * (monthly_interest * pow(1 + monthly_interest, number_of_payments)) / (pow(1 + monthly_interest, number_of_payments) - 1)

        return mortgage

    def get_remaining_balances(self):
        number_of_payments = int(self.get_number_of_payments())  # Cast to int to avoid float issues
        balances = [self.calculate_balance(month) for month in range(1, number_of_payments + 1)]
        return balances

    def get_monthly_interest(self):
        return self.annual_interest / self.PERCENT / self.MONTHS_IN_YEAR

    def get_number_of_payments(self):
        return self.years * self.MONTHS_IN_YEAR  # Ensure this returns an integer
