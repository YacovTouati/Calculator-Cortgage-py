import locale

class MortgageReport:
    def __init__(self, calculator):
        self.calculator = calculator
        # Try setting to 'en_US.UTF-8' locale, fallback to default if unavailable
        try:
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # You can change this to a different locale if needed
        except locale.Error:
            print("Warning: Locale 'en_US.UTF-8' not available. Falling back to default locale.")
            locale.setlocale(locale.LC_ALL, '')  # Use the system default locale if the desired one is unavailable

    def print_payment_schedule(self):
        print("\nPAYMENT SCHEDULE")
        print("----------------")
        for balance in self.calculator.get_remaining_balances():
            try:
                print(locale.currency(balance, grouping=True))
            except ValueError:
                print(f"${balance:,.2f}")  # Fallback to simple formatting if currency formatting fails

    def print_mortgage(self):
        mortgage = self.calculator.calculate_mortgage()
        try:
            mortgage_formatted = locale.currency(mortgage, grouping=True)
        except ValueError:
            mortgage_formatted = f"${mortgage:,.2f}"  # Fallback to simple formatting
        print("\nMORTGAGE")
        print("--------")
        print(f"Monthly Payments: {mortgage_formatted}")
