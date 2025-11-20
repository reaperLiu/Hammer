# 🔨 Hammer - 日常工作小工具集合

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-deployed-brightgreen)](https://reaperliu.github.io/Hammer/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Tools](https://img.shields.io/badge/tools-6-orange.svg)](#工具列表)

专为提高工作效率而生的实用工具集合，涵盖数据验证、格式转换、文本处理等常用功能。所有工具均支持本地运行，保护数据隐私安全。

## 🌟 在线体验

- 🌐 **主页**: [https://reaperliu.github.io/Hammer/](https://reaperliu.github.io/Hammer/)
- 🆔 **身份证验证器**: [https://reaperliu.github.io/Hammer/tools/chinaidcard/standalone_ui.html](https://reaperliu.github.io/Hammer/tools/chinaidcard/standalone_ui.html)

## 🎯 项目特色

- ✅ **完全本地运行** - 所有工具在浏览器本地执行，不上传任何数据
- 🛡️ **隐私安全** - 零数据收集，保护用户隐私
- 📱 **响应式设计** - 支持手机、平板、桌面设备
- 🚀 **即开即用** - 无需安装，打开浏览器即可使用
- 🎨 **现代化界面** - 美观易用的用户界面
- 🔄 **持续更新** - 定期添加新工具和功能

## 🛠️ 工具列表

### ✅ 已上线工具

| 工具 | 状态 | 描述 | 链接 |
|------|------|------|------|
| 🆔 身份证号&手机号校验器 | ✅ 已上线 | 批量验证身份证号和手机号，智能识别类型，支持空格处理 | [使用](tools/chinaidcard/standalone_ui.html) |

### 🚧 即将上线

| 工具 | 状态 | 描述 | 预计上线 |
|------|------|------|----------|
| 📋 JSON格式化工具 | 🚧 开发中 | JSON数据格式化、压缩、验证 | 2025-12 |
| 🔐 Base64编解码器 | 🚧 开发中 | 文本和文件的Base64编解码 | 2025-12 |
| 🔗 URL编解码器 | 🚧 开发中 | URL编码解码和格式验证 | 2025-12 |
| ⏰ 时间戳转换器 | 🚧 开发中 | 多格式时间戳转换工具 | 2025-12 |
| 🔍 正则表达式测试器 | 🚧 开发中 | 正则表达式测试和学习工具 | 2025-12 |

## 📋 详细功能

### 🆔 身份证号&手机号批量去空格校验器
- **智能识别**: 自动识别输入是身份证号还是手机号
- **批量验证**: 支持一次验证多个号码
- **智能处理**: 自动去除输入中的空格和分隔符
- **结果分类**: 合法和不合法号码分别显示
- **详细信息**: 提取地区、年龄、性别、运营商等信息
- **一键复制**: 支持复制验证结果到剪贴板
- **格式支持**: 支持各种空格和分隔符格式的输入

### 📋 JSON格式化工具 (即将上线)
- **格式化美化**: JSON数据格式化和美化显示
- **数据压缩**: 移除空格和换行，压缩JSON数据
- **语法验证**: 检测和提示JSON语法错误
- **格式转换**: JSON转CSV、XML等格式
- **结构可视化**: 树形结构展示JSON数据
- **大文件支持**: 支持处理大型JSON文件

## 🚀 快速开始

### 在线使用（推荐）
直接访问 [https://reaperliu.github.io/Hammer/](https://reaperliu.github.io/Hammer/) 即可使用所有工具。

### 本地部署
```bash
# 克隆项目
git clone https://github.com/reaperLiu/Hammer.git
cd Hammer

# 启动本地服务器
python3 -m http.server 8000

# 在浏览器中访问
# http://localhost:8000
```

## 📁 项目结构

```
Hammer/
├── index.html              # 主页
├── tools/                  # 工具目录
│   ├── chinaidcard/       # 身份证验证器
│   │   ├── standalone_ui.html
│   │   ├── id_validator.py
│   │   └── ...
├── assets/                 # 静态资源（即将添加）
├── docs/                   # 文档（即将添加）
├── README.md              # 项目说明
└── LICENSE                # 许可证
```

## 🔧 技术栈

- **前端**: HTML5 + CSS3 + 原生JavaScript
- **设计**: 响应式设计，CSS Grid/Flexbox
- **部署**: GitHub Pages
- **版本控制**: Git

## 🤝 贡献指南

欢迎贡献新工具或改进现有功能！

### 添加新工具
1. 在 `tools/` 目录下创建新的工具文件夹
2. 实现工具的HTML界面和功能
3. 在主页 `index.html` 中添加工具卡片
4. 更新 README.md 文档
5. 提交 Pull Request

### 工具开发规范
- 所有工具必须支持本地运行
- 不得上传用户数据到服务器
- 界面需要响应式设计
- 代码需要适当注释
- 提供使用说明文档

## 📊 统计数据

- 🛠️ **工具数量**: 6个（1个已上线，5个开发中）
- 🔒 **隐私保护**: 100%本地运行
- 📱 **设备支持**: 桌面、平板、手机
- 🌐 **浏览器兼容**: Chrome、Firefox、Safari、Edge

## 📝 更新日志

### v1.0.0 (2025-11-20)
- 🎉 项目初始版本发布
- ✅ 添加中国身份证验证器
- 🎨 完成主页界面设计
- 📚 完善项目文档

### 即将发布
- 📋 JSON格式化工具
- 🔐 Base64编解码器
- 🔗 URL编解码器

## 🔗 相关链接

- [GitHub仓库](https://github.com/reaperLiu/Hammer)
- [在线演示](https://reaperliu.github.io/Hammer/)
- [问题反馈](https://github.com/reaperLiu/Hammer/issues)
- [功能建议](https://github.com/reaperLiu/Hammer/discussions)

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。

## 🙏 致谢

感谢所有贡献者和用户的支持！

---

**⚠️ 隐私声明**: 本项目所有工具均在本地运行，不会收集、存储或上传任何用户数据。

*最后更新: 2025-11-20*