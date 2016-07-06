#!/use/bin/env python

# for tutorials refer here only http://gnipsel.com/glade

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk as gtk

class handler:
	def on_window1_destroy(self, object, data=None): # object comes from GtkObject signal category into which  this functin was embeded
		print "destroyed from cross"
		gtk.main_quit()

	def on_gtk_quit_activate(self, menuitem, data=None):# menuitem comes from GtkMenuitem signal category into which this function was embeded
		print "quit from menu"
		gtk.main_quit()

	def on_gtk_about_activate(self, menuitem, data=None): # look your glade file and see signal category to verify above statements
		print "About dialog box called"
		self.response=self.aboutdialog.run()
		# run function holds the dialog box on screen untill any destroy is pressed. once pressed code moves to next line
		# untill then it is engaged in loop in run(). so other part of code or gui other then dialog wont work
		self.aboutdialog.hide()
		# hide() then hides the dialog box

	def __init__(self):
		self.gladefile="tutorial2.glade"
		self.builder=gtk.Builder()
		self.builder.add_from_file(self.gladefile)

		self.builder.connect_signals(self)
		# If you opt for no construcutor function then just use handler() instead of self as arguement to this line outisde class def	

		self.window1=self.builder.get_object('window1')
		self.aboutdialog=self.builder.get_object('aboutdialog1')
		# need to create instances of objects onto which functions are applied
		self.window1.show_all()

main=handler()
gtk.main()

