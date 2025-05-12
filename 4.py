
class MusicalInstrument:
    """
    Класс, представляющий музыкальный инструмент.
    """
    instrument_type: str = "Generic"  # Атрибут класса: тип инструмента 
    origin_country: str = "Unknown"  # Атрибут класса: страна происхождения

    def __init__(self, name: str, manufacturer: str, year_made: int, material: str, is_electronic: bool) -> None:
        """
        Инициализирует объект MusicalInstrument.

        Args:
            name: Название инструмента.
            manufacturer: Производитель.
            year_made: Год выпуска.
            material: Материал изготовления.
            is_electronic: Является ли инструмент электронным.
        """
        self.name = name
        self.manufacturer = manufacturer
        self.year_made = year_made
        self.material = material
        self.is_electronic = is_electronic

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"{self.name} by {self.manufacturer} ({self.year_made})"

    def play(self, notes: List[str] = None) -> None:
        """
        Simulates playing the instrument.

        Args:
            notes: Список нот для воспроизведения (необязательный).
        """
        if notes:
            print(f"Playing {', '.join(notes)} on the {self.name}")
        else:
            print(f"Playing the {self.name}")

    def get_age(self, current_year: int) -> int:
        """
        Calculates the age of the instrument.

        Args:
            current_year: Текущий год.

        Returns:
            Возраст инструмента.
        """
        return current_year - self.year_made

    def is_antique(self) -> bool:
        """
        Checks if the instrument is over 100 years old.

        Returns:
            True, если инструмент старше 100 лет, иначе False.
        """
        return self.get_age(2024) > 100

    def change_manufacturer(self, new_manufacturer: str) -> None:
        """
        Changes the instrument's manufacturer.

        Args:
            new_manufacturer: Новое название производителя.
        """
        self.manufacturer = new_manufacturer

    def __eq__(self, other: object) -> bool:
        """
        Сравнивает два инструмента по названию, производителю и году выпуска.
        """
        if not isinstance(other, MusicalInstrument):
            return False
        return (self.name == other.name and
                self.manufacturer == other.manufacturer and
                self.year_made == other.year_made)


# Создание объектов
guitar = MusicalInstrument("Electric Guitar", "Fender", 2020, "Wood", True)
piano = MusicalInstrument("Grand Piano", "Yamaha", 1980, "Wood", False)
violin = MusicalInstrument("Violin", "Stradivarius", 1720, "Wood", False)

# Использование методов
print(guitar)  # Вывод: Electric Guitar by Fender (2020)
print(piano.get_age(2024))  # Вывод: 44
print(violin.is_antique())  # Вывод: True
guitar.play(["C", "D", "E"])  # Вывод: Playing C, D, E on the Electric Guitar
piano.change_manufacturer("Steinway & Sons")
print(piano)  # Вывод: Grand Piano by Steinway & Sons (1980)

# Проверка __eq__
violin2 = MusicalInstrument("Violin", "Stradivarius", 1720, "Wood", False)
print(violin == violin2) # Вывод: True
print(guitar == piano) # Вывод: False

ChatGPT4 | Midjourney, [4 мая 2025 г., 22:01:28]:
Описание кода:
...
