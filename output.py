import mingus.core.notes as notes
import mingus.core.keys as Key
from mingus.containers import Bar, NoteContainer
# import lilypond as LilyPond
import mingus.extra.lilypond as LilyPond
from mingus.midi import midi_file_out

# Create midi file
# @parameters list of note string
def createMidi(noteList):
    if not noteList:
        print("Invalid: List of notes is empty")
    else:
        # nc = NoteContainer(noteList)
        b = Bar()
        for note in noteList:
            b + note
        # midi_file_out.write_NoteContainer("music1.mid", nc)
        midi_file_out.write_Bar("music.mid", b, 120, 1)

# Create music sheet PDF
# @parameters list of note string
def createMusicsheet(noteList):
    if not noteList:
        print("Invalid: List of notes is empty")
    else:
        b = Bar()
        for note in noteList:
            b + note
        bar = LilyPond.from_Bar(b)
        print(bar)
        LilyPond.to_pdf(bar, "my_first_bar")

# Example call
# noteList = ["C", "E", "G", "B","C", "E", "G", "B"]
# createMusicsheet(noteList)
# createMidi(noteList)
