// ==UserScript==
// @name         网站防沉迷提醒脚本
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  访问指定沉迷网站时，每2小时仅提醒一次，需输入指定文字才能访问
// @author       你自己
// @match        *://*/*  // 匹配所有网站，后续通过脚本过滤指定网站
// @grant        GM_registerMenuCommand
// @grant        GM_setValue
// @grant        GM_getValue
// @run-at       document-start  // 页面加载前触发，避免网站提前加载
// ==/UserScript==

(function() {
    'use strict';

    // ===================== 可自定义配置 =====================
    // 1. 填写你需要防沉迷的网站（域名包含即可，比如"douyin.com"匹配所有抖音域名）
    const ADDICT_WEBSITES = [
        "douyin.com",    // 抖音
        "kuaishou.com",  // 快手
        "bilibili.com",  // B站（可根据需要增减）
        "game.com",       // 示例游戏网站
        "youtube.com"
    ];
    // 2. 提醒间隔：2小时（单位：毫秒，7200000 = 2*60*60*1000）
    const REMIND_INTERVAL = 7200000;
    // 3. 需要输入的验证文字
    const VERIFY_TEXT = "我坚持要访问这个容易沉迷的网站";
    // ========================================================

    // 获取当前页面域名
    const currentHost = window.location.hostname;
    // 判断当前网站是否在沉迷列表中
    const isAddictSite = ADDICT_WEBSITES.some(site => currentHost.includes(site));

    if (!isAddictSite) return; // 非沉迷网站，直接放行

    // 获取最后一次提醒的时间戳
    const lastRemindTime = GM_getValue("lastRemindTime", 0);
    const now = Date.now();

    // 检查是否超过2小时间隔
    if (now - lastRemindTime < REMIND_INTERVAL) {
        return; // 2小时内已提醒过，直接放行
    }

    // 触发提醒流程
    function showRemindDialog() {
        // 阻止页面加载
        window.stop();
        document.documentElement.innerHTML = ""; // 清空页面内容

        // 创建提醒弹窗
        const dialog = document.createElement("div");
        dialog.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: #f5f5f5;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            z-index: 999999;
        `;

        // 提醒文字
        const tipText = document.createElement("p");
        tipText.textContent = "⚠️ 该网站容易沉迷，建议不要访问！你可以使用其他爱好或习惯来代替这个习惯";
        tipText.style.cssText = "font-size: 20px; color: #e63946; margin-bottom: 20px;";

        // 输入框
        const input = document.createElement("input");
        input.type = "text";
        input.placeholder = "输入指定文字以继续访问...";
        input.style.cssText = `
            padding: 12px 20px;
            width: 400px;
            font-size: 16px;
            border: 2px solid #ccc;
            border-radius: 8px;
            margin-bottom: 20px;
            outline: none;
        `;
        input.addEventListener("focus", () => {
            input.style.borderColor = "#2196f3";
        });
        input.addEventListener("blur", () => {
            input.style.borderColor = "#ccc";
        });

        // 确认按钮
        const confirmBtn = document.createElement("button");
        confirmBtn.textContent = "确认访问";
        confirmBtn.style.cssText = `
            padding: 12px 40px;
            font-size: 16px;
            background: #2196f3;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s;
        `;
        confirmBtn.addEventListener("mouseover", () => {
            confirmBtn.style.background = "#1976d2";
        });
        confirmBtn.addEventListener("mouseout", () => {
            confirmBtn.style.background = "#2196f3";
        });

        // 验证逻辑
        confirmBtn.addEventListener("click", () => {
            if (input.value.trim() === VERIFY_TEXT) {
                // 记录本次提醒时间
                GM_setValue("lastRemindTime", now);
                // 刷新页面，正常访问
                window.location.reload();
            } else {
                alert("❌ 输入错误！请准确输入指定文字。");
                input.value = "";
                input.focus();
            }
        });

        // 组装弹窗
        dialog.appendChild(tipText);
        dialog.appendChild(input);
        dialog.appendChild(confirmBtn);
        document.body.appendChild(dialog);

        // 自动聚焦输入框
        input.focus();
    }

    // 执行提醒弹窗
    showRemindDialog();

})();