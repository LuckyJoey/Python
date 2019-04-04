# class Song(object):
# 	def __init__(self, lyrics):
# 		self.lyrics = lyrics
#
# 	def sing_me_a_song(self):
# 		for line in self.lyrics:
# 			print("line:",line)
#
# happy_bday = Song("happy")
# happy_bday.sing_me_a_song()

class Dance():
	def __init__(self, dance):
		self.dance = dance
		
	def Dance(self):
		for line in self.dance:
			print("line:",line)

dance = Dance(["breaking","popping"])
dance.Dance()