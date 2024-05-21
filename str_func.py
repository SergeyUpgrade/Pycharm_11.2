def words_UP(value: str):
    """Было неправильно описано, теперь я правильно описал"""
    return value.upper()


def first_word_up(value: str):
    """Делаем заглавными первые буквы каждой строки"""
    return value.capitalize()


value = input()

print(f"{first_word_up(value)}")

