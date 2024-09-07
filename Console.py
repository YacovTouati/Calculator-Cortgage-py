class Console:
    @staticmethod
    def read_number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def read_number_with_range(prompt, min_val, max_val):
        while True:
            try:
                value = float(input(prompt))
                if min_val <= value <= max_val:
                    return value
                else:
                    print(f"Enter a value between {min_val} and {max_val}")
            except ValueError:
                print("Invalid input. Please enter a number.")
