# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Tube:
    """
        Документация на класс.
        Класс описывает модель втулки.
    """

    def __init__(self, height: float, radius: float):
        """
         Создание и подготовка к работе объекта Втулка.
         :param height: высота втулки
         :param radius: радиус втулки
         Примеры:
         >>> tube = Tube(90.0, 5.0)  # инициализация экземпляра класса
         """

        if not isinstance(height, float):
            raise TypeError("Высота втулки должна быть типа float")
        if height <= 0:
            raise ValueError("Высота втулка должна быть положительным числом")
        self.height = height

        if not isinstance(radius, float):
            raise TypeError("Радиус должен быть float")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def sqare(self):
        """
                Функция которая позволяет вычислить площадь втулки
                :return: Площадь втулки
                Примеры:
                >>> tube = Tube(60.0, 8.0)
                >>> tube.sqare()
        """
        ...

    def new_density(self, new_height: float) -> float:
        """
            Функция, которая позволяет вычислить новую плотность втулки для заданной высоты и такого же радиуса
            :return: Плотность втулки
            Примеры:
            >>> tube = Tube(60.0, 8.0)
            >>> tube.new_density(40.0)
        """
        if new_height <= 0:
            raise ValueError("Высота втулки должна быть положительным числом")
        ...
class Dragon:
    """
        Документация на класс.
        Класс описывает модель дракона.
    """

    def __init__(self, length: float, age: int):
        """
         Создание и подготовка к работе объекта Дракон.
         :param length: длина дракона
         :param age: возраст дракона
         Примеры:
         >>> dragon = Dragon(210.4,6)  # инициализация экземпляра класса
         """

        if not isinstance(length, float):
            raise TypeError("Длина дракона должно быть типа float")
        if length <= 0:
            raise ValueError("Длина дракона должно быть быть положительным числом")
        self.length = length

        if not isinstance(age, int):
            raise TypeError("Возраст дракона внутри должно быть типа int")
        if age <= 0:
            raise ValueError("Возраст дракона внутри быть быть положительным числом")
        self.age = age

    def height(self) -> float:
        """
                Функция которая позволяет вычислить высоту Дракона
                :return: Высота дракона
                Примеры:
                >>> dragon = Dragon(210.4,6)
                >>> dragon.height()
        """
        ...

    def hunger(self) -> bool:
        """
        Функция которая проверяет является ли дракон голодным
        :return: Является ли дракон глодным
        Примеры:
        >>> dragon = Dragon(210.4,6)
        >>> dragon.hunger()
        """
        ...

class FTech:
    """
        Документация на класс.
        Класс описывает модель компании 4Tech.
    """

    def __init__(self, people: int, salary: int):
        """
         Создание и подготовка к работе объекта компания 4Tech.
         :param people: количество людей в компании 4Tech
         :param salary: Средняя зарплата в компании 4Tech
         Примеры:
         >>> fTech = FTech(1235410,30570)  # инициализация экземпляра класса
         """

        if not isinstance(people, int):
            raise TypeError("Количество людей в компании 4Tech должно быть типа int")
        if people <= 0:
            raise ValueError("Количество людей в компании 4Tech должно быть положительным числом")
        self.people = people

        if not isinstance(salary, int):
            raise TypeError("Средняя зарплата в компании 4Tech должно быть типа int")
        if salary <= 0:
            raise ValueError("Средняя зарплата в компании 4Tech должно быть положительным числом")
        self.salary = salary

    def sum_salary(self) -> float:
        """
                Функция которая позволяет вычислить примерную сумму всех зарплат сотрудников компании 4Tech
                :return: Примерная сумма всех зарплат сотрудников компании 4Tech
                Примеры:
                >>> fTech = FTech(1235410,30570)
                >>> fTech.sum_salary()
        """
        ...

    def is_exceed_sum(self, new_salary: int) -> bool:
        """
        Функция которая проверяет разницу примерных сумма всех зарплат при повышении средней зарплаты сотрудников компании 4Tech
        :return: Привысила ли примерная сумма всех зарплат разницу в 5 процентов
        Примеры:
        >>> fTech = FTech(1235410,30570)
        >>> fTech.is_exceed_sum(20647)
        """
        if not isinstance(new_salary, int):
            raise TypeError("Новая средняя зарплата в компании 4Tech должна быть типа int")
        if new_salary <= 0:
            raise ValueError("Новая средняя зарплата в компании 4Tech должна быть положительным числом")
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()