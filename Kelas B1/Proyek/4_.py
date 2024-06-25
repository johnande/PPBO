import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import functools
import pygame
import re
from mutagen.mp3 import MP3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

pygame.init()
pygame.mixer.init()

class Model:
    def __init__(self):
        self.songDirectories = {
            "Pop": r"D:\Kuliah\PPBO\Project\Music\Pop",
            "Rock": r"D:\Kuliah\PPBO\Project\Music\Rock",
            "Instrumental": r"D:\Kuliah\PPBO\Project\Music\Instrumental",
            "Relaxing": r"D:\Kuliah\PPBO\Project\Music\Relaxing"
        }
        self.iconDirectory = r"D:\Kuliah\PPBO\Project\Icons"
        self.backgroundImage = r"D:\Kuliah\PPBO\Project\Background\background song"
        self.allSongsList = []
        self.currentSong = None

    def searchForSongs(self):
        self.allSongsList = []
        for genre in self.songDirectories.values():
            a = os.listdir(genre)
            for x in a:
                if x.endswith(".mp3"):
                    self.allSongsList.append(x)         
        self.originalSongsList = self.allSongsList.copy() 


    def filterSongs(self, searchText):
        if not searchText:
            self.allSongsList = self.originalSongsList.copy()
        else:
            self.allSongsList = [song for song in self.originalSongsList if searchText.lower() in song.lower()]

    def shuffleSongs(self):
        import random
        random.shuffle(self.allSongsList)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.listWidgetMusic.itemClicked.connect(self.playNewSong)
        self.view.labelPlayPause.mousePressEvent = functools.partial(self.playPause)
        self.view.labelNextSong.mousePressEvent = functools.partial(self.playNextSong)
        self.view.labelPreviousSong.mousePressEvent = functools.partial(self.playPreviousSong)
        self.view.horizontalSliderMusic.sliderReleased.connect(self.seekSong)
        self.view.lineEditSearch.textEdited.connect(self.filterSongs)
        self.view.buttonShuffle.clicked.connect(self.shuffleSongs)
        self.view.buttonMenu.clicked.connect(self.openGenreWindow)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000) 
        self.timer.timeout.connect(self.updateProgress)
        self.is_seeking = False 
    def playNewSong(self, event=None):
        self.view.horizontalSliderMusic.setValue(0)  
        selected_items = self.view.listWidgetMusic.selectedItems()
        if not selected_items:
            return
        self.model.currentSong = selected_items[0].text() + ".mp3"

        song_path = None
        for genre, path in self.model.songDirectories.items():
            potential_path = os.path.join(path, self.model.currentSong)
            if os.path.exists(potential_path):
                song_path = potential_path
                break

        if not song_path:
            return
        
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        self.timer.start()
        self.view.labelPlayPause.setPixmap(QtGui.QPixmap(os.path.join(self.model.iconDirectory, "pause.png")))
        
        try:
            metaData = MP3(song_path)
            duration = int(metaData.info.length)
        except Exception as e:
            sound = pygame.mixer.Sound(song_path)
            duration = int(sound.get_length())
        
        self.view.horizontalSliderMusic.setMaximum(duration) 

        title = os.path.splitext(os.path.basename(song_path))[0]
        artist = str(metaData.get("TPE1", "Unknown Artist")) if 'metaData' in locals() else "Unknown Artist"
        artist = re.sub(r"[\(\[].*?[\)\]]", "", artist)
        self.view.labelSongName.setText(title)
        self.view.labelSongArtist.setText(artist)
        self.view.startScrollingTitle(title)

    def updateProgress(self):
        self.view.horizontalSliderMusic.setValue(self.view.horizontalSliderMusic.value() + 1)
        if self.view.horizontalSliderMusic.value() == self.view.horizontalSliderMusic.maximum():
            self.playNextSong(None)

    def playPause(self, event):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.timer.stop()  
            self.view.labelPlayPause.setPixmap(QtGui.QPixmap(os.path.join(self.model.iconDirectory, "play.png")))
        else:
            pygame.mixer.music.unpause()
            self.timer.start()  
            self.view.labelPlayPause.setPixmap(QtGui.QPixmap(os.path.join(self.model.iconDirectory, "pause.png")))


    def playNextSong(self, event):
        if hasattr(self.model, 'allSongsList'):
            current_index = self.view.listWidgetMusic.currentRow()
            next_index = (current_index + 1) % self.view.listWidgetMusic.count()
            self.view.listWidgetMusic.setCurrentRow(next_index)
            selected_item = self.view.listWidgetMusic.currentItem()
            if selected_item:
                self.playNewSong()

    def playPreviousSong(self, event=None):
        if hasattr(self.model, 'allSongsList'):
            current_index = self.view.listWidgetMusic.currentRow()
            previous_index = (current_index - 1) % self.view.listWidgetMusic.count()
            self.view.listWidgetMusic.setCurrentRow(previous_index)
            selected_item = self.view.listWidgetMusic.currentItem()
            if selected_item:
                self.playNewSong()

    def seekSong(self):
        seek_pos = self.view.horizontalSliderMusic.value()
        song_path = ""
        for genre, path in self.model.songDirectories.items():
            potential_path = os.path.join(path, self.model.currentSong)
            if os.path.exists(potential_path):
                song_path = potential_path
                break

        metaData = MP3(song_path)
        song_duration = metaData.info.length

        if not self.is_seeking:
            self.is_seeking = True
            self.timer.stop()  

        pygame.mixer.music.stop()
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(start=seek_pos)
        self.view.horizontalSliderMusic.setValue(seek_pos)
        self.timer.start()
        self.is_seeking = False

    def filterSongs(self, searchText):
        self.model.filterSongs(searchText)
        self.view.listWidgetMusic.clear()
        for song in self.model.allSongsList:
            song = song.replace(".mp3", "")
            item = QtWidgets.QListWidgetItem()
            item.setText(song)
            self.view.listWidgetMusic.addItem(item)

    def shuffleSongs(self):
        self.model.shuffleSongs()
        self.view.listWidgetMusic.clear()
        for song in self.model.allSongsList:
            song = song.replace(".mp3", "")
            item = QtWidgets.QListWidgetItem()
            item.setText(song)
            self.view.listWidgetMusic.addItem(item)

    def openGenreWindow(self):
        genre_model = GenreModel()
        genre_view = GenreView()
        self.genre_controller = GenreController(genre_model, genre_view, self)
        genre_view.show()


class View(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Relaxify")
        self.resize(1040, 562)
        self.setStyleSheet("background-color:black")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Relaxify")

        self.labelBackground = QtWidgets.QLabel(self)
        self.labelBackground.setGeometry(QtCore.QRect(730, -30, 400, 800))
        self.labelBackground.setText("")
        self.setScaledBackground(self.labelBackground, r"D:\Kuliah\PPBO\Project\Background\background song")
        self.labelBackground.setObjectName("labelBackground")

        self.labelNextSong = QtWidgets.QLabel(self)
        self.labelNextSong.setGeometry(QtCore.QRect(930, 470, 41, 61))
        self.labelNextSong.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.labelNextSong.setText("")
        self.labelNextSong.setPixmap(QtGui.QPixmap(os.path.join(r"D:\Kuliah\PPBO\Project\Icons", "skip")))
        self.labelNextSong.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNextSong.setObjectName("labelNextSong")
        
        self.horizontalSliderMusic = QtWidgets.QSlider(self)
        self.horizontalSliderMusic.setGeometry(QtCore.QRect(750, 450, 261, 10))
        self.horizontalSliderMusic.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.horizontalSliderMusic.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderMusic.setObjectName("horizontalSliderMusic")
        
        self.labelPreviousSong = QtWidgets.QLabel(self)
        self.labelPreviousSong.setGeometry(QtCore.QRect(790, 470, 41, 61))
        self.labelPreviousSong.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.labelPreviousSong.setText("")
        self.labelPreviousSong.setPixmap(QtGui.QPixmap(os.path.join(r"D:\Kuliah\PPBO\Project\Icons", "previous")))
        self.labelPreviousSong.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPreviousSong.setObjectName("labelPreviousSong")
        
        self.labelPlayPause = QtWidgets.QLabel(self)
        self.labelPlayPause.setGeometry(QtCore.QRect(850, 470, 61, 61))
        self.labelPlayPause.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.labelPlayPause.setText("")
        self.labelPlayPause.setPixmap(QtGui.QPixmap(os.path.join(r"D:\Kuliah\PPBO\Project\Icons", "play.png")))
        self.labelPlayPause.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlayPause.setObjectName("labelPlayPause")
        
        self.labelSongNameContainer = QtWidgets.QWidget(self)
        self.labelSongNameContainer.setGeometry(QtCore.QRect(760, 80, 950, 111))
        self.labelSongNameContainer.setStyleSheet("background: transparent;")
        self.labelSongName = QtWidgets.QLabel(self.labelSongNameContainer)
        self.labelSongName.setGeometry(QtCore.QRect(0, 0, 251, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(28)
        self.labelSongName.setFont(font)
        self.labelSongName.setStyleSheet("color:white; background: transparent;")
        self.labelSongName.setAlignment(Qt.AlignCenter)
        self.labelSongName.setObjectName("labelSongName")
        
        self.labelSongArtist = QtWidgets.QLabel(self)
        self.labelSongArtist.setGeometry(QtCore.QRect(760, 170, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(16)
        self.labelSongArtist.setFont(font)
        self.labelSongArtist.setStyleSheet("color:white; background: transparent;")
        self.labelSongArtist.setAlignment(Qt.AlignCenter)
        self.labelSongArtist.setObjectName("labelSongArtist")

        self.labelCloseWindow = QtWidgets.QLabel(self)
        self.labelCloseWindow.setGeometry(QtCore.QRect(950, 40, 61, 61))
        self.labelCloseWindow.setStyleSheet("background-color:rgba()")
        self.labelCloseWindow.setText("")
        self.labelCloseWindow.setPixmap(QtGui.QPixmap(os.path.join(r"D:\Kuliah\PPBO\Project\Icons", "close")))
        self.labelCloseWindow.setObjectName("labelCloseWindow")
        
        self.listWidgetMusic = QtWidgets.QListWidget(self)
        self.listWidgetMusic.setGeometry(QtCore.QRect(70, 140, 601, 331))
        self.listWidgetMusic.setStyleSheet("background-color:rgb(20,20,20);\nborder-radius: 10px;\ncolor:white")
        self.listWidgetMusic.setObjectName("listWidgetMusic")

        self.lineEditSearch = QtWidgets.QLineEdit(self)
        self.lineEditSearch.setGeometry(QtCore.QRect(70, 70, 601,40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight Condensed")
        font.setPointSize(18)
        self.lineEditSearch.setFont(font)
        self.lineEditSearch.setStyleSheet("border-radius:1px;\nborder-color:white;\ncolor:white;\nbackground-color:rgb(10,10,10)\n")
        self.lineEditSearch.setText("")
        self.lineEditSearch.setObjectName("lineEditSearch")

        self.labelSearch = QtWidgets.QLabel(self)
        self.labelSearch.setGeometry(QtCore.QRect(780, 350, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        self.labelSearch.setFont(font)
        self.labelSearch.setStyleSheet("color:white;\nbackground-color:rgba()")
        self.labelSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSearch.setObjectName("labelSearch")
        self.labelCloseWindow.mousePressEvent = functools.partial(self.closeApp)

        self.labelSearchforsong = QtWidgets.QLabel(self)
        self.labelSearchforsong.setGeometry(QtCore.QRect(70, 30, 251, 40))  
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        self.labelSearchforsong.setFont(font)
        self.labelSearchforsong.setStyleSheet("color:white;\nbackground-color:rgba()")
        self.labelSearchforsong.setAlignment(Qt.AlignLeft)
        self.labelSearchforsong.setObjectName("labelSearch")
        self.labelSearchforsong.setText("Search for a song:")

        self.buttonShuffle = QtWidgets.QPushButton(self)
        self.buttonShuffle.setGeometry(QtCore.QRect(340, 490, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.buttonShuffle.setFont(font)
        self.buttonShuffle.setStyleSheet("color:white; background-color:rgb(30,30,30); border-radius:10px;")
        self.buttonShuffle.setObjectName("buttonShuffle")
        self.buttonShuffle.setText("Shuffle")
        
        self.buttonMenu = QtWidgets.QPushButton(self)
        self.buttonMenu.setGeometry(QtCore.QRect(110, 490, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.buttonMenu.setFont(font)
        self.buttonMenu.setStyleSheet("color:white; background-color:rgb(30,30,30); border-radius:10px;")
        self.buttonMenu.setObjectName("buttonMenu")
        self.buttonMenu.setText("Menu")
    
    def startScrollingTitle(self, title):
        font_metrics = QtGui.QFontMetrics(self.labelSongName.font())
        text_width = font_metrics.width(title)
        self.labelSongName.setFixedWidth(text_width)
        self.animation = QtCore.QPropertyAnimation(self.labelSongName, b"geometry")
        self.animation.setDuration(12000)
        self.animation.setStartValue(QtCore.QRect(self.labelSongNameContainer.width(), 0, self.labelSongName.width(), self.labelSongName.height()))
        self.animation.setEndValue(QtCore.QRect(-self.labelSongName.width(), 0, self.labelSongName.width(), self.labelSongName.height()))
        self.animation.setLoopCount(-1)
        self.animation.start()

    def setScaledBackground(self, label, image_path):
        pixmap = QtGui.QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
        label.setPixmap(scaled_pixmap)

    def closeApp(self, event):
        app.closeAllWindows()

class GenreModel:
    def __init__(self):
        self.genres = {
            "Pop": r"D:\Kuliah\PPBO\Project\Music\Pop",
            "Rock": r"D:\Kuliah\PPBO\Project\Music\Rock",
            "Instrumental": r"D:\Kuliah\PPBO\Project\Music\Instrumental",
            "Relaxing": r"D:\Kuliah\PPBO\Project\Music\Relaxing"
        }
    
    def get_genre_path(self, genre):
        return self.genres.get(genre, None)
    
class GenreView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Genre Window")
        self.resize(600, 300)
        self.setStyleSheet("background-color:black")
        self.setWindowTitle("Genre Selection")
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 10, 300, 70))
        self.label.setStyleSheet("color:white; background: transparent;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Pilih genre music yang anda butuhkan <3")

        self.buttonPop = QtWidgets.QPushButton(self)
        self.buttonPop.setGeometry(QtCore.QRect(100, 70, 400, 30))
        self.buttonPop.setStyleSheet("color:white; background-color:rgb(30,30,30); border-radius:10px;")
        self.buttonPop.setObjectName("buttonPop")
        self.buttonPop.setText("Pop")

        self.buttonRock = QtWidgets.QPushButton(self)
        self.buttonRock.setGeometry(QtCore.QRect(100, 110, 400, 30))
        self.buttonRock.setStyleSheet("color:white; background-color:rgb(30,30,30); border-radius:10px;")
        self.buttonRock.setObjectName("buttonRock")
        self.buttonRock.setText("Rock")

        self.buttonInstrumental = QtWidgets.QPushButton(self)
        self.buttonInstrumental.setGeometry(QtCore.QRect(100, 150, 400, 30))
        self.buttonInstrumental.setStyleSheet("color:white; background-color:rgb(30,30,30); border-radius:10px;")
        self.buttonInstrumental.setObjectName("buttonInstrumental")
        self.buttonInstrumental.setText("Instrumental")

        self.buttonRelaxing = QtWidgets.QPushButton(self)
        self.buttonRelaxing.setGeometry(QtCore.QRect(100, 190, 400, 30))
        self.buttonRelaxing.setStyleSheet("color:white; background-color:rgb(30,30,30); border-radius:10px;")
        self.buttonRelaxing.setObjectName("buttonRelaxing")
        self.buttonRelaxing.setText("Relaxing")
        
        self.buttonBack = QtWidgets.QPushButton(self)
        self.buttonBack.setGeometry(QtCore.QRect(250, 240, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonBack.setStyleSheet("color:white; background-color:rgb(30,30,30); border-radius:10px;")
        self.buttonBack.setObjectName("buttonBack")
        self.buttonBack.setText("Back")

class GenreController:
    def __init__(self, model, view, main_controller):
        self.model = model
        self.view = view
        self.main_controller = main_controller
        self.view.buttonPop.clicked.connect(lambda: self.genreSelected("Pop"))
        self.view.buttonRock.clicked.connect(lambda: self.genreSelected("Rock"))
        self.view.buttonInstrumental.clicked.connect(lambda: self.genreSelected("Instrumental"))
        self.view.buttonRelaxing.clicked.connect(lambda: self.genreSelected("Relaxing"))
        self.view.buttonBack.clicked.connect(self.view.close)

    def genreSelected(self, genre):
        genre_path = self.model.get_genre_path(genre)
        if genre_path:
            songs = [f for f in os.listdir(genre_path) if f.endswith(".mp3")]
            self.main_controller.model.allSongsList = songs 
            self.main_controller.view.listWidgetMusic.clear()
            for song in songs:
                item = QtWidgets.QListWidgetItem()
                item.setText(os.path.splitext(song)[0])
                self.main_controller.view.listWidgetMusic.addItem(item)
            self.main_controller.view.labelSongName.setText("")
            self.main_controller.view.labelSongArtist.setText("")
            self.view.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    model = Model()
    model.searchForSongs() 
    view = View()
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
