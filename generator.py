class NumberGenerator:
    def __init__(self):
        self.filename = "pass.txt"

    def get_range(self):
        start, end = input("Start (8 digits): "), input("End (8 digits): ")
        return int(start), int(end) if start.isdigit() and end.isdigit() and len(start) == 8 and len(end) == 8 and int(start) <= int(end) else self.get_range()

    def generate(self, start, end):
        with open(self.filename, "w") as f:
            f.writelines(f"{i:08d}\n" for i in range(start, end + 1))

NumberGenerator().generate(*NumberGenerator().get_range())
