import argparse
import os

class CliParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='A paw-some CLI tool to fluff through files!',
            epilog='Thanks for using the FluffScript CLI tool! Keep wagging!'
        )
        self.parser.add_argument(
            'source_path', 
            type=str, 
            help='Path to the FluffScript source file'
        )
        self.parser.add_argument(
            '-v', '--version', 
            action='version', 
            version='%(prog)s 1.0',
            help='Show the version of the FluffScript tool and exit'
        )

    def parse_args(self):
        args = self.parser.parse_args()
        if not os.path.exists(args.source_path):
            self.parser.error(f"The fluffy file {args.source_path} does not exist. Check your paws!")
        return args
