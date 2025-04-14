def 欢迎():
    print("欢迎来到 \"阿明之家\"！")
    print("输入 '帮助' 可以提供帮助信息")

def 等待输入():
    while True:
        user_input = input("请输入命令：")
        if user_input == "帮助":
            print("帮助信息：\n1. 输入 '帮助' 查看帮助信息\n2. 输入 '退出' 退出程序")
        elif user_input == "退出":
            print("感谢使用，再见！")
            break
        else:
            print(f"未知命令：{user_input}")

def 执行流程():
    # todo 1
    欢迎()
    # todo2
    等待输入()

    
执行流程()

