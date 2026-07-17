# GameNN 架构演化展示站点

玄幕安全团队 · July 2026

GameNN 从博弈推演引擎到语言模型侧枝决策，再到独立智能 WAF 产品的完整演化历程。

## 页面构成

| 区块 | 内容 |
|------|------|
| **Hero** | 统计概览 + 渐变标题 + 动态粒子背景 |
| **演化史** | 5 阶段时间线，含仓库 + 论文链接 |
| **版本对比** | 11 维度 × 5 版本对比表 + 论文引用卡片 |
| **核心架构** | 贯穿所有版本的统一神经回路流程图 |
| **项目族谱** | 5 个项目卡片，含指标 + 论文/仓库链接 |
| **关键数据** | 8 个核心数字 |

## 设计

- **动态粒子** — Canvas 粒子系统 + 连接线
- **浮动光晕** — 3 个 CSS 渐变球体浮动动画
- **渐变文字** — 标题 cyan→purple 渐变 + 背景漂移动画
- **网格叠加** — 60px 网格线，随滚动弱视差
- **滚动动画** — IntersectionObserver 驱动的渐入效果
- **导航高亮** — 滚动时导航边框变色
- **主题** — 深色，zero emoji，纯几何装饰

## 部署到 GitHub Pages

```bash
# 1. 创建 GitHub 仓库，推送到 main
git init
git add .
git commit -m "init: GameNN evolution site"
git remote add origin https://github.com/你的用户名/gamenn-evolution.git
git branch -M main
git push -u origin main

# 2. 仓库 Settings → Pages → 选 Deploy from branch main / (root) → Save
# 3. 等待 1-2 分钟，访问 https://你的用户名.github.io/gamenn-evolution
```

## 本地预览

```bash
python -m http.server 8000
# → http://localhost:8000
```

## 许可证

MIT
