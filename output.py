import mingus.core.notes as notes
from mingus.containers import Bar, NoteContainer, Track, Composition
import mingus.extra.lilypond as LilyPond
from mingus.midi import midi_file_out
from input import Input

# NOTE: Must install lilypond.exe (for Windows), LilyPond in the $PATH is needed, and pip install mingus before running

# Create midi file
def createMidi(input):
    if not input:
        print("Invalid: input is empty")
    else:
        c = Composition()
        subtitle = "time = " + input.time + ", tempo = " + input.tempo + ", composer = " + input.composer + ", year = " + input.year + ", key = " + input.key
        c.set_author(input.arrangedBy, 'author@email.com')
        title = input.title
        c.set_title(title, subtitle)
        t = createTrack(input.body)
        c.add_track(t)
        title += ".mid"
        print("Creating a Midi file")
        midi_file_out.write_Composition(title, c)

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
            (note, duration) = item
            b.place_notes(note, duration)
        t += b
    return t

# Call example
# def main():
#     example = Input()
#     createMusicsheet(example)
#     createMidi(example)

if __name__ == "__main__":
    main()
