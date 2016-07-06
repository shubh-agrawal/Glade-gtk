#!/use/bin/env python

# for tutorials refer here only http://gnipsel.com/glade

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk as gtk

class handler:
	def on_window1_destroy(self, object, data=None):
		print "destroyed from cross"
		gtk.main_quit()

	def on_gtk_quit_activate(self, menuitem, data=None):
		print "quit from menu"
		gtk.main_quit()

	def __init__(self):
		self.gladefile="tutorial1.glade"
		self.builder=gtk.Builder()
		self.builder.add_from_file(self.gladefile)

		self.builder.connect_signals(self)
		# If you opt for no construcutor function then just use handler() instead of self as arguement to this line outisde class def	

		self.window1=self.builder.get_object('window1')
		self.window1.show_all()

main=handler()
gtk.main()

