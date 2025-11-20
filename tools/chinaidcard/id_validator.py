#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中国身份证号码验证器
Chinese ID Card Validator

支持18位身份证号码的完整验证，包括：
- 格式验证
- 地区代码验证
- 出生日期验证
- 校验码验证
- 性别和年龄提取
"""

import re
import datetime
from typing import Dict, Tuple, Optional


class ChineseIDValidator:
    """中国身份证号码验证器类"""
    
    # 校验码权重数组
    WEIGHTS = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    
    # 校验码对应表
    CHECK_CODES = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    
    # 地区代码映射表（部分主要地区）
    AREA_CODES = {
        '11': '北京市', '12': '天津市', '13': '河北省', '14': '山西省', '15': '内蒙古自治区',
        '21': '辽宁省', '22': '吉林省', '23': '黑龙江省',
        '31': '上海市', '32': '江苏省', '33': '浙江省', '34': '安徽省', '35': '福建省', '36': '江西省', '37': '山东省',
        '41': '河南省', '42': '湖北省', '43': '湖南省', '44': '广东省', '45': '广西壮族自治区', '46': '海南省',
        '50': '重庆市', '51': '四川省', '52': '贵州省', '53': '云南省', '54': '西藏自治区',
        '61': '陕西省', '62': '甘肃省', '63': '青海省', '64': '宁夏回族自治区', '65': '新疆维吾尔自治区',
        '71': '台湾省', '81': '香港特别行政区', '82': '澳门特别行政区'
    }
    
    def __init__(self):
        """初始化验证器"""
        pass
    
    def validate(self, id_number: str) -> Dict:
        """
        验证身份证号码
        
        Args:
            id_number: 身份证号码字符串
            
        Returns:
            Dict: 验证结果，包含是否有效、错误信息、详细信息等
        """
        # 去除首尾和中间的所有空格
        original_id = id_number
        id_number = id_number.replace(' ', '').strip() if id_number else ''
        
        result = {
            'valid': False,
            'id_number': id_number,
            'original_input': original_id,
            'errors': [],
            'info': {}
        }
        
        # 基本格式检查
        if not self._check_format(id_number):
            result['errors'].append('身份证号码格式不正确')
            return result
        
        # 地区代码检查
        area_code = id_number[:2]
        if not self._check_area_code(area_code):
            result['errors'].append('地区代码不存在')
        else:
            result['info']['area'] = self.AREA_CODES.get(area_code, '未知地区')
        
        # 出生日期检查
        birth_date_str = id_number[6:14]
        birth_date, birth_valid = self._check_birth_date(birth_date_str)
        if not birth_valid:
            result['errors'].append('出生日期不合法')
        else:
            result['info']['birth_date'] = birth_date.strftime('%Y-%m-%d')
            result['info']['age'] = self._calculate_age(birth_date)
        
        # 校验码检查
        if not self._check_verification_code(id_number):
            result['errors'].append('校验码不正确')
        
        # 性别信息
        sequence_code = int(id_number[16])
        result['info']['gender'] = '男' if sequence_code % 2 == 1 else '女'
        
        # 如果没有错误，则验证通过
        if not result['errors']:
            result['valid'] = True
        
        return result
    
    def _check_format(self, id_number: str) -> bool:
        """
        检查身份证号码格式
        
        Args:
            id_number: 身份证号码
            
        Returns:
            bool: 格式是否正确
        """
        if not id_number or len(id_number) != 18:
            return False
        
        # 前17位必须是数字，最后一位可以是数字或X
        pattern = r'^\d{17}[\dX]$'
        return bool(re.match(pattern, id_number.upper()))
    
    def _check_area_code(self, area_code: str) -> bool:
        """
        检查地区代码是否有效
        
        Args:
            area_code: 地区代码
            
        Returns:
            bool: 地区代码是否有效
        """
        return area_code in self.AREA_CODES
    
    def _check_birth_date(self, birth_date_str: str) -> Tuple[Optional[datetime.date], bool]:
        """
        检查出生日期是否有效
        
        Args:
            birth_date_str: 出生日期字符串 (YYYYMMDD)
            
        Returns:
            Tuple[Optional[datetime.date], bool]: (日期对象, 是否有效)
        """
        try:
            year = int(birth_date_str[:4])
            month = int(birth_date_str[4:6])
            day = int(birth_date_str[6:8])
            
            # 检查年份范围（1900-当前年份）
            current_year = datetime.date.today().year
            if year < 1900 or year > current_year:
                return None, False
            
            birth_date = datetime.date(year, month, day)
            
            # 检查日期是否在未来
            if birth_date > datetime.date.today():
                return None, False
                
            return birth_date, True
            
        except ValueError:
            return None, False
    
    def _check_verification_code(self, id_number: str) -> bool:
        """
        检查校验码是否正确
        
        Args:
            id_number: 身份证号码
            
        Returns:
            bool: 校验码是否正确
        """
        expected_code = self.generate_check_code(id_number[:17])
        return id_number[17].upper() == expected_code
    
    def generate_check_code(self, id_17: str) -> str:
        """
        生成校验码
        
        Args:
            id_17: 身份证号码前17位
            
        Returns:
            str: 校验码
        """
        if len(id_17) != 17 or not id_17.isdigit():
            raise ValueError('前17位必须都是数字')
        
        # 计算加权和
        total = sum(int(digit) * weight for digit, weight in zip(id_17, self.WEIGHTS))
        
        # 计算校验码
        remainder = total % 11
        return self.CHECK_CODES[remainder]
    
    def _calculate_age(self, birth_date: datetime.date) -> int:
        """
        计算年龄
        
        Args:
            birth_date: 出生日期
            
        Returns:
            int: 年龄
        """
        today = datetime.date.today()
        age = today.year - birth_date.year
        
        # 如果今年的生日还没到，年龄减1
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
            
        return age


def main():
    """主函数，用于演示和测试"""
    validator = ChineseIDValidator()
    
    # 测试用例
    test_cases = [
        '110101199003074899',    # 有效身份证
        ' 110101199003074899 ',  # 前后有空格的有效身份证
        '1101 0119 9003 0748 99', # 中间有空格的有效身份证
        '110101199003074897',    # 校验码错误
        '110101199002304896',    # 日期错误（2月30日）
        '99010119900307489X',    # 地区代码错误
        '110101200002304896',    # 未来日期
        '11010119900307489',     # 位数不够
        ' 1101 0119 9002 3048 96 ', # 有空格但日期错误
    ]
    
    print("中国身份证号码验证器测试")
    print("=" * 50)
    
    for i, id_num in enumerate(test_cases, 1):
        print(f"\n测试 {i}: {id_num}")
        result = validator.validate(id_num)
        
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


if __name__ == '__main__':
    main()