import asyncio
from ollama import AsyncClient

# OllamaサービスのURL。Dockerで起動した場合のデフォルトポートです。
OLLAMA_HOST_URL = "http://localhost:11434"
# Dockerで作成したモデル名
MODEL_NAME = "gemma-3-1b"

# チャット履歴を保持するリスト
messages = []

async def chat_with_ollama():
    """Ollamaとの非同期チャットセッションを開始します。"""
    print(f"Ollama Async Chat ({MODEL_NAME})を開始します。")
    print("終了するには 'exit' または 'quit' と入力してください。")
    print("-" * 30)

    # 非同期クライアントを初期化
    client = AsyncClient(host=OLLAMA_HOST_URL)

    try:
        while True:
            # ユーザーからの入力を非同期で待機
            user_input = await asyncio.to_thread(input, "あなた: ")

            if user_input.lower() in ['exit', 'quit']:
                print("チャットを終了します。")
                break

            if not user_input.strip():
                continue

            # ユーザーのメッセージを履歴に追加
            messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            print("モデル: ", end="", flush=True)
            
            # Ollama APIに非同期でリクエストを送信し、ストリーミングで応答を受け取る
            response_stream = await client.chat(
                model=MODEL_NAME,
                messages=messages,
                stream=True,  # ストリーミングを有効化
            )

            full_response_content = ""
            # ストリームからチャンクを順次読み込み、画面に出力
            async for chunk in response_stream:
                content = chunk.get("message", {}).get("content", "")
                if content:
                    print(content, end="", flush=True)
                    full_response_content += content
            
            # モデルの完全な応答を履歴に追加
            if full_response_content:
                messages.append(
                    {
                        "role": "assistant",
                        "content": full_response_content
                    }
                )

            # 新しい行に移動
            print()

    except Exception as e:
        print(f"\nエラーが発生しました: {e}")
    finally:
        print("-" * 30)

if __name__ == "__main__":
    # 非同期メイン関数を実行
    asyncio.run(chat_with_ollama())