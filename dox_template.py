from pystyle import Colors, Colorate, Center, Box
import os
import datetime
import pystyle
from pystyle import *

# Функция для очистки консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def create_dox_template():
    clear_console()
    
    pystyle.Write.Print(Box.DoubleCube("Создание шаблона докса\n"), pystyle.Colors.red_to_white, interval = 0.0005)

    # Ввод данных
    name = pystyle.Write.Input("Введите имя: ", pystyle.Colors.red_to_white, interval = 0.0005)
    age = pystyle.Write.Input("Введите возраст: ", pystyle.Colors.red_to_white, interval = 0.0005)
    dob = pystyle.Write.Input("Введите дату рождения: ", pystyle.Colors.red_to_white, interval = 0.0005)
    address = pystyle.Write.Input(f"Введите адрес: ", pystyle.Colors.red_to_white, interval = 0.0005)
    phone = pystyle.Write.Input("Введите номер телефона: ", pystyle.Colors.red_to_white, interval = 0.0005)
    email = pystyle.Write.Input("Введите электронную почту: ", pystyle.Colors.red_to_white, interval = 0.0005)
    card_number = pystyle.Write.Input("Введите номер карты: ", pystyle.Colors.red_to_white, interval = 0.0005)
    social_media = pystyle.Write.Input("Введите ссылки на социальные сети: ", pystyle.Colors.red_to_white, interval = 0.0005)
    additional_info = pystyle.Write.Input("Введите дополнительную информацию: ", pystyle.Colors.red_to_white, interval = 0.0005)

    # Создание шаблона
    template = f"""
    ------------------------------
    DOX Template
    ------------------------------
    Name: {name}
    Age: {age}
    Date of Birth: {dob}
    Address: {address}
    Phone: {phone}
    Email: {email}
    Card Number: {card_number}
    Social Media: {social_media}
    Additional Info: {additional_info}
    ------------------------------
    """
    
    # Сохранение в файл
    file_count = len([f for f in os.listdir('.') if f.startswith('dox_template') and f.endswith('.txt')])
    filename = f'dox_template{file_count + 1}.txt'
    
    with open(filename, 'w') as file:
        file.write(template)
    
    pystyle.Write.Print(template, pystyle.Colors.red_to_white, interval = 0.0005)
    pystyle.Write.Print(f"\nШаблон сохранён в файл {filename}", pystyle.Colors.red_to_white, interval = 0.0005)

    pystyle.Write.Input("\nНажмите Enter для возврата в меню...", pystyle.Colors.red_to_white, interval = 0.0005)

if __name__ == "__main__":
    create_dox_template()
