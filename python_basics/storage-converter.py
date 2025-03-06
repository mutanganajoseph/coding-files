class StorageConverter:
    def __init__(self):
        self.units = {
            "B": 1,
            "KB": 1024,
            "MB": 1024 ** 2,
            "GB": 1024 ** 3,
            "TB": 1024 ** 4,
            "PB": 1024 ** 5,
            "EB": 1024 ** 6,
            "ZB": 1024 ** 7,
            "YB": 1024 ** 8
        }

    def convert(self, from_unit, to_unit, value):
        """Convert value from one unit to another."""
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError("Invalid units")
        # Convert to bytes first, then to the target unit
        value_in_bytes = value * self.units[from_unit]
        return value_in_bytes / self.units[to_unit]

    def display_units(self):
        """Displays all available units."""
        return list(self.units.keys())


def main():
    converter = StorageConverter()

    print("\nAvailable units: ", converter.display_units())
    while True:
        try:
            # Get user input for from_unit, to_unit, and value
            from_unit = input("Enter the source unit (e.g., 'MB'): ").upper()
            to_unit = input("Enter the target unit (e.g., 'GB'): ").upper()
            value = float(input(f"Enter the value to convert from {from_unit} to {to_unit}: "))

            # Perform the conversion
            result = converter.convert(from_unit, to_unit, value)
            print(f"{value} {from_unit} is {result} {to_unit}\n")

        except ValueError as ve:
            print(f"Error: {ve}")
            continue  # If input is invalid, restart the loop

        # Ask if the user wants to continue
        continue_choice = input("Do you want to make another conversion? (y/n): ").lower()
        if continue_choice != "y":
            break


if __name__ == "__main__":
    main()
