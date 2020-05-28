class Input(object):
  
  def __init__(self):
    self.title = None
    self.time = None
    self.tempo = None
    self.composer = None
    self.year = None 
    self.arranger = None
    self.key = None 
    self.body = None

  def setTitle(self, title):
    print("SETTING TITLE IN BUILD")
    self.title = title

  def setTime(self, time): pass

  def setTempo(self, temp): pass

  def setComposer(self, composer):
    self.composer = composer

  def setYear(self, year): pass

  def setArranger(self, arranger):
    self.arranger = arranger

  def setKey(self, key): pass

  def updateBody(self, key, val): pass

  def updateBodyBars(self, val): pass

  def __repr__(self):
    return "<Test title:%s, composer:%s, arranger:%s>" % (self.title, self.composer, self.arranger)
