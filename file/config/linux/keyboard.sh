# 交换Caps Lock 和 Ctrl 键
setxkbmap -option "ctrl:swapcaps"

# 清除所有键盘选项
setxkbmap -option ""

# 禁用触摸板
# synclient touchpadoff=1

# 交换鼠标左键和右键
# xmodmap -e 'pointer = 2 1 3'

# 鼠标按钮交换
# xmodmap -e 'pointer = 3 2 1'

# 左右键恢复
xmodmap -e 'pointer = 1 2 3'


# 旋转显示器
# xrandr --output HDMI-0 --rotate left  --output DP-0 --mode 2560x1440  --primary --right-of HDMI-0
# xrandr --output LVDS-1-1 --primary --output HDMI-1-1 --mode 1920x1080 --right-of LVDS-1-1
