import sys

from templify import start_django


def main():
    commands = sys.argv[1:]
    commands_count = len(commands)
    if not commands_count:
        return "Hello from Templify"
    if commands_count == 1 and commands[0] == 'start_django':
        return start_django()


if __name__ == "__main__":
    main()
