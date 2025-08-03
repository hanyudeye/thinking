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

