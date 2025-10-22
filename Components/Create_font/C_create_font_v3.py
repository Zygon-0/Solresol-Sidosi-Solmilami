def font_set(font_size=12, fancy_font=0, bold=0, italic=0):
    """
    creates font in a very simple way
    :param fancy_font: changes font to gorgia if set to <1>
    :param font_size: sets font size to chosen number (default <12>)
    :param bold: makes font bold if set to <1>
    :param italic: makes font italic if set to <1>
    :return:
    """

    font = ["Arial", font_size]

    if fancy_font:
        font[0] = "Georgia"

    if bold:
        font.append("bold")

    if italic:
        font.append("italic")

    return tuple(font)