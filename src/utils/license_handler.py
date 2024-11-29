from Crypto.Cipher import AES
import base58
import os

def verify_license(license_key):
    # ライセンス検証ロジック
    license_key = license_entry.get()

    if check_date(license_key):  # ここに実際のライセンスキーを設定
        with open(LICENSE_FILE, "w") as file:
            file.write(license_key)
        license_window.destroy()  # ライセンスウィンドウを閉じる
        main()  # main関数を呼び出す

        return True
    else:
        return False
    pass

def save_license(license_key):
    # ライセンスキーの保存
    pass
