#!/use/bin/env python

# for tutorials refer here only http://gnipsel.com/glade

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk as gtk

import math

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

	def on_push_status_activate(self, menuitem, data=None):
		self.status_count += 1
		self.statusbar.push(self.context_id,"message id is %s"%str(self.status_count))

	def on_pop_status_activate(self, menuitem, data=None):
		self.status_count -= 1
		self.statusbar.pop(self.context_id)

	def on_clear_status_activate(self, menuitem, data=None):
		while (self.status_count>0):
			self.statusbar.pop(self.context_id)
			self.status_count -= 1	

	def on_sfm_button_clicked(self, button, data=None):# button comes from GtkButton signal category into which  this functin was embeded
		self.sfm=float(self.entry1.get_text())
		self.diameter=float(self.entry2.get_text())
		# get the text from the GtkEntry widget and convert
    	# it to a float value so we can calculate the result

		self.rpm=str(int(self.sfm*((12/math.pi)/self.diameter)))
		self.result1.set_text(self.rpm)

		self.statusbar.push(self.context_id,"Successful !!")
		self.status_count += 1
		print "RPM is ",self.rpm
		

	def __init__(self):
		self.gladefile="tutorial4.glade"
		self.builder=gtk.Builder()
		self.builder.add_from_file(self.gladefile)

		self.builder.connect_signals(self)
		# If you opt for no construcutor function then just use handler() instead of self as arguement to this line outisde class def	

		self.window1=self.builder.get_object('window1')
		self.aboutdialog=self.builder.get_object('aboutdialog1')
		# need to create instances of objects onto which functions are applied
		
		# exclusively for status bar activities
		self.statusbar=self.builder.get_object('statusbar1')
		self.context_id=self.statusbar.get_context_id('status')
		self.status_count=0

		# Excusively for SFM calculator
		self.entry1=self.builder.get_object('entry1')
		self.entry2=self.builder.get_object('entry2')
		self.result1=self.builder.get_object('result1')

		self.window1.show_all()
		

main=handler()
gtk.main()

