# 中国身份证号码验证器

一个完整的18位中国身份证号码验证程序，支持格式验证、地区代码验证、出生日期验证、校验码验证等功能。

## 功能特性

### 核心验证功能
- ✅ **完整验证**: 支持18位身份证号码的全面验证
- ✅ **格式检查**: 验证号码长度和字符格式
- ✅ **智能空格处理**: 自动去除首尾和中间的所有空格
- ✅ **地区验证**: 验证地区代码的有效性
- ✅ **日期验证**: 验证出生日期的合法性
- ✅ **校验码验证**: 按照GB11643-1999标准验证校验码
- ✅ **信息提取**: 提取性别、年龄、地区等信息
- ✅ **校验码生成**: 支持根据前17位生成正确的校验码

### UI界面功能 🎨
- ✅ **批量验证**: 支持一次验证多个身份证号码
- ✅ **结果分类**: 合法和不合法身份证分别显示
- ✅ **一键复制**: 支持复制验证结果到剪贴板
- ✅ **现代化界面**: 响应式设计，支持多设备
- ✅ **即开即用**: 独立HTML界面，无需安装依赖

## 文件结构

```
chinaidcard/
├── id_validator.py         # 主验证器类
├── test_cases.py           # 测试用例
├── demo_space_handling.py  # 空格处理功能演示
├── standalone_ui.html      # 独立HTML界面（推荐） ⭐
├── id_validator_ui.py      # 桌面GUI界面（需要tkinter）
├── web_ui.py              # Web界面后端（需要Flask）
├── templates/             # Web界面模板
│   └── index.html         # Web界面前端
├── UI_使用说明.md          # UI界面使用说明
├── requirements.txt       # 依赖包列表
└── README.md              # 说明文档
```

## 快速开始

### 🎯 UI界面使用（推荐）

**方法一：独立HTML界面（最简单）**
```bash
# 启动本地HTTP服务器
python3 -m http.server 8000

# 在浏览器中访问
# http://localhost:8000/standalone_ui.html
```

**方法二：Web界面**
```bash
# 安装Flask依赖
pip3 install --break-system-packages Flask

# 启动Web服务
python3 web_ui.py

# 访问 http://localhost:5000
```

**方法三：桌面GUI界面**
```bash
# 需要系统支持tkinter
python3 id_validator_ui.py
```

详细使用说明请查看 [UI_使用说明.md](UI_使用说明.md)

### 📚 编程接口使用

### 基本使用

```python
from id_validator import ChineseIDValidator

# 创建验证器实例
validator = ChineseIDValidator()

# 验证身份证号码（支持包含空格的输入）
result = validator.validate(' 110101 199003 074899 ')

if result['valid']:
    print("身份证号码有效")
    print(f"原始输入: {result['original_input']}")
    print(f"处理后: {result['id_number']}")
    print(f"地区: {result['info']['area']}")
    print(f"出生日期: {result['info']['birth_date']}")
    print(f"年龄: {result['info']['age']}岁")
    print(f"性别: {result['info']['gender']}")
else:
    print("身份证号码无效")
    for error in result['errors']:
        print(f"错误: {error}")
```

### 校验码生成

```python
# 根据前17位生成校验码
check_code = validator.generate_check_code('11010119900307489')
print(f"校验码: {check_code}")  # 输出: 6
```

## 运行测试

### 运行主程序演示
```bash
python id_validator.py
```

### 运行完整测试套件
```bash
python test_cases.py
```

### 运行空格处理功能演示
```bash
python demo_space_handling.py
```

### 启动UI界面
```bash
# 启动独立HTML界面（推荐）
python3 -m http.server 8000
# 然后访问 http://localhost:8000/standalone_ui.html

# 或启动Web界面
python3 web_ui.py
# 然后访问 http://localhost:5000

# 或启动桌面GUI界面（需要tkinter支持）
python3 id_validator_ui.py
```

## API 文档

### ChineseIDValidator 类

#### `validate(id_number: str) -> Dict`

验证身份证号码的主要方法。

**参数:**
- `id_number`: 18位身份证号码字符串

**返回值:**
```python
{
    'valid': bool,           # 是否有效
    'id_number': str,        # 处理后的身份证号码（已去除空格）
    'original_input': str,   # 原始输入（包含空格）
    'errors': List[str],     # 错误信息列表
    'info': {                # 详细信息（仅当有效时）
        'area': str,         # 地区名称
        'birth_date': str,   # 出生日期 (YYYY-MM-DD)
        'age': int,          # 年龄
        'gender': str        # 性别 ('男'/'女')
    }
}
```

#### `generate_check_code(id_17: str) -> str`

根据身份证号码前17位生成校验码。

**参数:**
- `id_17`: 身份证号码前17位数字

**返回值:**
- `str`: 校验码 ('0'-'9' 或 'X')

## 验证规则

### 1. 格式验证
- **空格处理**: 自动去除输入中的所有空格（首尾和中间）
- 长度必须为18位（去除空格后）
- 前17位必须是数字
- 第18位可以是数字或字母X

### 2. 地区代码验证
支持的地区代码包括：
- 直辖市：北京(11)、天津(12)、上海(31)、重庆(50)
- 各省份：河北(13)、山西(14)、辽宁(21)等
- 特别行政区：香港(81)、澳门(82)

### 3. 出生日期验证
- 年份范围：1900年至当前年份
- 月份范围：01-12
- 日期必须是有效日期
- 不能是未来日期

### 4. 校验码验证
按照GB11643-1999国家标准：
- 权重系数：[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
- 校验码对应表：['1','0','X','9','8','7','6','5','4','3','2']
- 计算方法：(∑(ai×wi)) mod 11

## 测试用例

程序包含丰富的测试用例，覆盖：

- ✅ 有效身份证号码
- ✅ 包含各种空格格式的有效身份证号码
- ❌ 格式错误（位数不对、包含非法字符）
- ❌ 地区代码错误
- ❌ 出生日期错误（无效日期、未来日期）
- ❌ 校验码错误
- ❌ 包含空格但其他信息错误的身份证号码

## 技术实现

### 核心算法

1. **格式检查**: 使用正则表达式验证格式
2. **地区验证**: 基于预定义的地区代码映射表
3. **日期验证**: 使用Python datetime模块验证日期有效性
4. **校验码计算**: 实现GB11643-1999标准算法

### 性能特点

- 单次验证时间复杂度：O(1)
- 内存占用：极低
- 无外部依赖：仅使用Python标准库

## 使用示例

### 批量验证
```python
validator = ChineseIDValidator()
id_numbers = [
    '110101199003074899',      # 标准格式
    ' 110101199003074899 ',    # 前后有空格
    '1101 0119 9003 0748 99',  # 中间有空格
    '310101198501011236', 
    '440101198501011235'
]

for id_num in id_numbers:
    result = validator.validate(id_num)
    print(f"原始: \"{id_num}\" -> 处理后: \"{result['id_number']}\" -> {'有效' if result['valid'] else '无效'}")
```

### 空格处理示例
```python
# 支持各种空格格式
test_cases = [
    '110101199003074899',           # 无空格
    ' 110101199003074899 ',         # 前后空格
    '110101 199003074899',          # 中间空格
    ' 110 101 1990 0307 4899 ',     # 多个空格分组
    '   110101199003074899   '      # 多个前后空格
]

for case in test_cases:
    result = validator.validate(case)
    if result['valid']:
        print(f"✓ \"{case}\" -> \"{result['id_number']}\"")
    else:
        print(f"✗ \"{case}\" -> 验证失败")
```

### 错误处理
```python
try:
    result = validator.validate(user_input)
    if not result['valid']:
        print("验证失败原因:")
        for error in result['errors']:
            print(f"- {error}")
except Exception as e:
    print(f"验证过程出错: {e}")
```

## 注意事项

1. **隐私保护**: 本程序仅用于格式验证，不存储任何身份信息
2. **数据安全**: 建议在生产环境中加入适当的安全措施
3. **地区代码**: 程序包含主要地区代码，如需完整列表可扩展AREA_CODES字典
4. **年龄计算**: 年龄计算基于当前日期，结果可能随时间变化

## 许可证

本项目采用MIT许可证，详见LICENSE文件。

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

---

*最后更新: 2025-11-20*