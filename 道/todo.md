---
title: todo
date:  2026-02-05T13:10:10+08:00
draft: true
---

Todo:  使用下 openclaw ，简单充值 豆包 10元，deepseek 10元，尝试功能，因为很多博主说很不错

Todo: spacex 2026 年 6 月中旬上市，准备点现金购买，每股 $79–$100 

配置查找，编辑，用终端学习
bindkey -s '^F' 'fzf --preview "cat {}" --bind "enter:execute(vim {})"\n'


什么东西可以放在手里盘，且能很好地使人放松 (硬币)

更新下 tmux
git clone --single-branch https://github.com/gpakosz/.tmux.git

zsh
plugins=(git autojump  zsh-navigation-tools fzf)

安装neovim,安装插件
vim 必备插件有哪些，可以组成ide

配置nvim
~/.config/nvim/init.lua

local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
vim.opt.rtp:prepend(lazypath)

require("lazy").setup({

   {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate"
  },
{ "nvim-lualine/lualine.nvim" },

})


-- 配置键映射

现在大型项目不用文件树，而是直接查找
vim.keymap.set("n", "<leader>ff", require("telescope.builtin").find_files)



emacs 设置透明背景
  (set-face-background 'default "unspecified")

  (set-frame-parameter nil 'alpha-background 70)
  (add-to-list 'default-frame-alist '(alpha-background . 70))
 
