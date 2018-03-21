# -*- coding: utf-8 -*-
#
# This file is part of Linux Show Player
#
# Copyright 2012-2018 Francesco Ceruti <ceppofrancy@gmail.com>
# Copyright 2012-2016 Thomas Achtner <info@offtools.de>
#
# Linux Show Player is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Linux Show Player is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Linux Show Player.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtCore import QT_TRANSLATE_NOOP, Qt
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QLabel, \
    QHBoxLayout, QSpinBox, QLineEdit

from lisp.ui.settings.settings_page import ConfigurationPage
from lisp.ui.ui_utils import translate


class OscSettings(ConfigurationPage):
    Name = QT_TRANSLATE_NOOP('SettingsPageName', 'OSC settings')

    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)

        self.groupBox = QGroupBox(self)
        self.groupBox.setLayout(QVBoxLayout())
        self.groupBox.setTitle(translate('OscSettings', 'OSC Settings'))
        self.layout().addWidget(self.groupBox)

        hbox = QHBoxLayout()
        self.inportBox = QSpinBox(self)
        self.inportBox.setMinimum(1000)
        self.inportBox.setMaximum(99999)
        label = QLabel(translate('OscSettings', 'Input Port:'))
        hbox.layout().addWidget(label)
        hbox.layout().addWidget(self.inportBox)
        self.groupBox.layout().addLayout(hbox)

        hbox = QHBoxLayout()
        self.outportBox = QSpinBox(self)
        self.outportBox.setMinimum(1000)
        self.outportBox.setMaximum(99999)
        label = QLabel(translate('OscSettings', 'Output Port:'))
        hbox.layout().addWidget(label)
        hbox.layout().addWidget(self.outportBox)
        self.groupBox.layout().addLayout(hbox)

        hbox = QHBoxLayout()
        self.hostnameEdit = QLineEdit()
        self.hostnameEdit.setText('localhost')
        self.hostnameEdit.setMaximumWidth(200)
        label = QLabel(translate('OscSettings', 'Hostname:'))
        hbox.layout().addWidget(label)
        hbox.layout().addWidget(self.hostnameEdit)
        self.groupBox.layout().addLayout(hbox)

        self.loadConfiguration()

    def applySettings(self):
        self.config['inPort'] = self.inportBox.value()
        self.config['outPort'] = self.outportBox.value()
        self.config['hostname'] = self.hostnameEdit.text()

        self.config.write()

    def loadConfiguration(self):
        self.inportBox.setValue(self.config['inPort'])
        self.outportBox.setValue(self.config['outPort'])
        self.hostnameEdit.setText(self.config['hostname'])
