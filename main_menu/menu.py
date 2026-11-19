class Start:
    def run_menu(self):
        while True:
            print("Welcome to the Game")
            start_input = input("""
        Press 1 to start
        Press 2 to quit
""")
            if start_input == "1":
                return True
            if start_input == "2":
                return False
            print("Please enter either 1 or 2")
