from gui import UI_MainWindow   
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QDateEdit, QLabel, QPushButton, QListWidgetItem, QListWidget
from widgets import FileSelectionWidget
from help_func.read_http_log import filter_logs_by_date, read_l
from help_func.timezones import get_region_from_timezone
from constants import LOG_MASTER_LENGTH
import sys

need_refresh = False
all_logs = []
logs_and_logs_short = {}

def handle_select_file_button(main_window: UI_MainWindow):
    file_widget = main_window.findChild(FileSelectionWidget, "file_widget")

    file_path = file_widget.select_file()
    add_file_to_list_widget(main_window, file_path)

    global need_refresh
    need_refresh = True
    get_all_logs(main_window)


def add_file_to_list_widget(main_window: UI_MainWindow, file_path: str):
    list_widget = main_window.findChild(QListWidget, "list_widget")
    
    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        QMessageBox.critical(main_window, "Error", "File not found")
        return
    
    for line in file:
        short_line = line[:LOG_MASTER_LENGTH] + "..." if len(line) > LOG_MASTER_LENGTH else line

        global logs_and_logs_short
        logs_and_logs_short[short_line] = line
        list_widget.addItem(short_line)


def handle_list_widget_item_click(main_window: UI_MainWindow):
    list_widget = main_window.findChild(QListWidget, "list_widget")
    selected_item = list_widget.currentItem()
    selected_item = logs_and_logs_short[selected_item.text()]
    if selected_item:
        fill_labels_from_log(main_window, selected_item)


def fill_labels_from_log(main_window: UI_MainWindow, log):
    log_tuple = read_l(log)
    if len(log_tuple) != 6:
        QMessageBox.critical(main_window, "Error", "Invalid log format")
        return

    remote_host, date, method, resource, code, bytes = log_tuple[0], log_tuple[1], log_tuple[2], log_tuple[3], log_tuple[4], log_tuple[5]
    
    middle_right_widget = main_window.findChild(QWidget, "middle_right_widget")

    host_name_label = middle_right_widget.findChild(QLabel, "remote_host_label")
    host_name_label.setText(remote_host)

    date_label = middle_right_widget.findChild(QLabel, "date_label")
    date_label.setText(date.strftime("%Y-%m-%d"))

    time_label = middle_right_widget.findChild(QLabel, "time_label")
    time_label.setText(date.strftime("%H:%M:%S"))

    timezone_label = middle_right_widget.findChild(QLabel, "timezone_label")
    region = get_region_from_timezone(date.strftime("%z"))
    timezone_label.setText(region)
    
    status_label = middle_right_widget.findChild(QLabel, "status_label")
    status_label.setText(code)

    method_label = middle_right_widget.findChild(QLabel, "method_label")
    method_label.setText(method)

    resource_label = middle_right_widget.findChild(QLabel, "resource_label")
    resource_label.setText(resource) if resource != '/' else resource_label.clear()

    size_label = middle_right_widget.findChild(QLabel, "size_label")
    size_label.setText(bytes + " bytes") if bytes != None else size_label.clear()

def clear_all_labels(main_window: UI_MainWindow):
    middle_right_widget = main_window.findChild(QWidget, "middle_right_widget")

    host_label = middle_right_widget.findChild(QLabel, "remote_host_label")
    host_label.clear()

    date_label = middle_right_widget.findChild(QLabel, "date_label")
    date_label.clear()

    time_label = middle_right_widget.findChild(QLabel, "time_label")
    time_label.clear()

    timezone_label = middle_right_widget.findChild(QLabel, "timezone_label")
    timezone_label.clear()

    status_label = middle_right_widget.findChild(QLabel, "status_label")
    status_label.clear()

    method_label = middle_right_widget.findChild(QLabel, "method_label")
    method_label.clear()

    resource_label = middle_right_widget.findChild(QLabel, "resource_label")
    resource_label.clear()

    size_label = middle_right_widget.findChild(QLabel, "size_label")
    size_label.clear()


def get_current_list_item_row(list_widget):
    current_item = list_widget.currentItem()
    if current_item:
        current_row = list_widget.row(current_item)
        return current_row
    else:
        return None

def handle_previous_button(main_window: UI_MainWindow):
    list_widget = main_window.findChild(QListWidget, "list_widget")
    current_row = get_current_list_item_row(list_widget)
    if current_row > 0:
        list_widget.setCurrentRow(current_row - 1)
        fill_labels_from_log(main_window, list_widget.currentItem().data)
    elif current_row == None:
        list_widget.setCurrentRow(0)
        fill_labels_from_log(main_window, list_widget.currentItem().data)

def handle_next_button(main_window: UI_MainWindow):
    list_widget = main_window.findChild(QListWidget, "list_widget")
    current_row = get_current_list_item_row(list_widget)
    
    if current_row < list_widget.count() - 1:
        list_widget.setCurrentRow(current_row + 1)
        fill_labels_from_log(main_window, list_widget.currentItem().data)

    elif current_row == None:
        list_widget.setCurrentRow(0)
        fill_labels_from_log(main_window, list_widget.currentItem().data)

def handle_clear_button(main_window: UI_MainWindow):
    clear_all_labels(main_window)



def handle_date_change(main_window: UI_MainWindow):
    date_from_widget = main_window.findChild(QDateEdit, "date_picker_from")
    date_from = date_from_widget.date().toPython()
    date_to_widget = main_window.findChild(QDateEdit, "date_picker_to")
    date_to = date_to_widget.date().toPython()

    global all_logs
    filtered_logs = filter_logs_by_date(all_logs, date_from, date_to)
    update_list_widget(main_window, filtered_logs)
    

def update_list_widget(main_window: UI_MainWindow, logs):
    list_widget = main_window.findChild(QListWidget, "list_widget")
    list_widget.clear()
    for log in logs:
        short_log = log[:LOG_MASTER_LENGTH] + "..." if len(log) > LOG_MASTER_LENGTH else log

        global logs_and_logs_short
        logs_and_logs_short[short_log] = log
        list_widget.addItem(short_log)

def get_all_logs(main_window: UI_MainWindow):
    global need_refresh
    global all_logs

    if need_refresh:
        file_widget = main_window.findChild(FileSelectionWidget, "file_widget")
        file_path = file_widget.get_file_path()

        new_logs = []
        try:
            with open(file_path, "r") as file:
                for line in file:
                    new_logs.append(line)
        except FileNotFoundError:
            QMessageBox.critical(main_window, "Error", "File not found")
        
        all_logs = new_logs
        need_refresh = False
        return all_logs
    else:
        return all_logs


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = UI_MainWindow()
    main_window.show()

    
    select_file_button = main_window.findChild(QPushButton, "select_file_button")
    select_file_button.clicked.connect(lambda: handle_select_file_button(main_window))

    list_widget = main_window.findChild(QListWidget, "list_widget")
    list_widget.itemClicked.connect(lambda: handle_list_widget_item_click(main_window))

    previous_button = main_window.findChild(QPushButton, "previous_button")
    previous_button.clicked.connect(lambda: handle_previous_button(main_window))

    next_button = main_window.findChild(QPushButton, "next_button")
    next_button.clicked.connect(lambda: handle_next_button(main_window))

    clear_button = main_window.findChild(QPushButton, "clear_button")
    clear_button.clicked.connect(lambda: handle_clear_button(main_window))

    date_from_widget = main_window.findChild(QDateEdit, "date_picker_from")
    date_from_widget.dateChanged.connect(lambda: handle_date_change(main_window))

    date_to_widget = main_window.findChild(QDateEdit, "date_picker_to")
    date_to_widget.dateChanged.connect(lambda: handle_date_change(main_window))


    sys.exit(app.exec())