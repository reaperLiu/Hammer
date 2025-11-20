#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中国身份证号码验证器 - GUI界面
Chinese ID Card Validator - GUI Interface

支持批量验证身份证号码，并提供合法/不合法结果分类显示和复制功能
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from id_validator import ChineseIDValidator


class IDValidatorGUI:
    """身份证验证器GUI类"""
    
    def __init__(self, root):
        self.root = root
        self.validator = ChineseIDValidator()
        self.valid_ids = []
        self.invalid_ids = []
        
        self.setup_ui()
        
    def setup_ui(self):
        """设置用户界面"""
        self.root.title("中国身份证号码批量验证器")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # 标题
        title_label = ttk.Label(main_frame, text="中国身份证号码批量验证器", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # 输入区域
        input_frame = ttk.LabelFrame(main_frame, text="输入身份证号码（每行一个）", padding="10")
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(0, weight=1)
        
        self.input_text = scrolledtext.ScrolledText(input_frame, height=8, width=80)
        self.input_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # 添加示例文本
        sample_text = """110101199003074899
 310101198501011236 
440 101 198501 011235
110101199003074897
99010119900307489X"""
        self.input_text.insert(tk.END, sample_text)
        
        # 按钮区域
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)
        
        # 验证按钮
        validate_btn = ttk.Button(button_frame, text="开始验证", 
                                 command=self.validate_ids, style='Accent.TButton')
        validate_btn.pack(side=tk.LEFT, padx=5)
        
        # 清空按钮
        clear_btn = ttk.Button(button_frame, text="清空输入", 
                              command=self.clear_input)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # 结果区域
        result_frame = ttk.Frame(main_frame)
        result_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        result_frame.columnconfigure(0, weight=1)
        result_frame.columnconfigure(1, weight=1)
        result_frame.rowconfigure(1, weight=1)
        
        # 合法身份证区域
        valid_frame = ttk.LabelFrame(result_frame, text="合法身份证", padding="5")
        valid_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        valid_frame.columnconfigure(0, weight=1)
        valid_frame.rowconfigure(1, weight=1)
        
        # 合法身份证按钮区域
        valid_btn_frame = ttk.Frame(valid_frame)
        valid_btn_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.valid_count_label = ttk.Label(valid_btn_frame, text="数量: 0")
        self.valid_count_label.pack(side=tk.LEFT)
        
        copy_valid_btn = ttk.Button(valid_btn_frame, text="复制合法", 
                                   command=self.copy_valid_ids)
        copy_valid_btn.pack(side=tk.RIGHT)
        
        # 合法身份证文本框
        self.valid_text = scrolledtext.ScrolledText(valid_frame, height=15, width=40)
        self.valid_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 不合法身份证区域
        invalid_frame = ttk.LabelFrame(result_frame, text="不合法身份证", padding="5")
        invalid_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(5, 0))
        invalid_frame.columnconfigure(0, weight=1)
        invalid_frame.rowconfigure(1, weight=1)
        
        # 不合法身份证按钮区域
        invalid_btn_frame = ttk.Frame(invalid_frame)
        invalid_btn_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.invalid_count_label = ttk.Label(invalid_btn_frame, text="数量: 0")
        self.invalid_count_label.pack(side=tk.LEFT)
        
        copy_invalid_btn = ttk.Button(invalid_btn_frame, text="复制不合法", 
                                     command=self.copy_invalid_ids)
        copy_invalid_btn.pack(side=tk.RIGHT)
        
        # 不合法身份证文本框
        self.invalid_text = scrolledtext.ScrolledText(invalid_frame, height=15, width=40)
        self.invalid_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
    def validate_ids(self):
        """验证身份证号码"""
        # 清空之前的结果
        self.valid_text.delete(1.0, tk.END)
        self.invalid_text.delete(1.0, tk.END)
        self.valid_ids.clear()
        self.invalid_ids.clear()
        
        # 获取输入文本
        input_content = self.input_text.get(1.0, tk.END).strip()
        if not input_content:
            messagebox.showwarning("警告", "请输入要验证的身份证号码")
            return
        
        # 分割成行
        lines = input_content.split('\n')
        lines = [line.strip() for line in lines if line.strip()]
        
        if not lines:
            messagebox.showwarning("警告", "请输入要验证的身份证号码")
            return
        
        self.status_var.set(f"正在验证 {len(lines)} 个身份证号码...")
        self.root.update()
        
        # 逐行验证
        for line in lines:
            original_input = line
            result = self.validator.validate(line)
            
            if result['valid']:
                # 合法身份证
                info = result['info']
                detail_info = f"{result['id_number']} - {info.get('area', '未知')} | {info.get('birth_date', '未知')} | {info.get('gender', '未知')}"
                self.valid_ids.append({
                    'original': original_input,
                    'processed': result['id_number'],
                    'info': detail_info
                })
            else:
                # 不合法身份证
                error_info = f"{original_input} - 错误: {', '.join(result['errors'])}"
                self.invalid_ids.append({
                    'original': original_input,
                    'processed': result.get('id_number', original_input),
                    'error': error_info
                })
        
        # 更新显示
        self.update_results()
        
        # 更新状态
        self.status_var.set(f"验证完成 - 合法: {len(self.valid_ids)} 个，不合法: {len(self.invalid_ids)} 个")
        
    def update_results(self):
        """更新结果显示"""
        # 更新合法身份证显示
        self.valid_text.delete(1.0, tk.END)
        for item in self.valid_ids:
            self.valid_text.insert(tk.END, item['info'] + '\n')
        
        # 更新不合法身份证显示
        self.invalid_text.delete(1.0, tk.END)
        for item in self.invalid_ids:
            self.invalid_text.insert(tk.END, item['error'] + '\n')
        
        # 更新计数标签
        self.valid_count_label.config(text=f"数量: {len(self.valid_ids)}")
        self.invalid_count_label.config(text=f"数量: {len(self.invalid_ids)}")
        
    def copy_valid_ids(self):
        """复制合法身份证号码"""
        if not self.valid_ids:
            messagebox.showinfo("提示", "没有合法的身份证号码可复制")
            return
        
        # 只复制处理后的身份证号码
        valid_numbers = [item['processed'] for item in self.valid_ids]
        clipboard_text = '\n'.join(valid_numbers)
        
        try:
            # 使用 tkinter 内置的剪贴板功能
            self.root.clipboard_clear()
            self.root.clipboard_append(clipboard_text)
            self.root.update()  # 更新剪贴板
            messagebox.showinfo("成功", f"已复制 {len(valid_numbers)} 个合法身份证号码到剪贴板")
        except Exception as e:
            messagebox.showerror("错误", f"复制失败: {str(e)}")
            
    def copy_invalid_ids(self):
        """复制不合法身份证号码"""
        if not self.invalid_ids:
            messagebox.showinfo("提示", "没有不合法的身份证号码可复制")
            return
        
        # 复制原始输入
        invalid_numbers = [item['original'] for item in self.invalid_ids]
        clipboard_text = '\n'.join(invalid_numbers)
        
        try:
            # 使用 tkinter 内置的剪贴板功能
            self.root.clipboard_clear()
            self.root.clipboard_append(clipboard_text)
            self.root.update()  # 更新剪贴板
            messagebox.showinfo("成功", f"已复制 {len(invalid_numbers)} 个不合法身份证号码到剪贴板")
        except Exception as e:
            messagebox.showerror("错误", f"复制失败: {str(e)}")
            
    def clear_input(self):
        """清空输入"""
        self.input_text.delete(1.0, tk.END)
        self.valid_text.delete(1.0, tk.END)
        self.invalid_text.delete(1.0, tk.END)
        self.valid_ids.clear()
        self.invalid_ids.clear()
        self.valid_count_label.config(text="数量: 0")
        self.invalid_count_label.config(text="数量: 0")
        self.status_var.set("就绪")


def main():
    """主函数"""
    root = tk.Tk()
    
    # 设置样式
    style = ttk.Style()
    style.theme_use('clam')  # 使用现代主题
    
    app = IDValidatorGUI(root)
    
    # 设置窗口图标（如果有的话）
    try:
        root.iconbitmap('icon.ico')  # 可选：添加图标文件
    except:
        pass
    
    # 设置窗口关闭事件
    def on_closing():
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    # 启动GUI
    root.mainloop()


if __name__ == '__main__':
    main()