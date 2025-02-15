if __name__ == "__main__":
    class Entity:
        """
        Базовый класс для сущностей.
        """

        def __init__(self, name: str):
            """
            Конструктор класса Entity.
            :param name: Название сущности.
            """
            self.name = name

        def info(self) -> str:
            return f"Сущность: {self.name}"

        def __str__(self) -> str:
            return self.info()

        def __repr__(self) -> str:
            return f"Сущность(name={self.name})"
    pass


    class Tree(Entity):
        """
        Дочерний класс для хвойных деревьев.
        """

        def __init__(self, name: str, type: str):
            """
            Конструктор класса Tree.
            :param name: Название хвойного дерева.
            :param type: Вид хвойного дерева.
            """
            super().__init__(name)
            self.type = type

        def info(self) -> str:
            """
            Перегруженный метод для отображения информации о дереве.
            Этот метод переопределяет базовый метод info, чтобы предоставить
            более детальную информацию о конкретном типе сущности (дереве), включая его тип.
            """
            return f"Дерево: {self.type} {self.name}"

        def Purchase(self, money: int) -> str:
            """
            Метод для продажи хвойных дереьев.
            :param money: Цена хвойного дерева.
            :return: Сообщение о расценке хвойного дерева.
            """
            return f"{self.type} {self.name} стоит {money} рублей."

        def __str__(self) -> str:
            return f"Дерево: {self.type} {self.name}"

        def __repr__(self) -> str:
            return f"Дерево(name={self.name}, вид={self.type})"