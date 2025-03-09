from src.cli_interface import CliParser

def main():
    cli = CliParser()
    args = cli.parse_args()
    print(args)

if __name__ == '__main__':
    main()
    