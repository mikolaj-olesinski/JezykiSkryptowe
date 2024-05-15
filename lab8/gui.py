import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDateEdit, QListWidget, QFormLayout
from PySide6.QtCore import Qt, QRect
from widgets import FileSelectionWidget, DateSelectionWidget, LabelForForm
from constants import (WIDTH, HEIGHT, 
                       MIDDLE_LAYOUT_WIDTH, 
                       MIDDLE_LAYOUT_HEIGHT, 
                       MIDDLE_RIGHT_WIDTH, 
                       MIDDLE_RIGHT_HEIGHT, 
                       LABEL_HEIGHT,                 
                       REMOTE_HOST_LABEL_WIDTH,
                       REMOTE_HOST_LABEL_HEIGHT,
                        DATE_LABEL_WIDTH,
                        DATE_LABEL_HEIGHT,
                        TIME_LABEL_WIDTH,
                        TIME_LABEL_HEIGHT,
                        TIME_ZONE_LABEL_WIDTH,
                        TIME_ZONE_LABEL_HEIGHT,
                        STATUS_LABEL_WIDTH,
                        STATUS_LABEL_HEIGHT,
                        METHOD_LABEL_WIDTH,
                        METHOD_LABEL_HEIGHT,
                        RESOURCE_LABEL_WIDTH,
                        RESOURCE_LABEL_HEIGHT,
                        SIZE_LABEL_WIDTH,
                        SIZE_LABEL_HEIGHT,
                        PREVIOUS_BUTTON_WIDTH,
                        PREVIOUS_BUTTON_HEIGHT,
                        NEXT_BUTTON_WIDTH,
                        NEXT_BUTTON_HEIGHT,
                        CLEAR_BUTTON_WIDTH, 
                        CLEAR_BUTTON_HEIGHT
                        )



class UI_MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Log browser')
        self.setGeometry(200, 200, WIDTH, HEIGHT)
        self.setFixedSize(WIDTH, HEIGHT)

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        top_widget = QWidget(self)
        middle_widget = QWidget(self)
        bottom_widget = QWidget(self)

        main_layout.addWidget(top_widget)
        main_layout.addWidget(middle_widget)
        main_layout.addWidget(bottom_widget)

        top_layout = QHBoxLayout(top_widget)
        middle_layout = QHBoxLayout(middle_widget)
        bottom_layout = QHBoxLayout(bottom_widget)

        top_layout.setObjectName("top_layout")
        middle_layout.setObjectName("middle_layout")
        bottom_layout.setObjectName("bottom_layout")

        top_layout.setContentsMargins(15, 0, 0, 0)
        middle_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setContentsMargins(65, 0, 50, 0)

        top_widget.setLayout(top_layout)
        middle_widget.setLayout(middle_layout)
        bottom_widget.setLayout(bottom_layout)

        self.setup_top_layout(top_layout)
        self.setup_middle_layout(middle_layout, middle_widget)
        self.setup_bottom_layout(bottom_layout)


    def help_setup_middle_layout(self, layout):

        middle_widget = layout.findChild(QWidget, "middle_widget")

        middle_left_widget = QWidget(middle_widget)
        middle_left_top_widget = QWidget(middle_left_widget)
        middle_left_bottom_widget = QWidget(middle_left_widget)

        middle_right_widget = QWidget(middle_widget)
        middle_right_widget.setObjectName("middle_right_widget")

        layout.addWidget(middle_left_widget)
        layout.addWidget(middle_right_widget, alignment=Qt.AlignCenter | Qt.AlignCenter)

        middle_left_layout = QVBoxLayout(middle_left_widget)
        middle_left_top_layout = QHBoxLayout(middle_left_top_widget)
        middle_left_bottom_layout = QVBoxLayout(middle_left_bottom_widget)

        middle_left_layout.setObjectName("middle_left_layout")
        middle_left_top_layout.setObjectName("middle_left_top_layout")
        middle_left_bottom_layout.setObjectName("middle_left_bottom_layout")

        middle_left_layout.addWidget(middle_left_top_widget)
        middle_left_layout.addWidget(middle_left_bottom_widget)
        middle_left_widget.setLayout(middle_left_layout)
        middle_left_top_widget.setLayout(middle_left_top_layout)
        middle_left_bottom_widget.setLayout(middle_left_bottom_layout)

        middle_right_layout = QFormLayout(middle_right_widget)
        middle_right_layout.setContentsMargins(0, 100, 0, 0)
        middle_right_layout.setObjectName("middle_right_layout")
        middle_right_widget.setLayout(middle_right_layout)

        middle_left_widget.setFixedSize(MIDDLE_LAYOUT_WIDTH * 0.6, MIDDLE_LAYOUT_HEIGHT)
        middle_right_widget.setFixedSize(MIDDLE_LAYOUT_WIDTH * 0.4, MIDDLE_LAYOUT_HEIGHT)

        middle_left_top_widget.setFixedSize(MIDDLE_LAYOUT_WIDTH * 0.6, MIDDLE_LAYOUT_HEIGHT * 0.1)
        middle_left_bottom_widget.setFixedSize(MIDDLE_LAYOUT_WIDTH * 0.6, MIDDLE_LAYOUT_HEIGHT * 0.9)
        middle_left_bottom_layout.setContentsMargins(0, 0, 0, 0)
        middle_left_top_layout.setContentsMargins(15, 0, 0, 15)


    def setup_top_layout(self, layout):

        file_widget = FileSelectionWidget()
        file_widget.setObjectName("file_widget")
        file_widget.select_button.setObjectName("select_file_button")
        layout.addWidget(file_widget, alignment=Qt.AlignCenter)

    def setup_middle_layout(self, layout, widget):
    
        self.help_setup_middle_layout(layout)

        date_from_label = QLabel("Data od:")
        date_to_label = QLabel("Data do:")
        date_picker_from = DateSelectionWidget()
        date_picker_to = DateSelectionWidget()
        date_picker_from.date_edit.setObjectName("date_picker_from")
        date_picker_to.date_edit.setObjectName("date_picker_to")

        middle_left_top_layout = widget.findChild(QHBoxLayout, "middle_left_top_layout")
        middle_left_bottom_layout = widget.findChild(QVBoxLayout, "middle_left_bottom_layout")
        middle_right_layout = widget.findChild(QFormLayout, "middle_right_layout")


        middle_left_top_layout.addWidget(date_from_label, alignment=Qt.AlignCenter)
        middle_left_top_layout.addWidget(date_picker_from, alignment=Qt.AlignLeft)
        middle_left_top_layout.addWidget(date_to_label, alignment=Qt.AlignCenter)
        middle_left_top_layout.addWidget(date_picker_to, alignment=Qt.AlignLeft)

        middle_right_widget = widget.findChild(QWidget, "middle_right_widget")
        list_widget = QListWidget(middle_right_widget)
        list_widget.setObjectName("list_widget")
        list_widget.setFixedSize(500, 480)
        middle_left_bottom_layout.addWidget(list_widget, alignment=Qt.AlignTop | Qt.AlignCenter)

        remote_host_label = LabelForForm("Remote Host:", REMOTE_HOST_LABEL_WIDTH, REMOTE_HOST_LABEL_HEIGHT)
        remote_host_label.label_with_info.setObjectName("remote_host_label")

        date_label = LabelForForm("Date:", DATE_LABEL_WIDTH, DATE_LABEL_HEIGHT)
        date_label.label_with_info.setObjectName("date_label")

        time_label = LabelForForm("Time:", TIME_LABEL_WIDTH, TIME_LABEL_HEIGHT)
        time_label.label_with_info.setObjectName("time_label")

        timezone_label = LabelForForm("Timezone:", TIME_ZONE_LABEL_WIDTH, TIME_ZONE_LABEL_HEIGHT)
        timezone_label.label_with_info.setObjectName("timezone_label")

        status_label = LabelForForm("Status:", STATUS_LABEL_WIDTH, STATUS_LABEL_HEIGHT)
        status_label.label_with_info.setObjectName("status_label")

        method_label = LabelForForm("Method:", METHOD_LABEL_WIDTH, METHOD_LABEL_HEIGHT)
        method_label.label_with_info.setObjectName("method_label")

        resource_label = LabelForForm("Resource:", RESOURCE_LABEL_WIDTH, RESOURCE_LABEL_HEIGHT)
        resource_label.label_with_info.setObjectName("resource_label")

        size_label = LabelForForm("Size:", SIZE_LABEL_WIDTH, SIZE_LABEL_HEIGHT)
        size_label.label_with_info.setObjectName("size_label")

        middle_right_layout.addRow(remote_host_label.label, remote_host_label.label_with_info)
        middle_right_layout.addRow(date_label.label, date_label.label_with_info)
        middle_right_layout.addRow(time_label.label, time_label.label_with_info)
        middle_right_layout.addRow(timezone_label.label, timezone_label.label_with_info)
        middle_right_layout.addRow(status_label.label, status_label.label_with_info)
        middle_right_layout.addRow(method_label.label, method_label.label_with_info)
        middle_right_layout.addRow(resource_label.label, resource_label.label_with_info)
        middle_right_layout.addRow(size_label.label, size_label.label_with_info)


    def setup_bottom_layout(self, layout):
        previous_button = QPushButton("Previous")
        previous_button.setObjectName("previous_button")
        previous_button.setFixedSize(PREVIOUS_BUTTON_WIDTH, PREVIOUS_BUTTON_HEIGHT)

        next_button = QPushButton("Next")
        next_button.setObjectName("next_button")
        next_button.setFixedSize(NEXT_BUTTON_WIDTH, NEXT_BUTTON_HEIGHT)

        clear_button = QPushButton("Clear")
        clear_button.setObjectName("clear_button")
        clear_button.setFixedSize(CLEAR_BUTTON_WIDTH, CLEAR_BUTTON_HEIGHT)

        

        layout.addWidget(previous_button, alignment=Qt.AlignLeft)
        layout.addSpacing(160)
        layout.addWidget(next_button, alignment=Qt.AlignLeft)
        layout.addWidget(clear_button, alignment=Qt.AlignRight)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = UI_MainWindow()
    main_window.show()
    sys.exit(app.exec())