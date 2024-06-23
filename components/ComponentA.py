class ExampleCommand1:
    COMMANDS = ['ex_cmd_1', 'ex_cmd_2']  # List of commands

    def execute(self, command, args=None):
        if args is None:
            args = []
        if command == self.COMMANDS[0]:
            print("Executing ex_cmd_1, with arguments: {}".format(args))
        elif command == self.COMMANDS[1]:
            print("Executing ex_cmd_2, with arguments: {}".format(args))
        else:
            print(f"Unknown command: {command}")


class ExampleCommand2:
    COMMANDS = ['ex_cmd_3', 'ex_cmd_4']  # List of commands

    def execute(self, command, args=None):
        if args is None:
            args = []
        if command == self.COMMANDS[0]:
            print("Executing ex_cmd_3, with arguments: {}".format(args))
        elif command == self.COMMANDS[1]:
            print("Executing ex_cmd_4, with arguments: {}".format(args))
        else:
            print(f"Unknown command: {command}")
