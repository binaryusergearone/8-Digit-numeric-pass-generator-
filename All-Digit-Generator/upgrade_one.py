class NumericPasswordGenerator:
    def __init__(self, start, end, filename):
        self.start = start
        self.end = end
        self.filename = filename

    def generate(self):
        try:
            start_num = int(self.start)
            end_num = int(self.end)

            if len(self.start) != len(self.end):
                print("Error: Mismatched digit lengths. Try again.")
                return

            with open(self.filename, 'w') as file:
                for num in range(start_num, end_num + 1):
                    file.write(f"{str(num).zfill(len(self.start))}\n")

            print(f"List stored in {self.filename}.")
        except ValueError:
            print("Error: Invalid input. Numbers only.")
        except Exception as e:
            print(f"Something went wrong: {e}")

if __name__ == "__main__":
    start = input("Start: ")
    end = input("End: ")
    filename = input("File: ")

    generator = NumericPasswordGenerator(start, end, filename)
    generator.generate()
