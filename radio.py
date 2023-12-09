from car_radio import *
from PyQt6.QtWidgets import *


class Radio(QMainWindow, Ui_MainWindow):
    """
    Class representing the workings of a car radio
    """
    def __init__(self, songs_bluetooth, songs_aux, songs_usb, songs_cd, volume, mode) -> None:
        """
        Method to initialize the values needed for the car radio
        :param songs_bluetooth: the song count for bluetooth
        :param songs_aux: the song count for aux
        :param songs_usb: the song count for usb
        :param songs_cd: the song count for cd
        :param volume: the volume of the radio
        :param mode: the value for the mode the radio is on
        """
        super().__init__()
        self.setupUi(self)
        self.songs_bluetooth = songs_bluetooth
        self.songs_aux = songs_aux
        self.songs_usb = songs_usb
        self.songs_cd = songs_cd
        self.volume = volume
        self.mode = mode
        self.label_big.setText(f'Hit the power button')
        self.button_power.setStyleSheet("border-image : url(power.png);")
        self.label_picture.hide()
        self.button_player.setCheckable(True)
        self.button_power.setCheckable(True)
        self.button_power.clicked.connect(lambda: self.power())
        self.button_ff.setIcon(QtGui.QIcon('ff.png'))
        self.button_play.setIcon(QtGui.QIcon('play.png'))
        self.button_vol.setIcon(QtGui.QIcon('vol.png'))
        self.button_rw.setIcon(QtGui.QIcon('rw.png'))

    def power(self) -> None:
        """
        Method to turn on and off the car radio
        """
        if self.button_power.isChecked():
            self.label_big.setText('Please select a listening mode')
            self.button_94.setChecked(True)
            self.label_picture.show()
            self.label_picture.setStyleSheet("border-image : url(home.png);")
            self.button_fm.clicked.connect(lambda: self.fm())
            self.button_bluetooth.clicked.connect(lambda: self.bluetooth())
            self.button_aux.clicked.connect(lambda: self.check_aux())
            self.button_usb.clicked.connect(lambda: self.check_usb())
            self.button_cd.clicked.connect(lambda: self.check_cd())
            self.button_vol.clicked.connect(lambda: self.vol())
            self.button_ff.clicked.connect(lambda: self.ff())
            self.button_rw.clicked.connect(lambda: self.rw())
        else:
            self.label_big.setText('')
            self.label_artist.setText('')
            self.label_album.setText('')
            self.label_song.setText('')
            self.label_vol.setText('')
            self.label_picture.setStyleSheet('')
            self.label.setText('')

    # def reset(self) -> None:
        """
        Method to help the function go back to a common point without restarting
        """
        # self.button_fm.clicked.connect(lambda: self.fm())
        # self.button_bluetooth.clicked.connect(lambda: self.bluetooth())
        # self.button_aux.clicked.connect(lambda: self.check_aux())
        # self.button_usb.clicked.connect(lambda: self.check_usb())
        # self.button_cd.clicked.connect(lambda: self.check_cd())
        # self.button_vol.clicked.connect(lambda: self.vol())
        # self.button_ff.clicked.connect(lambda: self.ff())
        # self.button_rw.clicked.connect(lambda: self.rw())

    def fm(self) -> None:
        """
        Method to explain how the fm works and a transition to the songs that can be played
        """
        self.outlet.setExclusive(False)
        self.button_radio_aux.setChecked(False)
        self.button_radio_usb.setChecked(False)
        self.outlet.setExclusive(True)
        self.button_94.setChecked(True)
        self.label_album.setText('')
        self.label_artist.setText('')
        self.label_song.setText('')
        self.label_big.setText('Please select station then hit play')
        self.button_play.clicked.connect(lambda: self.check_station())

    def check_station(self) -> None:
        """
        Method to determine the station is on for the fm to determine the song displayed
        """
        self.label_big.setText('')
        if self.button_94.isChecked():
            self.label_song.setText(f'Home')
            self.label_artist.setText(f'Phillip Phillip')
            self.label_album.setText(f'Home')
            self.label_picture.setStyleSheet("border-image : url(home.png);")
        elif self.button_96.isChecked():
            self.label_song.setText(f'Sing')
            self.label_artist.setText(f'Ed Sheeran')
            self.label_album.setText(f'X')
            self.label_picture.setStyleSheet("border-image : url(x.png);")
        elif self.button_98.isChecked():
            self.label_song.setText(f'Payphone')
            self.label_artist.setText(f'Maroon 5, Wiz Khalifa')
            self.label_album.setText(f'Overexposed')
            self.label_picture.setStyleSheet("border-image : url(pay.jpeg);")
        elif self.button_101.isChecked():
            self.label_song.setText(f'Wagon Wheel')
            self.label_artist.setText(f'Darius Rucker')
            self.label_album.setText(f'True Believers')
            self.label_picture.setStyleSheet("border-image : url(wagon.png);")
        elif self.button_104.isChecked():
            self.label_song.setText(f'Bohemian Rhapsody')
            self.label_artist.setText(f'Queen')
            self.label_album.setText(f'A Night At The Opera')
            self.label_picture.setStyleSheet("border-image : url(opera.png);")

    def bluetooth(self) -> None:
        """
        Method for bluetooth to display the songs
        """
        self.mode = 0
        self.station.setExclusive(False)
        self.button_94.setChecked(False)
        self.button_98.setChecked(False)
        self.button_101.setChecked(False)
        self.button_96.setChecked(False)
        self.button_104.setChecked(False)
        self.station.setExclusive(True)
        self.outlet.setExclusive(False)
        self.button_radio_aux.setChecked(False)
        self.button_radio_usb.setChecked(False)
        self.outlet.setExclusive(True)
        self.label_big.setText('')
        songs = ['Bang Bang', 'Paper Planes', 'Ophelia']
        artists = ['Jessie J', 'M.I.A.', 'The Lumineers']
        albums = ['Sweet Talker', 'Kala', 'Cleopatra']
        pictures = ['sweet', 'kala', 'cleopatra']
        self.label_song.setText(f'{songs[self.songs_bluetooth]}')
        self.label_artist.setText(f'{artists[self.songs_bluetooth]}')
        self.label_album.setText(f'{albums[self.songs_bluetooth]}')
        self.label_picture.setStyleSheet(f'border-image : url({pictures[self.songs_bluetooth]}.png);')

    def ff(self) -> None:
        """
        Method for fast forwarding through songs
        """
        if self.mode == 0:
            if self.songs_bluetooth == 1 or self.songs_bluetooth == 0:
                self.songs_bluetooth = self.songs_bluetooth + 1
                self.bluetooth()
            else:
                self.songs_bluetooth = 0
                self.bluetooth()
        elif self.mode == 1:
            if self.songs_aux == 1 or self.songs_aux == 0:
                self.songs_aux = self.songs_aux + 1
                self.aux()
            else:
                self.songs_aux = 0
                self.aux()
        elif self.mode == 2:
            if self.songs_usb == 1 or self.songs_usb == 0:
                self.songs_usb = self.songs_usb + 1
                self.usb()
            else:
                self.songs_usb = 0
                self.usb()
        elif self.mode == 3:
            self.check_ff()
            if self.check_ff() == 'yes':
                if self.songs_cd == 1 or self.songs_cd == 0:
                    self.songs_cd = self.songs_cd + 1
                    self.cd()
                else:
                    self.songs_cd = 0
                    self.cd()
            else:
                self.label_song.setText('')
                self.label_album.setText('')
                self.label_artist.setText('')
                self.label_big.setText(f'Please insert CD')

    def rw(self) -> None:
        """
        Method for rewinding through songs
        """
        if self.mode == 0:
            if self.songs_bluetooth == 1 or self.songs_bluetooth == 2:
                self.songs_bluetooth = self.songs_bluetooth - 1
                self.bluetooth()
            else:
                self.songs_bluetooth = 2
                self.bluetooth()
        elif self.mode == 1:
            if self.songs_aux == 1 or self.songs_aux == 2:
                self.songs_aux = self.songs_aux - 1
                self.aux()
            else:
                self.songs_aux = 2
                self.aux()
        elif self.mode == 2:
            if self.songs_usb == 1 or self.songs_usb == 2:
                self.songs_usb = self.songs_usb - 1
                self.usb()
            else:
                self.songs_usb = 2
                self.usb()
        elif self.mode == 3:
            self.check_rw()
            if self.check_rw() == 'yes':
                if self.songs_cd == 1 or self.songs_cd == 2:
                    self.songs_cd = self.songs_cd - 1
                    self.cd()
                else:
                    self.songs_cd = 2
                    self.cd()
            else:
                self.label_song.setText('')
                self.label_album.setText('')
                self.label_artist.setText('')
                self.label_big.setText(f'Please insert CD')

    def aux(self) -> None:
        """
        Method for displaying songs on aux mode
        """
        self.mode = 1
        self.station.setExclusive(False)
        self.button_94.setChecked(False)
        self.button_98.setChecked(False)
        self.button_101.setChecked(False)
        self.button_96.setChecked(False)
        self.button_104.setChecked(False)
        self.station.setExclusive(True)
        self.label_song.setText('')
        self.label_album.setText('')
        self.label_artist.setText('')
        if self.button_radio_aux.isChecked():
            self.label_big.setText('')
            songs = ['Young Dumb & Broke', 'These Days', 'This City']
            artists = ['Khalid', 'mike.', 'Sam Fischer']
            albums = [f'American Teen', "This isn't The Album", 'This City']
            pictures = ['teen', 'mike', 'city']
            self.label_song.setText(f'{songs[self.songs_aux]}')
            self.label_artist.setText(f'{artists[self.songs_aux]}')
            self.label_album.setText(f'{albums[self.songs_aux]}')
            self.label_picture.setStyleSheet(f'border-image : url({pictures[self.songs_aux]}.png);')
            self.mode = 1
        else:
            self.label_big.setText(f'Please plug in the aux cord')

    def usb(self) -> None:
        """
        Method for displaying songs in usb mode
        """
        self.station.setExclusive(False)
        self.button_94.setChecked(False)
        self.button_98.setChecked(False)
        self.button_101.setChecked(False)
        self.button_96.setChecked(False)
        self.button_104.setChecked(False)
        self.station.setExclusive(True)
        self.label_song.setText('')
        self.label_album.setText('')
        self.label_artist.setText('')
        if self.button_radio_usb.isChecked():
            self.label_big.setText('')
            songs = ['Uptown Girl', "I Won't Back Down", 'Fly Like An Eagle']
            artists = ['Billy Joel', 'Tom Petty', 'Steve Miller Band']
            albums = ['An Innocent Man', 'Full Moon Fever', 'Fly Like An Eagle']
            pictures = ['uptown', 'moon', 'eagle']
            self.label_song.setText(f'{songs[self.songs_usb]}')
            self.label_artist.setText(f'{artists[self.songs_usb]}')
            self.label_album.setText(f'{albums[self.songs_usb]}')
            self.label_picture.setStyleSheet(f'border-image : url({pictures[self.songs_usb]}.png);')
            self.mode = 2
        else:
            self.label_big.setText(f'Please plug in the USB cord')

    def cd(self) -> None:
        """
        Method to display songs for cd mode
        """
        self.station.setExclusive(False)
        self.button_94.setChecked(False)
        self.button_98.setChecked(False)
        self.button_101.setChecked(False)
        self.button_96.setChecked(False)
        self.button_104.setChecked(False)
        self.station.setExclusive(True)
        self.outlet.setExclusive(False)
        self.button_radio_aux.setChecked(False)
        self.button_radio_usb.setChecked(False)
        self.outlet.setExclusive(True)
        self.label_song.setText('')
        self.label_album.setText('')
        self.label_artist.setText('')
        songs = ['Castle On The Hill', 'Perfect', 'Galway Girl']
        self.label_song.setText(f'{songs[self.songs_cd]}')
        self.label_artist.setText(f'Ed Sheeran')
        self.label_album.setText(f'Divide')
        self.label_picture.setStyleSheet("border-image : url(divide.png);")
        self.mode = 3

    def check_ff(self) -> str:
        """
        Method to check if the cd is in before fast forwarding
        :return: returning yes or no to check if the cd is in
        """
        if self.button_player.isChecked():
            self.label_big.setText('')
            return 'yes'
        else:
            return 'no'

    def check_rw(self) -> str:
        """
        Method to check if the cd is in before rewinding
        :return: returning yes or no to check if the cd is in
        """
        if self.button_player.isChecked():
            self.label_big.setText('')
            return 'yes'
        else:
            return 'no'

    def check_aux(self) -> None:
        """
        Method to check if the aux cord is plugged in
        """
        if self.button_radio_aux.isChecked():
            self.label.setText('Aux is plugged in')
            self.aux()
        else:
            self.label_song.setText('')
            self.label_album.setText('')
            self.label_artist.setText('')
            self.label_big.setText('Please plug in the aux')

    def check_usb(self) -> None:
        """
        Method to check if the usb is plugged in
        """
        if self.button_radio_usb.isChecked():
            self.label.setText('USB is plugged in')
            self.usb()
        else:
            self.label_song.setText('')
            self.label_album.setText('')
            self.label_artist.setText('')
            self.label_big.setText('Please plug in the USB')

    def check_cd(self) -> None:
        """
        Method to check if the cd has been inserted
        """
        if self.button_player.isChecked():
            self.label_big.setText('')
            self.cd()
        else:
            self.label_song.setText('')
            self.label_album.setText('')
            self.label_artist.setText('')
            self.label_big.setText(f'Please insert CD')

    def vol(self) -> None:
        """
        Method for increasing the volume until it reaches the maximum of 6
        """
        if self.volume == 0 or self.volume == 1 or self.volume == 2 or self.volume == 3 or self.volume == 4 or self.volume == 5:
            self.volume = self.volume + 1
            self.label_vol.setText(f'VOL {self.volume}')
        elif self.volume > 5:
            self.volume = 0
            self.label_vol.setText(f'VOL {self.volume}')
