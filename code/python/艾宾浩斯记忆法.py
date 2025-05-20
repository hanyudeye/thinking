import tkinter as tk
from tkinter import messagebox
import datetime

class EbbinghausApp:
    def __init__(self, root):
        self.root = root
        self.root.title("艾宾浩斯记忆法")
        
        self.review_days = [3, 7, 14]  # 预设复习天数，用户可以修改
        
        # 创建输入框用于设置复习天数
        self.setup_review_days()
        
        # 创建文本框来复制粘贴学习资源
        self.create_resource_input()
        
    def setup_review_days(self):
        # 创建标签与输入框来设置复习天数
        tk.Label(self.root, text="复习天数（如3, 7, 14天）:").pack()
        self.review_input = tk.Entry(self.root)
        self.review_input.pack()
        self.review_input.insert(0, "3,7,14")  # 默认复习天数
        
        # 创建按钮提交复习天数设置
        self.submit_button = tk.Button(self.root, text="设置复习天数", command=self.set_review_days)
        self.submit_button.pack()
        
    def set_review_days(self):
        days = self.review_input.get().split(",")
        self.review_days = [int(day) for day in days]
        messagebox.showinfo("设置成功", "复习天数已设置为：" + ", ".join(map(str, self.review_days)))
        
    def create_resource_input(self):
        # 创建资源输入框
        self.resource_input = tk.Text(self.root, height=10, width=50)
        self.resource_input.pack()
        
        # 创建按钮提交学习资源
        self.submit_resource_button = tk.Button(self.root, text="提交学习资源", command=self.submit_resource)
        self.submit_resource_button.pack()
        
    def submit_resource(self):
        resource = self.resource_input.get("1.0", tk.END).strip()
        if resource:
            # 保存资源并进入复习计划（简化版，实际应用中会存储在数据库）
            messagebox.showinfo("提交成功", "资源已提交，开始复习！")
            self.schedule_review(resource)
        
    def schedule_review(self, resource):
        # 根据复习天数生成复习日期
        today = datetime.date.today()
        review_dates = [today + datetime.timedelta(days=day) for day in self.review_days]
        messagebox.showinfo("复习计划", f"资源将在以下日期进行复习：{', '.join(map(str, review_dates))}")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = EbbinghausApp(root)
    root.mainloop()
