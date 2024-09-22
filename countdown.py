from qtpy.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
from qtpy.QtCore import Qt, QTimer
from qtpy.QtGui import QColor
import random
import sys

class CountdownApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Countdown Timer")
        self.resize(500,500);
        # self.showFullScreen()

        # Initial settings
        self.time_left = 180
        self.timer_running = False
        
        # Background color
        self.setStyleSheet("background-color: darkgreen;")
        
        # Timer label
        self.label = QLabel(self.format_time(self.time_left), self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 800px; color: white;")
        
        # Buttons
        self.start_button = QPushButton('Start', self)
        self.pause_button = QPushButton('Pause', self)
        self.reset_button = QPushButton('Reset', self)
        for button in [self.start_button, self.pause_button, self.reset_button]:
            button.setStyleSheet("font-size: 120px; color: white;")

        # Layout
        grid = QGridLayout(self)
        grid.addWidget(self.label, 0, 0, 1, 3, alignment=Qt.AlignCenter)
        
        grid.addWidget(self.start_button, 1, 0, alignment=Qt.AlignLeft)
        grid.addWidget(self.pause_button, 1, 1, alignment=Qt.AlignCenter)
        grid.addWidget(self.reset_button, 1, 3, alignment=Qt.AlignRight)
        
        
        # Connect buttons
        self.start_button.clicked.connect(self.start_timer)
        self.pause_button.clicked.connect(self.pause_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        
        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

    def start_timer(self):
        if not self.timer_running:
            self.timer.start(100)
            self.timer_running = True

    def pause_timer(self):
        if self.timer_running:
            self.timer.stop()
            self.timer_running = False

    def reset_timer(self):
        self.timer.stop()
        self.timer_running = False
        self.time_left = 180
        self.update_label()
        self.setStyleSheet("background-color: darkgreen;")

    def update_timer(self):
        self.time_left -= 1
        self.update_label()

        if self.time_left == 60:
            self.setStyleSheet("background-color: #FDDA0D;")
        elif self.time_left == 30:
            self.setStyleSheet("background-color: darkred;")
        elif self.time_left < 0:
            self.random_color()
        elif self.time_left < 15:
            if self.time_left % 2:
                self.setStyleSheet("background-color: darkred;")
            else:
                self.setStyleSheet("background-color: black;")
            
    def update_label(self):
        self.label.setText(self.format_time(self.time_left))

    def format_time(self, seconds):
        min, sec = divmod(max(0, seconds), 60)
        return f"{min}:{sec:02}"

    def random_color(self):
        r, g, b = [random.randint(0, 255) for _ in range(3)]
        self.setStyleSheet(f"background-color: rgb({r},{g},{b});")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CountdownApp()
    ex.show()
    sys.exit(app.exec_())