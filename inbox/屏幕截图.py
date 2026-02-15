"""
屏幕截图工具

用法：直接运行此脚本。按住鼠标左键拖动选择矩形区域，释放鼠标后会弹出预览窗口，点击 "保存" 按钮选择保存路径。

依赖：Pillow（安装：pip install pillow）

说明：脚本在选取完成时会临时隐藏选择层以获取屏幕像素，然后显示截图预览和保存对话框。
"""

import sys
import os
try:
	from PIL import ImageGrab, ImageTk
except Exception:
	print('请先安装 Pillow：pip install pillow')
	sys.exit(1)

import tkinter as tk
from tkinter import filedialog, messagebox


class ScreenCaptureTool:
	def __init__(self):
		self.root = tk.Tk()
		self.root.withdraw()

		# 选择窗口（覆盖全屏，用于绘制选区）
		self.sel = tk.Toplevel()
		self.sel.attributes('-fullscreen', True)
		self.sel.attributes('-topmost', True)
		# 半透明黑色背景，便于看到选区
		self.sel.configure(bg='black')
		try:
			self.sel.attributes('-alpha', 0.3)
		except Exception:
			pass

		self.canvas = tk.Canvas(self.sel, cursor='cross')
		self.canvas.pack(fill=tk.BOTH, expand=True)

		self.start_x = None
		self.start_y = None
		self.rect = None

		# 绑定事件
		self.canvas.bind('<ButtonPress-1>', self.on_button_press)
		self.canvas.bind('<B1-Motion>', self.on_move_press)
		self.canvas.bind('<ButtonRelease-1>', self.on_button_release)
		self.sel.bind('<Escape>', lambda e: self.cancel())

		# 选区坐标
		self.bbox = None

		# 截图对象
		self.captured_image = None

	def on_button_press(self, event):
		# 记录起始点（使用屏幕坐标）
		self.start_x = event.x_root
		self.start_y = event.y_root

		# 在 canvas 上画一个矩形（以窗口坐标为准）
		# 需要把屏幕坐标转换为 canvas 坐标
		cx = event.x
		cy = event.y
		if self.rect:
			self.canvas.delete(self.rect)
			self.rect = None
		self.rect = self.canvas.create_rectangle(cx, cy, cx, cy, outline='red', width=2)

	def on_move_press(self, event):
		if not self.rect:
			return
		# 更新矩形（canvas 坐标）
		x1 = self.start_x - self.sel.winfo_rootx()
		y1 = self.start_y - self.sel.winfo_rooty()
		x2 = event.x_root - self.sel.winfo_rootx()
		y2 = event.y_root - self.sel.winfo_rooty()
		self.canvas.coords(self.rect, x1, y1, x2, y2)

	def on_button_release(self, event):
		# 计算屏幕坐标的选区
		end_x = event.x_root
		end_y = event.y_root
		left = int(min(self.start_x, end_x))
		top = int(min(self.start_y, end_y))
		right = int(max(self.start_x, end_x))
		bottom = int(max(self.start_y, end_y))

		# 最小尺寸保护
		if right - left < 5 or bottom - top < 5:
			messagebox.showinfo('提示', '选区太小，取消截图')
			self.cancel()
			return

		self.bbox = (left, top, right, bottom)

		# 隐藏选择窗口以便截取真实屏幕（避免遮挡）
		self.sel.withdraw()
		self.root.update()

		try:
			img = ImageGrab.grab(bbox=self.bbox)
		except Exception as e:
			messagebox.showerror('错误', f'截图失败：{e}')
			self.sel.deiconify()
			return

		self.captured_image = img
		self.show_preview()

	def show_preview(self):
		# 预览窗口
		preview = tk.Toplevel()
		preview.title('截图预览')
		preview.geometry('+200+200')
		preview.attributes('-topmost', True)

		# 将 PIL 图转为 PhotoImage
		tk_img = ImageTk.PhotoImage(self.captured_image)
		lbl = tk.Label(preview, image=tk_img)
		lbl.image = tk_img
		lbl.pack()

		btn_frame = tk.Frame(preview)
		btn_frame.pack(fill=tk.X, pady=5)

		def save_action():
			filetypes = [('PNG 图片', '*.png'), ('JPEG 图片', '*.jpg;*.jpeg'), ('BMP 图片', '*.bmp')]
			initial = os.path.expanduser('~')
			# 确保保存对话框在预览窗口之上
			preview.lift()
			preview.attributes('-topmost', True)
			preview.update()
			path = filedialog.asksaveasfilename(parent=preview, defaultextension='.png', filetypes=filetypes, initialdir=initial)
			# 取消强制顶置（避免影响其它窗口）
			try:
				preview.attributes('-topmost', False)
			except Exception:
				pass
			if path:
				try:
					# 根据扩展名决定格式
					ext = os.path.splitext(path)[1].lower()
					fmt = 'PNG'
					if ext in ('.jpg', '.jpeg'):
						fmt = 'JPEG'
					elif ext == '.bmp':
						fmt = 'BMP'
					self.captured_image.save(path, fmt)
					messagebox.showinfo('保存成功', f'已保存到：{path}')
					# 关闭所有窗口并退出程序
					try:
						preview.destroy()
					except Exception:
						pass
					try:
						self.sel.destroy()
					except Exception:
						pass
					try:
						self.root.destroy()
					except Exception:
						# 作为退路，尝试 quit
						try:
							self.root.quit()
						except Exception:
							pass
				except Exception as e:
					messagebox.showerror('保存失败', str(e))

		def cancel_action():
			preview.destroy()
			# 恢复选择层，允许重新选择
			self.sel.deiconify()

		save_btn = tk.Button(btn_frame, text='保存', command=save_action, width=12)
		save_btn.pack(side=tk.LEFT, padx=8)
		cancel_btn = tk.Button(btn_frame, text='重新选择', command=cancel_action, width=12)
		cancel_btn.pack(side=tk.LEFT)

		# 也允许按键保存（S）或退出（Esc）
		preview.bind('<Escape>', lambda e: (preview.destroy(), self.sel.destroy(), self.root.quit()))
		preview.bind('<s>', lambda e: save_action())

		# 等待预览窗口关闭（更安全，不创建新的 mainloop）
		preview.wait_window()

	def cancel(self):
		try:
			self.sel.destroy()
		except Exception:
			pass
		self.root.quit()

	def run(self):
		self.sel.mainloop()


if __name__ == '__main__':
	app = ScreenCaptureTool()
	app.run()

