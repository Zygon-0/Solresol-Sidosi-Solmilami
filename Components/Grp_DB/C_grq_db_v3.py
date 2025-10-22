questions_list = [   # progressive sorted diffs for questions (~4)
    # all diffs
    [
        # questions to choose from within diff 1
        [
            ["l", "What is the first letter in the Solresol alphabet?", 10],
            ["b", "Sol", "#3C9", "#33BAFE", None, 5, 2, "\"Sol\", is the 5th letter in Solresol"],
            ["b", "Do", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "La", "#06F", "#0055FF", None, 5, 3, "\"La\", is the 6th letter in Solresol"]
        ],
        [
            ["l", "Which Solresol syllable comes after Do?", 10],
            ["b", "La", "#06F", "#0055FF", None, 5, 2, "\"la\", comes after \"Sol\", in Solresol"],
            ["b", "Re", "#F80", "#FFAA00", None, 5, 1, ""]
        ],
        [
            ["l", "Which syllable comes before Mi?", 10],
            ["b", "Si", "#E33", "#FF3333", None, 5, 2, "\"Si\", is the last letter in Solresol, so it doesn't come before anything"],
            ["b", "Re", "#F80", "#FFAA00", None, 5, 1, ""],
            ["b", "Sol", "#3C9", "#33BAFE", None, 5, 3, "\"Sol\", comes before \"La\", in Solresol"]
        ],
        [
            ["l", "Which Solresol syllable has correlations to the English word sunlight?", 10],
            ["b", "Mi", "#06F", "#0055FF", None, 5, 2, "\"Mi-ar\", I dont think that's a word"],
            ["b", "Sol", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "Re", "#F80", "#FFAA00", None, 5, 3, "\"Rear\", that is a word, but not one related to sunlight"],
            ["b", "Do", "#E33", "#FF3333", None, 5, 4, "\"Do-ar\", I dont think that's a word"]
        ],
        [
            ["l", "What is the third syllable in the Solresol scale?", 10],
            ["b", "Mi", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "Fa", "#06F", "#0055FF", None, 5, 2, "\"Fa\", is the 4th letter in Solresol"]
        ],
        [
            ["l", "Which Solresol syllable comes before Si?", 10],
            ["b", "La", "#06F", "#0055FF", None, 5, 1, ""],
            ["b", "Do", "#E33", "#FF3333", None, 5, 2, "\"Do\", comes before \"Re\", in Solresol"],
            ["b", "Mi", "#3C9", "#33BAFE", None, 5, 3, "\"Mi\", comes before \"Fa\", in Solresol"],
            ["b", "Fa", "#F80", "#FFAA00", None, 5, 4, "\"Fa\", comes before \"Sol\", in Solresol"]
        ],
        [
            ["l", "How many syllables are in Solresol?", 10],
            ["b", "5", "#06F", "#0055FF", None, 5, 2, "Maybe try counting them in your head"],
            ["b", "6", "#E33", "#FF3333", None, 5, 3, "Close but not quite I'm afraid"],
            ["b", "7", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "8", "#F80", "#FFAA00", None, 5, 4, "Woah there budy, you seem to have overshot a bit"]
        ],
        [
            ["l", "Which is not a syllable in Solresol?", 10],
            ["b", "Si", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "La", "#06F", "#0055FF", None, 5, 2, "\"La\" is the 6th letter in Solresol"],
            ["b", "Fa", "#F80", "#FFAA00", None, 5, 3, "\"Fa\" is the 4th letter in Solresol"],
            ["b", "Si", "#E33", "#FF3333", None, 5, 4, "\"Si\" is the 7th letter in Solresol"]
        ],
        [
            ["l", "Which syllable comes directly after Fa?", 10],
            ["b", "La", "#06F", "#0055FF", None, 5, 2, "\"La\" comes directly after \"Sol\", in Solresol"],
            ["b", "Mi", "#E33", "#FF3333", None, 5, 3, "\"Mi\" comes directly after \"Re\", in Solresol"],
            ["b", "Sol", "#3C9", "#33BAFE", None, 5, 1, ""]
        ],
        [
            ["l", "Which syllable is last in the Solresol scale?", 10],
            ["b", "Fa", "#F80", "#FFAA00", None, 5, 2, "\"Fa\" is the verry middle letter in Solresol"],
            ["b", "Si", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "La", "#06F", "#0055FF", None, 5, 3, "\"La\" is the second to last letter in Solresol"]
        ],
        [
            ["l", "Which of these is the second Solresol syllable?", 10],
            ["b", "Re", "#F80", "#FFAA00", None, 5, 1, ""],
            ["b", "Sol", "#06F", "#0055FF", None, 5, 2, "\"Sol\" is the third to last letter in Solresol"],
            ["b", "Mi", "#3C9", "#33BAFE", None, 5, 3, "\"Mi\" is the third letter in Solresol"],
            ["b", "Si", "#E33", "#FF3333", None, 5, 4, "\"Si\" is the last letter in Solresol"]
        ],
        [
            ["l", "Which syllable is used in both music and Solresol?", 10],
            ["b", "Lu", "#3C9", "#33BAFE", None, 5, 2, "Do, Re, Mi, Fa, Sol, Lu, Si. No, that doesn't sound right"],
            ["b", "Do", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "No", "#F80", "#FFAA00", None, 5, 3, "Well you are close, but that's the definition of the correct answer, not the answer itself"]
        ],
        [
            ["l", "Which syllable comes after La?", 10],
            ["b", "Si", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "Mi", "#F80", "#FFAA00", None, 5, 2, "\"Mi\" comes after \"Re\", in Solresol"]
        ],
        [
            ["l", "Which syllable comes before Re?", 10],
            ["b", "Do", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "Fa", "#06F", "#0055FF", None, 5, 2, "\"Fa\" comes before \"Sol\", in Solresol"],
            ["b", "Mi", "#3C9", "#33BAFE", None, 5, 3, "\"Mi\" comes after \"Re\", try reading the question carefully"]
        ],
        [
            ["l", "Which syllable follows Sol in the Solresol scale?", 10],
            ["b", "Fa", "#3C9", "#33BAFE", None, 5, 2, "\"Fa\" follows after \"Mi\", in Solresol"],
            ["b", "Do", "#F80", "#FFAA00", None, 5, 3, "\"Do\" doesn't follow after anything as it's the 1st letter in Solresol"],
            ["b", "Mi", "#E33", "#FF3333", None, 5, 4, "\"Mi\" follows after \"Re\", in Solresol"],
            ["b", "La", "#06F", "#0055FF", None, 5, 1, ""]
        ]
    ],

    [
        # questions to choose from within diff 2
        [
            ["l", "What does the Solresol syllable 'Do' mean?", 10],
            ["b", "Yes, willingly", "#3C9", "#33BAFE", None, 5, 2, "\"Yes, willingly\" is the definition of \"Si\", in Solresol"],
            ["b", "No, not, nor", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "At, to", "#06F", "#0055FF", None, 5, 3, "\"At, to\" is the definition of \"Fa\", in Solresol"],
            ["b", "Or", "#F80", "#FFAA00", None, 5, 4, "\"Or\" is the definition of \"Mi\", in Solresol"]
        ],
        [
            ["l", "What does the syllable 'Re' mean in Solresol?", 10],
            ["b", "And", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "If", "#06F", "#0055FF", None, 5, 2, "\"If\" is the definition of \"Sol\", in Solresol"],
            ["b", "Yes, willingly", "#3C9", "#33BAFE", None, 5, 3, "\"Yes, willingly\" is the definition of \"Si\", in Solresol"],
            ["b", "The", "#F80", "#FFAA00", None, 5, 4, "\"The\" is the definition of \"La\", in Solresol"]
        ],
        [
            ["l", "What does the word 'Mi' mean in Solresol?", 10],
            ["b", "Or", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "The", "#06F", "#0055FF", None, 5, 2, "\"The\" is the definition of \"La\", in Solresol"],
            ["b", "At, to", "#F80", "#FFAA00", None, 5, 3, "\"At, to\" is the definition of \"Fa\", in Solresol"]
        ],
        [
            ["l", "What does 'Fa' mean in Solresol?", 10],
            ["b", "At, to", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "And", "#3C9", "#33BAFE", None, 5, 2, "\"And\" is the definition of \"Re\", in Solresol"],
            ["b", "Yes, willingly", "#06F", "#0055FF", None, 5, 3, "\"Yes, willingly\" is the definition of \"Si\", in Solresol"],
            ["b", "Or", "#F80", "#FFAA00", None, 5, 4, "\"Or\" is the definition of \"Mi\", in Solresol"]
        ],
        [
            ["l", "What does 'Sol' mean in Solresol?", 10],
            ["b", "Or", "#06F", "#0055FF", None, 5, 2, "\"Or\" is the definition of \"Mi\", in Solresol"],
            ["b", "If", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "The", "#E33", "#FF3333", None, 5, 3, "\"The\" is the definition of \"La\", in Solresol"],
            ["b", "Yes, willingly", "#F80", "#FFAA00", None, 5, 4, "\"Yes, willingly\" is the definition of \"Si\", in Solresol"],
            ["b", "And", "#088", "#00BB88", None, 5, 5, "\"And\" is the definition of \"Re\", in Solresol"]
        ],
        [
            ["l", "What is the meaning of 'La' in Solresol?", 10],
            ["b", "The", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "At, to", "#F80", "#FFAA00", None, 5, 2, "\"At, to\" is the definition of \"Fa\", in Solresol"],
            ["b", "Yes, willingly", "#06F", "#0055FF", None, 5, 3, "\"Yes, willingly\" is the definition of \"Si\", in Solresol"],
            ["b", "If", "#E33", "#FF3333", None, 5, 4, "\"If\" is the definition of \"Sol\", in Solresol"]
        ],
        [
            ["l", "What does 'Si' mean in Solresol?", 10],
            ["b", "Yes, willingly", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "At, to", "#3C9", "#33BAFE", None, 5, 2, "\"At, to\" is the definition of \"Fa\", in Solresol"],
            ["b", "Or", "#06F", "#0055FF", None, 5, 3, "\"Or\" is the definition of \"Mi\", in Solresol"],
            ["b", "No, not, nor", "#F80", "#FFAA00", None, 5, 4, "\"No, not, nor\" is the definition of \"Do\", in Solresol"]
        ]
    ]
]