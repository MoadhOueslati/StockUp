import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Video Player")
        self.setGeometry(100, 100, 800, 600)  # Set the window size

        # Create a QWebEngineView widget
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # Load the YouTube video URL
        video_url = "https://www.youtube.com/embed/Wh-0FcxP-kU?autoplay=1"
        self.browser.load(QUrl(video_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoPlayer()
    window.show()
    sys.exit(app.exec_())
