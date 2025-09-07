# -----------------------------------------------------------------------------
# サンプルコード (Sample Code)
#
# このファイルは、本テンプレートのアーキテクチャを理解していただくためのサンプルです。
# `domain`層にビジネスオブジェクト(モデル)を配置する例を示します。
#
# 実際の開発を開始する際は、このファイルを削除し、ご自身のドメインモデルに
# 置き換えてください。
# -----------------------------------------------------------------------------
from pydantic import BaseModel, Field


class Item(BaseModel):
    """商品データを表すドメインモデル。"""

    id: int = Field(..., description="商品ID")
    name: str = Field(..., min_length=1, description="商品名")
    price: float = Field(..., gt=0, description="価格(0より大きい必要があります)")
    description: str | None = Field(None, description="商品説明")
