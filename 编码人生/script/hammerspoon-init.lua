
-- hammerspoon 脚本

-- 监听 Cmd+F，执行 killall say
hs.hotkey.bind({"cmd"}, "F", function()
    hs.execute("killall say")
end)

-- 激活名为“备忘录”的窗口
hs.hotkey.bind({"cmd"}, ".", function()
    local win = hs.window.find("备忘录")
    if win then
        win:focus()
        win:raise()
    else
        hs.alert.show("未找到窗口：备忘录")
    end
end)