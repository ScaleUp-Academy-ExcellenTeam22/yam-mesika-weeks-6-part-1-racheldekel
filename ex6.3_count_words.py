import string


def clean_text(text):
    """
    function that gets full syntax to remove punctuations and digits using translate it
    :param text: text of sentence
    :return: the words text split to
    """
    exclist = string.punctuation + string.digits
    table = str.maketrans('', '', exclist)
    return text.translate(table).split()


def words_length(sentence):
    """
    function that calculate the letters in sentence
    :param sentence:
    :return: the length of any word in the sentence
    """
    return {word: len(word) for word in sentence}


if __name__ == '__main__':
    text_to_parse = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    new_text = words_length(clean_text(text_to_parse))
    print(new_text)
