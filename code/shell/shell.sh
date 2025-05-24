echo "hello";

a="world"
echo "$a"

# 如果不是交互式 shell，就退出
if [[ 'abiff' == *i* ]]; then
  echo "Not an interactive shell, exiting."
fi