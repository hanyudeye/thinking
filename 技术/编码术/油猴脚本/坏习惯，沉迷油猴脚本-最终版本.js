// ==UserScript==
// @name         防沉迷 - 每个网站独立2小时冷却
// @namespace    http://tampermonkey.net/
// @version      2.0
// @description  每个网站独立计时，互不干扰，验证文字才能进，2小时内不再提醒
// @author       豆包
// @match        *://*/*
// @grant        GM_setValue
// @grant        GM_getValue
// @run-at       document-start
// ==/UserScript==

(function() {
    'use strict';

    // ====================== 你自己的配置 ======================
    const ADDICT_SITES = [
        "bilibili.com",
        "douyin.com",
        "kuaishou.com",
        "xiaohongshu",
        "taobao.com",
        "jd.com",
        "youtube.com"
    ];

    const COOLDOWN = 2 * 60 * 60 * 1000; // 2小时
    const MUST_INPUT_TEXT = "我坚持要访问这个容易沉迷的网站";
    const WARNING_TEXT = "⚠️ 这个网站容易沉迷，请尽量不要访问！";
    // ==========================================================

    // 获取当前域名
    const host = window.location.hostname;

    // 判断是否在沉迷列表里
    const isTarget = ADDICT_SITES.some(site => host.includes(site));
    if (!isTarget) return;

    // 每个网站独立 key
    const storageKey = "last_warn_" + host;
    const now = Date.now();
    const last = GM_getValue(storageKey, 0);

    // 没到冷却时间，直接放行
    if (now - last < COOLDOWN) {
        return;
    }

    // ============== 开始拦截 ==============
    window.stop();
    document.documentElement.innerHTML = '';

    // 第一步：警告
    const goOn = confirm(WARNING_TEXT + "\n\n确定要继续访问吗？你可以使用其他爱好或习惯来代替这个习惯");
    if (!goOn) {
        window.location.href = "about:blank";
        return;
    }

    // 第二步：输入验证
    const input = prompt("请输入确认文字才能访问：\n" + MUST_INPUT_TEXT);
    if (input !== MUST_INPUT_TEXT) {
        alert("❌ 输入错误，禁止访问");
        window.location.href = "about:blank";
        return;
    }

    // 验证成功：给当前网站独立记录冷却时间
    GM_setValue(storageKey, now);
    alert("✅ 已确认，2小时内不再提醒");
    window.location.reload();
})();