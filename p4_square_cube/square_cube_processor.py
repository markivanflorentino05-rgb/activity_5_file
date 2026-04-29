<<<<<<< HEAD
import os

class SquareCubeTransformer:
    def __init__(self, input_file_path, even_squares_path, odd_cubes_path):
        self.input_file_path = input_file_path
        self.even_squares_path = even_squares_path
        self.odd_cubes_path = odd_cubes_path

    def read_integers(self):
        numbers = []
        # Auto-create if missing
        if not os.path.exists(self.input_file_path):
            print(f"⚠️ File '{self.input_file_path}' not found. Creating sample file...")
            self.create_sample_integers()
=======
# square_cube_processor.py
class SquareCubeTransformer:
    def __init__(self, input_file_path, even_squares_path, odd_cubes_path):
        self.input_file_path = input_file_path
        self.even_squares_path = even_squares_path      # double.txt
        self.odd_cubes_path = odd_cubes_path            # triple.txt

    def read_integers(self):
        numbers = []
>>>>>>> c10d9e3ef1337412e8a39926ad34beb777bfddf0
        with open(self.input_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        numbers.append(int(line))
                    except ValueError:
                        continue
        return numbers

<<<<<<< HEAD
    def create_sample_integers(self):
        """Create a sample integers.txt with 20 integers."""
        sample_numbers = [
            3, 4, 7, 8, 11, 12, 15, 16, 19, 20,
            23, 24, 27, 28, 31, 32, 35, 36, 39, 40
        ]
        with open(self.input_file_path, 'w') as f:
            for num in sample_numbers:
                f.write(f"{num}\n")
        print(f"✅ Sample integers file created: {self.input_file_path}")

    def process(self):
        integers = self.read_integers()
        if not integers:
            print("No integers loaded. Please check input file.")
            return
=======
    def process(self):
        integers = self.read_integers()
>>>>>>> c10d9e3ef1337412e8a39926ad34beb777bfddf0
        squares_of_evens = [num ** 2 for num in integers if num % 2 == 0]
        cubes_of_odds = [num ** 3 for num in integers if num % 2 != 0]

        with open(self.even_squares_path, 'w') as even_file:
            for value in squares_of_evens:
                even_file.write(f"{value}\n")

        with open(self.odd_cubes_path, 'w') as odd_file:
            for value in cubes_of_odds:
                odd_file.write(f"{value}\n")

        print(f"✅ Even numbers squared → {self.even_squares_path} ({len(squares_of_evens)} values)")
        print(f"✅ Odd numbers cubed → {self.odd_cubes_path} ({len(cubes_of_odds)} values)")

if __name__ == "__main__":
<<<<<<< HEAD
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "integers.txt")
    doubles_path = os.path.join(script_dir, "double.txt")
    triples_path = os.path.join(script_dir, "triple.txt")

    transformer = SquareCubeTransformer(input_path, doubles_path, triples_path)
=======
    transformer = SquareCubeTransformer("integers.txt", "double.txt", "triple.txt")
>>>>>>> c10d9e3ef1337412e8a39926ad34beb777bfddf0
    transformer.process()