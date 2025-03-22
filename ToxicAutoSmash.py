import time 
import win32api
import random
import keyboard
import pyautogui
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController

# Settings | Настройки
enabled = False  # Script enable/disable flag | Флаг включения/выключения скрипта
toggle_button = 'num lock'  # Script on/off key | Клавиша включения/выключения скрипта
f5_button = 'f5'  # Key to activate the set 1 | Клавиша для активации набора 1
f6_button = 'f6'  # Key to activate the set 2 | Клавиша для активации набора 2
f7_button = 'f7'  # Key to activate the set 3 | Клавиша для активации набора 3
side_button_1_code = 0x06  # Code for the first side mouse button | Код первой боковой кнопки мыши
side_button_2_code = 0x05  # Code for the second side mouse button | Код второй боковой кнопки мыши
side_button_3_code = 0x04  # Code middle mouse button | Код средней кнопки мыши

current_set = 1  # # Set switch (1 - first set, 2 - second set, 3 - third set) | Переключатель наборов (1 - первый набор, 2 - второй набор, 3 - третий набор)

# Keyboard shortcuts for the first set | Комбинации клавиш для первого набора
set1_scm = [('4', 0.3), ('e', 0.7), ('8', 0.5), ('3', 0.7), ('5', 0.4), ('1', 0.8), ('9', 0.5), ('6', 0.7), ('7', 0.1), ('7', 0.7), ('1', 0.8), ('5', 0.7), ('6', 0.8), ('2', 0.7), ('r', 0.7)]
set1_btn1 = [('4', 0.3), ('3', 0.7), ('5', 0.4), ('1', 0.8), ('6', 0.7), ('7', 0.1), ('7', 0.7), ('5', 0.4), ('1', 0.8), ('6', 0.7), ('2', 0.8), ('r', 0)]
set1_btn2 = [('4', 0.3), ('e', 0.7), ('8', 0.5), ('3', 0.7), ('5', 0.4), ('1', 0.8), ('9', 0.5), ('6', 0.7), ('7', 0.1), ('7', 0.7), ('1', 0.8), ('5', 0.7), ('6', 0.8), ('2', 0.7), ('r', 0.7)]

# Keyboard shortcuts for the second set | Комбинации клавиш для второго набора
set2_scm = [('4', 0.3), ('8', 0.7), ('5', 0.4), ('1', 0.8), ('6', 0.7)]
set2_btn1 = [('4', 0), ('3', 0), ('1', 0), ('2', 0), ('1', 0), ('4', 0), ('5', 0), ('6', 0), ('7', 0), ('7', 0), ('5', 0), ('5', 0)]
set2_btn2 = [('4', 0), ('3', 0), ('1', 0), ('2', 0), ('1', 0), ('4', 0), ('5', 0), ('6', 0), ('7', 0), ('7', 0)]

# Keyboard shortcuts for the third set | Комбинации клавиш для третьего набора
set3_scm = [('5', 0.3), ('w', 0.5), ('9', 0.6), ('1', 0.4), ('4', 0.3), ('8', 0.5), ('2', 0.7), ('0', 0.5), ('r', 0.6)]
set3_btn1 = [('2', 0.4), ('3', 0.6), ('6', 0.5), ('1', 0.4), ('7', 0.8), ('5', 0.6)]
set3_btn2 = [('8', 0.5), ('3', 0.4), ('0', 0.6), ('5', 0.7), ('2', 0.4)]

# Initialize controllers for mouse and keyboard | Инициализация контроллеров для мыши и клавиатуры
mouse = MouseController()
keyboard_ctrl = KeyboardController()

def is_button_pressed(button_code):
    """Checks if the side mouse button is pressed by its code | Проверяет, нажата ли боковая кнопка мыши по её коду"""
    return win32api.GetKeyState(button_code) < 0

def perform_key_combination(keys, button_code):
    """The keys are triggered with delays: fixed or random. | Выполняет комбинацию клавиш с задержками: фиксированными или случайными"""
    for key, delay in keys:
        if not is_button_pressed(button_code):
            break

        if key == 'left_click':
            pyautogui.click(button='left')
        elif key == 'right_click':
            pyautogui.click(button='right')
        else:
            keyboard_ctrl.press(key)
            keyboard_ctrl.release(key)

        if delay == 0:
            random_delay = random.uniform(0.3, 0.5)
            time.sleep(random_delay)
        else:
            time.sleep(delay)

# Basic execution cycle | Основной цикл выполнения комбинации клавиш
print("Script started! | Скрипт запущен!")
print("Disabled | Отключен" if not enabled else "Enabled | Включен")

last_state = False
last_f5_state = False
last_f6_state = False
last_f7_state = False

try:
    while True:
        key_down = keyboard.is_pressed(toggle_button)
        if key_down != last_state:
            last_state = key_down
            if last_state:
                enabled = not enabled
                print("Script enable | включен" if enabled else "Script disable | отключен")

        f5_pressed = keyboard.is_pressed(f5_button)
        if f5_pressed and not last_f5_state:
            current_set = 1
            last_f5_state = True
            print("Set 1 activated | Набор 1 активирован")
        elif not f5_pressed:
            last_f5_state = False

        f6_pressed = keyboard.is_pressed(f6_button)
        if f6_pressed and not last_f6_state:
            current_set = 2
            last_f6_state = True
            print("Set 2 activated | Набор 2 активирован")
        elif not f6_pressed:
            last_f6_state = False

        f7_pressed = keyboard.is_pressed(f7_button)
        if f7_pressed and not last_f7_state:
            current_set = 3
            last_f7_state = True
            print("Set 3 activated | Набор 3 активирован")
        elif not f7_pressed:
            last_f7_state = False

        if enabled:
            if current_set == 1:
                if is_button_pressed(side_button_1_code):
                    perform_key_combination(set1_btn1, side_button_1_code)
                if is_button_pressed(side_button_2_code):
                    perform_key_combination(set1_btn2, side_button_2_code)
                if is_button_pressed(side_button_3_code):
                    perform_key_combination(set1_scm, side_button_3_code)

            elif current_set == 2:
                if is_button_pressed(side_button_1_code):
                    perform_key_combination(set2_btn1, side_button_1_code)
                if is_button_pressed(side_button_2_code):
                    perform_key_combination(set2_btn2, side_button_2_code)
                if is_button_pressed(side_button_3_code):
                    perform_key_combination(set2_scm, side_button_3_code)

            elif current_set == 3:
                if is_button_pressed(side_button_1_code):
                    perform_key_combination(set3_btn1, side_button_1_code)
                if is_button_pressed(side_button_2_code):
                    perform_key_combination(set3_btn2, side_button_2_code)
                if is_button_pressed(side_button_3_code):
                    perform_key_combination(set3_scm, side_button_3_code)

        time.sleep(0.001)
except KeyboardInterrupt:
    print("Script stopped by user. | Скрипт остановлен пользователем.")
