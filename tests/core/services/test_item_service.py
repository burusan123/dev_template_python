# -----------------------------------------------------------------------------
# サンプルコード (Sample Code)
#
# このファイルは、本テンプレートのテスト構造を理解していただくためのサンプルです。
# `tests`ディレクトリが`src`ディレクトリの構造をミラーリングする例を示します。
#
# 実際の開発を開始する際は、このファイルを削除し、ご自身のサービスのテストに
# 置き換えてください。
# -----------------------------------------------------------------------------
import pytest

from core.services.item_service import create_item
from domain.models.item import Item


def test_create_item_success() -> None:
    """商品が正常に作成されることをテストします。"""
    item = create_item(
        item_id=1,
        name="Test Item",
        price=100.0,
        description="A test item",
    )
    assert isinstance(item, Item)
    assert item.id == 1
    assert item.name == "Test Item"
    assert item.price == 100.0
    assert item.description == "A test item"


def test_create_item_invalid_price() -> None:
    """価格が不正な場合にValueErrorが発生することをテストします。"""
    with pytest.raises(ValueError, match="Price must be positive"):
        create_item(item_id=2, name="Invalid Item", price=0)

    with pytest.raises(ValueError, match="Price must be positive"):
        create_item(item_id=3, name="Invalid Item", price=-50.0)


def test_create_item_without_description() -> None:
    """商品説明がなくても商品が作成されることをテストします。"""
    item = create_item(item_id=4, name="Simple Item", price=50.0)
    assert item.description is None
    assert item.name == "Simple Item"
