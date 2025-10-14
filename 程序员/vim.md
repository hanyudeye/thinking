---
layout: default
toc: false
title: vim
date:  2025-08-16T11:07:29+08:00
draft: true
---
我安装了 github 扩展，所以，打开 ~/.vim_runtime/readme.md 文件夹可以查看文档。

Nerdtree 默认 的快捷键是 <leader> nn :NERDTreeToggle


inoremap kj <ESC>   kj 按键绑定<ESC> 键

在 Vim 中，高效使用通常依赖于一些基本配置、快捷键优化和插件管理。以下是一个精简而实用的配置指南，适合大多数开发者和日常使用。

## 1️⃣ 基本设置（`~/.vimrc` 或 `~/.config/nvim/init.vim`）

```vim
" ===== 基础界面优化 =====
set nocompatible        " 禁用兼容模式
set number              " 显示行号
set relativenumber      " 显示相对行号
set cursorline          " 高亮当前行
set cursorline 高亮当前行
set showcmd             " 显示部分命令
set showcmd 显示部分命令
set showmode            " 显示当前模式
set showmode 显示当前模式
set wildmenu            " 命令补全菜单
set laststatus=2        " 总是显示状态栏

" ===== 编辑体验 =====
set expandtab           " 使用空格代替制表符
set tabstop=4           " 一个 tab 显示为 4 个空格
set shiftwidth=4        " 缩进宽度为 4
set smartindent         " 智能缩进
set autoindent          " 自动缩进
set nowrap              " 不折行
set scrolloff=5         " 保持光标上下 5 行
set clipboard=unnamed   " 使用系统剪贴板

" ===== 搜索优化 =====
set ignorecase          " 搜索忽略大小写
set smartcase           " 包含大写字母时区分大小写
set incsearch           " 实时搜索
set hlsearch            " 高亮搜索结果

" ===== 备份与撤销 =====
set undofile            " 持久化撤销
set undodir=~/.vim/undo " 撤销文件存放路径
set backup              " 启用备份
set backupdir=~/.vim/backup
set swapfile            " 启用 swap 文件
set directory=~/.vim/swap
```

## 关闭选项
```
set nonumber      " 关闭行号
set nocursorline  " 关闭高亮当前行
```

| 类型     | 清除/关闭          | 恢复默认                            |
| ------ | -------------- | ------------------------------- |
| 布尔值    | `set nooption` | `set option&` 或 `set invoption` |
| 字符串/数值 | `set option=`  | `set option&`                   |


## 2️⃣ 常用快捷键优化

```vim
" ===== 分屏快捷键 =====
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

" ===== 文本操作 =====
nnoremap <leader>y "+y      " 复制到系统剪贴板
nnoremap <leader>p "+p      " 粘贴系统剪贴板
vnoremap <leader>y "+y

" ===== 撤销/重做 =====
nnoremap U <C-r>            " 统一重做

" ===== 视觉模式快速缩进 =====
vnoremap < <gv
vnoremap > >gv
```

> ⚡ 说明：
>
> * `<leader>` 默认是 `\`，可以用 `let mapleader=","` 改成更方便的 `,`
> * `<C-*>` 是 Ctrl 键组合

---

## 3️⃣ 推荐插件（需插件管理器，如 [vim-plug](https://github.com/junegunn/vim-plug)）

```vim
call plug#begin('~/.vim/plugged')

" 语法和文件树
Plug 'preservim/nerdtree'       " 文件树
Plug 'Xuyuanp/nerdtree-git-plugin'

" 代码高亮与补全
Plug 'sheerun/vim-polyglot'     " 多语言语法高亮
Plug 'neoclide/coc.nvim', {'branch': 'release'} " 智能补全

" 状态栏美化
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" 颜色主题
Plug 'morhetz/gruvbox'

call plug#end()
```

---

## 4️⃣ 高效使用 Vim 的核心技巧

1. **善用分屏**：

   * 水平分屏：`:split` 或 `:sp`
   * 垂直分屏：`:vsplit` 或 `:vsp`
   * 快速移动光标：`Ctrl+h/j/k/l`

2. **快速搜索与跳转**：

   * `/pattern` 搜索
   * `*`/`#` 快速搜索光标下单词
   * `%` 跳转匹配括号

3. **使用寄存器和系统剪贴板**：

   * `"+y` 复制到系统剪贴板
   * `"+p` 从系统剪贴板粘贴

4. **撤销与重做**：

   * `u` 撤销
   * `Ctrl+r` 重做
   * `:undolist` 查看历史撤销点

5. **宏与多行操作**：

   * `q<letter>` 开始录制宏
   * `@<letter>` 执行宏
   * `.` 重复上一个操作

6. **插件辅助**：

   * NERDTree 打开文件树
   * coc.nvim 提供智能补全和 LSP 支持
   * vim-airline 美化状态栏并显示文件信息

---

## vim 有能 多跳几个单词的快捷键吗，有时一个个单词跳太慢了

可以使用大写 的 W，E，B