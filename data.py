from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestData():
    bun = Bun('с кунжутом', 10.80)

    ingredient_1 = Ingredient('начинка', 'котлета куриная', 20.50)
    ingredient_2 = Ingredient('начинка', 'салат', 5.00)
    ingredient_3 = Ingredient('соус', 'горчица', 10.00)
    ingredient_4 = Ingredient('соус', 'кетчуп', 10.10)


    one_bun_one_ingredient = [bun,[ingredient_1],42.10]
    one_bun_none_ingredient = [bun, [], 21.60]
    one_bun_some_ingredients = [bun, [ingredient_1, ingredient_2, ingredient_3],57.10]

    one_bun_one_ingredient_receipt = [bun, [ingredient_1], """(==== с кунжутом ====)
= начинка котлета куриная =
(==== с кунжутом ====)

Price: 42.1"""]
    one_bun_none_ingredient_receipt = [bun, [], """(==== с кунжутом ====)
(==== с кунжутом ====)

Price: 21.6"""]
    one_bun_some_ingredients_receipt = [bun, [ingredient_1, ingredient_2, ingredient_3], """(==== с кунжутом ====)
= начинка котлета куриная =
= начинка салат =
= соус горчица =
(==== с кунжутом ====)

Price: 57.1"""]
