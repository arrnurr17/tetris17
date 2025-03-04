# Tetris на Pygame

## Описание

Tetris – это классическая игра, в которой игрок управляет падающими фигурами (тетромино), вращая и перемещая их, чтобы заполнить ряды. Когда ряд полностью заполняется, он исчезает, а игрок получает очки.

## Установка и запуск

### 1. Клонирование репозитория

Скачайте проект с GitHub:

```sh
git clone https://github.com/arrnurr17/tetris17.git

```

### 2. Установка зависимостей

Перед запуском установите Pygame, если он не установлен:

```sh
pip install -r requirements.txt
```

Если файла `requirements.txt` нет, установите Pygame вручную:

```sh
pip install pygame
```

### 3. Запуск игры

Выполните команду:

```sh
python main.py
```

## Управление

- **Стрелка влево (←)** – перемещение влево
- **Стрелка вправо (→)** – перемещение вправо
- **Стрелка вниз (↓)** – ускоренное падение
- **Стрелка вверх (↑)** – вращение
- **Пробел** – мгновенный сброс фигуры
- **P** – пауза
- **R** – рестарт игры

## Структура проекта

```
Tetris/
│── main.py         # Главный файл запуска игры
│── requirements.txt # Список зависимостей
│── tetris/
│   ├── game.py     # Основная логика игры
│   ├── constants.py # Константы (размеры, цвета, управление)
│   ├── tetrimino.py # Класс тетромино
│   ├── ui.py       # Отображение интерфейса
```

## Особенности

✔️ Классический геймплей Tetris
✔️ Гибкое управление
✔️ Отображение следующей фигуры
✔️ Поддержка паузы и перезапуска
✔️ Адаптивная сложность (ускорение с уровнями)

Приятной игры! 🎮

 
