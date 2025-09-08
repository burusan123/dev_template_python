# scripts/setup_mode.py
import argparse
import shutil
from pathlib import Path

# プロジェクトのルートディレクトリを取得
ROOT_DIR = Path(__file__).parent.parent


def setup_mode(mode: str) -> None:
    """pre-commitの設定ファイルを指定されたモードに切り替えます。"""
    if mode not in ["poc", "production"]:
        raise ValueError("モードは 'poc' または 'production' を指定してください。")

    src_file = ROOT_DIR / f".pre-commit-config.{mode}.yaml"
    dest_file = ROOT_DIR / ".pre-commit-config.yaml"

    try:
        shutil.copy(src_file, dest_file)
        print(f"✅ モードが '{mode}' に設定されました。")
        print(f"   '{src_file.name}' -> '{dest_file.name}'")
        print("\n[INFO] pre-commitフックを再インストールしてください:")
        print("   pre-commit install")
    except FileNotFoundError:
        print(f"❌エラー: '{src_file}' が見つかりません。")
        exit(1)
    except Exception as e:
        print(f"❌エラーが発生しました: {e}")
        exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
開発モードを切り替えます(PoCまたはProduction)。
これにより、pre-commitフックの厳格さが変更されます。
"""
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["poc", "production"],
        required=True,
        help="設定する開発モード ('poc' または 'production')",
    )
    args = parser.parse_args()
    setup_mode(args.mode)
