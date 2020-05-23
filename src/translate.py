from googletrans import Translator
from googletrans import LANGUAGES
from src.colors import Colors
import os

translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.com.br'
])


def codes_viewer():
    for k, v in LANGUAGES.items():
        print(f'{Colors.OKGREEN} Initials: {Colors.FAIL}{k}\t{Colors.OKGREEN}Language: {Colors.FAIL}{v} {Colors.ENDC}')


def codes(code_lang: str):
    for code, lang in LANGUAGES.items():
        if code == code_lang:
            return True
    return False


def translate(path: str, language: str):
    abspath = os.path.abspath(path)

    if not os.path.exists(abspath + '/' + 'translated_legends'):
        os.mkdir(abspath + '/' + 'translated_legends')
    fileslist = os.listdir(abspath)
    for files in fileslist:
        phrase = []

        if files == 'translated_legends':
            continue

        if not files.split('.')[-1] == '.str':
            filename = files
            print(Colors.WARNING + 'The {} file is being translated'.format(files) + Colors.ENDC)
            with open(abspath + '/' + files) as file:
                for lines in file:
                    if lines[0].rstrip().isalpha():
                        phrase.append(lines.rstrip())
                file.close()

            translation = translator.translate(phrase, dest=language)

            count = 0
            with open(abspath + '/' + 'translated_legends' + '/' + files, 'w') as save:
                with open(abspath + '/' + files) as file:
                    for lines in file:
                        if lines[0].rstrip().isalpha():
                            save.write(translation[count].text + '\n')
                            count += 1
                        else:
                            save.write(lines)
                    file.close()
                save.close()
            print(Colors.OKGREEN + 'The file {} was translated'.format(filename) + Colors.ENDC)
        else:
            continue
    print(Colors.OKGREEN + 'Files have been saved in {}'.format(abspath + '/' + 'translated_legends'))


def translate_file(path: str, language: str):
    abspath = os.path.abspath(path)

    phrase = []
    print(Colors.WARNING + 'The {} file is being translated'.format(abspath.split('/')[-1]) + Colors.ENDC)
    with open(abspath) as file:
        for lines in file:
            if lines[0].rstrip().isalpha():
                phrase.append(lines.rstrip())
        file.close()

    translation = translator.translate(phrase, dest=language)

    count = 0
    with open(language + '-' + path, 'w') as save:
        with open(abspath) as file:
            for lines in file:
                if lines[0].rstrip().isalpha():
                    save.write(translation[count].text + '\n')
                    count += 1
                else:
                    save.write(lines)
            file.close()
        save.close()
    print(Colors.OKGREEN + 'The file {} was translated'.format(abspath.split('/')[-1]) + Colors.ENDC)
