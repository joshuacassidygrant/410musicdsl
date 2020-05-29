from ast.APP_VISITOR import Visitor
from ast.COMPOSITION import COMPOSITION
from ast.BAR import BAR
from ast.SEQUENCE import SEQUENCE
from ast.SEQUENCE import SEQUENCE
from build import Input

# Evaluator follows the Visitor pattern from class
# UBC CPSC 410

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
    s = e.staffs[0].accept(self)
    return s
  
  def visit_chord(self, e)-> None:
    print("-----visit_chord-----", e.name.value)
    chord = []
    c = Evaluator.symbolTable[e.name.value]
    for pitch in c.pitches:
      p = pitch.accept(self)
      chord.append(p)
    l = e.length.accept(self)
    print("Chord note array: ", chord)
    return (chord, l)
  
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

  def visit_key(self, e)-> None: 
    print("-----visit_key_of-----")
    self.input.setKey(e.value)
  
  def visit_length(self, e)-> None:
    print("-----visit_length-----", e.value)
    return e.value
  
  def visit_meta_data(self, e)-> None:
    print("-----visit_metadata-----")
    for meta in e.metas:
      meta.accept(self)
  
  def visit_name(self, e)-> None:
    print("-----visit_name-----", e.value)
    return e.value
  
  def visit_note(self, e)-> None:
    print("-----visit_note-----", e)
    pitch = e.pitch.accept(self)
    length = e.length.accept(self)
    return (pitch, length)
  
  def visit_pitch(self, e)-> None:
    print("-----visit_pitch-----", e.note, e.octave)
    note = e.note
    octave = e.octave
    pitch = e.note + "-" + e.octave
    return pitch
  
  def visit_play(self, e)-> None:
    print("-----visit_play-----", e.name.value)
    seq = Evaluator.symbolTable[e.name.value]
    measures = []
    for measure in seq.measures:
      evaluatedMeasure = measure.accept(self)
      if isinstance(measure, BAR):
        measures.append(evaluatedMeasure)
      else:
        for m in evaluatedMeasure:
          measures.append(m)
    for m in measures:
      print("play MEASURE: ", m)
    self.input.setBodyBars(measures)
  
  def visit_sequence(self, e)-> None:
    print("-----visit_sequence------", e.name.value)
    seq = Evaluator.symbolTable[e.name.value]
    measures = []
    for i in range(int(e.repeats)):
      for measure in seq.measures:
        evaluatedMeasure = measure.accept(self)
        measures.append(evaluatedMeasure)
    return measures
      
  def visit_set_chord(self, e)-> None: 
    print("-----visit_set_chord-----", e.name.value)
    Evaluator.symbolTable[e.name.value] = e

  def visit_set_sequence(self, e)-> None:
    print("------visit_set_sequence-----", e.name.value)
    Evaluator.symbolTable[e.name.value] = e
  
  def visit_staff(self, e)-> None:
    print("-----visit_staff-----")
    sounds = []
    for sound in e.sounds:
      s = sound.accept(self)
      sounds.append(s)
    return sounds
    
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