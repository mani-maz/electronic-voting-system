import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLCDNumber,
    QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy,
    QLineEdit, QMessageBox, QSpinBox, QScrollArea, QDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


# -------------------- Vote Item --------------------
class VoteItem(QWidget):
    def __init__(self, username):
        super().__init__()

        self.count = 0

        self.label = QLabel(username)
        self.label.setFont(QFont("Arial", 11, QFont.Bold))
        self.label.setStyleSheet("color: blue;")

        self.button = QPushButton("Vote")
        self.button.setMinimumWidth(70)
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(3)
        self.lcd.display(0)
        self.lcd.setMinimumWidth(100)
        self.lcd.hide()

        layout = QHBoxLayout()
        layout.addWidget(self.label, 2)
        layout.addWidget(self.button, 2)
        layout.addWidget(self.lcd, 2)

        self.setLayout(layout)

        #self.button.clicked.connect(self.add_vote)

    def add_vote(self):
        self.count += 1
        self.lcd.display(self.count)


# -------------------- Welcome Window --------------------
class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Electronic Voting System")
        self.resize(700, 300)

        label = QLabel("Electronic Voting System")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 30, QFont.Bold))

        subtitle = QLabel("Secure and simple electronic voting")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont("Arial", 11))

        button = QPushButton("Continue")
        button.setMinimumHeight(44)
        button.clicked.connect(self.open_nomination)

        footer = QLabel("created_by_mani_maz")
        footer.setAlignment(Qt.AlignCenter)
        footer.setFont(QFont("Arial", 9))

        layout = QVBoxLayout()
        layout.setContentsMargins(45, 30, 45, 18)
        layout.addStretch()
        layout.addWidget(label)
        layout.addSpacing(8)
        layout.addWidget(subtitle)
        layout.addSpacing(28)
        layout.addWidget(button)
        layout.addStretch()
        layout.addWidget(footer)

        self.setLayout(layout)

    def open_nomination(self):
        self.nomination = NominationWindow()
        self.nomination.show()
        self.close()


# -------------------- Nomination Window --------------------
class NominationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nomination")
        self.resize(750, 300)

        self.candidates = []

        title = QLabel("Election Setup")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 22, QFont.Bold))

        subtitle = QLabel("Set the number of candidates and voting rules")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont("Arial", 10))

        candidate_layout = QHBoxLayout()
        candidate_label = QLabel("Number of candidates")
        candidate_label.setFont(QFont("Arial", 11, QFont.Bold))

        self.spin = QSpinBox()
        self.spin.setMinimum(1)
        self.spin.setMaximum(1000)
        self.spin.valueChanged.connect(self.update_vote_setting_limits)

        candidate_layout.addWidget(candidate_label)
        candidate_layout.addStretch()
        candidate_layout.addWidget(self.spin)

        settings_layout = QHBoxLayout()

        top_label = QLabel("Number of winners to highlight")
        top_label.setFont(QFont("Arial", 10, QFont.Bold))

        self.top_count_spin = QSpinBox()
        self.top_count_spin.setMinimum(1)
        self.top_count_spin.setMaximum(self.spin.value())
        self.top_count_spin.setValue(1)

        lock_label = QLabel("Lock after votes")
        lock_label.setFont(QFont("Arial", 10, QFont.Bold))

        self.lock_after_spin = QSpinBox()
        self.lock_after_spin.setMinimum(1)
        self.lock_after_spin.setMaximum(self.spin.value())
        self.lock_after_spin.setValue(min(5, self.spin.value()))

        settings_layout.addWidget(top_label)
        settings_layout.addWidget(self.top_count_spin)
        settings_layout.addSpacing(24)
        settings_layout.addWidget(lock_label)
        settings_layout.addWidget(self.lock_after_spin)
        settings_layout.addStretch()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter candidate name and press Enter")
        self.name_edit.returnPressed.connect(self.add_candidate)

        self.delete_button = QPushButton("Delete the Last")
        self.delete_button.setMinimumHeight(35)
        self.delete_button.clicked.connect(self.delete_last_candidate)

        self.ok_button = QPushButton("Start Voting")
        self.ok_button.setMinimumHeight(40)
        self.ok_button.clicked.connect(self.finish_nomination)

        self.show_button = QPushButton("Show Candidates")
        self.show_button.setMinimumHeight(40)
        self.show_button.clicked.connect(self.show_candidates)

        footer = QLabel("created_by_mani_maz")
        footer.setAlignment(Qt.AlignCenter)
        footer.setFont(QFont("Arial", 9))

        layout = QVBoxLayout()
        layout.setContentsMargins(35, 24, 35, 15)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(14)
        layout.addLayout(candidate_layout)
        layout.addLayout(settings_layout)
        layout.addSpacing(16)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.delete_button, alignment=Qt.AlignLeft)
        layout.addStretch()

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.show_button)
        buttons_layout.addWidget(self.ok_button)

        layout.addLayout(buttons_layout)
        layout.addWidget(footer)

        self.setLayout(layout)

    def update_vote_setting_limits(self, value):
        self.top_count_spin.setMaximum(max(1, value))
        self.lock_after_spin.setMaximum(max(1, value))

        if self.top_count_spin.value() > value:
            self.top_count_spin.setValue(value)

        if self.lock_after_spin.value() > value:
            self.lock_after_spin.setValue(value)

    def add_candidate(self):
        name = self.name_edit.text().strip()

        if name:
            self.candidates.append(name)
            self.name_edit.clear()
    
    def delete_last_candidate(self):
        if self.candidates:
            removed = self.candidates.pop()

            QMessageBox.information(
                self,
                "Deleted",
                f"Removed: {removed}"
            )
        else:
            QMessageBox.warning(
                self,
                "Warning",
                "No candidate to remove."
            )


    def show_candidates(self):
        if not self.candidates:
            QMessageBox.information(
                self,
                "Candidates",
                "No candidates entered yet."
            )
            return

        text = "Candidates (in entered order):\n\n"

        for i, name in enumerate(self.candidates, 1):
            text += f"{i}. {name}\n"

        QMessageBox.information(
            self,
            "Candidates",
            text
        )



    def finish_nomination(self):
        required = self.spin.value()

        if len(self.candidates) != required:
            QMessageBox.warning(
                self,
                "Error",
                f"You must enter exactly {required} candidate name(s).\\nCurrent: {len(self.candidates)}"
            )
        
            return
        self.voting = VotingWindow(
            self.candidates,
            self.top_count_spin.value(),
            self.lock_after_spin.value()
        )
        self.voting.show()
        self.close()
    


#------------------- End Button ---------------------------

class ResultWindow(QDialog):
    def __init__(self, results, top_count):
        super().__init__()

        self.setWindowTitle("Voting Result")
        self.resize(600, 650)
        self.top_count = max(1, min(top_count, len(results)))

        main_layout = QVBoxLayout()

        title = QLabel("Voting Result")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(title)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QWidget()
        result_layout = QVBoxLayout(content)

        for index, (name, votes) in enumerate(results):

            row = QHBoxLayout()

            rank_label = QLabel(f"{index + 1}.")
            rank_label.setFont(QFont("Arial", 12, QFont.Bold))
            rank_label.setMinimumWidth(35)

            name_label = QLabel(name)
            name_label.setFont(QFont("Arial", 12, QFont.Bold))

            vote_label = QLabel(f"{votes} vote(s)")
            vote_label.setFont(QFont("Arial", 11))
            vote_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            if index < self.top_count:
                name_label.setStyleSheet("""
                    QLabel {
                        background-color: #F4C542;
                        color: #15171C;
                        padding: 7px 9px;
                        border-radius: 7px;
                    }
                """)

            row.addWidget(rank_label)
            row.addWidget(name_label, 1)
            row.addWidget(vote_label)

            result_layout.addLayout(row)

            result_layout.addSpacing(8)

        result_layout.addStretch()

        scroll.setWidget(content)

        main_layout.addWidget(scroll)

        close_button = QPushButton("Close")
        close_button.setMinimumHeight(35)
        close_button.clicked.connect(self.close)

        main_layout.addWidget(close_button)

        footer = QLabel("created_by_mani_maz")
        footer.setAlignment(Qt.AlignCenter)
        footer.setFont(QFont("Arial", 9))
        main_layout.addWidget(footer)

        self.setLayout(main_layout)

# -------------------- Voting Window --------------------
class VotingWindow(QWidget):
    def __init__(self, candidates, top_count, lock_after):
        super().__init__()

        self.setWindowTitle("Electronic Voting System")
        self.resize(1100, 700)

        self.vote_items = []
        self.can_vote = False
        self.current_votes = 0
        self.max_votes = max(1, min(lock_after, len(candidates)))
        self.top_count = max(1, min(top_count, len(candidates)))
        self.voted_items = set()
        self.votes_visible = False

        # Scroll Area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()
        grid = QGridLayout()
        grid.setSpacing(15)

        n = len(candidates)

        if n % 3 == 0:
            base = n
            extra = 0
        else:
            base = n - (n % 3)
            extra = n % 3

        rows_per_col = base // 3 if base else 0

        index = 0

        for col in range(3):
            for row in range(rows_per_col):
                item = VoteItem(candidates[index])
                self.vote_items.append(item)
                grid.addWidget(item, row, col)
                index += 1

        if extra:
            for row in range(extra):
                item = VoteItem(candidates[index])
                self.vote_items.append(item)
                grid.addWidget(item, row, 3)
                index += 1
                
        for item in self.vote_items: 
            item.button.setEnabled(False) 
            item.button.clicked.connect(lambda _, i=item: self.cast_vote(i))

        container.setLayout(grid)
        scroll.setWidget(container)

        self.voter_count = 0
        self.voter_names = []

        bottom_layout = QHBoxLayout()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter voter name...")
        self.name_edit.returnPressed.connect(self.register_voter)

        self.bottom_lcd = QLCDNumber()
        self.bottom_lcd.setDigitCount(4)
        self.bottom_lcd.display(0)
        self.bottom_lcd.setMinimumWidth(120)
        
        self.show_voters_button = QPushButton("Show Voters")
        self.show_voters_button.setMinimumHeight(35)
        self.show_voters_button.clicked.connect(self.show_voters)

        self.show_votes_button = QPushButton("Show Votes")
        self.show_votes_button.setMinimumHeight(35)
        self.show_votes_button.clicked.connect(self.toggle_votes)

        self.finish_button = QPushButton("Finish")
        self.finish_button.setMinimumHeight(35)
        self.finish_button.clicked.connect(self.finish_current_voter)
        self.finish_button.hide()

        bottom_layout.addWidget(self.name_edit, 4)
        bottom_layout.addWidget(self.bottom_lcd, 1)
        bottom_layout.addWidget(self.show_voters_button)
        bottom_layout.addWidget(self.show_votes_button)
        bottom_layout.addWidget(self.finish_button)

        self.end_button = QPushButton("END")
        self.end_button.setMinimumHeight(40)
        self.end_button.clicked.connect(self.show_top_voters)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll)
        main_layout.addLayout(bottom_layout)
        main_layout.addWidget(self.end_button)

        footer = QLabel("created_by_mani_maz")
        footer.setAlignment(Qt.AlignCenter)
        footer.setFont(QFont("Arial", 9))
        main_layout.addWidget(footer)

        self.setLayout(main_layout)

    def register_voter(self):
        name = self.name_edit.text().strip()

        if name:
            self.voter_names.append(name)

            self.voter_count += 1
            self.bottom_lcd.display(self.voter_count)

            self.can_vote = True
            self.current_votes = 0
            self.voted_items.clear()

        # فعال کردن همه دکمه‌ها
        for item in self.vote_items:
            item.button.setEnabled(True)

        # نمایش دکمه Finish
        self.finish_button.show()

        self.name_edit.clear()
            
    def cast_vote(self, item):

        if not self.can_vote:
            return

    # جلوگیری از رأی تکراری
        if item in self.voted_items:
            return

    # ثبت رأی
        item.count += 1
        item.lcd.display(item.count)

    # قفل کردن همان دکمه
        item.button.setEnabled(False)

        self.voted_items.add(item)
        self.current_votes += 1

    # اگر 5 رأی کامل شد
        if self.current_votes >= self.max_votes:
            self.finish_current_voter()
    
    def finish_current_voter(self):

        self.can_vote = False

    # غیرفعال کردن همه دکمه‌ها
        for item in self.vote_items:
            item.button.setEnabled(False)

    # ریست وضعیت رأی‌دهنده فعلی
        self.current_votes = 0
        self.voted_items.clear()

    # مخفی کردن Finish
        self.finish_button.hide()
            
    def toggle_votes(self):
        self.votes_visible = not self.votes_visible

        for item in self.vote_items:
            if self.votes_visible:
                item.lcd.show()
            else:
                item.lcd.hide()

        self.show_votes_button.setText(
            "Hide Votes" if self.votes_visible else "Show Votes"
        )

    def show_voters(self):
        if not self.voter_names:
            QMessageBox.information(
                self,
                "Voters",
                "No voters have been entered yet."
            )
            return

        text = "Voters:\n\n"

        for i, name in enumerate(self.voter_names, 1):
            text += f"{i}. {name}\n"

        QMessageBox.information(
            self,
            "Voters",
            text
        )

    def show_top_voters(self):

        results = []

        for item in self.vote_items:
            results.append(
                (item.label.text(), item.count)
            )

        results.sort(
            key=lambda x: x[1],
            reverse=True
            )

        self.result_window = ResultWindow(results, self.top_count)
        self.result_window.exec_()


# -------------------- Run App --------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("""
        QWidget {
            background: #15171C;
            color: #E8EAF0;
            font-family: Arial;
            font-size: 10pt;
        }

        QLabel {
            color: #E8EAF0;
        }

        QLineEdit, QSpinBox {
            background: #20232B;
            border: 1px solid #3A3F4B;
            border-radius: 8px;
            padding: 8px 10px;
            color: #F3F4F6;
            selection-background-color: #F4C542;
            selection-color: #15171C;
        }

        QLineEdit:focus, QSpinBox:focus {
            border: 1px solid #F4C542;
        }

        QPushButton {
            background: #252933;
            border: 1px solid #3A3F4B;
            border-radius: 8px;
            padding: 8px 16px;
            color: #F3F4F6;
            min-height: 30px;
        }

        QPushButton:hover {
            background: #303541;
            border: 1px solid #F4C542;
        }

        QPushButton:pressed {
            background: #1D2027;
        }

        QPushButton:disabled {
            background: #1B1E24;
            color: #6E7480;
            border-color: #2A2E36;
        }

        QScrollArea {
            border: 1px solid #2F343E;
            border-radius: 10px;
            background: #111318;
        }

        QScrollArea QWidget {
            background: #111318;
        }

        QLCDNumber {
            background: #0D0F13;
            color: #F4C542;
            border: 1px solid #343944;
            border-radius: 7px;
        }
    """)

    window = WelcomeWindow()
    window.show()

    sys.exit(app.exec_())
