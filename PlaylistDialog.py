#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#
# generated by wxGlade 0.6.8 (standalone edition) on Thu Dec 26 13:45:35 2013
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade



class PlaylistDialog(wx.Dialog):
		def __init__(self, *args, **kwds):
		    # begin wxGlade: PlaylistDialog.__init__
		    kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.DIALOG_NO_PARENT
		    wx.Dialog.__init__(self, *args, **kwds)
		    self.list_box_1 = wx.ListBox(self, wx.ID_ANY, choices=[])
		    self.PlayButton = wx.Button(self, wx.ID_ANY, _("Play"))
		    self.CancelButton = wx.Button(self, wx.ID_ANY, _("Cancel"))
		
		    self.__set_properties()
		    self.__do_layout()
		
		    self.Bind(wx.EVT_BUTTON, self.OnPlay, self.PlayButton)
		    self.Bind(wx.EVT_BUTTON, self.OnCancel, self.CancelButton)
		    # end wxGlade
		
		def __set_properties(self):
		    # begin wxGlade: PlaylistDialog.__set_properties
		    self.SetTitle(_("Play Playlist"))
		    self.SetSize(wx.DLG_SZE(self, (136, 149)))
		    self.list_box_1.SetMinSize((200, 166))
		    # end wxGlade
		
		def __do_layout(self):
		    # begin wxGlade: PlaylistDialog.__do_layout
		    sizer_1 = wx.BoxSizer(wx.VERTICAL)
		    sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
		    sizer_1.Add(self.list_box_1, 5, 0, 0)
		    sizer_2.Add(self.PlayButton, 0, 0, 0)
		    sizer_2.Add(self.CancelButton, 0, wx.LEFT, 10)
		    sizer_1.Add(sizer_2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
		    self.SetSizer(sizer_1)
		    self.Layout()
		    # end wxGlade
		
		def OnPlay(self, event):  # wxGlade: PlaylistDialog.<event_handler>
				self.Close()
				self.cb(self.list_box_1.GetStringSelection())
		
		def OnCancel(self, event):  # wxGlade: PlaylistDialog.<event_handler>
				self.Close()
		
		def SetCallback(self, func):
				self.cb = func

# end of class PlaylistDialog
class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # Content of this block not found. Did you rename this class?
        pass

    def __set_properties(self):
        # Content of this block not found. Did you rename this class?
        pass

    def __do_layout(self):
        # Content of this block not found. Did you rename this class?
        pass

    def OnPlay(self, event):  # wxGlade: MyDialog.<event_handler>
				self.Close()

    def OnCancel(self, event):  # wxGlade: MyDialog.<event_handler>
				self.Close()

# end of class MyDialog
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog_1 = PlaylistDialog(None, wx.ID_ANY, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()
