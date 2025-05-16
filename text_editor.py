from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import os

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64]

class textEditor(QWidget):
    def __init__(self, *args, **kwargs):
        super(textEditor, self).__init__(*args, **kwargs)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.editor = QTextEdit()
        self.editor.setAutoFormatting(QTextEdit.AutoAll)
        self.editor.selectionChanged.connect(self.update_format)
        self.editor.setFont(QFont('Times', 12))
        self.editor.setFontPointSize(12)

        self.editor.setStyleSheet("QTextEdit { background-color: white; border: 1px solid rgb(29, 35, 50) }")

        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(0, 0, 0, 0)

        # Edit Toolbar
        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setStyleSheet("border: none")
        edit_toolbar.setIconSize(QSize(16, 16))

        cut_action = QAction(QIcon(os.path.join('pictures', 'scissors.png')), "Cut", self)
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)

        copy_action = QAction(QIcon(os.path.join('pictures', 'document-copy.png')), "Copy", self)
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)

        paste_action = QAction(QIcon(os.path.join('pictures', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)

        select_action = QAction(QIcon(os.path.join('pictures', 'selection-input.png')), "Select all", self)
        select_action.triggered.connect(self.editor.selectAll)
        edit_toolbar.addAction(select_action)

        self.fontsize = QComboBox()
        self.fontsize.setStyleSheet("""QComboBox {
                                        border: 1px solid gray;
                                        border-radius: 3px;
                                        padding: 1px 18px 1px 3px;
                                    }""")
        self.fontsize.addItems([str(s) for s in FONT_SIZES])
        self.fontsize.currentIndexChanged[str].connect(lambda s: self.editor.setFontPointSize(float(s)))
        edit_toolbar.addWidget(self.fontsize)

        self.bold_action = QAction(QIcon(os.path.join('pictures', 'edit-bold.png')), "Bold", self)
        self.bold_action.setCheckable(True)
        self.bold_action.toggled.connect(lambda x: self.editor.setFontWeight(QFont.Bold if x else QFont.Normal))
        edit_toolbar.addAction(self.bold_action)

        self.italic_action = QAction(QIcon(os.path.join('pictures', 'edit-italic.png')), "Italic", self)
        self.italic_action.setCheckable(True)
        self.italic_action.toggled.connect(self.editor.setFontItalic)
        edit_toolbar.addAction(self.italic_action)

        self.underline_action = QAction(QIcon(os.path.join('pictures', 'edit-underline.png')), "Underline", self)
        self.underline_action.setCheckable(True)
        self.underline_action.toggled.connect(self.editor.setFontUnderline)
        edit_toolbar.addAction(self.underline_action)

        self.alignl_action = QAction(QIcon(os.path.join('pictures', 'edit-alignment.png')), "Align left", self)
        self.alignl_action.setCheckable(True)
        self.alignl_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
        edit_toolbar.addAction(self.alignl_action)

        self.alignc_action = QAction(QIcon(os.path.join('pictures', 'edit-alignment-center.png')), "Align center", self)
        self.alignc_action.setCheckable(True)
        self.alignc_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignCenter))
        edit_toolbar.addAction(self.alignc_action)

        self.alignr_action = QAction(QIcon(os.path.join('pictures', 'edit-alignment-right.png')), "Align right", self)
        self.alignr_action.setCheckable(True)
        self.alignr_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
        edit_toolbar.addAction(self.alignr_action)

        self.alignj_action = QAction(QIcon(os.path.join('pictures', 'edit-alignment-justify.png')), "Justify", self)
        self.alignj_action.setCheckable(True)
        self.alignj_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignJustify))
        edit_toolbar.addAction(self.alignj_action)

        format_group = QActionGroup(self)
        format_group.setExclusive(True)
        format_group.addAction(self.alignl_action)
        format_group.addAction(self.alignc_action)
        format_group.addAction(self.alignr_action)
        format_group.addAction(self.alignj_action)

        self.text_color_action = QAction(QIcon(os.path.join('pictures', 'edit-color.png')), "Text color...", self)
        self.text_color_action.triggered.connect(self.change_text_color)
        edit_toolbar.addAction(self.text_color_action)


        self.image_action = QAction(QIcon(os.path.join('pictures', 'ui-tab--plus.png')), "insert image", self)
        self.image_action.triggered.connect(self.insert_image)
        edit_toolbar.addAction(self.image_action)


        # Add the format toolbar to the horizontal layout
        toolbar_layout.addWidget(edit_toolbar)
        # toolbar_layout.addSpacing(60)  

        # Add the horizontal toolbar layout to the main layout
        layout.addLayout(toolbar_layout)

        layout.addWidget(self.editor)

        self._format_actions = [
            self.fontsize,
            self.bold_action,
            self.italic_action,
            self.underline_action,
        ]

        self.update_format()

    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    def update_format(self):
        self.block_signals(self._format_actions, True)
        self.fontsize.setCurrentText(str(int(self.editor.fontPointSize())))
        self.italic_action.setChecked(self.editor.fontItalic())
        self.underline_action.setChecked(self.editor.fontUnderline())
        self.bold_action.setChecked(self.editor.fontWeight() == QFont.Bold)
        self.alignl_action.setChecked(self.editor.alignment() == Qt.AlignLeft)
        self.alignc_action.setChecked(self.editor.alignment() == Qt.AlignCenter)
        self.alignr_action.setChecked(self.editor.alignment() == Qt.AlignRight)
        self.alignj_action.setChecked(self.editor.alignment() == Qt.AlignJustify)
        self.block_signals(self._format_actions, False)

    def change_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            cursor = self.editor.textCursor()
            format = cursor.charFormat()
            format.setForeground(QBrush(color))
            cursor.mergeCharFormat(format)
    
    def insert_image(self):
        # Open file dialog to select an image
        filePath, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
        print(filePath)

        if filePath:
            # Load the image using QPixmap to get its original size
            pixmap = QPixmap(filePath)

            # Get the width of the image
            image_width = pixmap.width()
            image_height = pixmap.height()
            print(f"Original Image Width: {image_width} px")
            print(f"Original Image Height: {image_height} px")

            # Create a QTextImageFormat object
            imageFormat = QTextImageFormat()
            imageFormat.setName(filePath)

            if image_height > 400 or image_width > 400:
                # Set the desired width and height for the image
                desired_width = image_width // 2  # Change this value to control the width
                desired_height = image_height // 2 # Change this value to control the height
                imageFormat.setWidth(desired_width)
                imageFormat.setHeight(desired_height)

            # Get the QTextCursor at the current position
            cursor = self.editor.textCursor()
            
            # Insert the image with the specified format
            cursor.insertImage(imageFormat)