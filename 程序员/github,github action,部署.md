---
layout: default
toc: false
title: github,github action,自动部署
date: 2025-07-13T14:46:00+08:00
categories: ['']
draft: true
---

!技能直接可以变现，而不是看文档
重心，专注，实际操作学的更快

## 查看git 项目 的远程地址

1.  git remote -v
2. 打开 .git/config 文件查看

## 做贡献 contributor

分叉 别人的项目 ，创建 分支后 进行  修改[ 使用  git add -p ]，然后提交到线上分支 [git push -u origin 分支名]，然后请求合并 

## github page

- 每个账号最多支持 1 个用户主页仓库（username.github.io）
- 其他项目可以用子路径托管（如 username.github.io/project-name/）

## github action

相当于 给项目 [上传，拉取]等状态，设置 行为。

``` yml

# Deploy
# ci.yml
name: deploy to aliyun
on:
  push:
    branches:
      - master
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # 切换分支
      - name: Checkout
        uses: actions/checkout@master
      # 使用 node:10
      - name: use Node.js 10
        uses: actions/setup-node@v1
        with:
          node-version: 10
      # npm install
      - name: npm install and build
        run: |
          yarn install
          npm run build
        env:
          CI: true
      - name: Deploy
        uses: easingthemes/ssh-deploy@v2.0.7
        env:
          SSH_PRIVATE_KEY: ${{ secrets.ACCESS_TOKEN }}
          ARGS: "-avz --delete"
          SOURCE: "build/"
          REMOTE_HOST: ${{ secrets.REMOTE_HOST }}
          REMOTE_USER: ${{ secrets.REMOTE_USER }}
          TARGET: ${{ secrets.TARGET }}
```

变量在 github setting 里面设置

# github 如何自动更新 子模块

在 Git 里，子模块（submodule）默认是**固定指向某个特定提交**的，所以即使主仓库更新了，子模块不会自动跟随更新，除非你明确去拉取和更新它。

如果你想让 GitHub 上的仓库**自动更新子模块**，常见有两种方式：

---

## 1. 手动更新（本地执行）

在本地更新子模块，然后推送：

```bash
# 更新子模块到最新远程提交
git submodule update --remote --merge

# 如果有多个子模块，可以全部更新
git submodule update --init --recursive --remote

# 提交更新后的子模块引用
git add path/to/submodule
git commit -m "Update submodule"
git push
```

优点：简单
缺点：需要人工执行，不能自动化

---

## 2. GitHub Actions 自动更新（推荐）

如果你想**自动化**，可以用 GitHub Actions 定时拉取子模块的最新提交并推送。

**示例 `.github/workflows/update-submodules.yml`**

```yaml
name: Update Submodules

on:
  schedule:
    - cron: '0 2 * * *' # 每天凌晨 2 点运行
  workflow_dispatch:     # 允许手动触发

jobs:
  update-submodules:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout main repo
        uses: actions/checkout@v4
        with:
          submodules: true
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Update submodules to latest commit
        run: |
          git submodule update --remote --merge
          git add .
          if ! git diff --cached --quiet; then
            git config --global user.name "github-actions[bot]"
            git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
            git commit -m "Auto update submodules"
            git push
          fi
```

这样，GitHub 会：

1. 定时或手动触发
2. 拉取所有子模块到远程最新
3. 如果有变化就自动提交

---

## 3. 让子模块永远跟踪分支（**危险模式**）

你也可以让子模块**跟踪某个分支**，而不是固定提交，但这会在拉取主仓库时自动变更子模块内容，可能引起构建不一致。

设置方法：

```bash
git config -f .gitmodules submodule.path/to/submodule.branch main
```

然后更新：

```bash
git submodule update --remote
```

但**不建议在生产环境用这个方法**，因为可能导致构建不可重现。

---

如果你愿意，我可以帮你写一个 **支持多个子模块自动更新并 PR** 的 GitHub Actions 脚本，这样每次更新都会自动发 PR，而不是直接推送到 main。这样会更安全。
你是想让我帮你做这种自动 PR 的版本吗？

## 如何测试 github actions 脚本能否运行

测试 GitHub Actions 脚本能否运行，可以分成两种情况来看：

## 1. **本地测试（不用频繁 push 到 GitHub）**

如果你想在本地就验证脚本是否能执行，可以用 [**act**](https://github.com/nektos/act) 这个工具，它能在你本机模拟 GitHub Actions 运行环境。

### 安装 act

```bash
# macOS
brew install act

# Linux
curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```

### 本地运行

在你的仓库根目录执行：

```bash
act
```

它会读取 `.github/workflows/*.yml` 并执行对应的 job。
如果只想跑某个特定 workflow：

```bash
act -W .github/workflows/ci.yml
```

或者只跑一个指定的事件：

```bash
act push
act pull_request
```

> **注意**
>
> * `act` 使用 Docker 模拟环境，你需要先装好 Docker。
> * 有些官方 runner 镜像很大，第一次下载会比较慢。
> * 不支持所有 GitHub Actions 的功能（尤其是 GitHub 托管的 secrets / 部分 API）。

## 2. **在 GitHub 上测试（真机运行）**

如果你不想装 act，或者想直接验证 GitHub 托管环境：

1. **建一个测试分支**（比如 `actions-test`）
2. 在 `.github/workflows/` 里添加或修改 workflow
3. push 到 GitHub
4. 在仓库的 **Actions** 页面查看执行结果

你也可以用 `workflow_dispatch` 事件加一个手动触发按钮：

```yaml
on:
  workflow_dispatch:  # 这样可以在 Actions 页面手动运行
```

然后在 GitHub UI 点击 “Run workflow” 就能测试，不用等 push 或 PR 触发。

---

## 3. **调试技巧**

* 在步骤里加 `echo` 输出变量：

```yaml
- name: Debug env
  run: |
    echo "GITHUB_REF=$GITHUB_REF"
    echo "PWD=$(pwd)"
```

* 开启更详细日志：

```bash
ACTIONS_STEP_DEBUG=true
```

在 GitHub 仓库 → **Settings → Secrets and variables → Actions → Variables** 添加 `ACTIONS_STEP_DEBUG` 变量并设为 `true`，重新运行 workflow。
