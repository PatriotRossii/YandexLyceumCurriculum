import string


def strip_punctuation_ru(data):
    table = {ord(e): " " for e in string.punctuation if e != "-"}
    return " ".join([e.strip(string.punctuation).translate(table).replace("  ", " ") for e in data.split()])