from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys


# Front end Design
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("ChatBot")
        # create widgets
        textbox = QTextEdit(self)
        textbox.setReadOnly(True)
        textbox.setGeometry(10, 10, 380, 300)

        linebox = QLineEdit(self)
        linebox.setGeometry(10,330,380,30)

        sendbutton = QPushButton('send', self)
        sendbutton.setGeometry(400,330,50,30)

app = QApplication(sys.argv)
chatbot = ChatbotWindow()
chatbot.show()
sys.exit(app.exec())
