def font_set(f=False, s=12, b=False, i=False):
    """
    creates font in a very simple way
    :param f: changes font to gorgia if set to <True>
    :param s: sets font size to chosen number
    :param b: makes font bold if set to <True>
    :param i: makes font italic if set to <True>
    :return:
    """

    font = ["Arial", s]

    if f is True:
        font.pop(0)
        font.append("Georgia")
        font.reverse()

    if b is True:
        font.append("bold")

    if i is True:
        font.append("italic")

    return tuple(font)