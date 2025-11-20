#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
身份证号码空格处理功能演示
Demonstration of space handling in ID card validation
"""

from id_validator import ChineseIDValidator

def demo_space_handling():
    """演示空格处理功能"""
    validator = ChineseIDValidator()
    
    # 生成一个有效的身份证号码作为基础
    base_id_17 = '110101199003074899'[:17]
    check_code = validator.generate_check_code(base_id_17)
    valid_id = base_id_17 + check_code
    
    print("身份证号码空格处理功能演示")
    print("=" * 50)
    print(f"基础有效身份证号码: {valid_id}")
    print()
    
    # 测试不同格式的空格
    test_cases = [
        {
            'input': valid_id,
            'description': '无空格（标准格式）'
        },
        {
            'input': f' {valid_id} ',
            'description': '前后有空格'
        },
        {
            'input': f'   {valid_id}   ',
            'description': '前后有多个空格'
        },
        {
            'input': f'{valid_id[:6]} {valid_id[6:]}',
            'description': '中间有一个空格'
        },
        {
            'input': f'{valid_id[:3]} {valid_id[3:6]} {valid_id[6:10]} {valid_id[10:14]} {valid_id[14:]}',
            'description': '按常见分组格式添加空格'
        },
        {
            'input': f' {valid_id[:2]} {valid_id[2:6]} {valid_id[6:10]} {valid_id[10:14]} {valid_id[14:17]} {valid_id[17]} ',
            'description': '复杂空格格式（前后+多个分组）'
        },
        {
            'input': f'{valid_id.replace("", " ")[1:-1]}',  # 每个字符间加空格
            'description': '每个字符间都有空格'
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        input_id = case['input']
        description = case['description']
        
        print(f"测试 {i}: {description}")
        print(f"输入: \"{input_id}\"")
        
        result = validator.validate(input_id)
        
        print(f"处理后: \"{result['id_number']}\"")
        print(f"原始输入: \"{result.get('original_input', 'N/A')}\"")
        
        if result['valid']:
            print("✓ 验证通过")
            info = result['info']
            print(f"  地区: {info.get('area', '未知')}")
            print(f"  出生日期: {info.get('birth_date', '未知')}")
            print(f"  年龄: {info.get('age', '未知')}岁")
            print(f"  性别: {info.get('gender', '未知')}")
        else:
            print("✗ 验证失败")
            for error in result['errors']:
                print(f"  错误: {error}")
        
        print("-" * 50)
    
    # 演示错误情况
    print("\n错误情况演示:")
    print("=" * 50)
    
    error_cases = [
        {
            'input': f' {valid_id[:-1]}7 ',  # 校验码错误
            'description': '有空格但校验码错误'
        },
        {
            'input': ' 110101 199013 074899 ',  # 月份错误
            'description': '有空格但日期无效（13月）'
        },
        {
            'input': '   ',  # 只有空格
            'description': '只有空格'
        },
        {
            'input': ' 1101 0119 9003 0748 ',  # 位数不够
            'description': '有空格但位数不够'
        }
    ]
    
    for i, case in enumerate(error_cases, 1):
        input_id = case['input']
        description = case['description']
        
        print(f"错误测试 {i}: {description}")
        print(f"输入: \"{input_id}\"")
        
        result = validator.validate(input_id)
        
        print(f"处理后: \"{result['id_number']}\"")
        print(f"结果: {'✓ 有效' if result['valid'] else '✗ 无效'}")
        
        if not result['valid']:
            for error in result['errors']:
                print(f"  错误: {error}")
        
        print("-" * 30)

if __name__ == '__main__':
    demo_space_handling()