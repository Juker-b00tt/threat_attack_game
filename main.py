def start_game():
    print("=== Welcome to Virus Baster Game ===")
    is_running = True

    while is_running:
        command = input("Select. (move/attack/quit):").lower()

        if command == "move":
            print("moved!")
        elif command == "attack":
            print("attacked!")
        elif command == "quit":
            print("finished!")
            is_running = False
        else:
            print("INVALID COMMAND.")
        
start_game()