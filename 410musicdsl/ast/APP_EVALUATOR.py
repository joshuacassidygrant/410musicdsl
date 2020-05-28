from ast.APP_VISITOR import Visitor
from ast.COMPOSITION import COMPOSITION
from build import Input

class Evaluator(Visitor):

  def __init__(self, input):
    self.input = input
    print("Initialized visitor: ", self.input)
  
  def visit_arranger(self, e)-> None:
    print("=====visit_arrange=====", e.value)
    self.input.setArranger(e.value)

  def visit_bar(self, e)-> None: pass
  
  
  def visit_chord(self, e)-> None: pass
  
  
  def visit_composer(self, e)-> None:
    print("=====visit_composer=====", e.value)
    self.input.setComposer(e.value)
  
  
  def visit_composition(self, e: COMPOSITION)-> None:
    print("=====visit_composition=====")
    m = e.metadata
    m.accept(self)
    print("METADATA: ", e.metadata)


  def visit_declaration(self, e)-> None: pass
  
  
  def visit_integer(self, e)-> None: pass
  
  
  def visit_key_of(self, e)-> None: pass
  
  
  def visit_key(self, e)-> None: pass
  
  
  def visit_length(self, e)-> None: pass
  
  
  def visit_meta(self, e)-> None: pass
  
  
  def visit_meta_data(self, e)-> None:
    print("=====visit_metadata=====")
    for meta in e.metas:
      meta.accept(self)
      pass
  
  def visit_name(self, e)-> None: pass
  
  
  def visit_note(self, e)-> None: pass
  
  
  def visit_pitch(self, e)-> None: pass
  
  
  def visit_play(self, e)-> None: pass
  
  
  def visit_sequence(self, e)-> None: pass
  
  
  def visit_set_chord(self, e)-> None: pass
  
  
  def visit_set_sequence(self, e)-> None: pass

  
  def visit_staff(self, e)-> None: pass

  
  def visit_string(self, e)-> None: pass

  
  def visit_tempo(self, e)-> None: pass

  
  def visit_time_sig(self, e)-> None: pass

  
  def visit_time(self, e)-> None: pass

  
  def visit_title(self, e)-> None:
    print("=====visit_title=====", e.value)   
    self.input.setTitle(e.value)
    pass
  
  def visit_year(self, e)-> None: pass