# Неделя 9

Полезные "штучки", которые мы упоминали:

* `flake8` — линтер, ищет стилистические и фактические ошибки
* `autopep8` — автоматическое форматирование кода
* запуск интерпретатора с командой (вместо файла)
    ```
    PS> python -c "import os; print(os.name)"
    nt
    ```
* ключ `-i` — остаться в интерактивном режиме после завершения исполнения
    ```
    PS> python -i main.py
    Hello, world!
    >>> main()
    Hello, world!
    ```
* ZeroMQ (`pyzmq`) — асинхронная библиотека передачи сообщений, message queue на socket-ах.
* OpenCV (`opencv-python`) — мощная библиотека для задач компьютерного зрения.

## Ключевые слова этой недели

`CLI`, `argparse`, `stream`, `file object`, `stdin/stdout/stderr`, `message queue`, `filter`, `pipeline`, `logging`
