// ==UserScript==
// @name         Force Mobile View for Specific Site
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  在指定网站自动使用手机浏览器模式访问
// @author       You
// @match        https://example.com/*
// @match        https://zhihu.com/*
// @run-at       document-start
// ==/UserScript==

(function() {
    'use strict';
    // 模拟 iPhone Safari 的 User-Agent
    const mobileUA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1';

    // 重写浏览器的 UA
    Object.defineProperty(navigator, 'userAgent', {
        value: mobileUA,
        configurable: false
    });

    // 可选：也修改 platform 与 appVersion（有些网站会检测）
    Object.defineProperty(navigator, 'platform', {
        value: 'iPhone',
        configurable: false
    });
    Object.defineProperty(navigator, 'appVersion', {
        value: mobileUA,
        configurable: false
    });
})();
