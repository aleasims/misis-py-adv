# Неделя 8

Примеры кода асинхронного сервера тут в репозитории. Просмотрите их с целью ознакомиться с принципом. Это игрушечные примеры, которые тем не менее хорошо иллюстрируют принципы работы этих механизмов. Особенный интерес представляет асинхронность на генераторах (`server_gen.py`).

Тема "Многозадачность" вообще крайне важна. С параллельной обработкой данных вы встретитесь и в машинном обучении, и в веб-приложениях. Поэтому понимание работы процессов, потоков — это важный момент. Для программиста на Python так же важно понимать, что такое GIL и как он работает. 

Хорошо бы, чтобы после этого занятия вы могли спокойно отвечать на вопрос: "Что такое Х?", где Х — любой термин из Ключевых слов этой недели. Если у вас появились вопросы, задавайте их в личке.

Обещанная домашка по `asyncio` [тут](./HW.md).

## Ключевые слова этой недели

`parallel execution`, `concurrent execution`, `process`, `process environment`, `thread`, `multiprocessing`, `threading`, `join`, `mutex`, `queue`, `IPC`, `pipe`, `shared memory`, `GIL`, `asynchronous methods`, `cooperative multitasking`, `preemptive multitasking`, `event loop`, `coroutine`, `asyncio`

## Дополнительные материалы

На этой неделе у нас прям много годных материалов. Обязательно почитайте на досуге :)

* Очень классный [канал](https://www.youtube.com/playlist?list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8) на YouTube с короткими видео по асинхронности. Вообще рекомендую весь [канал Олега Молчанова](https://www.youtube.com/user/zaemiel/playlists), там очень много толковых уроков по Python.
* [GIL со слов Дэвида Бизли](http://www.dabeaz.com/GIL/). Очень рекомендую его [лекцию](https://www.youtube.com/watch?v=Obt-vMVdM8s) про GIL, чтобы хорошо разобраться в этой теме (а вот его [слайды](https://www.dabeaz.com/python/UnderstandingGIL.pdf)).
* [Документация](https://docs.python.org/3/library/asyncio.html) по `asyncio` — библия будущего асинхронного кода на Python.
* Очень годная [статья](https://realpython.com/async-io-python/) с введением в асинхронность. Объясняются основные идеи и даются примеры кода. Поскольку эта тема у нас почти что на самостоятельном изучении, это первая статья, которую я рекомендую прочитать.
* [Статья](https://www.geeksforgeeks.org/inter-process-communication-ipc/?ref=lbp) про IPC — очень доступно объясняются приципы работы.
* [Статья](https://medium.com/@avneesh.chadha/python-tutorial-speed-up-your-io-operations-with-futures-in-python-51ccd027284c) с введением в `futures` — очень интересная штука. Там разбирается практически такой же код, как мы писали на семинаре (`multitask_fetch.py`), но с использованием Executor-ов. Очень рекомендую к прочтению!
* Еще одна [статья](https://medium.com/@ageitgey/quick-tip-speed-up-your-python-data-processing-scripts-with-process-pools-cf275350163a) на эту же тему: как ExecutorPool-ы помогают ускорять программы, не усложняя код.
* [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/) — очень годная статья с разбором примеров распараллеливания кода приложения. Сравниваюся синхронные, многопроцессорные, многопоточные и асинхронные версии программ.
* [Документация](https://www.tornadoweb.org/en/stable/guide/intro.html) асинхронного веб-фреймворка Tornado — вдохновителя `asyncio`.
