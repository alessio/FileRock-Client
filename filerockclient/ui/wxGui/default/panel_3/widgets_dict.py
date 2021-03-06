# -*- coding: ascii -*-
#  ______ _ _      _____            _       _____ _ _            _
# |  ____(_) |    |  __ \          | |     / ____| (_)          | |
# | |__   _| | ___| |__) |___   ___| | __ | |    | |_  ___ _ __ | |_
# |  __| | | |/ _ \  _  // _ \ / __| |/ / | |    | | |/ _ \ '_ \| __|
# | |    | | |  __/ | \ \ (_) | (__|   <  | |____| | |  __/ | | | |_
# |_|    |_|_|\___|_|  \_\___/ \___|_|\_\  \_____|_|_|\___|_| |_|\__|
#
# Copyright (C) 2012 Heyware s.r.l.
#
# This file is part of FileRock Client.
#
# FileRock Client is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FileRock Client is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FileRock Client. If not, see <http://www.gnu.org/licenses/>.
#

"""
This is the widgets_dict module.




----

This module is part of the FileRock Client.

Copyright (C) 2012 - Heyware s.r.l.

FileRock Client is licensed under GPLv3 License.

"""

from filerockclient.ui.wxGui.default.panel_3.widgets.SettingsWidgets import *


WIDGETS = {
    'User': {
        'warebox_path': lambda parent, val, _: DirPickerCtrl(parent, -1, val)
    },
    "NOCFG": {
        'cloud_storage': lambda parent,
                                val,
                                _: CloudComboBox(parent,
                                                 -1,
                                                 style=wx.CB_READONLY),
        'replica_cloud': lambda parent,
                                val,
                                _: ReplicaComboBox(parent,
                                                   -1,
                                                   style=wx.CB_READONLY),
    },
    "User Defined Options": {
        'osx_label_shellext': lambda parent, val, _: CheckBox(val, parent),
        'on_tray_click': lambda parent,
                                val,
                                _: ComboBox(parent,
                                            -1,
                                            val,
                                            choices=TASKBARLEFTCLICKACTIONS_LABELS,
                                            style=wx.CB_READONLY),
        'proxy_usage': lambda parent,
                              val,
                              panel: Proxy_options(val,
                                                   parent,
                                                   panel,
                                                   wx.HORIZONTAL),

    }
}