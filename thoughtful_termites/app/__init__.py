def run():
    """
    Convenience function for running the app.
    """
    import sys
    from thoughtful_termites.app import qt
    from thoughtful_termites.app.widgets import UnlocksWindow

    app = qt.QApplication(sys.argv)
    sys.excepthook = sys.__excepthook__

    window = UnlocksWindow()
    window.show()

    return app.exec()
