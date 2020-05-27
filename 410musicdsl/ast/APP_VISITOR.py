from abc import ABC, abstractmethod

class Visitor(ABC):

  @abstractmethod
  def visit_arranger(self, e): pass

  @abstractmethod
  def visit_bar(self, e): pass
  
  @abstractmethod
  def visit_chord(self, e): pass
  
  @abstractmethod
  def visit_composer(self, e): pass
  
  @abstractmethod
  def visit_composition(self, e): pass
  
  @abstractmethod
  def visit_declaration(self, e): pass
  
  @abstractmethod
  def visit_integer(self, e): pass
  
  @abstractmethod
  def visit_key_of(self, e): pass
  
  @abstractmethod
  def visit_key(self, e): pass
  
  @abstractmethod
  def visit_length(self, e): pass
  
  @abstractmethod
  def visit_meta(self, e): pass
  
  @abstractmethod
  def visit_meta_data(self, e): pass
  
  @abstractmethod
  def visit_name(self, e): pass
  
  @abstractmethod
  def visit_note(self, e): pass
  
  @abstractmethod
  def visit_pitch(self, e): pass
  
  @abstractmethod
  def visit_play(self, e): pass
  
  @abstractmethod
  def visit_sequence(self, e): pass
  
  @abstractmethod
  def visit_set_chord(self, e): pass
  
  @abstractmethod
  def visit_set_sequence(self, e): pass

  @abstractmethod
  def visit_staff(self, e): pass

  @abstractmethod
  def visit_string(self, e): pass

  @abstractmethod
  def visit_tempo(self, e): pass

  @abstractmethod
  def visit_time_sig(self, e): pass

  @abstractmethod
  def visit_time(self, e): pass

  @abstractmethod
  def visit_title(self, e): pass

  @abstractmethod
  def visit_year(self, e): pass