def words_length(sentence):
    """
    function that calculate the letters in sentence
    :param sentence:
    :return: the length of any word in the sentence
    """
    return list(map(len, sentence.split()))


if __name__ == '__main__':
    s = "Toto, I've a feeling we're not in Kansas anymore"
    print(words_length(s))
