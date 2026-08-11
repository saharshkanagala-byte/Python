class Song:
  def __init__(self, title, artist):
    self.title = title
    self.artist = artist
    self.next = None
class Playlist:
  def __init__(self):
    self.head = None
  def add_song(self, title, artist):
    newnode = Song(title, artist)
    if self.head is None:
      self.head = newnode
      return
    else:
      current = self.head 
      while current.next is not None:
        current = current.next
      current.next = newnode
  def delete_song(self, title):
    if self.head == None:
      print('Playlist is empty')
      return
    if self.head.data == title:
      self.head = self.head.next
      return
    previous = None
    current = self.head
    while current is not None and current != title:
      previous = current
      current = current.next
    if current is None:
      print('title not found')
      return
    previous.next = current.next
    
