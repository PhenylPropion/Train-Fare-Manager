def create_license_window(root):
    global license_entry, license_window
    license_window = tk.Toplevel(root)
    license_window.title("ライセンスキー認証画面")
    license_window.geometry("800x600")  # ウィンドウサイズを設定
    tk.Label(license_window, text="ライセンスキーを入力してください:").pack(pady=10)
    license_entry = tk.Entry(license_window, width=30)
    license_entry.pack(pady=5)
    tk.Button(license_window, text="認証", command=check_license).pack(pady=10)
    # ウィンドウを閉じるときの処理を設定
    license_window.protocol("WM_DELETE_WINDOW", on_closing)
