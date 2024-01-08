[![Practicum.Yandex](https://img.shields.io/badge/-Practicum.Yandex-464646?style=flat&logo=Practicum.Yandex&logoColor=56C0C0&color=008080)](https://practicum.yandex.ru/)

# Парсер стандартов написания кода Python PEP

## Описание

Парсер собирает информацию с сайта [https://peps.python.org/](https://peps.python.org/). Результат работы скрипта - 2 файла:

- pep_{время_парсинга}.csv - в этом файле собраны все стандарты PEP в виде (номер, назване, статус).
- status_summary_{время_парсинга}.csv - общая сводка по статусам PEP, сколько найдено документов в каждом статусе (статус, количество) и общее количество статусов в последней строке.


## Как исполльзовать скрипт

Для использования скрипта необходимо склонировать проект из репозитория

```
git clone git@github.com:orbikadm/bs4_parser_pep.git
```
Перейти в директорию проекта
```
cd scrapy_parser_pep
```
создать виртуальное окружение
```
python -m venv venv
```
активировать виртуальное окружение
```
source venv/bin/activate
```
установть в окружение необходимые библиотеки из файла зависимостей requirements.txt
```
pip3 install -r requirements.txt
```

Всё, скрипт готов к работе

## Как запустить парсер

Для запуска парсера нужно находясь в директории проекта воспользоваться командой

```
scrapy crawl pep
```

## Над проектом работал

[Константин Упоров](https://github.com/orbikadm)

## Используемые технологии

- [Python](https://www.python.org/) версии 3.9.13;
- [Scrapy](https://scrapy.org/);
