# test_main.py

# Імпортуємо наші функції з файлу main.py
from main import count_words, is_text_alpha

# Тест №1: Перевіряємо правильний підрахунок слів
def test_count_words():
    # Очікуємо, що у фразі "Привіт світ" буде рівно 2 слова
    assert count_words("Привіт світ") == 2
    # Очікуємо, що порожній рядок поверне 0 слів
    assert count_words("") == 0

# Тест №2: Перевіряємо аналіз тексту на літери
def test_is_text_alpha():
    # Текст без цифр має повернути True
    assert is_text_alpha("Тільки літери") == True
    # Текст із цифрами має повернути False
    assert is_text_alpha("Літери та цифри 123") == False