class Input(object):
    # title = "Ode to Joy"
    # time = "4/4"
    # tempo = 120
    # composer = "Ludwig Van Beethoven"
    # year = 1824
    # arrangedBy = "Eduardo Garza"
    # key = "CMaj"

    def __init__(self):
        self.title = "Ode to Joy"
        self.time = "4/4"
        self.tempo = "120"
        self.composer = "Ludwig Van Beethoven"
        self.year = "1824"
        self.arrangedBy = "Eduardo Garza"
        self.key = "CMaj"
        self.body = {
        "key": "C",
        "meter": (4, 4),
        "bars": [[("E-4", 4), ("E-4", 4), ("F-4", 4), ("G-4", 4)], [("G-4", 4), ("F-4", 4), ("E-4", 4), ("D-4", 4)],
        [("C-4", 4), ("C-4", 4), ("D-4", 4), ("E-4", 4)], [("E-4", 4), ("D-4", 8), ("D-4", 2)]]
        }
