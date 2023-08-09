

import openai

openai.api_key = "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"  # 替换为你的 OpenAI API 密钥

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # 或其他适合的 GPT 模型引擎
        prompt=prompt,
        max_tokens=50  # 控制回复的长度
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("ChatGPT: 你好！我是 ChatGPT，我们开始聊天吧！输入 '退出' 可退出对话。")
    while True:
        user_input = input("你: ")
        if user_input == "退出":
            print("ChatGPT: 再见！")
            break
        prompt = f"你: {user_input}\nChatGPT:"
        response = chat_with_gpt(prompt)
        print(response)
