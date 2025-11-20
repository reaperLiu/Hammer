#!/bin/bash
# Hammer 项目一键部署脚本

echo "🔨 Hammer 工具集合 - GitHub Pages 部署脚本"
echo "=============================================="

# 检查是否在正确的目录
if [ ! -f "index.html" ]; then
    echo "❌ 错误: 请在 Hammer 项目根目录下运行此脚本"
    exit 1
fi

# 初始化Git仓库（如果还没有）
if [ ! -d ".git" ]; then
    echo "📦 初始化Git仓库..."
    git init
    
    # 设置Git用户信息（如果还没有设置）
    if [ -z "$(git config user.name)" ]; then
        echo "⚙️  设置Git用户信息..."
        git config user.name "ReaperLiu"
        git config user.email "reaper@example.com"
    fi
fi

# 添加所有文件
echo "📝 添加项目文件..."
git add .

# 检查是否有更改需要提交
if git diff --staged --quiet; then
    echo "ℹ️  没有新的更改需要提交"
else
    echo "💾 提交更改..."
    git commit -m "feat: 更新Hammer工具集合

- 🔨 主页界面优化
- 🆔 集成身份证验证器
- 📚 完善项目文档
- 🎨 响应式设计改进"
fi

# 检查是否已经设置了远程仓库
if git remote get-url origin > /dev/null 2>&1; then
    echo "✅ 远程仓库已设置"
    git remote -v
else
    echo "⚙️  设置远程仓库..."
    git remote add origin https://github.com/reaperLiu/Hammer.git
fi

# 推送到GitHub
echo "🚀 推送到GitHub..."
if git push -u origin main; then
    echo ""
    echo "🎉 部署成功！"
    echo ""
    echo "📱 你的网站将在几分钟内在以下地址可用："
    echo "🌐 主页: https://reaperliu.github.io/Hammer/"
    echo "🆔 身份证验证器: https://reaperliu.github.io/Hammer/tools/chinaidcard/standalone_ui.html"
    echo ""
    echo "⚙️  请确保在GitHub仓库设置中启用了GitHub Pages："
    echo "   1. 进入 https://github.com/reaperLiu/Hammer/settings/pages"
    echo "   2. Source 选择 'Deploy from a branch'"
    echo "   3. Branch 选择 'main'"
    echo "   4. 点击 Save"
    echo ""
    echo "📊 项目统计:"
    echo "   - 工具数量: $(find tools -name "*.html" | wc -l | tr -d ' ') 个"
    echo "   - 文件总数: $(find . -type f | wc -l | tr -d ' ') 个"
    echo "   - 项目大小: $(du -sh . | cut -f1)"
else
    echo ""
    echo "❌ 推送失败！"
    echo ""
    echo "可能的原因："
    echo "1. 远程仓库不存在或无权限"
    echo "2. 网络连接问题"
    echo "3. 需要GitHub身份验证"
    echo ""
    echo "💡 解决方案："
    echo "1. 确保在GitHub上创建了 'Hammer' 仓库"
    echo "2. 检查网络连接"
    echo "3. 配置GitHub身份验证 (SSH密钥或PAT)"
    echo "4. 手动运行: git push -u origin main"
fi

echo ""
echo "🔗 相关链接:"
echo "   - GitHub仓库: https://github.com/reaperLiu/Hammer"
echo "   - 问题反馈: https://github.com/reaperLiu/Hammer/issues"
echo "   - 功能建议: https://github.com/reaperLiu/Hammer/discussions"