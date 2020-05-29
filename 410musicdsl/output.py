import mingus.core.notes as notes
import mingus.core.chords as chords
import mingus.core.value as value
from mingus.containers import Bar, NoteContainer, Track, Composition
import mingus.extra.lilypond as LilyPond
from mingus.midi import midi_file_out

# NOTE: Must install lilypond.exe (for Windows), LilyPond in the $PATH is needed, and pip install mingus before running

dur = {
    "q": 4,
    "e": 8,
    "h": 2,
    "w": 1,
    "s": 16,
    ".q": value.dots(value.quarter),
    ".e": value.dots(value.eighth),
    ".h": value.dots(value.half),
    ".w": value.dots(value.whole),
    ".s": value.dots(value.sixteenth),
}

# Create music sheet PDF and MIDI file
def createOutputs(input):
    if not input:
        print("Invalid: input is empty")
    else:
        c = Composition()
        subtitle = "time = " + input.time + ", tempo = " + input.tempo + ", composer = " + input.composer + ", year = " + input.year + ", key = " + input.key
        c.set_author(input.arranger, 'author@email.com')
        title = input.title
        c.set_title(title, subtitle)
        t = createTrack(input.body)
        c.add_track(t)
        compString = LilyPond.from_Composition(c)
        print("Creating a music sheet pdf")
        LilyPond.to_pdf(compString, title)
        title += ".mid"
        print("Creating a MIDI file")
        midi_file_out.write_Composition(title, c)

def createTrack(body):
    t = Track()
    key = body["key"]
    meterStr = body['meter']
    bars = body['bars']
    if "maj" in key:
        key = key[0]
    if "min" in key:
        key = key[0].lower()
    meterList = meterStr.split("/")
    meter = (int(meterList[0]), int(meterList[1]))
    # Create individual bar
    for bar in bars:
        b = Bar(key) 
        if meter:
            b.set_meter(meter) 
        for item in bar:
            (note, duration) = item
            b.place_notes(note, dur[duration]) 
        t += b
    return t
