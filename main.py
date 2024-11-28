import sys
import os
from src.gui.main_window import MainWindow
from src.gui.license_window import LicenseWindow
from src.utils.license_handler import verify_license


def main():
    # ライセンスの確認
    license_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "license_key.txt")

    if not os.path.exists(license_file):
        license_window = LicenseWindow()
        if not license_window.verify_and_save():
            sys.exit(1)

    # メインウィンドウの起動
    app = MainWindow()
    app.run()


if __name__ == "__main__":
    main()