def font_set(f="Arial", s=12, b=False, i=False):
    """
    creates font in a very simple way
    :param f: changes font to any font it is set to
    :param s: sets font size to chosen number
    :param b: makes font bold if set to <1>
    :param i: makes font italic if set to <1>
    :return:
    """

    font = (f, s)

    if (b == True) and (i == True):
        font = (f, s, b, i)

    elif b == 1:
        font = (f, s, b)

    elif i == 1:
        font = (f, s, i)

    return font