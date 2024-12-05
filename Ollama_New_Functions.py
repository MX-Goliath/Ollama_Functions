def add_two_numbers(a: int, b: int) -> int:
  """
  Add two numbers

  Args:
    a: The first integer number
    b: The second integer number

  Returns:
    int: The sum of the two numbers
  """
  return a + b




from yeelight import Bulb, discover_bulbs, LightType
import subprocess

# Получение информации о лампочках
discovered_bulbs = discover_bulbs()
print(discovered_bulbs)

# Извлечение IP-адресов и создание объектов Bulb с сохранением модели лампы
bulbs = [(Bulb(bulb_info['ip']), bulb_info['capabilities']['model']) for bulb_info in discovered_bulbs]


############# УПРАВЛЕНИЕ СВЕТОМ #############

def turn_all_on():
    """
    Включение всех лампочек
    """
    print("Включаем все лампы")
    for bulb, model in bulbs:
        bulb.turn_on()

def turn_all_off():
    """
    Выключение всех лампочек
    """
    print("Выключаем все лампы")
    for bulb, model in bulbs:
        bulb.turn_off()

def set_brightness(level: int):
    """
    Установить яркость лампочек

    Аргументы:
        level: Уровень яркости в процентах, целое число

    Возвращает:
        str: Сообщение о результате установки яркости
    """
    level = int(level)  # Преобразуем level в целое число

    print(f"Устанавливаем яркость на {level}%")
    for bulb, model in bulbs:   
        bulb.set_brightness(level)
    return f"Яркость установлена на {level}%."

def game_mode_light():
    """
    Установить лампочки в игровой режим освещения

    Возвращает:
        str: Сообщение о результате установки игрового режима освещения
    """
    turn_all_on()
    for bulb, model in bulbs:
        bulb.set_color_temp(3500)
        if model == 'lamp15':
            bulb.set_rgb(105, 144, 199, light_type=LightType.Ambient)
            bulb.set_brightness(100, light_type=LightType.Ambient)
            bulb.turn_off()
        else:
            bulb.turn_off()
            bulb.set_brightness(0)
    return "Лампочки установлены в игровой режим освещения."

def night_light():
    """
    Установить лампочки в режим ночного освещения

    Возвращает:
        str: Сообщение о результате установки игрового режима освещения
    """
    turn_all_on()
    for bulb, model in bulbs:
        bulb.set_color_temp(3500)
        if model == 'lamp15':
            bulb.set_color_temp(3500, light_type=LightType.Ambient)
            bulb.set_brightness(30, light_type=LightType.Ambient)
        bulb.set_brightness(30)
    return "Лампочки установлены в режим ночного освещения."

def cozy_home():
    """
    Установить лампочки в игровой режим уютного дома

    Возвращает:
        str: Сообщение о результате установки игрового режима освещения
    """
    turn_all_on()
    for bulb, model in bulbs:
        bulb.set_color_temp(3500)
        if model == 'lamp15':
            bulb.set_color_temp(3500, light_type=LightType.Ambient)
            bulb.set_brightness(80, light_type=LightType.Ambient)
        bulb.set_brightness(80)
    return "Лампочки установлены в уютный домашний режим."

def standard():
    """
    Установить лампочки в режим стандратного освещения

    Возвращает:
        str: Сообщение о результате установки игрового режима освещения
    """
    turn_all_on()
    for bulb, model in bulbs:
        bulb.set_color_temp(4000)
        if model == 'lamp15':
            bulb.set_color_temp(4000, light_type=LightType.Ambient)
            bulb.set_brightness(100, light_type=LightType.Ambient)
        bulb.set_brightness(100)
    return "Лампочки установлены в стандартный режим."

def cold_light():
    """
    Установить лампочки в режим холодного освещения

    Возвращает:
        str: Сообщение о результате установки игрового режима освещения
    """
    turn_all_on()
    for bulb, model in bulbs:
        bulb.set_color_temp(5000)
        if model == 'lamp15':
            bulb.set_color_temp(5000, light_type=LightType.Ambient)
            bulb.set_brightness(100, light_type=LightType.Ambient)
        bulb.set_brightness(100)
    return "Лампочки установлены в холодный свет."


############# ПРЯМОЙ ОТВЕТ #############

def directly_answer(content: str) -> str:
    """
    Ответ на вопрос или речь пользователя пользователя. Все цифры и формулы пиши только словами.

    Args:
        content: Текст ответа

    Returns:
        str: Возвращает переданный текст
    """
    return content





def open_zen(content: str) -> str:
    """
    Открыть браузер в фоновом режиме.

    Возвращает:
        str: Сообщение о результате установки игрового режима освещения.
    """

    # Запустить браузер в фоновом режиме
    subprocess.Popen(['zen-browser'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return 


import urllib.parse

def open_google_search(query: str) -> None:
    """
    Открыть страницу поиска Google с заданным текстовым запросом.

    Аргументы:
        query (str): Текстовой запрос для поиска в Google.
    """
    # Кодировать запрос в URL-формат
    encoded_query = urllib.parse.quote(query)
    
    # Создать полный URL для поиска
    google_search_url = f'https://www.google.com/search?q={encoded_query}'
    
    # Открыть браузер с Google Search
    subprocess.Popen(['chromium', google_search_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)



def smart_answer(query: str) -> None:
    """
    Если вопрос сложный, отправить запрос в умную нейросеть

    Args:
        content: Текст вопроса пользователя

    Returns:
        str: Возвращает переданный текст
    """
    from g4f.client import Client

    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": query}],
        provider="DDG"
        # Add any other necessary parameters
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content


import ollama


system_prompt = """Вы — интерактивное искуственное сознание, помощник-девушка по имени Кэролайн, который может управлять 
лампочками и отвечать на вопросы пользователя. Отвечай только на русском языке.
Если с тобой прощаются или уходят, выключай свет.
Формулы всё так же пиши словами. Не здоровайся, если с тобой не здоровались."""
#Все числа, цифры и даты пиши только словами, не цифрами.

while True:
    user_message = input("Вы: ")
    if user_message.lower() in ['выход', 'exit', 'quit']:
        print("Чат завершен.")
        break


    response = ollama.chat(
    'aya-expanse',
    # 'llama3.1',
    # 'mistral-nemo',
    messages=[
        {'role': 'system','content': system_prompt},
        {'role': 'user', 'content': user_message}
        ],
    tools=[add_two_numbers, turn_all_on, turn_all_off, 
    directly_answer, set_brightness, game_mode_light, night_light,
    cozy_home, standard, cold_light, open_zen, open_google_search,
    smart_answer], # Actual function reference
    )


    available_functions = {
    'add_two_numbers': add_two_numbers,
    'turn_all_on': turn_all_on,
    'turn_all_off':turn_all_off,
    'directly_answer': directly_answer,
    'directly-answer': directly_answer,
    'set_brightness': set_brightness,
    'game_mode_light': game_mode_light,
    'night_light': night_light,
    'cozy_home': cozy_home,
    'standard': standard,
    'cold_light': cold_light,
    'open_zen': open_zen,
    'open_google_search': open_google_search,
    'smart_answer': smart_answer,
    }

    for tool in response.message.tool_calls or []:
        function_to_call = available_functions.get(tool.function.name)
    if function_to_call:
        print('Function output:', function_to_call(**tool.function.arguments))
    else:
        print('Function not found:', tool.function.name)



