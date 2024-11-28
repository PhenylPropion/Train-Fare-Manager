import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ..utils.file_handler import load_file, save_file


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("運賃マネージャー《1.1》")
        self.root.geometry("1020x600")
        self.setup_ui()

    def setup_ui(self):
        # UIコンポーネントの設定
        self.create_employee_tree()
        self.create_destination_entry()
        self.create_result_tree()
        self.create_buttons()

    def create_employee_tree(self):
        """従業員データを表示するTreeviewを作成"""
        # フレームの作成
        tree_frame = ttk.Frame(self.root)
        tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # スクロールバーの作成
        scrollbar_y = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL)
        scrollbar_x = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)

        # Treeviewの作成
        self.employee_tree = ttk.Treeview(
            tree_frame,
            columns=("名前", "部署", "出発地", "目的地", "料金", "日付"),
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        # スクロールバーの設定
        scrollbar_y.config(command=self.employee_tree.yview)
        scrollbar_x.config(command=self.employee_tree.xview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # カラム見出しの設定
        self.employee_tree.heading("名前", text="名前")
        self.employee_tree.heading("部署", text="部署")
        self.employee_tree.heading("出発地", text="出発地")
        self.employee_tree.heading("目的地", text="目的地")
        self.employee_tree.heading("料金", text="料金")
        self.employee_tree.heading("日付", text="日付")

        # カラム幅の設定
        self.employee_tree.column("名前", width=100, minwidth=100)
        self.employee_tree.column("部署", width=100, minwidth=100)
        self.employee_tree.column("出発地", width=150, minwidth=150)
        self.employee_tree.column("目的地", width=150, minwidth=150)
        self.employee_tree.column("料金", width=100, minwidth=100)
        self.employee_tree.column("日付", width=100, minwidth=100)

        # Treeviewの配置
        self.employee_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 選択イベントのバインド
        self.employee_tree.bind('<<TreeviewSelect>>', self.on_tree_select)

        # 右クリックメニューの作成
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="削除", command=self.delete_selected_item)
        self.employee_tree.bind("<Button-3>", self.show_context_menu)

    def on_tree_select(self, event):
        """ツリーアイテムが選択されたときの処理"""
        selected_items = self.employee_tree.selection()
        if selected_items:
            item = selected_items[0]
            values = self.employee_tree.item(item)['values']
            # 選択されたアイテムの値を他のウィジェットに反映する処理など

    def show_context_menu(self, event):
        """右クリックメニューを表示"""
        item = self.employee_tree.identify_row(event.y)
        if item:
            self.employee_tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)

    def delete_selected_item(self):
        """選択されたアイテムを削除"""
        selected_items = self.employee_tree.selection()
        if selected_items:
            if messagebox.askyesno("確認", "選択したアイテムを削除しますか？"):
                for item in selected_items:
                    self.employee_tree.delete(item)

    def add_employee(self, name, department, from_location, to_location, fare, date):
        """従業員データをツリーに追加"""
        self.employee_tree.insert(
            "",
            tk.END,
            values=(name, department, from_location, to_location, fare, date)
        )

    def clear_tree(self):
        """ツリーの全データをクリア"""
        for item in self.employee_tree.get_children():
            self.employee_tree.delete(item)

    def get_all_employees(self):
        """ツリーの全データを取得"""
        employees = []
        for item in self.employee_tree.get_children():
            values = self.employee_tree.item(item)['values']
            employees.append({
                '名前': values[0],
                '部署': values[1],
                '出発地': values[2],
                '目的地': values[3],
                '料金': values[4],
                '日付': values[5]
            })
        return employees

    def on_closing(self):
        self.root.quit()
        self.root.destroy()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()