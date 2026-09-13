# CLAUDE.md

このファイルは、このリポジトリで作業する Claude Code (claude.ai/code) への指針を提供する。

## プロジェクト概要

画像アセット自動生成のルール・スクリプト（Gemini / Nano Banana）を検証するためのサンドボックスプロジェクト。`scripts/generate_image.py` を bash から直接呼ぶ方式と、GitHub Actions ワークフロー経由でリポジトリに画像をコミットする方式の両方を持つ。

`build-app` という個人ワークスペース内の1プロジェクトとして管理されているが、それ自体は独立した git リポジトリ。**PC全体で共有されている `generate-illustration` スキル（`~/.claude/skills/generate-illustration/`）は、このプロジェクトで検証した仕組みを土台にした現行版。** 他プロジェクトで新しく画像生成が必要な場合はスキル側を使うこと。

## 画像アセットのルール

このプロジェクトで挿絵・背景画像・アイコンなど新しいビジュアル素材が
必要になった場合、必ず以下の手順で自動生成すること。手描きのプレース
ホルダーやSVGでの代替は禁止。

1. `scripts/generate_image.py "<英語のプロンプト>" "<出力ファイル名>"`
   を bash で実行して画像を生成する
2. 生成先は `assets/images/` 配下に統一する
3. 生成後、コード側から相対パスで参照する
4. 生成に失敗した場合はプロンプトを調整して最大2回までリトライする

## コマンド

- **ローカル生成**: `python scripts/generate_image.py "<プロンプト>" "<出力パス>"`（環境変数 `GEMINI_API_KEY` が必要。モデルは `gemini-3.1-flash-image`＝通称 Nano Banana 2）
- **GitHub Actions経由**: Actions タブ →「Generate Image」ワークフロー → `prompt` と `output_path` を指定して実行（`GEMINI_API_KEY` は `Gemini_API` environment のシークレットから読む）
- **ビルド／lint／テスト**: 該当コマンド無し。

## 注意事項

- `GEMINI_API_KEY` はワークフローのシークレットまたはローカル環境変数として渡し、コードにハードコードしないこと。
