import random

# Приводим ответ к виду ДА или НЕТ. В функцию подается ответ уже в нижнем регистре
def is_answer_valid(word):
     if word == 'да':
          return True
     elif word == 'нет':
          return False
     else:
          return is_answer_valid(input('Пожалуйста, отвечайте только ДА или НЕТ' + '\n'))

# Проверяем, что на вход подается натуральное число, чтобы сгенерировать длину пароля
# в качестве минимальной длины сюда приходит переменная condition_counter из функции questions
def is_number_valid(num, min_lenght):
     if num.isdigit():
          num = int(num)
          if num >= min_lenght:
               return num
          else:
               return is_number_valid(input(f'Этого слишком мало, попробуйте длину побольше. Минимальное количество символов для пароля с данными условиями: {min_lenght}' + '\n'), min_lenght)
     else:
          return is_number_valid(input(f'Это не та длина, которую мы ищем. Пожалуйста, укажите желаемую длину пароля. Минимальное количество символов для пароля с данными условиями: {min_lenght}' + '\n'), min_lenght)

def questions():  # Задаем параметры для генерации пароля

     digits = '0123456789'
     lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
     uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     punctuation = '!#$%&*+-=?@^_'
     homonyms = 'il1Lo0O'
     
     flag_uppercase_letters = False
     flag_lowercase_letters = False
     flag_digits = False
     flag_punctuation = False

     condition_counter = 0
     chars = ''  # Сюда добавляем символы, которые будут использоваться при генерации

     if is_answer_valid(input('Будет ли пароль включать прописные буквы?' + '\n').lower()):
          chars += uppercase_letters
          condition_counter += 1
          flag_uppercase_letters = True
     if is_answer_valid(input('Будет ли пароль включать строчные буквы?' + '\n').lower()):
          chars += lowercase_letters
          condition_counter += 1
          flag_lowercase_letters = True
     if is_answer_valid(input('Будет ли пароль включать цифры?' + '\n').lower()):
          chars += digits
          condition_counter += 1
          flag_digits = True
     if is_answer_valid(input('Будет ли пароль включать дополнительные символы?' + '\n').lower()):
          chars += punctuation
          condition_counter += 1
          flag_punctuation = True
     if not is_answer_valid(input('Будет ли пароль включать неоднозначные символы? (Например, О и 0)' + '\n').lower()):
          for c in homonyms:  # использую переменную, чтобы все строки хранились рядом
               chars = chars.replace(c, '')

     if chars == '':
          print('Упс! Кажется, для генерации пароля не осталось подходящих символов' +
                '\n' + 'Давайте попробуем еще раз!')
          return questions()
     
     password_lenght = is_number_valid(
         input('Укажите желаемую длину пароля' + '\n'), condition_counter)
     
     password = check_password(
         password_lenght, flag_digits, flag_lowercase_letters, flag_uppercase_letters, flag_punctuation, chars)

     print(password)

     if is_answer_valid(input('Готово! Хотите сгенерировать еще один пароль?' + '\n').lower()):
          return questions()
     else:
          print('До встречи! Возвращайтесь, когда понадобится сгенерировать пароль!')

# генерируем пароль по заданным параметрам
def generate_password(password_lenght, chars):
     password = ''
     for i in range(1, password_lenght + 1):
          password += random.choice(chars)
     return password

# проверяем вхождение всех символов, которые запросил пользователь
def check_password(password_lenght, flag_digits, flag_lowercase_letters, flag_uppercase_letters, flag_punctuation, chars):
     password = generate_password(password_lenght, chars)
     flag_1, flag_2, flag_3, flag_4 = False, False, False, False
     if flag_digits:
          for c in password:
               if c in '0123456789':
                    flag_1 = True
                    break
     else:
          flag_1 = True
     if flag_lowercase_letters:
          for c in password:
               if c in 'abcdefghijklmnopqrstuvwxyz':
                    flag_2 = True
                    break
     else:
          flag_2 = True
     if flag_uppercase_letters:
          for c in password:
               if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    flag_3 = True
                    break
     else:
          flag_3 = True
     if flag_punctuation:
          for c in password:
               if c in '!#$%&*+-=?@^_':
                    flag_4 = True
                    break
     else:
          flag_4 = True
     if flag_1 and flag_2 and flag_3 and flag_4:
          return password
     else:
          return check_password(password_lenght, flag_digits, flag_lowercase_letters, flag_uppercase_letters, flag_punctuation, chars)



# Запускаем программу

if is_answer_valid(input('Сгенерировать пароль?' + '\n').lower()):
     questions()
else:
     print('До встречи! Возвращайтесь, когда понадобится сгенерировать пароль!')
