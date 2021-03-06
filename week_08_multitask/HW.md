# Опциональное домашнее задание

Дедлайн **10 мая 23:59**, максимальный балл: **20 баллов**.

Перед тем, как приступить к выполнению задания на асинхронность, я настоятельно рекомендую ознакомиться с материалами этой недели. Там правда много годных вещей, которые помогут в понимании.

Для выполнения этого задания вам необходимо ознакомиться с темой асинхронного программирования в Python самостоятельно. Предлагаемые ресурсы для этого:

* [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
* [Лекция от Computer Science Center](https://compscicenter.ru/courses/python/2018-autumn/classes/4300/)
* [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)

Вы, разумеется, можете также изучать любые материалы, какие найдете.

## `asyncio`

Ключевые слова `async/await` дают вам возможность создавать корутины и "ожидать" их. Библиотека `asyncio` дает возможность их запускать и манипулировать ими. Все решения по использованию этой библиотеки в этом задании вам предоставляется сделать самостоятельно. У вас есть инструмент — пользуйтесь!

## Задание

На выделенном сервере размещены изображения в некотором количестве.

> IP-адрес сервера: `142.93.138.114`

Изображения находятся в директории `/images`, т.е. их адрес имеет вид `http://ip_addr/images/name.ext`

*Убедитесь, что вы можете скачать картинку по ссылке: http://142.93.138.114/images/example.jpg*

Вам необходимо написать программу, которая будет:

1. получать **список изображений** с сервера GET-запросом по адресу http://142.93.138.114/images/ (возвращает обычный текстовый файл)

2. **загружать** указанные там изображения

3. локально преобразовывать их: **отображать зеркально** относительно вертикальной оси

<img src="../img/mirror_example.png" height="300">

4. **отправлять** на сервер преобразованный вариант POST-запросом по адресу http://142.93.138.114/images/.

### Комментарии

1. Для работы с асинхронными веб-запросами есть [библиотека](https://docs.aiohttp.org/en/stable/) `aiohttp`. Она не стандартная, ее надо установить pip-ом, но является решением "по умолчанию" для асинхронных запросов. Однако выбор все также предоставляется вам.

2. Обрабатывать картинки можно любым известным вам способом. Например, это можно делать с помощью [библиотеки Pillow](https://pillow.readthedocs.io/en/stable/installation.html) (модуль `ImageOps`).

3. В ответ на ваш POST-запрос сервер должен присылать ответ 200 OK. В противном случае это значит, что что-то пошло не так при отправке.

4. Мы познакомились некоторыми вспомогательными инструментами (`argparse`, `logging`). Их использование приветствуется. Не забывайте и про обработку ошибок :)

5. Архитектура вашего приложения — также ваше решение. Рекомендуется использовать один из подходов, описанных в статье [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/): использовать очередь результатов или цепочку корутин. Т.е. вы можете:
    * пулом загрузчиков сохранять изображения в очередь, откуда их будут забирать пул обработчиков
    * загружать, обрабатывать и отправлять изображения одной цепочкой (соответственно, у вас есть пул таких цепочек).

    Подумайте, какая архитектура подходит в данном случае лучше и почему.

6. Обратите внимание: асинхронный код хорошо работает на I/O операциях! Процессорный код (например, по обработке изображения) от асинхронности почти ничего не выиграет (а может и проиграет). Подумайте, что должно выполняться асинхронно, а что нет.

Все вопросы по заданию можно задавать мне в личку.

## Отправка решения

Дедлайн: **10 мая 23:59**

Решения принимаются в виде **репозитория на GitHub** ([гайд по созданию репозитория](https://help.github.com/en/enterprise/2.16/user/github/getting-started-with-github/create-a-repo)). Создайте свой репозиторий, загрузите туда код и присылайте в личку ссылку на него. Репозиторий должен быть *публичным*, иначе я его не увижу. Отправить ссылку нужно *до дедлайна*.

Решение оценивается в **20 баллов** максимум. В критерии оценивания, как обычно, входят:

* codestyle,
* архитектура кода,

а также 

* использование асинхронности,
* использование вспомогательных бибилотек (в том числе логгирования и конфигурации параметров),
* общая структура проекта.
