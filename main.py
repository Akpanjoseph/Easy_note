import sys

from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

class liteWord(QMainWindow):

    def __init__(self):
        super(liteWord, self).__init__()
        self.setGeometry(50,100,500,700)

        self.editor = QTextEdit()
        self.editor.setFontPointSize(14)
        self.editor.setStyleSheet('color:blue;')

        self.fontSize_box = QSpinBox()
        self.setCentralWidget(self.editor)

        self.create_menuBar()
        self.create_toolBar()

    def create_menuBar(self):
        menu = QMenuBar()
        self.setMenuBar(menu)

        file_menu = QMenu('&File',self)
        menu.addMenu(file_menu)

        save_to_pdf = QAction('Save as pdf',self)
        save_to_pdf.triggered.connect(self.save_as_pdf)
        file_menu.addAction(save_to_pdf)

        view_menu = QMenu('&view', self)
        menu.addMenu(view_menu)

        edit_menu = QMenu('&Edit', self)
        menu.addMenu(edit_menu)
    def create_toolBar(self):
        tool_bar= QToolBar()
        self.addToolBar(tool_bar)


        undo_action = QAction('\t\t\t\tUndo',self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)

        re_action = QAction('Redo', self)
        re_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(re_action)

        cut_action = QAction('cut', self)
        cut_action.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut_action)

        paste_action = QAction('paste', self)
        paste_action.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste_action)

        copy_action = QAction('copy', self)
        copy_action.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy_action)

        tool_bar.addSeparator()

        fontText = QLabel('fontSize',self)
        tool_bar.addWidget(fontText)

        self.fontSize_box.setValue(14)
        self.fontSize_box.valueChanged.connect(self.set_font_Size)
        tool_bar.addWidget(self.fontSize_box)

    def set_font_Size(self):
        value = self.fontSize_box.value()
        self.editor.setFontPointSize(value)

    def save_as_pdf(self):
        file_path , _=QFileDialog.getSaveFileName(
            self,
            caption='Save as Pdf',
            filter='text(*.txt)'
        )
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(file_path)
        self.editor.document().print_(printer)

app = QApplication(sys.argv)
window = liteWord()
window.show()
app.exec_()
