## Task Tracker
## Created by dbugr (https://dbugr.vercel.app/)

import sys
from PyQt6.QtCore import QTimer, QTime
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                             QWidget, QSpinBox, QTextEdit, QGridLayout, QInputDialog,
                             QMessageBox, QWidgetAction, QSystemTrayIcon, QDialog, QLineEdit, QDialogButtonBox, QVBoxLayout)
from plyer import notification
from About import AboutDialog
from TaskManager import TaskManager
from TaskManager import Task

class TaskTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.work_time = 25 * 60
        self.break_time = 5 * 60
        self.time_remaining = self.work_time
        self.running = False
        self.is_break = False
        self.task_manager = TaskManager()

        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        about_action = QWidgetAction(self)
        about_action.setText("About")
        about_action.triggered.connect(self.show_about_dialog)
        menubar = self.menuBar()
        help_menu = menubar.addMenu("&Help")
        help_menu.addAction(about_action)

        self.setWindowTitle("Task Tracker")
        self.show()

    def show_about_dialog(self):
        about_dialog = AboutDialog(self)
        about_dialog.exec()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)

        self.timer_label = QLabel()
        self.timer_label.setStyleSheet("font-size: 30px;")
        layout.addWidget(self.timer_label, 0, 0, 1, 4)
        self.update_display()

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button, 1, 0)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_timer)
        layout.addWidget(self.stop_button, 1, 1)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)
        layout.addWidget(self.reset_button, 1, 2)

        self.work_duration_label = QLabel("Work (min):")
        layout.addWidget(self.work_duration_label, 1, 3)

        self.work_duration = QSpinBox()
        self.work_duration.setRange(1, 120)
        self.work_duration.setValue(self.work_time // 60)
        self.work_duration.valueChanged.connect(self.update_work_duration)
        layout.addWidget(self.work_duration, 1, 4)

        self.break_duration_label = QLabel("Break (min):")
        layout.addWidget(self.break_duration_label, 2, 3)

        self.break_duration = QSpinBox()
        self.break_duration.setRange(1, 120)
        self.break_duration.setValue(self.break_time // 60)
        self.break_duration.valueChanged.connect(self.update_break_duration)
        layout.addWidget(self.break_duration, 2, 4)

        self.task_label = QLabel("Tasks")
        self.task_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.task_label, 3, 0, 1, 5)

        self.task_list = QTextEdit()
        self.task_list.setReadOnly(True)
        layout.addWidget(self.task_list, 4, 0, 1, 5)

        self.add_task_button = QPushButton("Add Task")
        self.add_task_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_task_button, 5, 0)

        self.remove_task_button = QPushButton("Remove Task")
        self.remove_task_button.clicked.connect(self.remove_task)
        layout.addWidget(self.remove_task_button, 5, 1)

        self.save_tasks_button = QPushButton("Save Tasks")
        self.save_tasks_button.clicked.connect(self.save_tasks_to_db)
        layout.addWidget(self.save_tasks_button, 5, 2)

        self.load_tasks_button = QPushButton("Load Tasks")
        self.load_tasks_button.clicked.connect(self.load_tasks_from_db)
        layout.addWidget(self.load_tasks_button, 5, 3)

        self.setWindowTitle("Task Tracker")
        self.setWindowIcon(QIcon("icon.png"))
        self.show()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.timer.start(1000)

    def stop_timer(self):
        self.running = False
        self.timer.stop()

    def reset_timer(self):
        self.running = False
        self.timer.stop()
        self.is_break = False
        self.time_remaining = self.work_time
        self.update_display()

    def update_timer(self):
        if self.running:
            self.time_remaining -= 1
            if self.time_remaining == 0:
                self.is_break = not self.is_break
                self.time_remaining = self.break_time if self.is_break else self.work_time
                if self.is_break:
                    title = "Break time!"
                    message = "Time to relax and take a break."
                else:
                    title = "Task Tracker"
                    message = "Time's up! Start your break."
                self.show_notification(title, message)
            self.update_display()

    def update_display(self):
        time = QTime(0, 0).addSecs(self.time_remaining)
        self.timer_label.setText(time.toString("mm:ss"))

    def update_work_duration(self, value):
        self.work_time = value * 60

    def update_break_duration(self, value):
        self.break_time = value * 60

    def add_task(self):
        task_dialog = QDialog(self)
        task_dialog.setWindowTitle("Add Task")
        
        layout = QVBoxLayout()
        
        description_label = QLabel("Task Description:")
        layout.addWidget(description_label)
        description_input = QLineEdit()
        layout.addWidget(description_input)
        
        duration_label = QLabel("Task Duration (min, max 25):")
        layout.addWidget(duration_label)
        duration_input = QSpinBox()
        duration_input.setRange(1, 25)
        layout.addWidget(duration_input)
        
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(task_dialog.accept)
        buttons.rejected.connect(task_dialog.reject)
        layout.addWidget(buttons)
        
        task_dialog.setLayout(layout)
        
        result = task_dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            task_description = description_input.text()
            task_duration = duration_input.value()* 60
            if task_description:
                task = Task(task_description, task_duration)
                self.task_manager.add_task(task)
                self.refresh_task_list()
        else:
            print("This is NOT clause")

    def remove_task(self):
        task_index, ok = QInputDialog.getInt(self, "Remove Task", "Enter the task index:")
        if ok and task_index >= 0:
            self.task_manager.remove_task(task_index - 1)
            self.refresh_task_list()

    def save_tasks_to_db(self):
        self.task_manager.save_tasks_to_db()
        QMessageBox.information(self, "Task Tracker", "Tasks saved successfully")

    def load_tasks_from_db(self):
        self.task_manager.load_tasks_from_db()
        self.refresh_task_list()        

    def refresh_task_list(self):
        tasks = self.task_manager.list_tasks()
        self.task_list.clear()
        for index, (task_description, task_duration) in enumerate(tasks, start=1):
            task_duration_min = task_duration // 60
            self.task_list.append(f"{index}. {task_description} ({task_duration_min} min)")

    def show_notification(self, title, message):
        icon = QSystemTrayIcon()
        icon.setIcon(QIcon("icon.png"))
        icon.showMessage(title, message, QSystemTrayIcon.MessageType.Information, 5000)

    def show_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.exec()

if __name__ == "__main__":
        app = QApplication(sys.argv)
        task_tracker = TaskTracker()
        sys.exit(app.exec())
            

