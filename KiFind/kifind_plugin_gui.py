# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class kifind_gui
###########################################################################

class kifind_gui ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 404,330 ), style = wx.DEFAULT_DIALOG_STYLE )

		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sizer_main = wx.BoxSizer( wx.VERTICAL )

		sb_find = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"To find: " ), wx.HORIZONTAL )

		self.radio_tracks = wx.RadioButton( sb_find.GetStaticBox(), wx.ID_ANY, u"Tracks", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.radio_tracks.SetValue( True )
		sb_find.Add( self.radio_tracks, 0, wx.ALL, 5 )


		sb_find.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.radio_vias = wx.RadioButton( sb_find.GetStaticBox(), wx.ID_ANY, u"Vias", wx.DefaultPosition, wx.DefaultSize, 0 )
		sb_find.Add( self.radio_vias, 0, wx.ALL, 5 )


		sb_find.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		sizer_main.Add( sb_find, 1, wx.EXPAND, 5 )

		sb_units = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Units: " ), wx.HORIZONTAL )

		self.radio_mm = wx.RadioButton( sb_units.GetStaticBox(), wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.radio_mm.SetValue( True )
		sb_units.Add( self.radio_mm, 0, wx.ALL, 5 )


		sb_units.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.radio_mils = wx.RadioButton( sb_units.GetStaticBox(), wx.ID_ANY, u"mils", wx.DefaultPosition, wx.DefaultSize, 0 )
		sb_units.Add( self.radio_mils, 0, wx.ALL, 5 )


		sb_units.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		sizer_main.Add( sb_units, 1, wx.EXPAND, 5 )

		self.list_result = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_SINGLE_SEL|wx.LC_REPORT )
		self.list_result.SetMinSize( wx.Size( -1,150 ) )

		sizer_main.Add( self.list_result, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.but_show = wx.Button( self, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.but_show, 0, wx.ALL, 5 )

		self.but_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.but_cancel, 0, wx.ALL, 5 )


		sizer_main.Add( bSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( sizer_main )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


