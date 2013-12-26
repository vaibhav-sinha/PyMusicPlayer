#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.6.8 (standalone edition) on Wed Dec 25 22:15:57 2013
#

import wx
import mp3play
import sys
from threading import Thread, Event
from AddDialog import AddDialog
from PlaylistDialog import PlaylistDialog

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

currsong = 0
numsong = 0

class MyThread(Thread):
		def __init__(self, event, frame):
				Thread.__init__(self)
				self.stopped = event
				self.frame = frame
		
		def run(self):
				while not self.stopped.wait(1):
						self.frame.KeepTime()

class Frame(wx.Frame):
		def __init__(self, *args, **kwds):
				# begin wxGlade: Frame.__init__
				kwds["style"] = wx.DEFAULT_FRAME_STYLE
				wx.Frame.__init__(self, *args, **kwds)
				self.Play = wx.Button(self, wx.ID_ANY, _("Play"))
				self.Stop = wx.Button(self, wx.ID_ANY, _("Stop"))
				self.Previous = wx.Button(self, wx.ID_ANY, _("Previous"))
				self.Next = wx.Button(self, wx.ID_ANY, _("Next"))
				self.Playlist = wx.Button(self, wx.ID_ANY, _("Playlist"))
				self.Add = wx.Button(self, wx.ID_ANY, _("Add"))
				self.Open = wx.Button(self, wx.ID_ANY, _("Open"))
				self.slider_1 = wx.Slider(self, wx.ID_ANY, 0, 0, 10)
				self.time = 0
				self.state = "IDLE"

				self.__set_properties()
				self.__do_layout()
				# end wxGlade
				self.Bind(wx.EVT_BUTTON, self.OnPlay, self.Play)
				self.Bind(wx.EVT_BUTTON, self.OnStop, self.Stop)
				self.Bind(wx.EVT_BUTTON, self.OnPrevious, self.Previous)
				self.Bind(wx.EVT_BUTTON, self.OnNext, self.Next)
				self.Bind(wx.EVT_BUTTON, self.OnPlaylist, self.Playlist)
				self.Bind(wx.EVT_BUTTON, self.OnOpen, self.Open)
				self.Bind(wx.EVT_BUTTON, self.OnAdd, self.Add)
				self.Bind(wx.EVT_CLOSE, self.WhenClosed)
		
		def __set_properties(self):
		    # begin wxGlade: Frame.__set_properties
		    self.SetTitle(_("PyMp3Player"))
		    self.SetSize((366, 140))
		    self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DLIGHT))
		    self.Play.SetMinSize((50, 50))
		    self.Stop.SetMinSize((50, 50))
		    self.Previous.SetMinSize((50, 50))
		    self.Next.SetMinSize((50, 50))
		    self.Playlist.SetMinSize((50, 50))
		    self.Add.SetMinSize((50, 50))
		    self.Open.SetMinSize((50, 50))
		    self.slider_1.SetMinSize((350, 30))
		    self.slider_1.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DLIGHT))
		    self.slider_1.SetForegroundColour(wx.Colour(0, 0, 255))
		    # end wxGlade
		
		def __do_layout(self):
		    # begin wxGlade: Frame.__do_layout
		    sizer_1 = wx.BoxSizer(wx.VERTICAL)
		    sizer_2 = wx.BoxSizer(wx.VERTICAL)
		    sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
		    sizer_3.Add(self.Play, 0, 0, 0)
		    sizer_3.Add(self.Stop, 0, 0, 0)
		    sizer_3.Add(self.Previous, 0, 0, 0)
		    sizer_3.Add(self.Next, 0, 0, 0)
		    sizer_3.Add(self.Playlist, 0, 0, 0)
		    sizer_3.Add(self.Add, 0, 0, 0)
		    sizer_3.Add(self.Open, 0, 0, 0)
		    sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
		    sizer_2.Add(self.slider_1, 0, 0, 0)
		    sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
		    self.SetSizer(sizer_1)
		    self.Layout()
		    # end wxGlade
		
		def OnPlay(self, event):
				if self.mp3.isplaying():
						self.mp3.pause()
						self.Play.SetLabel("Play")
						self.state = "PAUSE"
				elif self.mp3.ispaused():
						self.mp3.unpause()
						self.Play.SetLabel("Pause")
						self.state = "PLAY"
				else:		
						self.mp3.play()
						self.Play.SetLabel("Pause")
						self.state = "PLAY"

		def OnStop(self, event):
				self.mp3.stop()
				self.Play.SetLabel("Play")
				self.state = "STOP"
				self.time = 0

		def OnPrevious(self, event):
				self.mp3.stop()
				self.time = 0
				global currsong, numsong
				if currsong > 0:
						currsong = currsong - 1
						self.mp3 = mp3play.load(songlist[currsong])
						self.mp3.play()
				else:
						self.state = "END"

		def OnNext(self, event):
				self.mp3.stop()
				self.time = 0
				global currsong, numsong
				if currsong < numsong - 1:
						currsong = currsong + 1
						self.mp3 = mp3play.load(songlist[currsong])
						self.mp3.play()
				else:
						self.state = "END"

		def OnPlaylist(self, event):
				self.playlist_dialog.Show()

		def OnOpen(self, event):
				global songlist, currsong, numsong
				openFileDialog = wx.FileDialog(self, "Open MP3 file", "", "", "MP3 files (*.mp3)|*.mp3", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
				if openFileDialog.ShowModal() != wx.ID_CANCEL:
						self.mp3.stop()
						self.mp3 = mp3play.load(openFileDialog.GetPath())
						self.time = 0
						self.status = "PLAY"
						self.mp3.play()
						songlist = []
						currsong = 0
						numsong = 0

		def OnAdd(self, event):
				self.add_dialog.Show()

		def WhenClosed(self, event):
				self.e.set()
				self.Destroy()

		def SetSong(self, mp3):
				self.mp3 = mp3

		def SetEvent(self, e):
				self.e = e

		def SetAddDialog(self, dialog):
				self.add_dialog = dialog

		def SetPlaylistDialog(self, dialog):
				self.playlist_dialog = dialog

		def KeepTime(self):
				#if self.mp3.isplaying():
				global currsong, numsong
				if self.state == "PLAY":
						self.time = self.time + 1
						if self.time >= self.mp3.seconds():
								self.mp3.stop()
								self.time = 0
								if currsong < numsong - 1:
										currsong = currsong + 1
										self.mp3 = mp3play.load(songlist[currsong])
										self.mp3.play()
								else:
										self.state = "END"

# end of class Frame
if __name__ == "__main__":
		gettext.install("app") # replace with the appropriate catalog name
		
		if len(sys.argv) > 1:
				filename = sys.argv[1]
		else:	
				filename = "d:/temp.mp3"
		mp3 = mp3play.load(filename)

		songlist = []
		numsong = len(sys.argv) - 1;
		currsong = 0
		if len(sys.argv) > 1:
				for i in range(1,len(sys.argv)):
						songlist.append(sys.argv[i])


		app = wx.PySimpleApp(0)
		wx.InitAllImageHandlers()
		stop = Event()

		frame_1 = Frame(None, wx.ID_ANY, "")
		add_dialog = AddDialog(frame_1, wx.ID_ANY, "")
		playlist_dialog = PlaylistDialog(frame_1, wx.ID_ANY, "")
		frame_1.SetEvent(stop)
		app.SetTopWindow(frame_1)
		frame_1.SetSong(mp3)
		frame_1.SetAddDialog(add_dialog)
		frame_1.SetPlaylistDialog(playlist_dialog)
		frame_1.Show()

		thread = MyThread(stop, frame_1)
		thread.start()

		if len(sys.argv) > 1:
				mp3.play()
				frame_1.Play.SetLabel("Pause")
				frame_1.state = "PLAY"

		app.MainLoop()
