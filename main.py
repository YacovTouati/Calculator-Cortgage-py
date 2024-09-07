from Console import Console  # Assuming Console class is in a separate file named console.py
from MortgageCalculator import MortgageCalculator
from MortgageReport import MortgageReport


class Main:
    @staticmethod
    def main():
        principal = Console.read_number_with_range("Principal: ", 1000, 1_000_000)
        annual_interest = Console.read_number_with_range("Annual Interest Rate: ", 1, 30)
        years = Console.read_number_with_range("Period (Years): ", 1, 30)

        calculator = MortgageCalculator(principal, annual_interest, years)
        report = MortgageReport(calculator)
        report.print_mortgage()
        report.print_payment_schedule()

if __name__ == "__main__":
    Main.main()
