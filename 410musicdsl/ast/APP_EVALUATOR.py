from ast.APP_VISITOR import Visitor
from ast.COMPOSITION import COMPOSITION
from build import Input

class Evaluator(Visitor):
  symbolTable = None

  def __init__(self, input):
    Evaluator.symbolTable = {}
    self.input = input
    print("Initialized visitor: ", self.input)
  
  def visit_arranger(self, e)-> None:
    print("-----visit_arrange-----", e.value)
    self.input.setArranger(e.value)

  def visit_bar(self, e)-> None:
    print("-----visit_bar-----")
    staffs = []
    for staff in e.staffs:
      staff.accept(self)
      print(staff.sounds)
    return staffs
  
  def visit_chord(self, e)-> None:
    print("-----visit_chord-----")
  
  
  def visit_composer(self, e)-> None:
    print("-----visit_composer-----", e.value)
    self.input.setComposer(e.value)
  
  def visit_composition(self, e: COMPOSITION)-> None:
    print("-----visit_composition-----")
    m = e.metadata
    m.accept(self)
    decs = e.declarations
    for d in decs:
      d.accept(self)
    p = e.play
    p.accept(self)
    print("METADATA: ", e.metadata)

  def visit_declaration(self, e)-> None: pass
  
  
  def visit_key(self, e)-> None: 
    print("-----visit_key_of-----")
    self.input.setKey(e.value)
  
  def visit_length(self, e)-> None:
    print("-----visit_length-----", e.value)
    return e.value
  
  def visit_meta(self, e)-> None: pass
  
  
  def visit_meta_data(self, e)-> None:
    print("-----visit_metadata-----")
    for meta in e.metas:
      meta.accept(self)
      pass
  
  def visit_name(self, e)-> None:
    print("-----visit_name-----", e.value)
    return e.value
  
  def visit_note(self, e)-> None:
    print("-----visit_note-----", e)
    pitch = e.pitch.accept(self)
    print("JUST CHECKING TYPE", pitch)
    length = e.length.accept(self)
    print("pitch, length: ", pitch, length)
    return (pitch, length)
  
  def visit_pitch(self, e)-> None:
    print("-----visit_pitch-----", e.note, e.octave)
    note = e.note
    octave = e.octave
    pitch = e.note + "-" + e.octave
    print("pitch: ", pitch)
    return pitch
  
  def visit_play(self, e)-> None:
    print("-----visit_play-----", e.name.value)
    print("name: " + e.name.value)
    seq = Evaluator.symbolTable[e.name.value]
    measures = []
    for measure in seq.measures:
      print("measure type: ", measure)
      evaluatedMeasure = measure.accept(self)
      print("HERE IS THE EVALUATED MEASURE: ", evaluatedMeasure)
      measures.append(evaluatedMeasure)
    print("notes here: ", measures)
  
  def visit_sequence(self, e)-> None:
    print("-----visit_sequence------", e.name.value)
  
  def visit_set_chord(self, e)-> None: 
    print("-----visit_set_chord-----")
    print("chord.name: ", e.name.value)
    Evaluator.symbolTable[e.name.value] = e
    print("symbol table: ", Evaluator.symbolTable[e.name.value])
    for note in e.pitches:
      print("e.pitches note: " + note.note)

  def visit_set_sequence(self, e)-> None:
    print("------visit_set_sequence-----")
    print("sequence.name: ", e.name.value)
    Evaluator.symbolTable[e.name.value] = e
    print("symbol table: ", Evaluator.symbolTable)
  
  def visit_staff(self, e)-> None:
    print("-----visit_staff-----")
    sounds = []
    for sound in e.sounds:
      sound.accept(self)
      sounds.append(sound)
      print("sound here: ", sound)
    return sound
    

  def visit_string(self, e)-> None: pass

  
  def visit_tempo(self, e)-> None:
    print("-----visit_tempo-----", e.value)
    self.input.setTempo(e.value)
  
  def visit_time(self, e)-> None:
    print("-----visit_time-----", e.value)
    self.input.setTime(e.value)
  
  def visit_title(self, e)-> None:
    print("-----visit_title-----", e.value)   
    self.input.setTitle(e.value)
  
  def visit_year(self, e)-> None:
    print("-----visit_year-----")
    self.input.setYear(e.value)