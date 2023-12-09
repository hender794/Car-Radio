from radio import *


def main():
    application = QApplication([])
    window = Radio(songs_bluetooth=0, songs_aux=0, songs_usb=0, songs_cd=0, volume=0, mode=0)
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
