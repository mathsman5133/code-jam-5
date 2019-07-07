from thoughtful_termites.app import qt
from thoughtful_termites.shared.constants import get_db


COMPLETED_GOALS_PATH = "./resources/completed_goals.txt"


class UnlocksWindow(qt.QDialog):
    @staticmethod
    def set_completed_goals(n: int):
        with open(COMPLETED_GOALS_PATH, "w") as f:
            f.write(str(n))

    @staticmethod
    def completed_goals():
        with open(COMPLETED_GOALS_PATH, "r") as f:
            contents = f.read().strip()
            return int(contents)

    def __init__(self, parent: qt.QWidget):
        super().__init__(parent)

        self.db = get_db()

        self.unlock_commentary_button = qt.QPushButton()
        self.unlock_commentary_button.setText("Climate Commentary")
        self.unlock_commentary_button.addAction(self.on_unlock("commentary"))

        self.unlock_rankings_button = qt.QPushButton()
        self.unlock_rankings_button.setText("Rankings Minigame")
        self.unlock_rankings_button.addAction(self.on_unlock("rankings"))

        self.unlock_hangman_button = qt.QPushButton()
        self.unlock_hangman_button.setText("Hangman")
        self.unlock_hangman_button.addAction(self.on_unlock("hangman"))

        self.unlock_minesweeper_button = qt.QPushButton()
        self.unlock_minesweeper_button.setText("Minesweeper")
        self.unlock_minesweeper_button.addAction(self.on_unlock("minesweeper"))

        completed_goals = UnlocksWindow.completed_goals()

        if completed_goals < 1:
            self.unlock_commentary_button.setEnabled(False)
        if completed_goals < 2:
            self.unlock_rankings_button.setEnabled(False)
        if completed_goals < 4:
            self.unlock_hangman_button.setEnabled(False)
        if completed_goals < 8:
            self.unlock_minesweeper_button.setEnabled(False)

        self.layout = qt.QGridLayout()
        self.layout.setRowStretch(0, 2)
        self.layout.setRowStretch(1, 2)

        self.layout.addWidget(self.unlock_commentary_button, 0, 0)
        self.layout.addWidget(self.unlock_rankings_button, 0, 1)
        self.layout.addWidget(self.unlock_hangman_button, 1, 0)
        self.layout.addWidget(self.unlock_minesweeper_button, 1, 1)

        self.main_layout = qt.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addChildLayout(self.layout)

        self.setWindowTitle("Unlocking Minigames")

    def on_unlock(self, name):
        def inner():
            unlock = self.db.get_unlock_by_name(name)
            unlock.is_unlocked = True
            unlock.update()

        return inner
