// ==UserScript==
// @name         屏蔽feeder网站元素通用脚本
// @description  feeder 订阅软件根据CSS类名、ID等屏蔽网站上的不需要的元素
// @match        https://feeder.co/*
// @grant        none
// @run-at       document-start
// ==/UserScript==

(function() {
    'use strict';

    // ===== 配置区域 =====
    // 在这里配置要隐藏的元素

    // 指定要隐藏的类名（支持多个，用逗号分隔）
    const HIDE_CLASSES = [
        // 例如：'ad-container', 'popup-menu', 'selection-menu'
        'navigation-stack-item'
    ];

    // 指定要隐藏的ID（支持多个）
    const HIDE_IDS = [
        // 例如：'ad-banner', 'modal-popup'
    ];

    // 指定要隐藏的标签类型
    const HIDE_TAGS = [
        // 例如：'script', 'iframe'
    ];

    // 正则表达式匹配的类名（需要包含的文本）
    const HIDE_CLASS_PATTERNS = [
        // 例如：'ad', 'popup', 'modal'
    ];

    // ===== 执行函数 =====

    // 隐藏指定类名的元素
    function hideByClasses() {
        if (HIDE_CLASSES.length > 0) {
            const selector = HIDE_CLASSES.map(cls => `.${cls}`).join(', ');
            const elements = document.querySelectorAll(selector);
            elements.forEach(el => {
                el.style.display = 'none';
                el.remove();
            });
        }
    }

    // 隐藏指定ID的元素
    function hideByIds() {
        if (HIDE_IDS.length > 0) {
            HIDE_IDS.forEach(id => {
                const element = document.getElementById(id);
                if (element) {
                    element.style.display = 'none';
                    element.remove();
                }
            });
        }
    }

    // 隐藏指定标签的元素
    function hideByTags() {
        if (HIDE_TAGS.length > 0) {
            HIDE_TAGS.forEach(tag => {
                const elements = document.querySelectorAll(tag);
                elements.forEach(el => {
                    el.style.display = 'none';
                    el.remove();
                });
            });
        }
    }

    // 使用正则表达式隐藏含有特定文本的类名元素
    function hideByClassPatterns() {
        if (HIDE_CLASS_PATTERNS.length > 0) {
            const allElements = document.querySelectorAll('*');
            allElements.forEach(el => {
                const className = el.className;
                if (typeof className === 'string') {
                    HIDE_CLASS_PATTERNS.forEach(pattern => {
                        if (className.includes(pattern)) {
                            el.style.display = 'none';
                            el.remove();
                        }
                    });
                }
            });
        }
    }

    // 观察新添加的DOM元素，动态隐藏
    function observeDOM() {
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.addedNodes.length > 0) {
                    mutation.addedNodes.forEach(node => {
                        if (node.nodeType === 1) { // 元素节点
                            // 检查是否需要隐藏
                            const className = node.className;
                            if (typeof className === 'string') {
                                // 检查类名
                                if (HIDE_CLASSES.some(cls => className.includes(cls)) ||
                                    HIDE_CLASS_PATTERNS.some(pattern => className.includes(pattern))) {
                                    node.style.display = 'none';
                                    node.remove();
                                }
                            }
                            // 检查ID
                            if (node.id && HIDE_IDS.includes(node.id)) {
                                node.style.display = 'none';
                                node.remove();
                            }
                        }
                    });
                }
            });
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }

    // 执行隐藏操作
    function hideElements() {
        hideByClasses();
        hideByIds();
        hideByTags();
        hideByClassPatterns();
    }

    // 页面加载完毕后执行（防止元素重新加载）
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', hideElements);
    } else {
        hideElements();
    }

    // 启动DOM观察器，动态隐藏新插入的元素
    observeDOM();

})();