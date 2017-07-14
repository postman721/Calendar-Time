#!/usr/bin/env python

#"Current Time" Copyright (c) 2016 JJ Posti <techtimejourney.net> 
#The program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")

#IMPORTING MODULES
from gi.repository import Gtk, Gdk
from gi.repository import GLib
import os, sys, pygtk, time

pygtk.require('2.0')
class CT(Gtk.Window):
	
    def update_clock(self, timer):
        real_time=time.strftime ("%d %b %Y \n %H:%M")

        a=str(real_time)
        self.timer.set_text(a)
        return True
        							   
####################################
#STARTING WINDOW DEFINITIONS
#################################
#GENERAL STUFF
#################################    
    def __init__(self):
    # Create THE WINDOW
        self.window1=Gtk.Window()
        self.window1.set_decorated(True)
        self.window1.set_title("Current Time")
        self.window1.set_resizable(False)
        self.window1.set_size_request(160,90)
        self.window1.set_keep_below(False)
        self.window1.set_position(Gtk.WindowPosition.CENTER)
        self.window1.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#30ff00"))
        self.window1.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#6d6969"))
        self.window1.stick()
        self.window1.set_border_width(12)
        self.window1.connect("destroy", Gtk.main_quit)

#Make Clock Label 
        self.timer=Gtk.Label()
        self.timer.set_justify(Gtk.Justification.CENTER)
        
#Make Frames
        self.frame=Gtk.Frame()
        self.frame.add(self.timer)
        self.frame2=Gtk.Frame()
        self.frame2.add(self.frame)

#Horizontal container

        self.hbox=Gtk.VBox()
        self.hbox.pack_start(self.frame2, True, True, True)
        
#Show everything
        self.window1.add(self.hbox)
        self.window1.show_all()
         
def main():
    Gtk.main()
    return 0

if __name__ == "__main__":
    cc=CT()
    GLib.timeout_add(200, cc.update_clock, None) 
    main()
