import os

class HighestGWAFinder:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def read_students(self):
        """Return list of tuples (name, gwa). Auto-create sample file if missing."""
        students = []
        # Check if file exists, if not create sample
        if not os.path.exists(self.input_file_path):
            print(f"⚠️ File '{self.input_file_path}' not found. Creating sample file...")
            self.create_sample_students()
        with open(self.input_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) == 2:
                    name = parts[0].strip()
                    try:
                        gwa = float(parts[1].strip())
                        students.append((name, gwa))
                    except ValueError:
                        continue  # skip lines with invalid GWA
        return students

    def create_sample_students(self):
        """Create a sample students.txt with 20 entries."""
        sample_data = [
            "Maria Santos, 1.25",
            "Jose Rizal, 1.75",
            "Andres Bonifacio, 1.50",
            "Gabriela Silang, 1.00",
            "Emilio Aguinaldo, 2.00",
            "Melchora Aquino, 1.80",
            "Apolinario Mabini, 1.60",
            "Gregoria de Jesus, 1.40",
            "Juan Luna, 2.20",
            "Antonio Luna, 1.90",
            "Diego Silang, 2.10",
            "Josefa Llanes Escoda, 1.35",
            "Marcelo H. del Pilar, 1.95",
            "Leona Florentino, 1.70",
            "Francisco Balagtas, 2.05",
            "Nemesio Prudente, 1.55",
            "Leticia Ramos Shahani, 1.65",
            "Carlos P. Romulo, 1.85",
            "Fe del Mundo, 1.45",
            "Ramon Magsaysay, 1.75"
        ]
        with open(self.input_file_path, 'w') as f:
            for line in sample_data:
                f.write(line + '\n')
        print(f"✅ Sample students file created: {self.input_file_path}")

    def find_highest_gwa_student(self):
        """Returns (name, gwa) of student with smallest GWA (best)."""
        students = self.read_students()
        if not students:
            return None
        best_student = min(students, key=lambda s: s[1])  # lower GWA is better
        return best_student

    def display_result(self):
        result = self.find_highest_gwa_student()
        if result:
            name, gwa = result
            print(f"🏆 Student with the highest GWA: {name} (GWA = {gwa})")
        else:
            print("No valid student records found.")

if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    students_path = os.path.join(script_dir, "students.txt")
    finder = HighestGWAFinder(students_path)
    finder.display_result()