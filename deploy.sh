#!/bin/bash
# GitHub 部署脚本

echo "🚀 中国身份证验证器 - GitHub 部署脚本"
echo "========================================"

# 检查是否已经设置了远程仓库
if git remote get-url origin > /dev/null 2>&1; then
    echo "✅ 远程仓库已设置"
    git remote -v
else
    echo "❌ 未设置远程仓库"
    echo ""
    echo "请先在GitHub创建一个新仓库，然后运行："
    echo "git remote add origin https://github.com/你的用户名/仓库名.git"
    echo ""
    echo "或者运行以下命令设置远程仓库："
    read -p "请输入你的GitHub用户名: " username
    read -p "请输入仓库名称 (默认: chinaidcard): " reponame
    reponame=${reponame:-chinaidcard}
    
    echo "设置远程仓库: https://github.com/$username/$reponame.git"
    git remote add origin "https://github.com/$username/$reponame.git"
fi

# 检查是否有未提交的更改
if ! git diff-index --quiet HEAD --; then
    echo "📝 发现未提交的更改，正在提交..."
    git add .
    git commit -m "update: 更新项目内容"
fi

# 推送到GitHub
echo "📤 推送到GitHub..."
if git push -u origin main; then
    echo ""
    echo "🎉 部署成功！"
    echo ""
    echo "📱 你的网站将在几分钟内在以下地址可用："
    
    # 尝试获取远程仓库URL并生成GitHub Pages链接
    remote_url=$(git remote get-url origin)
    if [[ $remote_url =~ github\.com[:/]([^/]+)/([^/]+)(\.git)?$ ]]; then
        username="${BASH_REMATCH[1]}"
        reponame="${BASH_REMATCH[2]}"
        echo "🌐 主页: https://$username.github.io/$reponame/"
        echo "🆔 验证器: https://$username.github.io/$reponame/standalone_ui.html"
    else
        echo "🌐 GitHub Pages: https://你的用户名.github.io/仓库名/"
    fi
    
    echo ""
    echo "⚙️  请确保在GitHub仓库设置中启用了GitHub Pages："
    echo "   1. 进入仓库的 Settings 页面"
    echo "   2. 找到 Pages 设置"
    echo "   3. Source 选择 'Deploy from a branch'"
    echo "   4. Branch 选择 'main'"
    echo "   5. 点击 Save"
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
    echo "1. 确保在GitHub上创建了对应的仓库"
    echo "2. 检查网络连接"
    echo "3. 配置GitHub身份验证 (SSH密钥或Personal Access Token)"
fi

echo ""
echo "📚 更多帮助请查看 部署指南.md 文件"