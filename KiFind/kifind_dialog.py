#!/usr/bin/env python

import wx
import pcbnew
import os
import time

from .kifind_plugin_gui import kifind_gui
from .kifind_plugin_action import FindAll, DoSelect, __version__

class KiFindDialog(kifind_gui):
    """Class that gathers all the Gui control"""

    def __ShowAll(self, do_tracks, do_mm):
        self.list_result.DeleteAllItems()
        vias = FindAll(self.board, do_tracks, do_mm)
        for key, value in vias.items():
            #print("Adding " + key)
            self.list_result.Append([key, value])        

    def __init__(self, board):
        """Init the brand new instance"""
        super(KiFindDialog, self).__init__(None)
        self.do_tracks = True
        self.do_mm = True
        self.index = 0
        self.board = board
        self.list_result.InsertColumn(0, "Value")
        self.list_result.InsertColumn(1, "Number")
        self.SetTitle("KiFind (ver.{})".format(__version__))
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
        self.but_cancel.Bind(wx.EVT_BUTTON, self.onCloseWindow)
        self.but_show.Bind(wx.EVT_BUTTON, self.onProcessAction)
        self.Bind(wx.EVT_RADIOBUTTON, self.onProcessMirror)
        self.list_result.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelected)
        #self.m_bitmap_help.SetBitmap(wx.Bitmap( os.path.join(os.path.dirname(os.path.realpath(__file__)), "rcs", "teardrops-help.png") ) )
        self.SetMinSize(self.GetSize())
        self.__ShowAll(self.do_tracks, self.do_mm)
                
    def onProcessMirror(self, event):
        rb = event.GetEventObject() 
        if rb == self.radio_tracks:
            self.do_tracks = True
        elif rb == self.radio_vias:
            self.do_tracks = False
        elif rb == self.radio_mm:
            self.do_mm = True
        elif rb == self.radio_mils:
            self.do_mm = False
        self.__ShowAll(self.do_tracks, self.do_mm)
        #print("Value: " + str(self.mirror_type))
        #print("Clicked: " + rb.GetLabel())

    def onProcessAction(self, event):
        try:
            # Executes the requested action
            #index = self.list_result.GetNextItem(0, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
            #print("Choosen: " + self.list_result.GetItemText(self.index))
            num = DoSelect(self.board, self.do_tracks, self.do_mm, self.list_result.GetItemText(self.index))
            pcbnew.UpdateUserInterface()
            s = ["vias", "tracks"][self.do_tracks]
            pcbnew.Refresh()            
            wx.MessageBox("Ready!\n\nProcessed: {} {}".format(num, s))
        except Exception as ex:
            wx.MessageBox("Error: {}".format(ex))
        self.EndModal(wx.ID_OK)
        
    def onSelected(self, event):
        #self.index = event.GetSelection()
        self.index = self.list_result.GetFirstSelected()
        #print("Selected: " + self.list_result.GetItemText(self.index))
        #DoSelect(self.board, do_tracks, self.list_result.GetItemText(index))

    def onCloseWindow(self, event):
        self.EndModal(wx.ID_OK)


def InitKiFindDialog(board):
    # Launch the dialog
    tg = KiFindDialog(board)
    tg.ShowModal()
    tg.Destroy()
    
if __name__ == '__main__':
    InitKiFindDialog(pcbnew.GetBoard())
