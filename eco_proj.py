import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk as gtk

import csv

class handler:
	
	def on_window1_destroy(self, widget, data=None): # object comes from GtkObject signal category into which  this functin was embeded
		#print "destroyed from cross"
		gtk.main_quit()

	
	def on_input_file_file_set(self, filechooserbutton, data=None):
		self.input_filename=self.filechooser.get_filename()
		print "Input filename: ",self.input_filename
		self.statusbar.push(self.context_id,"Selected file:"+self.input_filename)


	def on_calculate_clicked(self, button, data=None):
		self.output_filename=self.entry1.get_text()
		self.statusbar.push(self.context_id,"Calculating...")

		f=open(self.input_filename)
		csvReader=csv.reader(f)
		self.input_data=list(csvReader)  #input data being list of list here

		print input_data 
		# here call the function main_algo and save file here with above catched file name.	
		# Use the filename to output the file here itself. 
	
	def main_algorithm(self,input1):
		print "yolo"
		# Here code the main algo 
		# access the main csv file here with input1 as file input name
		# create new csv file and write it acc to algo
		# save csv file
	def on_about_app_activate(self, button, data=None):
		self.response=self.aboutdialog.run()
		self.aboutdialog.hide()

	def __init__(self):
		self.gladefile="eco_proj.glade"
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

		self.filechooser=self.builder.get_object('input_file')
		
		self.aboutdialog=self.builder.get_object('about_app')

		self.window1.show_all()


main=handler()
gtk.main()


 

