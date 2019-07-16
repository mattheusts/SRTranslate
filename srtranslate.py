import argparse
import googletrans
from util.translate import translate, translate_file, Colors

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir', help='Directory where the files are located. (.srt)', type=str, required=False)
parser.add_argument('-s', '--single', help='File for translation', type=str, required=False)
parser.add_argument('-l', '--language', help='Please enter your language. example: english = en, Portuguese = pt, German = de etc...', type=str,required=False)
parser.add_argument('-c', '--codes', help="View all language codes", action='store_true')
args = parser.parse_args()


if __name__ == '__main__':

    if args.codes:
        print(googletrans.LANGCODES)
    else:
        if args.dir == None and args.single == None:
            print(Colors.FAIL + 'No file or directory was passed' + Colors.ENDC)
        elif args.dir:
            translate(args.dir, args.language)
        elif args.single:
            translate_file(args.single, args.language)
        else:
            print(Colors.FAIL + 'No file or directory was passed' + Colors.ENDC)
