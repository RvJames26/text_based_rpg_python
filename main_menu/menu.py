class Start:

    def __init__(self, start_val):
        self.start_val = start_val

    def run_menu(self):
        while True:
                print("Welcome to the Game")
                start_input = input(f"""
        Press 1 to start
        Press 2 to quit
""")
                if start_input == "1":
                    break
                elif start_input == "2":
                    break
                else:
                    print("Please enter either 1 or 2")
                continue
