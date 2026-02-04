# Learn_Local_LLM

このプロジェクトは、Dockerを使用してローカル環境（CPUのみ）でLLMを動かし、Pythonでチャットを行うためのサンプルです。

## 構成

* **Ollama**: Docker上で動作するLLM推論エンジン
* **Gemma-3-1b**: Googleが提供する軽量なLLM（今回はこのモデルでチャットを行う想定で進めます。）
* **Python Client**: `ollama` ライブラリを使用した非同期チャットUI

## ディレクトリ構成

```text
.
├── compose.yaml                # Docker Composeファイル (複数マウント設定済み)
├── async_chat.py               # Pythonチャットクライアント (MODEL_NAMEを書き換えて使用)
├── README.md                   # 本ファイル
├── .gguf/                 # GGUFモデルファイルを格納するディレクトリ
│   ├── gemma-3-1b-it-qat-q4_0-gguf
│   └── # その他のモデルファイル
└── modelfiles/                 # モデル定義ファイルを格納するディレクトリ
    ├── Modelfile_gemma3        # Gemma 3 用の設定
    └── # その他のモデルの設定

```

## セットアップ手順

### 1. モデルの準備

Hugging FaceからGGUFモデルファイルをダウンロードしてください。
* モデル: `gemma-3-1b-it-qat-q4_0-gguf`

おすすめの方法はHugging Faceのトークンを利用してダウンロードする方法です。
```bash
git clone https://<ユーザ名>:<トークン>@huggingface.co/google/gemma-3-1b-it-qat-q4_0-gguf
```

### 2. Dockerコンテナの起動

以下のコマンドでOllamaコンテナをバックグラウンドで起動します。

```bash
docker compose up -d
```

### 3. Ollamaモデルの作成

マウントした `Modelfile` を基に、Ollama内にカスタムモデルを作成します。

```bash
docker exec -it ollama ollama create gemma3 -f Modelfiles/Modelfile_gemma3
```
async_chat.py内のMODEL_NAMEを"gemma3"に変更してください。（他の名前で作成したならその名前に合わせてください。）

### 4. Python環境の準備

必要なライブラリをインストールします。

```bash
pip install ollama
```

## 使用方法

### チャットの開始

以下のコマンドを実行すると、ターミナル上でチャットが始まります。

```bash
python async_chat.py
```

* **終了方法**: `exit` または `quit` と入力します。
