# SRTranslate
 A simple script for translating subtitles files

### Inspirations
I had to translate several files from one course. I used the Google feature for this, but it was annoying to translate file by file, so I decided to write something that would automate this for me.

### installation
```
$ pip install -r requirements.txt

```

### How to use it
```
usage: srtranslate.py [-h] [-d DIR] [-s SINGLE] [-l LANGUAGE]

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     Directory where the files are located. (.srt)
  -s SINGLE, --single SINGLE
                        File for translation
  -l LANGUAGE, --language LANGUAGE
                        Please enter your language. example: english = en,
                        Portuguese = en. etc...
                        
$ python -l en -s file.srt or -d Directory containing the files
```

## License
```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2018 Hardwayy

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  1. You just DO WHAT THE FUCK YOU WANT TO.
```
