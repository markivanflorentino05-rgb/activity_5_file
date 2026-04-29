# square_cube_processor.py
class SquareCubeTransformer:
    def __init__(self, input_file_path, even_squares_path, odd_cubes_path):
        self.input_file_path = input_file_path
        self.even_squares_path = even_squares_path      # double.txt
        self.odd_cubes_path = odd_cubes_path            # triple.txt

    def read_integers(self):
        numbers = []
        with open(self.input_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        numbers.append(int(line))
                    except ValueError:
                        continue
        return numbers

    def process(self):
        integers = self.read_integers()
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
    transformer = SquareCubeTransformer("integers.txt", "double.txt", "triple.txt")
    transformer.process()