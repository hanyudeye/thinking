import random
import time

class ChatBot:
    def __init__(self):
        self.responses = {
            "你好": ["你好!", "你好啊!", "很高兴见到你!"],
            "再见": ["再见!", "下次见!", "期待下次聊天!"],
            "天气": ["今天天气不错呢!", "是个出门的好日子!", "记得带伞哦!"],
            "名字": ["我叫小智，是你的AI助手!", "你可以叫我小智!", "我是小智~"],
            "心情": ["我今天心情不错!", "和你聊天让我很开心!", "希望你也开心!"],
            "吃饭": ["吃饭对身体很重要哦!", "记得按时吃饭!", "想吃什么好吃的呢?"],
            "帮助": ["你可以问我天气、心情、名字等问题，或输入'退出'结束对话。"]
        }
        self.default_responses = [
            "抱歉,我不太明白...",
            "这个问题有点难,换个话题吧!",
            "让我想想怎么回答...",
            "你说得很有趣呢!",
        ]
        self.exit_cmds = {"退出", "再见", "拜拜", "bye", "88", "quit", "exit"}

    def format_response(self, text):
        return f"\n🤖 AI助手: {text}\n"

    def format_user_input(self, text):
        return f"\n👤 你: {text}\n"

    def get_response(self, user_input):
        time.sleep(0.5)
        user_input = user_input.strip().lower()
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return random.choice(self.default_responses)

    def start_chat(self):
        print("\n" + "="*50)
        print("欢迎使用AI聊天助手! 输入'退出'、'再见'、'bye'等结束对话。")
        print("输入'帮助'获取可用指令。\n" + "="*50 + "\n")

        while True:
            user_input = input("请输入: ").strip()
            print(self.format_user_input(user_input))
            if user_input.lower() in self.exit_cmds:
                print(self.format_response("再见!期待下次聊天~"))
                break
            response = self.get_response(user_input)
            print(self.format_response(response))

def main():
    ChatBot().start_chat()

if __name__ == "__main__":
    main()
