import tkinter as tk
from mysql import connector
import login_page
# from login_page import LoginPage
from account import Account
import enable_face_recognition_page

class App(tk.Tk):
    def __init__(self):
        self.grey = '#CDCDCD'
        self.db = connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database='project'
        )

        self.cursor = self.db.cursor(buffered=True)

        tk.Tk.__init__(self)
        self.geometry('1000x700')
        self.resizable(0, 0)
        self.title('Project Name')
        self.configure(bg=self.grey)
        self._frame = None
        self.file_name = ''
        self.master_text = ''
        self.is_encrypted = False
        # self.account = Account(1, 'tom@gmail.com', 'tom', 'burke')
        self.switch_frame(login_page.LoginPage)
        # self.switch_frame(enable_face_recognition_page.EnableFaceRecognitionPage)
        self.file_in_db = False

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()