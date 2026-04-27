import os

class EvenOddSeparator:
    def __init__(self, input_file_path, even_output_path, odd_output_path):
        self.input_file_path = input_file_path
        self.even_output_path = even_output_path
        self.odd_output_path = odd_output_path

    def read_numbers(self):
        """Read integers from input file (one per line)."""
        numbers = []
        # Check if file exists
        if not os.path.exists(self.input_file_path):
            print(f"⚠️ File '{self.input_file_path}' not found.")
            print("Creating a sample numbers.txt with 20 integers...")
            self.create_sample_numbers()
        with open(self.input_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        numbers.append(int(line))
                    except ValueError:
                        continue
        return numbers

    def create_sample_numbers(self):
        """Create a sample numbers.txt file with 20 integers."""
        sample_numbers = [
            12, 45, 78, 23, 56, 89, 90, 33, 67, 82,
            41, 50, 63, 74, 19, 38, 91, 44, 77, 100
        ]
        with open(self.input_file_path, 'w') as f:
            for num in sample_numbers:
                f.write(f"{num}\n")
        print(f"✅ Sample file created: {self.input_file_path}")

    def separate(self):
        numbers = self.read_numbers()
        if not numbers:
            print("No numbers loaded. Please check the input file.")
            return
        even_numbers = [num for num in numbers if num % 2 == 0]
        odd_numbers = [num for num in numbers if num % 2 != 0]

        with open(self.even_output_path, 'w') as even_file:
            for num in even_numbers:
                even_file.write(f"{num}\n")

        with open(self.odd_output_path, 'w') as odd_file:
            for num in odd_numbers:
                odd_file.write(f"{num}\n")

        print(f"✅ Found {len(even_numbers)} even numbers → {self.even_output_path}")
        print(f"✅ Found {len(odd_numbers)} odd numbers → {self.odd_output_path}")

if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define file paths inside the same folder as the script
    numbers_path = os.path.join(script_dir, "numbers.txt")
    even_path = os.path.join(script_dir, "even.txt")
    odd_path = os.path.join(script_dir, "odd.txt")

    processor = EvenOddSeparator(numbers_path, even_path, odd_path)
    processor.separate()