import sys
import os
from src.gui.main_window import MainWindow
from src.gui.license_window import LicenseWindow
from src.utils.license_handler import verify_license


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを一時的に隠す

    # ライセンスキーが保存されているか確認
    if os.path.exists(LICENSE_FILE):
        with open(LICENSE_FILE, "r") as file:
            saved_license_key = file.read().strip()
            if check_date(saved_license_key):
                main()
            else:
                create_license_window(root)
    else:
        create_license_window(root)

    root.mainloop()
