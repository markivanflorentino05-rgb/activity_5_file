# even_odd_separator.py
class EvenOddSeparator:
    def __init__(self, input_file_path, even_output_path, odd_output_path):
        self.input_file_path = input_file_path
        self.even_output_path = even_output_path
        self.odd_output_path = odd_output_path

    def read_numbers(self):
        """Read integers from input file (one per line)."""
        numbers = []
        with open(self.input_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        numbers.append(int(line))
                    except ValueError:
                        continue  # skip non-integer lines
        return numbers

    def separate(self):
        numbers = self.read_numbers()
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
    processor = EvenOddSeparator("numbers.txt", "even.txt", "odd.txt")
    processor.separate()