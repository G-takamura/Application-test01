import os
from openai import OpenAI

# 1. クライアントの初期化（プロバイダーのBase URLとAPIキーを指定）
# ※ DeepInfra を使用する例:
client = OpenAI(
    api_key=os.environ.get("DEEPINFRA_API_KEY"),  # 環境変数からAPIキーを取得
    base_url="https://api.deepinfra.com/v1/openai",
)

def generate_text(prompt: str):
    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-4-Maverick-17B-Instruct",
            messages=[
                {"role": "system", "content": "あなたは優秀なAIアシスタントです。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None

if __name__ == "__main__":
    prompt_text = "Pythonでクイックソートを実装するコードを書いてください。"
    result = generate_text(prompt_text)
    
    if result:
        print("--- レスポンス ---")
        print(result)
