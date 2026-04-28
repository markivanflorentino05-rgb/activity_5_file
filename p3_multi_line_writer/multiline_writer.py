# multiline_writer.py
class MultiLineFileWriter:
    def __init__(self, output_file_path):
        self.output_file_path = output_file_path

    def write_lines(self):
        lines_to_write = []
        print(f"Writing to {self.output_file_path} (type 'exit' to finish or answer 'n'):")
        while True:
            one_line = input("Enter line: ")
            lines_to_write.append(one_line)
            more_lines = input("Are there more lines y/n? ").strip().lower()
            if more_lines != 'y':
                break

        with open(self.output_file_path, 'w') as file:
            for line in lines_to_write:
                file.write(line + '\n')

        print(f"✅ {len(lines_to_write)} lines written to {self.output_file_path}")

if __name__ == "__main__":
    writer = MultiLineFileWriter("mylife.txt")
    writer.write_lines()