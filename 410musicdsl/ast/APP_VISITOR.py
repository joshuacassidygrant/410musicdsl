from abc import ABC, abstractmethod

class Visitor(ABC):

  @abstractmethod
  def visit_arranger(self, e)-> None: pass

  @abstractmethod
  def visit_bar(self, e)-> None: pass
  
  @abstractmethod
  def visit_chord(self, e)-> None: pass
  
  @abstractmethod
  def visit_composer(self, e)-> None: pass
  
  @abstractmethod
  def visit_composition(self, e)-> None: pass
  
  @abstractmethod
  def visit_key(self, e)-> None: pass
  
  @abstractmethod
  def visit_length(self, e)-> None: pass
  
  @abstractmethod
  def visit_meta_data(self, e)-> None: pass
  
  @abstractmethod
  def visit_name(self, e)-> None: pass
  
  @abstractmethod
  def visit_note(self, e)-> None: pass
  
  @abstractmethod
  def visit_pitch(self, e)-> None: pass
  
  @abstractmethod
  def visit_play(self, e)-> None: pass
  
  @abstractmethod
  def visit_sequence(self, e)-> None: pass
  
  @abstractmethod
  def visit_set_chord(self, e)-> None: pass
  
  @abstractmethod
  def visit_set_sequence(self, e)-> None: pass

  @abstractmethod
  def visit_staff(self, e)-> None: pass

  @abstractmethod
  def visit_string(self, e)-> None: pass

  @abstractmethod
  def visit_tempo(self, e)-> None: pass

  @abstractmethod
  def visit_time(self, e)-> None: pass

  @abstractmethod
  def visit_title(self, e)-> None: pass

  @abstractmethod
  def visit_year(self, e)-> None: pass