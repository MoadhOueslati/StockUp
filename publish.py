
class Publish:
    def __init__(self, mw):
        self.mw = mw
        self.facebook_worker = None
        self.email_worker = None
        self.mw.emailPushButton.clicked.connect(self.open_email_worker)
        self.mw.facebookPushButton.clicked.connect(self.open_faecbook_worker)
        self.open_email_worker() 
    
    def open_faecbook_worker(self):
        self.mw.facebookConsolePlainTextEdit.setVisible(True)
        self.mw.emailConsolePlainTextEdit.setVisible(False)
        self.mw.publishStackedWidget.setCurrentIndex(0)
        if self.facebook_worker == None:
            from facebook import Facebook
            self.facebook_worker = Facebook(self.mw)
    
    def open_email_worker(self):
        self.mw.facebookConsolePlainTextEdit.setVisible(False)
        self.mw.emailConsolePlainTextEdit.setVisible(True)
        self.mw.publishStackedWidget.setCurrentIndex(1)
        if self.email_worker == None:
            from email_sender import EmailSender
            self.email_worker = EmailSender(self.mw)

    

