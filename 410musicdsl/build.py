class Input(object):
  
  def __init__(self):
    self.title = None
    self.time = None
    self.tempo = None
    self.composer = None
    self.year = None 
    self.arranger = None
    self.key = None 
    self.body = {}

  def setTitle(self, title):
    self.title = title

  def setTime(self, time):
    self.time = time

  def setTempo(self, tempo):
    self.tempo = tempo

  def setComposer(self, composer):
    self.composer = composer

  def setYear(self, year): 
    self.year = year

  def setArranger(self, arranger):
    self.arranger = arranger

  def setKey(self, key):
    print("setting key")
    self.key = key

  def setBodyBars(self, val):
    self.body["key"] = self.key
    self.body["meter"] = self.time
    self.body["bars"] = val

  def __repr__(self):
    return "<BUILDINPUT title:%s, time:%s, tempo:%s, composer:%s, year:%s, arranger:%s, key:%s, body:%s>" % (self.title, self.time, self.tempo, self.composer, self.year, self.arranger, self.key, self.body)
