### 📞 txt-phone-regexer ###

txt-phone-regexer — скрипт на Python 3.11+, который ищет номера телефонов в .txt файле и приводит их к формату:

+7(YYY)XXX-XX-XX

Извлекаются только уникальные номера в порядке появления.

### 🔥 Быстрый старт ###

Клонируйте репозиторий:

    git clone https://github.com/foxdusky/txt-phone-regexer
    cd txt-phone-regexer

Установите зависимости:

    pip install -r requirements.txt

Запустите скрипт, указав путь к файлу:

    python phone_regexer.py file_path.txt

### ⚙️ Что поддерживает ###

Номера в любом формате: +7 912 345 67 89, 8(912)345-67-89, 89123456789 и др.
Автоматическое приведение к стандартному виду.

### 🛠 Требования ###
Python 3.11+
