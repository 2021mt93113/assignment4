def censor_string(string, lst, char):
    modified_string = string.split()
    returned_words = [word if word not in lst else char * len(word) for word in modified_string]
    return ' '.join(returned_words)
