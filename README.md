# Docker Homework

проект, генерирующий CSV и HTML отчёты

## Описание проекта:
* **`Generator`** - генерирует файл `data.csv`
* **`Reporter`** - читает `data.csv` и создаёт HTML отчёт `report.html`


## Структура проекта:

HW 

|–– data 


|–– generator 

| |–– generate.py 

│ |–– Dockerfile 

|–– local_data 

|–– reporter 

| |–– report.js 

| |–– package.json 

| |–– Dockerfile 

|–– .gitignore

|–– run.sh 

 ## Команды:

**Генератор:**

Собрать образ:

`./run.sh build_generator`

Запустить генератор:

`./run.sh run_generator`

Создать данные локально:

`./run.sh create_local_data`

**Аналитик:**

Собрать образ:

`./run.sh build_reporter`

Запустить аналитика:

`./run.sh run_reporter`

**Дополнительно:**

Показать структуру проекта:

`./run.sh structure`

Очистить папку data:

`./run.sh clear_data`

Показать содержимое data из контейнера генератора:

`./run.sh inside_generator`

Показать содержимое data из контейнера аналитика:

`./run.sh inside_reporter`


*После выполнения команд* `./run.sh run_generator` *и* `./run.sh run_reporter` *в* `data` *появляются файлы с отчётами:* `data.csv` *и* `report.html`

## Автор

Голубцова Анастасия ББИ2501