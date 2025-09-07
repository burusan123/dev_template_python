# -----------------------------------------------------------------------------
# サンプルコード (Sample Code)
#
# このファイルは、本テンプレートのアーキテクチャを理解していただくためのサンプルです。
# `core`層にビジネスロジック(サービス)を配置する例を示します。
#
# 実際の開発を開始する際は、このファイルを削除し、ご自身のドメインサービスに
# 置き換えてください。
# -----------------------------------------------------------------------------
from domain.models.item import Item


def create_item(item_id: int, name: str, price: float, description: str | None = None) -> Item:
    """
    新しい商品インスタンスを作成します。

    Args:
        item_id: 商品ID
        name: 商品名
        price: 価格
        description: 商品説明

    Returns:
        新しいItemインスタンス

    Raises:
        ValueError: 価格が0以下の場合
    """
    if price <= 0:
        raise ValueError("Price must be positive")
    return Item(id=item_id, name=name, price=price, description=description)
