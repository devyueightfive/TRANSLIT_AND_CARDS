class TransliterationError(Exception):
    """Exception raised for errors in the input.
        Attributes:
            expr -- input expression in which the error occurred
            msg  -- explanation of the error
    """
    def __init__(self, expr, msg):
        """

        :param expr:
        :param msg:
        """
        self.expr = expr
        self.msg = msg


def get_transliteration(some_string, rules_dictionary):
    """

    :param some_string:
    :param rules_dictionary:
    :return:    translit from some_string
    """
    result = ''
    key_list = rules_dictionary.keys()
    for s in some_string:
        if s in key_list:
            result += rules_dictionary[s]
        else:
            result += s
    return result


def reversed_rules_as_list_of_sorted_tuples(rules_dictionary):
    """
    returns sorted rule-list for de-translit process
    :param rules_dictionary:
    :return:
    """
    result = []
    for (k, v) in rules_dictionary.items():
        result.append((v, k))
    result = sorted(result, key=lambda x: x[0], reverse=False)
    result = sorted(result, key=lambda x: len(x[0]), reverse=True)
    return result


def normalize_text(some_string, rules_dictionary):
    """
    de-translit process
    :param some_string: text
    :param rules_dictionary:
    :return:    normal text from translit
    """
    result = ''
    rules_dictionary = reversed_rules_as_list_of_sorted_tuples(rules_dictionary)
    max_len = max([len(x[0]) for x in rules_dictionary])
    # print(rules_dictionary)
    rules_dictionary = dict(rules_dictionary)
    key_list = rules_dictionary.keys()

    begin = 0
    end = len(some_string)
    # step = 0
    while end - begin > 0:
        key_len = max_len
        while end - begin < key_len:
            key_len -= 1
        success = False
        while success is False:
            key = some_string[begin:begin + key_len]
            if key in key_list:
                begin += key_len
                result += rules_dictionary[key]
                success = True
            else:
                key_len -= 1
                if key_len == 0:
                    begin += 1
                    result += key
                    success = True
            # step += 1
            # print("step ", step, ":")
            # print(end, begin, key_len, success, key, result)
            # input("click")

    return result
