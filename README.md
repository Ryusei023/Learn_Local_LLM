# Learn_Local_LLM

このプロジェクトは、Dockerを使用してローカル環境（CPUのみ）でLLM（Gemma-3-1b）を動かし、Pythonから非同期でチャットを行うためのサンプルです。

## 構成

* **Ollama**: Docker上で動作するLLM推論エンジン
* **Gemma-3-1b**: Googleが提供する軽量なLLM（GGUF版）
* **Python Client**: `ollama` ライブラリを使用した非同期チャットUI

## ディレクトリ構成

```text
.
├── compose.yaml                 # Docker Composeファイル
├── Modelfile                  　# モデルの設定とペルソナ定義
├── async_chat.py              　# Pythonチャットクライアント
├── README.md                  　# このファイル
└── gemma-3-1b-it-qat-q4_0-gguf　# ダウンロードしたモデルファイル

```

## セットアップ手順

### 1. モデルの準備

Hugging FaceからGGUFモデルファイルをダウンロードしてください。
* モデル: `gemma-3-1b-it-qat-q4_0-gguf`

おすすめの手順はHugging Faceのトークンを利用してダウンロードする方法です。
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
docker exec -it ollama ollama create gemma-3-1b -f Modelfile
```

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
