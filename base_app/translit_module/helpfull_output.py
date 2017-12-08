def deb_print(debug, *some_strings):
    """
    prints while debugging
    :param debug:
    :param some_strings:
    :return:
    """
    if debug == "Y":
        print(*some_strings)