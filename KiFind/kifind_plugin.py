#!/usr/bin/env python

import wx
import os
from pcbnew import ActionPlugin, GetBoard

from .kifind_dialog import InitKiFindDialog

class KiFindPlugin(ActionPlugin):
    """Class that gathers the actionplugin stuff"""
    def defaults(self):
        self.name = "KiFind"
        self.category = "Modify PCB"
        self.description = "Find tracks or vias with selected parameters"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'KiFind.png')
        self.show_toolbar_button = True

    def Run(self):
        InitKiFindDialog(GetBoard())
