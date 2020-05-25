import mingus.core.notes as notes
from mingus.containers import Bar, NoteContainer, Track, Composition
import mingus.extra.lilypond as LilyPond
from mingus.midi import midi_file_out
from input import Input

# NOTE: must install lilypond.exe (for Windiws) and pip install mingus before running
# LilyPond in the $PATH is needed.

# Create midi file
def createMidi(noteList):
    if not noteList:
        print("Invalid: List of notes is empty")
    else:
        # nc = NoteContainer(noteList)
        # midi_file_out.write_NoteContainer("music1.mid", nc)
        for note in noteList:
            b + note
        midi_file_out.write_Bar("music.mid", b, 120, 1)

# Create music sheet PDF
def createMusicsheet(input):
    if not input:
        print("Invalid: input is empty")
    else:
        c = Composition()
        subtitle = "time = " + input.time + ", tempo = " + input.tempo + ", composer = " + input.composer + ", year = " + input.year + ", key = " + input.key
        c.set_author(input.arrangedBy, 'author@email.com')
        c.set_title(input.title, subtitle)
        t = createTrack(input.body)
        c.add_track(t)
        compString = LilyPond.from_Composition(c)
        LilyPond.to_pdf(compString, input.title)

def createTrack(body):
    t = Track()
    key = body["key"]
    meter = body['meter']
    bars = body['bars']
    # Create individual bar
    for bar in bars:
        b = Bar(key)
        if meter:
            b.set_meter(meter)
        for item in bar:
            #TODO: major and minor
            (note, duration) = item
            b.place_notes(note, duration)
        t += b
    return t

def main():
    example = Input()
    createMusicsheet(example)

if __name__ == "__main__":
    main()
