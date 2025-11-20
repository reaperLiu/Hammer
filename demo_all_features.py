#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中国身份证验证器完整功能演示
Complete Feature Demonstration for Chinese ID Card Validator
"""

import os
import sys
import subprocess
import webbrowser
from id_validator import ChineseIDValidator

def print_header(title):
    """打印标题"""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def print_section(title):
    """打印章节标题"""
    print(f"\n🔸 {title}")
    print("-" * 40)

def demo_basic_validation():
    """演示基本验证功能"""
    print_header("基本验证功能演示")
    
    validator = ChineseIDValidator()
    
    # 测试用例
    test_cases = [
        {
            'id': '110101199003074899',
            'desc': '标准格式身份证'
        },
        {
            'id': ' 110101199003074899 ',
            'desc': '前后有空格'
        },
        {
            'id': '1101 0119 9003 0748 99',
            'desc': '中间有空格'
        },
        {
            'id': '110101199003074897',
            'desc': '校验码错误'
        },
        {
            'id': '99010119900307489X',
            'desc': '地区代码错误'
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        print_section(f"测试 {i}: {case['desc']}")
        print(f"输入: \"{case['id']}\"")
        
        result = validator.validate(case['id'])
        
        if result['valid']:
            print("✅ 验证通过")
            info = result['info']
            print(f"   处理后: \"{result['id_number']}\"")
            print(f"   地区: {info.get('area', '未知')}")
            print(f"   出生日期: {info.get('birth_date', '未知')}")
            print(f"   年龄: {info.get('age', '未知')}岁")
            print(f"   性别: {info.get('gender', '未知')}")
        else:
            print("❌ 验证失败")
            print(f"   处理后: \"{result['id_number']}\"")
            for error in result['errors']:
                print(f"   错误: {error}")

def demo_batch_validation():
    """演示批量验证功能"""
    print_header("批量验证功能演示")
    
    validator = ChineseIDValidator()
    
    # 批量测试数据
    batch_data = """110101199003074899
 310101198501011236 
1101 0119 9003 0748 99
440 101 198501 011235
110101199003074897
99010119900307489X
110101199002304896"""
    
    print("批量输入数据:")
    print(batch_data)
    
    lines = [line.strip() for line in batch_data.split('\n') if line.strip()]
    
    valid_ids = []
    invalid_ids = []
    
    print_section("验证结果")
    
    for line in lines:
        result = validator.validate(line)
        if result['valid']:
            valid_ids.append(result)
        else:
            invalid_ids.append(result)
    
    print(f"📊 统计结果:")
    print(f"   总数: {len(lines)}")
    print(f"   合法: {len(valid_ids)} 个")
    print(f"   不合法: {len(invalid_ids)} 个")
    
    print_section("合法身份证详情")
    for i, result in enumerate(valid_ids, 1):
        info = result['info']
        print(f"{i}. {result['id_number']} - {info.get('area', '未知')} | {info.get('birth_date', '未知')} | {info.get('gender', '未知')}")
    
    print_section("不合法身份证详情")
    for i, result in enumerate(invalid_ids, 1):
        print(f"{i}. {result['original_input']} - 错误: {', '.join(result['errors'])}")

def demo_check_code_generation():
    """演示校验码生成功能"""
    print_header("校验码生成功能演示")
    
    validator = ChineseIDValidator()
    
    test_prefixes = [
        ('110101199003074896', '生成北京身份证校验码'),
        ('310101198501011234', '生成上海身份证校验码'),
        ('440101198501011235', '生成广东身份证校验码'),
    ]
    
    for i, (prefix, desc) in enumerate(test_prefixes, 1):
        print_section(f"测试 {i}: {desc}")
        
        id_17 = prefix[:17]
        check_code = validator.generate_check_code(id_17)
        complete_id = id_17 + check_code
        
        print(f"前17位: {id_17}")
        print(f"生成校验码: {check_code}")
        print(f"完整身份证: {complete_id}")
        
        # 验证生成的身份证
        result = validator.validate(complete_id)
        print(f"验证结果: {'✅ 有效' if result['valid'] else '❌ 无效'}")
        
        if result['valid']:
            info = result['info']
            print(f"详细信息: {info.get('area', '未知')} | {info.get('birth_date', '未知')} | {info.get('gender', '未知')}")

def check_ui_availability():
    """检查UI界面可用性"""
    print_header("UI界面可用性检查")
    
    ui_options = []
    
    # 检查独立HTML界面
    html_file = 'standalone_ui.html'
    if os.path.exists(html_file):
        ui_options.append({
            'name': '独立HTML界面',
            'file': html_file,
            'command': f'python3 -m http.server 8000',
            'url': 'http://localhost:8000/standalone_ui.html',
            'available': True,
            'recommended': True
        })
        print("✅ 独立HTML界面可用 (推荐)")
    else:
        print("❌ 独立HTML界面不可用")
    
    # 检查tkinter支持
    try:
        import tkinter
        if os.path.exists('id_validator_ui.py'):
            ui_options.append({
                'name': '桌面GUI界面',
                'file': 'id_validator_ui.py',
                'command': 'python3 id_validator_ui.py',
                'url': None,
                'available': True,
                'recommended': False
            })
            print("✅ 桌面GUI界面可用 (需要tkinter)")
        else:
            print("❌ 桌面GUI界面文件不存在")
    except ImportError:
        print("❌ 桌面GUI界面不可用 (tkinter未安装)")
    
    # 检查Flask支持
    try:
        import flask
        if os.path.exists('web_ui.py'):
            ui_options.append({
                'name': 'Web界面',
                'file': 'web_ui.py',
                'command': 'python3 web_ui.py',
                'url': 'http://localhost:5000',
                'available': True,
                'recommended': False
            })
            print("✅ Web界面可用 (需要Flask)")
        else:
            print("❌ Web界面文件不存在")
    except ImportError:
        print("❌ Web界面不可用 (Flask未安装)")
    
    return ui_options

def launch_ui_interface():
    """启动UI界面"""
    print_header("启动UI界面")
    
    ui_options = check_ui_availability()
    
    if not ui_options:
        print("❌ 没有可用的UI界面")
        return False
    
    print("\n可用的UI界面选项:")
    for i, option in enumerate(ui_options, 1):
        status = "⭐ 推荐" if option.get('recommended') else ""
        print(f"{i}. {option['name']} {status}")
        print(f"   命令: {option['command']}")
        if option['url']:
            print(f"   访问: {option['url']}")
        print()
    
    try:
        choice = input("请选择要启动的界面 (输入数字，回车取消): ").strip()
        if not choice:
            return False
        
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(ui_options):
            selected = ui_options[choice_idx]
            print(f"\n🚀 启动 {selected['name']}...")
            
            if selected['name'] == '独立HTML界面':
                # 启动HTTP服务器
                print("启动本地HTTP服务器...")
                subprocess.Popen(['python3', '-m', 'http.server', '8000'], 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
                
                import time
                time.sleep(2)
                
                print(f"✅ 服务器已启动")
                print(f"📱 请在浏览器中访问: {selected['url']}")
                
                # 尝试自动打开浏览器
                try:
                    webbrowser.open(selected['url'])
                    print("🌐 已自动打开浏览器")
                except:
                    print("💡 请手动在浏览器中打开上述链接")
                
            elif selected['name'] == '桌面GUI界面':
                os.system(selected['command'])
            elif selected['name'] == 'Web界面':
                print("启动Web服务器...")
                subprocess.Popen(['python3', selected['file']], 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
                
                import time
                time.sleep(3)
                
                print(f"✅ 服务器已启动")
                print(f"📱 请在浏览器中访问: {selected['url']}")
                
                try:
                    webbrowser.open(selected['url'])
                    print("🌐 已自动打开浏览器")
                except:
                    print("💡 请手动在浏览器中打开上述链接")
            
            return True
        else:
            print("❌ 无效的选择")
            return False
            
    except (ValueError, KeyboardInterrupt):
        print("取消启动")
        return False

def main():
    """主函数"""
    print("🎯 中国身份证验证器完整功能演示")
    print("Chinese ID Card Validator - Complete Feature Demo")
    
    try:
        while True:
            print("\n" + "=" * 60)
            print("请选择演示内容:")
            print("1. 基本验证功能演示")
            print("2. 批量验证功能演示") 
            print("3. 校验码生成功能演示")
            print("4. 启动UI界面")
            print("5. 运行完整测试套件")
            print("0. 退出")
            print("=" * 60)
            
            choice = input("请输入选择 (0-5): ").strip()
            
            if choice == '0':
                print("👋 感谢使用！")
                break
            elif choice == '1':
                demo_basic_validation()
            elif choice == '2':
                demo_batch_validation()
            elif choice == '3':
                demo_check_code_generation()
            elif choice == '4':
                launch_ui_interface()
                input("\n按回车键继续...")
            elif choice == '5':
                print_header("运行完整测试套件")
                os.system('python3 test_cases.py')
            else:
                print("❌ 无效的选择，请重新输入")
            
            if choice in ['1', '2', '3']:
                input("\n按回车键继续...")
                
    except KeyboardInterrupt:
        print("\n\n👋 程序被中断，再见！")
    except Exception as e:
        print(f"\n❌ 程序出错: {e}")

if __name__ == '__main__':
    main()