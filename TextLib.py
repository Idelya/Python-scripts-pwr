import re
import os

#(?<!...) - nie jest poprzedzona danym wzorcem
#\w\.\w.
#
#(?<=\.|\?)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sentences_pattern = '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
declarative_pattern = '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.)'
interrogative_pattern = '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\?)'
imperative_pattern = '(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\!)'

mail_pattern = [r'\b[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+\b']

data_patterns = [
    r'\b\d{4}-\d{2}-\d{2}\b',
    r'\b\d{4}.\d{2}.\d{2}\b',
    r'\b\d{4}_\d{2}_\d{2}\b',
    r'\b\d{2}-\d{2}-\d{2}\b',
    r'\b\d{2}.\d{2}.\d{2}\b',
    r'\b\d{2}_\d{2}_\d{2}\b',
    r'\b\d{2}-\d{2}-\d{4}\b',
    r'\b\d{2}.\d{2}.\d{4}\b',
    r'\b\d{2}_\d{2}_\d{4}\b',
]

time_patterns = [
    r'\b\d{2}:\d{2}\b',
    r'\b\d{2}-\d{2}\b',
    r'\b\d{2}:\d{2}:\d{2}\b',
]

weeknames = [
    r'\bponiedziałek\b',
    r'\bpon\b',
    r'\bpn\b'
    r'\bwtorek\b',
    r'\bwt\b',
    r'\bśroda\b',
    r'\bśr\b',
    r'\bczwartek\b',
    r'\bczw\b',
    r'\bcz\b',
    r'\bpiątek\b',
    r'\bpt\b',
    r'\bsobota\b',
    r'\bso\b',
    r'\bsob\b',
    r'\bniedziela\b',
    r'\bndz\b',
    r'\bnd\b'
]


def saving(f, *args):
    def wrapper(*args):
        filename = ROOT_DIR+'/Assets/dekorator'
        filename_tmp=filename
        isExist = True
        i = 0
        while isExist:
            filename_tmp = filename
            i += 1
            filename_tmp += str(i)
            isExist = os.path.isfile(filename_tmp + '.txt')

        file = open(filename_tmp+'.txt', "w")
        res = f(*args)
        for elem in res:
            file.write(elem+'\n')
        file.close()
    return wrapper


def open_file(path: str) -> str:
    file = open(path, "r")
    contents = file.read()
    file.close()
    return contents


def isMail(email: str):
    return re.search(mail_pattern, email)


def isDate(date: str):
    for pattern in data_patterns:
        if re.search(pattern, date):
            return True
    return False


def isWeekname(weekname: str):
    for pattern in weeknames:
        if re.search(pattern, weekname):
            return True
    return False


def isDeclarative(sentence: str):
    return re.search(declarative_pattern, sentence)


def isInterrogative(sentence: str):
    return re.search(interrogative_pattern, sentence)


def isImperative(sentence: str):
    return re.search(imperative_pattern, sentence)

@saving
def findAll(text: str, patterns):
    list = []
    for pattern in patterns:
         list_tmp = re.findall(pattern, text)
         for elem in list_tmp:
             list.append(elem)
    return list


def find_word(email: str, text: str):
    words = text.split()
    for word in words:
        if word == email:
            return True
    return False


def seperateSentences(text: str):
    return re.split(sentences_pattern, text)


def analysis(text: str):
    findAll(text, data_patterns)
    findAll(text, weeknames)
    findAll(text, mail_pattern)
    findAll(text, time_patterns)


def count_match_sentences(text, fun):
    sentences = seperateSentences(text)
    i = 0
    for sen in sentences:
        if fun(sen):
            i += 1
    return i


def count_sentences(text: str):
    return [
        count_match_sentences(text, isDeclarative),
        count_match_sentences(text, isInterrogative),
        count_match_sentences(text, isImperative)
    ]
