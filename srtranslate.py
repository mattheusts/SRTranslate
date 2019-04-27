import argparse

from util.translate import Translate, Colors

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir', help='Directory where the files are located. (.srt)', required=False)
parser.add_argument('-s', '--single', help='File for translation', required=False)
parser.add_argument('-l', '--language', help='Please enter your language. example: english = en, Portuguese = en. etc...')
args = parser.parse_args()


if __name__ == '__main__':
    if args.dir == None and args.single == None:
        print(Colors.FAIL + 'No file or directory was passed' + Colors.ENDC)
    elif args.dir:
        Translate(args.dir, args.language, False)
    elif args.single:
        Translate(args.single, args.language)
    else:
        print(Colors.FAIL + 'No file or directory was passed' + Colors.ENDC)