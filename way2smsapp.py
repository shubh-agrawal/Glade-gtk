import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk as gtk

import urllib2
import cookielib
import sys
 
url = 'http://site24.way2sms.com/Login1.action?'

 
#For Cookies:
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
 
# Adding Header detail: fools webiste of being a browser
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]


class handler:
	def login(self, usr_data):
		global usock, opener, url
		
		try:
			usock = opener.open(url, usr_data)
		except IOError:
			#print "Error while logging in."
			self.statusbar.push(self.context_id,"Error while logging in.")

		#print "logged in"
		self.statusbar.push(self.context_id,"Logged in")	

	def send_sms(self,number,message):
	 	global cj, opener, jession_id
		
		jession_id = str(cj).split('~')[1].split(' ')[0]
		send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
		send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
		opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
		 
		try:
			sms_sent_page = opener.open(send_sms_url,send_sms_data)
		except IOError:
			#print "Error while sending message"
			self.statusbar.push(self.context_id,"Error while sending message")	   

		#print "SMS has been sent."
		self.statusbar.push(self.context_id,"SMS has been sent.")


	def on_window1_destroy(self, widget, data=None): # object comes from GtkObject signal category into which  this functin was embeded
		#print "destroyed from cross"
		gtk.main_quit()

	def on_gtk_login_clicked(self, button, data=None):
		self.username=self.entry1.get_text()
		self.password=self.entry2.get_text()
		self.usr_data = 'username='+self.username+'&password='+self.password+'&Submit=Sign+in'
		#print self.usr_data
		self.login(self.usr_data)
		
	def on_gtk_send_clicked(self, button, data=None):
			
		# Important example for running textview. Need to work with textbuffer
		self.TextBuffer=self.textview1.get_buffer()
		self.start=self.TextBuffer.get_start_iter()
		self.end=self.TextBuffer.get_end_iter()

		self.message=self.TextBuffer.get_text(self.start, self.end, True)
		#print self.message
		self.message = "+".join(self.message.split(' '))  # encoding ' ' to '+'
		self.send_mob=self.entry3.get_text()
		self.send_sms(self.send_mob, self.message)

	def on_aboutbutton_clicked(self, button, data=None):
		self.response=self.aboutdialog.run()
		self.aboutdialog.hide()

	def __init__(self):
		self.gladefile="way2smsapp2.0.glade"
		self.builder=gtk.Builder()
		self.builder.add_from_file(self.gladefile)

		self.builder.connect_signals(self)
		# If you opt for no construcutor function then just use handler() instead of self as arguement to this line outisde class def	

		self.window1=self.builder.get_object('window1')
		# need to create instances of objects onto which functions are applied
		
		# exclusively for status bar activities
		self.statusbar=self.builder.get_object('statusbar1')
		self.context_id=self.statusbar.get_context_id('status')

		self.entry1=self.builder.get_object('entry1')
		self.entry2=self.builder.get_object('entry2')
		self.entry3=self.builder.get_object('entry3')
		self.textview1=self.builder.get_object('textview1')
		self.aboutdialog=self.builder.get_object('aboutdialog1')


		self.window1.show_all()


main=handler()
gtk.main()


 


