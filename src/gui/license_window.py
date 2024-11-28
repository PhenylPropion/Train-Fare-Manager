import tkinter as tk
from tkinter import messagebox
from ..utils.license_handler import verify_license


class LicenseWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ライセンス認証")
        self.setup_ui()

    def setup_ui(self):
        # ライセンスウィンドウのUI設定
        self.license_entry = tk.Entry(self.window)
        # ... 残りの実装

    def verify_and_save(self):
        license_key = self.license_entry.get()
        if verify_license(license_key):
            self.window.destroy()
            return True
        return False