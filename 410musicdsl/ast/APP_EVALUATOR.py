import os
from ast.APP_VISITOR import Visitor
from ast.COMPOSITION import COMPOSITION
from build import Input

def open_file():
  fileDir = os.path.dirname(os.path.realpath('__file__'))
  filename = os.path.join(fileDir, '410musicdsl/output.ly')
  return filename

class Evaluator(Visitor):
  symbolTable = None

  def __init__(self, input):
    Evaluator.symbolTable = {}
    filename = open_file()
    f = open("output.ly", "w")
    f.write("")
    self.input = input
    print("Initialized visitor: ", self.input)
  
  def visit_arranger(self, e)-> None:
    print("-----visit_arrange-----", e.value)
    self.input.setArranger(e.value)

  def visit_bar(self, e)-> None: pass
  
  
  def visit_chord(self, e)-> None:
    print("-----visit_chord-----")
  
  
  def visit_composer(self, e)-> None:
    print("-----visit_composer-----", e.value)
    filename = open_file
    f = open("output.ly", "a")
    f.write("composer = " + '"' + e.value + '"' + "\n")
    f.close()
    self.input.setComposer(e.value)
  
  def visit_composition(self, e: COMPOSITION)-> None:
    print("-----visit_composition-----")
    filename = open_file()
    f = open("output.ly", "a")
    f.write('version "2.20.0"\n')
    f.write("\header{\n")
    f.close()
    m = e.metadata
    m.accept(self)
    decs = e.declarations
    for d in decs:
      d.accept(self)
    f = open("output.ly", "a")
    f.write("}\n")
    f.close()
    print("METADATA: ", e.metadata)


  def visit_declaration(self, e)-> None: pass
  
  
  def visit_integer(self, e)-> None: pass
  
  
  def visit_key_of(self, e)-> None: pass
  
  def visit_key(self, e)-> None: 
    print("-----visit_key_of-----")
    self.input.setKey(e.value)
  
  def visit_length(self, e)-> None: pass
  
  
  def visit_meta(self, e)-> None: pass
  
  
  def visit_meta_data(self, e)-> None:
    print("-----visit_metadata-----")
    for meta in e.metas:
      meta.accept(self)
      pass
  
  def visit_name(self, e)-> None: pass
  
  
  def visit_note(self, e)-> None: pass
  
  
  def visit_pitch(self, e)-> None: pass
  
  
  def visit_play(self, e)-> None: pass
  
  
  def visit_sequence(self, e)-> None: pass
  
  
  def visit_set_chord(self, e)-> None: 
    print("-----visit_set_chord-----")
    print("chord.name: ", e.name.value)
    Evaluator.symbolTable[e.name.value] = e
    print("symbol table: ", Evaluator.symbolTable[e.name.value])
    for note in e.pitches:
      print("e.pitches note: " + note.note)

  def visit_set_sequence(self, e)-> None: pass

  
  def visit_staff(self, e)-> None: pass

  
  def visit_string(self, e)-> None: pass

  
  def visit_tempo(self, e)-> None:
    print("-----visit_tempo-----", e.value)
    self.input.setTempo(e.value)
  
  def visit_time(self, e)-> None:
    print("-----visit_time-----", e.value)
    self.input.setTime(e.value)
  
  def visit_title(self, e)-> None:
    print("-----visit_title-----", e.value)   
    filename = open_file
    f = open("output.ly", "a")
    f.write("title = " + '"' + e.value + '"' + "\n")
    f.close()
    self.input.setTitle(e.value)
    pass
  
  def visit_year(self, e)-> None:
    print("-----visit_year-----")
    self.input.setYear(e.value)