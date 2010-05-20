__version__ = "0.0.1"
__Author__ = 'Antonio "john" Junior'
__license__ = "GPLv3"


import twitter
from threading import Timer
from getpass import getpass


class Urubu():

	def __init__(self):
		self._user_online = False
		self._enable_plot = False
		self.api = None
		self.usr = None		
		self.working = True
		

	def start(self):
		print 
		print "Urubu - A [very] simple Twitter client for shell et afins"
		print "Type 'h<enter>' to help"
		while self.working: self.run()
		


	def createTimer(self,value = 30):
		if not self.working:
			return
		self.t = Timer(value,self.plot, [True])
		self.t.start()

	def plot(self, _schedule_another_plot = False):	
		if self._enable_plot and self._user_online:	
			tl = self.api.GetFriendsTimeline()
			tl = tl[::-1]			
			for i in tl:
				print i.GetUser().screen_name
				print i.GetCreatedAt()
				print i.text.encode('UTF-8')
				print															
		if _schedule_another_plot: self.createTimer()
		print '->',

	def run(self):
		try:
			i = raw_input('->')
			self._enable_plot = False
		except KeyboardInterrupt:
			self._enable_plot = True
			return None

		if i == 'i':
			self.input()
		elif i == 'h':
			self._help()
		elif i == 'q':
			self.quit()
		elif i == 'r':
			self.reload()
		elif i == 'l':
			self.login()
		elif i == 'f':
			self.logoff()
		elif i == 'b':
			self.about()
		elif i == 's':
			self.settings()	
		else:
			print "Type 'h<enter>' for help"
		self._enable_plot = True
		return


	def settings(self):
		print 'Not Yet Implemented'

	def input(self):
		if not self._user_online:
			print "You must login before post a message!"
			return
		try:
			i = raw_input('i-> ')
			if len(i) > 140:
				print 'Out of bounds'
			else:
				if self.confirm():
					print "Posting..."
					self.api.PostUpdate(unicode(i))
					print "Done!"
				
		except KeyboardInterrupt:
			print
			return ''
	

	def login(self):
		self.usr = raw_input('Usr: ')
		pss = getpass()
		self.api = twitter.Api(username = self.usr, password = pss)
		#aqui eu deveria criar um teste para ver se logou mesmo!!!!
		self._user_online = True
		self._enable_plot = True
		self.plot()
		self.createTimer()
		
	def confirm(self, text = "Are you sure? "):
		a = raw_input(text)
		if a == 'y' or a == 'Y' or a == 'YES' or a == 'yes' or a == 'Yes':
			return True
		else:
			return False
		
	def _help(self):
		print
		print "Urubu - a simple Twitter client for shell et afins"
		print "Version %s" % (__version__)
		print 'h - Show this message'
		print 'l - Login'
		print 'f - Logout'
		print 'i - Input a new message'
		print 'r - Reload Tweets'
		print 'b - About'
		print 's - Settings'
		print 'q - Quit'
		

	def about(self):
		print
		print "Urubu - a simple Twitter client for shell at afins"
		print "Version %s" % (__version__)
		print "Writed by %s" % (__Author__)
		print "Licensed under %s" % (__license__)
		print "Use Python ;-)" 



	def quit(self):
		if self.confirm():
			self.working = False
			try:
				self.t.cancel()									
			except:
				pass			
			print "Bye..."
			

if __name__ == "__main__":
	u = Urubu()
	u.start()
