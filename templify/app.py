import sys

from templify.services import start_django


def main():
    commands = sys.argv[1:]
    commands_count = len(commands)
    if not commands_count:
        return "Hello from Templify"
    if commands_count == 1 and commands[0] == 'from_django':
        return start_django()
    if commands_count == 1 and commands[0] == 'start':
        return start_django()
    else:
        return 'Command not found'


if __name__ == "__main__":
    main()
