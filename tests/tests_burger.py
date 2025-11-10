from unittest.mock import MagicMock
import pytest
from data import TestData
from praktikum.burger import Burger


class TestBurger:
    def test_add_new_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_get_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)

        assert (len(burger.ingredients) == 1 and
                ingredient in burger.ingredients)

    def test_remove_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = MagicMock()
        ingredient1.get_name.return_value = "Салат"
        ingredient2 = MagicMock()
        ingredient2.get_name.return_value = "Горчица"

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)  # перемещаем Салат на второй индекс
        assert burger.ingredients == [ingredient2, ingredient1]  # Порядок должен быть: Горчица, Салат


    @pytest.mark.parametrize('data', [TestData.one_bun_one_ingredient,
                             TestData.one_bun_none_ingredient,
                             TestData.one_bun_some_ingredients])
    def test_get_price(self, data):
        burger = Burger()
        burger.set_buns(data[0])

        for ingr in data[1]:
            burger.add_ingredient(ingr)

        assert burger.get_price() == data[2]


    @pytest.mark.parametrize('data', [TestData.one_bun_one_ingredient_receipt,
                                      TestData.one_bun_none_ingredient_receipt,
                                      TestData.one_bun_some_ingredients_receipt])
    def test_get_receipt(self, data):
        burger = Burger()
        burger.set_buns(TestData.bun)

        for ingr in data[1]:
            burger.add_ingredient(ingr)

        assert burger.get_receipt() == data[2]