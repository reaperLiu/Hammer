#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
身份证验证器演示程序
简单的交互式身份证验证工具
"""

from id_validator import ChineseIDValidator


def main():
    print("🆔 中国身份证号码验证器")
    print("=" * 40)
    print("输入身份证号码进行验证")
    print("输入 'demo' 查看演示")
    print("输入 'quit' 退出程序")
    print("=" * 40)
    
    validator = ChineseIDValidator()
    
    while True:
        try:
            user_input = input("\n请输入身份证号码: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q', '退出']:
                print("👋 再见！")
                break
            
            if user_input.lower() == 'demo':
                show_demo(validator)
                continue
            
            if not user_input:
                continue
            
            # 验证身份证
            result = validator.validate(user_input)
            
            print(f"\n📋 验证结果:")
            print(f"身份证号码: {user_input}")
            
            if result['valid']:
                print("✅ 验证通过")
                info = result['info']
                print(f"📍 地区: {info.get('area', '未知')}")
                print(f"🎂 出生日期: {info.get('birth_date', '未知')}")
                print(f"👤 年龄: {info.get('age', '未知')}岁")
                print(f"⚧ 性别: {info.get('gender', '未知')}")
            else:
                print("❌ 验证失败")
                print("❗ 错误原因:")
                for error in result['errors']:
                    print(f"   • {error}")
                    
        except KeyboardInterrupt:
            print("\n\n👋 程序被中断，再见！")
            break
        except Exception as e:
            print(f"❌ 出现错误: {e}")


def show_demo(validator):
    """显示演示用例"""
    print("\n🎬 演示模式")
    print("-" * 30)
    
    # 生成一些有效的演示身份证
    demo_cases = [
        ('11010119900307489', '北京市男性，1990年出生'),
        ('31010119850101123', '上海市男性，1985年出生'),
        ('44010119920215123', '广东省男性，1992年出生'),
        ('51010119880808124', '四川省女性，1988年出生'),
    ]
    
    for i, (prefix, description) in enumerate(demo_cases, 1):
        check_code = validator.generate_check_code(prefix)
        full_id = prefix + check_code
        result = validator.validate(full_id)
        
        print(f"\n演示 {i}: {description}")
        print(f"身份证: {full_id}")
        
        if result['valid']:
            info = result['info']
            print(f"✅ 验证通过")
            print(f"   地区: {info['area']}")
            print(f"   出生: {info['birth_date']}")
            print(f"   年龄: {info['age']}岁")
            print(f"   性别: {info['gender']}")
        else:
            print(f"❌ 验证失败: {result['errors']}")


if __name__ == '__main__':
    main()