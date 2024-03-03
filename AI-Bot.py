from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from Backend import Chatbot
import threading


# Front end Design
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 400)
        self.setWindowTitle("AI-ChatBot")
        self.cb = Chatbot()
        # create widgets
        self.textbox = QTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setGeometry(10, 10, 380, 300)

        self.linebox = QLineEdit(self)
        self.linebox.setPlaceholderText("Message AI_BOT")
        self.linebox.setGeometry(10, 330, 380, 30)
        self.linebox.returnPressed.connect(self.send_clicked)

        sendbutton = QPushButton('send', self)
        sendbutton.setGeometry(400, 330, 50, 30)
        sendbutton.clicked.connect(self.send_clicked)

    def send_clicked(self):
        user_input = self.linebox.text().strip()
        self.textbox.append(f"<p style='color:#333333'><b>You:</b> {user_input}</p>")
        self.linebox.clear()

        thread = threading.Thread(target=self.get_bot_res, args=(user_input,))
        thread.start()

    def get_bot_res(self, user_input):
        response = self.cb.get_result(user_input)
        self.textbox.append(f"<p style='color:#333333;background-color:#E9E9E9'><b>AI-Bot:</b> {response}</p>")


app = QApplication(sys.argv)
chatbot = ChatbotWindow()
chatbot.show()
sys.exit(app.exec())
