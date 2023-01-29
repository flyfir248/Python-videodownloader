import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from pytube import YouTube
from PyQt5.QtWidgets import QFileDialog

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("YouTube Downloader")

        # Create a label for the URL textbox
        url_label = QLabel("Enter video URL:")

        # Create a textbox for the user to enter the video URL
        self.url_textbox = QLineEdit()

        # Create a button to initiate the download
        download_button = QPushButton("Download")
        download_button.clicked.connect(self.download_video)

        # Create a layout to hold the label, textbox, and button
        layout = QVBoxLayout()
        layout.addWidget(url_label)
        layout.addWidget(self.url_textbox)
        layout.addWidget(download_button)

        # Set the layout for the main window
        self.setLayout(layout)

    def download_video(self):
        url = self.url_textbox.text()
        yt = YouTube(url)
        stream = yt.streams.first()
        save_path = QFileDialog.getSaveFileName(self, "Save Video", "", "All Files (*);;MP4 Files (*.mp4)")
        stream.download(save_path[0])

app = QApplication(sys.argv)
youtube_downloader = YouTubeDownloader()
youtube_downloader.show()
sys.exit(app.exec_())