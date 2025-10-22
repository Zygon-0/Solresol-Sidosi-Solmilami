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
            ["b", "Ti", "#3C9", "#33BAFE", None, 5, 1, ""],
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
            ["b", "No", "#F80", "#FFAA00", None, 5, 3, "Well you are close, but that's the English translation of the correct answer, not the answer itself"]
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
        ]    ],
    [
        # questions to choose from within diff 2
        [
            ["l", "What does the Solresol syllable 'Do' mean?", 10],
            ["b", "Yes, willingly", "#3C9", "#33BAFE", None, 5, 2, "\"Yes, willingly\" is the English translation of \"Si\", in Solresol"],
            ["b", "No, not, nor", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "At, to", "#06F", "#0055FF", None, 5, 3, "\"At, to\" is the English translation of \"Fa\", in Solresol"],
            ["b", "Or", "#F80", "#FFAA00", None, 5, 4, "\"Or\" is the English translation of \"Mi\", in Solresol"]
        ],
        [
            ["l", "What does the syllable 'Re' mean in Solresol?", 10],
            ["b", "And", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "If", "#06F", "#0055FF", None, 5, 2, "\"If\" is the English translation of \"Sol\", in Solresol"],
            ["b", "Yes, willingly", "#3C9", "#33BAFE", None, 5, 3, "\"Yes, willingly\" is the English translation of \"Si\", in Solresol"],
            ["b", "The", "#F80", "#FFAA00", None, 5, 4, "\"The\" is the English translation of \"La\", in Solresol"]
        ],
        [
            ["l", "What does the word 'Mi' mean in Solresol?", 10],
            ["b", "Or", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "The", "#06F", "#0055FF", None, 5, 2, "\"The\" is the English translation of \"La\", in Solresol"],
            ["b", "At, to", "#F80", "#FFAA00", None, 5, 3, "\"At, to\" is the English translation of \"Fa\", in Solresol"]
        ],
        [
            ["l", "What does 'Fa' mean in Solresol?", 10],
            ["b", "At, to", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "And", "#3C9", "#33BAFE", None, 5, 2, "\"And\" is the translation of \"Re\", in Solresol"],
            ["b", "Yes, willingly", "#06F", "#0055FF", None, 5, 3, "\"Yes, willingly\" is the translation of \"Si\", in Solresol"],
            ["b", "Or", "#F80", "#FFAA00", None, 5, 4, "\"Or\" is the English translation of \"Mi\", in Solresol"]
        ],
        [
            ["l", "What does 'Sol' mean in Solresol?", 10],
            ["b", "Or", "#06F", "#0055FF", None, 5, 2, "\"Or\" is the English translation of \"Mi\", in Solresol"],
            ["b", "If", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "The", "#E33", "#FF3333", None, 5, 3, "\"The\" is the English translation of \"La\", in Solresol"],
            ["b", "Yes, willingly", "#F80", "#FFAA00", None, 5, 4, "\"Yes, willingly\" is the English translation of \"Si\", in Solresol"],
            ["b", "And", "#088", "#00BB88", None, 5, 5, "\"And\" is the English translation of \"Re\", in Solresol"]
        ],
        [
            ["l", "What is the meaning of 'La' in Solresol?", 10],
            ["b", "The", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "At, to", "#F80", "#FFAA00", None, 5, 2, "\"At, to\" is the English translation of \"Fa\", in Solresol"],
            ["b", "Yes, willingly", "#06F", "#0055FF", None, 5, 3, "\"Yes, willingly\" is the English translation of \"Si\", in Solresol"],
            ["b", "If", "#E33", "#FF3333", None, 5, 4, "\"If\" is the English translation of \"Sol\", in Solresol"]
        ],
        [
            ["l", "What does 'Si' mean in Solresol?", 10],
            ["b", "Yes, willingly", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "At, to", "#3C9", "#33BAFE", None, 5, 2, "\"At, to\" is the English translation of \"Fa\", in Solresol"],
            ["b", "Or", "#06F", "#0055FF", None, 5, 3, "\"Or\" is the English translation of \"Mi\", in Solresol"],
            ["b", "No, not, nor", "#F80", "#FFAA00", None, 5, 4, "\"No, not, nor\" is the English translation of \"Do\", in Solresol"]
        ],
        [
            ["l", "Which Solresol syllable means 'And'?", 10],
            ["b", "Re", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "Mi", "#3C9", "#33BAFE", None, 5, 2, "\"Mi\" is the Solresol translation for \"Or\", in English"],
            ["b", "Si", "#06F", "#0055FF", None, 5, 3, "\"Si\" is the Solresol translation for \"Yes, willingly\", in English"]
        ],
        [
            ["l", "Which syllable means 'Or' in Solresol?", 10],
            ["b", "Sol", "#F80", "#FFAA00", None, 5, 2, "\"Sol\" is the Solresol translation for \"If\", in English"],
            ["b", "Do", "#06F", "#0055FF", None, 5, 3, "\"Do\" is the Solresol translation for \"No\", in English"],
            ["b", "Mi", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "La", "#3C9", "#33BAFE", None, 5, 4, "\"La\" is the Solresol translation for \"The\", in English"]
        ],
        [
            ["l", "Which Solresol syllable means 'To, toward'?", 10],
            ["b", "Fa", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "Si", "#3C9", "#33BAFE", None, 5, 2, "\"Si\" is the Solresol translation for \"Yes, willingly\", in English"],
            ["b", "Re", "#F80", "#FFAA00", None, 5, 3, "\"Re\" is the Solresol translation for \"And\", in English"],
            ["b", "Do", "#06F", "#0055FF", None, 5, 4, "\"Do\" is the Solresol translation for \"No\", in English"]
        ],
        [
            ["l", "Which syllable means 'If' in Solresol?", 10],
            ["b", "Sol", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "Fa", "#E33", "#FF3333", None, 5, 2, "\"Fa\" is the Solresol translation for \"To, toward\", in English"],
            ["b", "La", "#06F", "#0055FF", None, 5, 3, "\"La\" is the Solresol translation for \"The\", in English"],
            ["b", "Do", "#F80", "#FFAA00", None, 5, 4, "\"Do\" is the Solresol translation for \"No\", in English"]
        ],
        [
            ["l", "Which syllable means 'The' in Solresol?", 10],
            ["b", "La", "#3C9", "#33BAFE", None, 5, 1, ""],
            ["b", "Mi", "#06F", "#0055FF", None, 5, 2, "\"Mi\" is the Solresol translation for \"Or\", in English"],
            ["b", "Re", "#E33", "#FF3333", None, 5, 3, "\"Re\" is the Solresol translation for \"And\", in English"],
            ["b", "Si", "#F80", "#FFAA00", None, 5, 4, "\"Si\" is the Solresol translation for \"Yes, willingly\", in English"]
        ],
        [
            ["l", "Which syllable means 'Yes, willingly'?", 10],
            ["b", "Sol", "#E33", "#FF3333", None, 5, 2, "\"Sol\" is the Solresol translation for \"If\", in English"],
            ["b", "Si", "#06F", "#0055FF", None, 5, 1, ""],
            ["b", "Do", "#3C9", "#33BAFE", None, 5, 3, "\"Do\" is the Solresol translation for \"No\", in English"],
            ["b", "La", "#F80", "#FFAA00", None, 5, 4, "\"La\" is the Solresol translation for \"The\", in English"],
            ["b", "Fa", "#099", "#00CCCC", None, 5, 5, "\"Fa\" is the Solresol translation for \"To, toward\", in English"]
        ],
        [
            ["l", "Which Solresol syllable means 'No, not, nor'?", 10],
            ["b", "Do", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "Re", "#3C9", "#33BAFE", None, 5, 2, "\"Re\" is the Solresol translation for \"And\", in English"],
            ["b", "La", "#F80", "#FFAA00", None, 5, 3, "\"La\" is the Solresol translation for \"The\", in English"],
            ["b", "Sol", "#06F", "#0055FF", None, 5, 4, "\"Sol\" is the Solresol translation for \"If\", in English"]
        ],
        [
            ["l", "Which syllable corresponds to the idea of agreement or affirmation?", 10],
            ["b", "Si", "#E33", "#FF3333", None, 5, 1, ""],
            ["b", "Fa", "#3C9", "#33BAFE", None, 5, 2, "Hmm, I dont think that's overly connected to anything, aside from surprise in a way"],
            ["b", "Mi", "#F80", "#FFAA00", None, 5, 3, "Mi eso es correcto"],
            ["b", "Do", "#06F", "#0055FF", None, 5, 4, "Well, your not overly wrong because of things like \"I Do\", but sorry that's not the answer i was after"]
        ]
    ],
    [
        # questions to choose from within diff 3
        # 1-2 Dore
        [
            ["l", "Which Solresol word means 'I, me, we'?", 10],
            ["b", "Dore", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Dore" is actually "I, me, we"'],
            ["b", "Domi", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Domi" is actually "you"'],
            ["b", "Redo", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Redo" is actually "my, mine"']
        ],
        [
            ["l", "If you want to refer to yourself in Solresol, which word would you use?", 10],
            ["b", "Remi", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Remi" is actually "your, yours"'],
            ["b", "Dore", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Dore" is actually "I, me, we"'],
            ["b", "Fado", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Fado" is actually "what?, what is this?"']
        ],

        # 3-4 Domi
        [
            ["l", "Which Solresol word means 'you'?", 10],
            ["b", "Domi", "#06F", "#0055FF", None, 5, 1, 'Sorry but the meaning of "Domi" is actually "you"'],
            ["b", "Fare", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Fare" is actually "that, that one, those"'],
            ["b", "Lafa", "#3C9", "#33BAFE", None, 5, 3, 'Sorry but the meaning of "Lafa" is actually "bad"']
        ],
        [
            ["l", "If you are talking directly to someone, which word represents 'you'?", 10],
            ["b", "Domi", "#E33", "#FF3333", None, 5, 1, 'Sorry but the meaning of "Domi" is actually "you"'],
            ["b", "Dore", "#3C9", "#33BAFE", None, 5, 2, 'Sorry but the meaning of "Dore" is actually "I, me, we"'],
            ["b", "Solre", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Solre" is actually "Why?, What for?"']
        ],

        # 5-6 Redo
        [
            ["l", "Which word means 'my, mine'?", 10],
            ["b", "Redo", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Redo" is actually "my, mine"'],
            ["b", "Remi", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Remi" is actually "your, yours"'],
            ["b", "Fami", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Fami" is actually "this, this one, these"']
        ],
        [
            ["l", "If you want to say something belongs to you, which Solresol word do you use?", 10],
            ["b", "Redo", "#E33", "#FF3333", None, 5, 1, 'Sorry but the meaning of "Redo" is actually "my, mine"'],
            ["b", "Fala", "#3C9", "#33BAFE", None, 5, 2, 'Sorry but the meaning of "Fala" is actually "good, tasty, exquisite, delicious"'],
            ["b", "Mido", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Mido" is actually "for"']
        ],

        # 7-8 Remi
        [
            ["l", "Which Solresol word means 'your, yours'?", 10],
            ["b", "Remi", "#E33", "#FF3333", None, 5, 1, 'Sorry but the meaning of "Remi" is actually "your, yours"'],
            ["b", "Fare", "#3C9", "#33BAFE", None, 5, 2, 'Sorry but the meaning of "Fare" is actually "that, that one, those"'],
            ["b", "Solfa", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Solfa" is actually "because"']
        ],
        [
            ["l", "When pointing to something that belongs to the listener, which word is correct?", 10],
            ["b", "Remi", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Remi" is actually "your, yours"'],
            ["b", "Domi", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Domi" is actually "you"'],
            ["b", "Fado", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Fado" is actually "what?, what is this?"']
        ],

        # 9-10 Mido
        [
            ["l", "Which Solresol word means 'for'?", 10],
            ["b", "Mido", "#06F", "#0055FF", None, 5, 1, 'Sorry but the meaning of "Mido" is actually "for"'],
            ["b", "Solfa", "#3C9", "#33BAFE", None, 5, 2, 'Sorry but the meaning of "Solfa" is actually "because"'],
            ["b", "Lafa", "#E33", "#FF3333", None, 5, 3, 'Sorry but the meaning of "Lafa" is actually "bad"']
        ],
        [
            ["l", "If giving something with a purpose ie 'this is for you', which word covers the 'for' part?", 10],
            ["b", "Mido", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Mido" is actually "for"'],
            ["b", "Remi", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Remi" is actually "your, yours"'],
            ["b", "Dore", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Dore" is actually "I, me, we"']
        ],

        # 13-14 Fado
        [
            ["l", "Which word is used to ask 'What?' or 'What is this?' in Solresol?", 10],
            ["b", "Fado", "#E33", "#FF3333", None, 5, 1, 'Sorry but the meaning of "Fado" is actually "what?, what is this?"'],
            ["b", "Fami", "#3C9", "#33BAFE", None, 5, 2, 'Sorry but the meaning of "Fami" is actually "this, this one, these"'],
            ["b", "Solre", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Solre" is actually "Why?, What for?"']
        ],
        [
            ["l", "If you see something strange and want to know what it is, which word works?", 10],
            ["b", "Fado", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Fado" is actually "what?, what is this?"'],
            ["b", "Redo", "#06F", "#0055FF", None, 5, 2, 'Sorry but the meaning of "Redo" is actually "my, mine"'],
            ["b", "Lafa", "#E33", "#FF3333", None, 5, 3, 'Sorry but the meaning of "Lafa" is actually "bad"']
        ],

        # 15-16 Fare
        [
            ["l", "Which word means 'that, that one, those'?", 10],
            ["b", "Fare", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Fare" is actually "that, that one, those"'],
            ["b", "Fami", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Fami" is actually "this, this one, these"'],
            ["b", "Remi", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Remi" is actually "your, yours"']
        ],
        [
            ["l", "If you point to an object far away and say 'that one', which word applies?", 10],
            ["b", "Fare", "#E33", "#FF3333", None, 5, 1, 'Sorry but the meaning of "Fare" is actually "that, that one, those"'],
            ["b", "Solre", "#3C9", "#33BAFE", None, 5, 2, 'Sorry but the meaning of "Solre" is actually "Why?, What for?"'],
            ["b", "Medo", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Medo" is actually "duty, obligation"']
        ],

        # 17-18 Fami
        [
            ["l", "Which Solresol word means 'this, this one, these'?", 10],
            ["b", "Fami", "#06F", "#0055FF", None, 5, 1, 'Sorry but the meaning of "Fami" is actually "this, this one, these"'],
            ["b", "Fare", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Fare" is actually "that, that one, those"'],
            ["b", "Fala", "#3C9", "#33BAFE", None, 5, 3, 'Sorry but the meaning of "Fala" is actually "good, tasty, exquisite, delicious"']
        ],
        [
            ["l", "If something is close to you and you want to refer to it, which word fits?", 10],
            ["b", "Fami", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Fami" is actually "this, this one, these"'],
            ["b", "Mido", "#06F", "#0055FF", None, 5, 2, 'Sorry but the meaning of "Mido" is actually "for"'],
            ["b", "Domi", "#E33", "#FF3333", None, 5, 3, 'Sorry but the meaning of "Domi" is actually "you"']
        ],

        # 19-20 Fala
        [
            ["l", "Which word means 'good, tasty, exquisite, delicious'?", 10],
            ["b", "Fala", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Fala" is actually "good, tasty, exquisite, delicious"'],
            ["b", "Lafa", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Lafa" is actually "bad"'],
            ["b", "Fado", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Fado" is actually "what?, what is this?"']
        ],
        [
            ["l", "After a great meal, which Solresol word could you use to describe it?", 10],
            ["b", "Fala", "#E33", "#FF3333", None, 5, 1, 'Sorry but the meaning of "Fala" is actually "good, tasty, exquisite, delicious"'],
            ["b", "Solre", "#3C9", "#33BAFE", None, 5, 2, 'Sorry but the meaning of "Solre" is actually "Why?, What for?"'],
            ["b", "Fare", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Fare" is actually "that, that one, those"']
        ],

        # 21-22 Solre
        [
            ["l", "Which Solresol word means 'Why?, What for?'?", 10],
            ["b", "Solre", "#06F", "#0055FF", None, 5, 1, 'Sorry but the meaning of "Solre" is actually "Why?, What for?"'],
            ["b", "Solfa", "#3C9", "#33BAFE", None, 5, 2, 'Sorry but the meaning of "Solfa" is actually "because"'],
            ["b", "Fado", "#E33", "#FF3333", None, 5, 3, 'Sorry but the meaning of "Fado" is actually "what?, what is this?"']
        ],
        [
            ["l", "If you want to ask for the reason something is happening, which word is correct?", 10],
            ["b", "Solre", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Solre" is actually "Why?, What for?"'],
            ["b", "Medo", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Medo" is actually "duty, obligation"'],
            ["b", "Fami", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Fami" is actually "this, this one, these"']
        ],

        # 23-24 Solfa
        [
            ["l", "Which Solresol word means 'because'?", 10],
            ["b", "Solfa", "#E33", "#FF3333", None, 5, 1, 'Sorry but the meaning of "Solfa" is actually "because"'],
            ["b", "Mido", "#06F", "#0055FF", None, 5, 2, 'Sorry but the meaning of "Mido" is actually "for"'],
            ["b", "Solre", "#3C9", "#33BAFE", None, 5, 3, 'Sorry but the meaning of "Solre" is actually "Why?, What for?"']
        ],
        [
            ["l", "When giving a reason for something, which word would you use?", 10],
            ["b", "Solfa", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Solfa" is actually "because"'],
            ["b", "Fado", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Fado" is actually "what?, what is this?"'],
            ["b", "Lafa", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Lafa" is actually "bad"']
        ],

        # 25-26 Lafa
        [
            ["l", "Which Solresol word means 'bad'?", 10],
            ["b", "Lafa", "#E33", "#FF3333", None, 5, 1, 'Sorry but the meaning of "Lafa" is actually "bad"'],
            ["b", "Fala", "#3C9", "#33BAFE", None, 5, 2, 'Sorry but the meaning of "Fala" is actually "good, tasty, exquisite, delicious"'],
            ["b", "Redo", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Redo" is actually "my, mine"']
        ],
        [
            ["l", "If something is unpleasant or not good, which word do you use?", 10],
            ["b", "Lafa", "#3C9", "#33BAFE", None, 5, 1, 'Sorry but the meaning of "Lafa" is actually "bad"'],
            ["b", "Fami", "#E33", "#FF3333", None, 5, 2, 'Sorry but the meaning of "Fami" is actually "this, this one, these"'],
            ["b", "Solre", "#06F", "#0055FF", None, 5, 3, 'Sorry but the meaning of "Solre" is actually "Why?, What for?"']
        ]
    ],
    [ # full sentences
        [
            ["l", "If asked the question \"Fami Mido Dore Sol\" what would be a Positive response", 10],
            ["b", "Si Mido Domi", "#3C9", "#33BAFE", None, 5, 1, ''],
            ["b", "Do Remi Lafa", "#E33", "#FF3333", None, 5, 2, 'Responding with "No your bad" doesnt really feel like a positive response too me'],
            ["b", "Solfa Fala Fa Mido Sol", "#06F", "#0055FF", None, 5, 3, 'What made you pick that one? That isn\'t even a proper sentence']
        ],
        [
            ["l", "If asked the question \"Solre Domi Lafa Mido Sol\" what would be a logical response", 10],
            ["b", "Do Dore Fala", "#3C9", "#33BAFE", None, 5, 1, ''],
            ["b", "Fa Solre Mi Do Fa Solre", "#E33", "#FF3333", None, 5, 2, '"To why or no to why", that is the question'],
            ["b", "Salami Fala Sol", "#06F", "#0055FF", None, 5, 3, 'yes, salami is good, especially with crackers and hummus']
        ],
        [
            ["l", "which of the following is in relation to an object", 10],
            ["b", "Fado Fami Mido", "#3C9", "#33BAFE", None, 5, 1, ''],
            ["b", "Solfa Remi Fala", "#E33", "#FF3333", None, 5, 2, 'im just gonna hope that "Fala" in that sentence, is meant as "good" and not somthing else'],
            ["b", "Domi Si Mi Do Sol", "#06F", "#0055FF", None, 5, 3, '"Dore si, Dore Si." - "...Fare Fala"']
        ]

    ]
]

print("you\'re trying to run the wrong piece of code")