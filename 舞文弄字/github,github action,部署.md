---
layout: default
toc: false
title: github,github action,自动部署
date: 2025-07-13T14:46:00+08:00
categories: ['']
draft: true
---

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

