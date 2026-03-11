// ==UserScript==
// @name         屏蔽feeder.co选中文本弹出菜单
// @description  屏蔽feeder.co网站的选中文本弹出菜单功能
// @match        https://feeder.co/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // 监听选中文本事件，隐藏弹出菜单
    document.addEventListener('selectionchange', function() {
        // 延迟执行，以确保菜单已经弹出
        setTimeout(function() {
            // 查找常见的弹出菜单元素，根据实际情况调整选择器
            const menus = document.querySelectorAll('.selection-menu, .text-selection-menu, .popup-menu, [class*="menu"], [id*="menu"]');
            menus.forEach(menu => {
                if (menu.style.display !== 'none') {
                    menu.style.display = 'none';
                }
            });
        }, 100);
    });

    // 也可以监听mouseup事件
    document.addEventListener('mouseup', function(e) {
        // 如果有选中文本
        const selection = window.getSelection();
        if (selection.toString().length > 0) {
            // 隐藏菜单
            setTimeout(function() {
                const menus = document.querySelectorAll('.selection-menu, .text-selection-menu, .popup-menu, [class*="menu"], [id*="menu"]');
                menus.forEach(menu => {
                    menu.style.display = 'none';
                });
            }, 50);
        }
    });

})();