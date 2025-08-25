---
layout: default
toc: false
title: css样式的学习
date:  2025-08-26T07:34:00+08:00
categories: ['']
---

<style>
    /*3列*/
.container3{
column-count:3; /*分成3列*/
column-gap:20px; /*列之间间隔*/
}

/*用来测试的块元素*/
sec{
border: 1px solid #333;
display:block;
}

.p1 {
    font-family: Arial, sans-serif; /* 设置字体 */
    font-size: 16px; /* 字体大小 */
    line-height: 1.5em; /* 行高 */
    color: #f00; /* 文字颜色 */
    text-align: center; /* 设置文字两端对齐 */
    border: 1px solid #333;
    border-radius: 5px;
    padding:5px;
    draggable:true; /*拖拽*/
}


</style>

CSS 用来 对 页面元素进行 精确 排版和设计样式。

## 排版

### 多列布局

---

<div class="container3">
<sec>列1</sec>
<sec>列2</sec>
<sec>列3</sec>
</div>

---

## 样式

### 字体

<p class="p1" >
字体，字体大小，行高，颜色，对齐方式：居中,拖拽
</p>
