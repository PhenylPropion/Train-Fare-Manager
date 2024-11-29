def main():
    global employee_tree, destination_entry, result_tree, license_entry

    # メインウィンドウ
    root = tk.Tk()
    root.title("運賃マネージャー《1.1》")
    root.geometry("1020x600")

    # ウィンドウを閉じるときの処理を設定
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # ライセンス有効期限の表示
    formatted_expiry = f"{expiry[:4]}/{expiry[4:6]}/{expiry[6:]}"
    tk.Label(root, text=f"ライセンス有効期限: {formatted_expiry}", anchor="w").grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)


    # ファイル読み込み部分
    tk.Button(root, text="従業員データを読み込む", command=load_file).grid(row=0, column=0, columnspan=2, pady=10)

    # 到着駅入力
    tk.Label(root, text="到着駅:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    destination_entry = tk.Entry(root, width=30)
    destination_entry.grid(row=1, column=1, padx=10, pady=5)

    # 従業員リスト
    tk.Label(root, text="従業員リスト:").grid(row=2, column=0, columnspan=2)
    employee_tree = ttk.Treeview(root, columns=("ID", "名前", "出発駅"), show="headings", height=8)
    employee_tree.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
    employee_tree.heading("ID", text="ID")
    employee_tree.heading("名前", text="名前")
    employee_tree.heading("出発駅", text="出発駅")

    # 運賃計算ボタン
    tk.Button(root, text="運賃を計算する", command=calculate_fares).grid(row=4, column=0, columnspan=2, pady=10)

    # 結果表示
    tk.Label(root, text="運賃計算結果:").grid(row=5, column=0, columnspan=2)
    result_tree = ttk.Treeview(root, columns=("ID", "名前", "出発駅", "到着駅", "運賃"), show="headings", height=8)
    result_tree.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
    result_tree.heading("ID", text="ID")
    result_tree.heading("名前", text="名前")
    result_tree.heading("出発駅", text="出発駅")
    result_tree.heading("到着駅", text="到着駅")
    result_tree.heading("運賃", text="運賃")

    # アプリ実行
    root.mainloop()
