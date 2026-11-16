import os
from anthropic import Anthropic

# APIキーを環境変数から取得（または直接文字列で指定）
# os.environ["ANTHROPIC_API_KEY"] = "your-api-key-here"

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "こんにちは！自己紹介を簡単にしてください。"}
    ]
)

# レスポンスの出力
print(response.content[0].text)
