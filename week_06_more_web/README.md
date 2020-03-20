# Неделя 6

Файлы из проекта, который мы сделали на семинаре, выложены здесь.

Ниже кратко прохожусь по тому, что мы сделали на семинаре и как развернуть свое приложение на Heroku.

## Ключевые слова этой недели

`cookie`, `session`, `API`, `Web Service`, `JSON`, `XML`, `SOAP`, `Web-RPC`, `Three-tier architecture`

## Дополнительные материалы

* [Про REST API](https://restfulapi.net/)
* Очень классная [статья](https://habr.com/ru/post/246699/) про реализацию RESTful API на Flask-е
* [Документация](https://devcenter.heroku.com/categories/reference) Heroku
* Ещё один [гайд](https://pybit.es/deploy-flask-heroku.html) про деплой приложения на Heroku

## Recap семинара

*(Все примеры из PowerShell)*

Что мы сделали, чтобы загрузить свое приложение на Heroku:

1. Установили `git`, `Heroku CLI`, создали аккаунт на Heroku

2. Залогинились из командной строки

```
PS> heroku login
```

3. Создали новое приложение Heroku

```
PS> heroku create
Creating app... done, ⬢ mysterious-thicket-32375
https://mysterious-thicket-32375.herokuapp.com/ | https://git.heroku.com/mysterious-thicket-32375.git
```

Первая ссылка, это ссылка на наш будущий сайт, вторая — на удаленный репозиторий, куда надо заливать код.

4. Склонировани репозиторий, который дал нам Heroku

```
PS> git clone https://git.heroku.com/mysterious-thicket-32375.git
Cloning into 'mysterious-thicket-32375'...
warning: You appear to have cloned an empty repository.
```

5. Зашли в репозиторий и создали там виртуальное окружение

```
PS> cd .\mysterious-thicket-32375\
PS mysterious-thicket-32375> py -m venv env
PS mysterious-thicket-32375> .\env\Scripts\Activate.ps1
(env) PS mysterious-thicket-32375>
```

> Те, кто делали это через PyCharm:
>
> 5.1 Создали проект, выбрав в качестве папки проекта нашу папку с репозиторием: `mysterious-thicket-32375`. Никакую другую папку! Ни выше, ни ниже, именно её!
>
> 5.2 Создали через PyCharm виртуально окружение в этой папке (см [Tools](../TOOLS.md#Создание-окружения)).

6. Создали файл `.gitignore`

```
__pycache__/
.idea/
env/
```

7. Создали Hello World приложение на Flask (см. предыдущую неделю)

8. Создали файл `requirements.txt` с зависимостями

```
flask
gunicorn
```

9. Создали файл `Procfile` с инструкциями по развертке для heroku

```
web: gunicorn hello:app
```

10. Залили все изменения в репозитории на сервер. Наше приложение при этом запустилось автоматически.

```
(env) PS mysterious-thicket-32375> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        .gitignore
        Procfile
        hello.py
        requirements.txt

nothing added to commit but untracked files present (use "git add" to track)
(env) PS mysterious-thicket-32375> git add .
(env) PS mysterious-thicket-32375> git commit -m "Initial commit"
[master (root-commit) 13d083f] Initial commit
 4 files changed, 14 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 Procfile
 create mode 100644 hello.py
 create mode 100644 requirements.txt
(env) PS C:\Users\alea\mysterious-thicket-32375> git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (6/6), 504 bytes | 168.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing python-3.6.10
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: Sqlite3 successfully installed.
remote: -----> Installing requirements with pip
remote:        Collecting flask
remote:          Downloading Flask-1.1.1-py2.py3-none-any.whl (94 kB)
remote:        Collecting gunicorn
remote:          Downloading gunicorn-20.0.4-py2.py3-none-any.whl (77 kB)
remote:        Collecting Werkzeug>=0.15
remote:          Downloading Werkzeug-1.0.0-py2.py3-none-any.whl (298 kB)
remote:        Collecting itsdangerous>=0.24
remote:          Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
remote:        Collecting Jinja2>=2.10.1
remote:          Downloading Jinja2-2.11.1-py2.py3-none-any.whl (126 kB)
remote:        Collecting click>=5.1
remote:          Downloading click-7.1.1-py2.py3-none-any.whl (82 kB)
remote:        Collecting MarkupSafe>=0.23
remote:          Downloading MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl (27 kB)
remote:        Installing collected packages: Werkzeug, itsdangerous, MarkupSafe, Jinja2, click, flask, gunicorn
remote:        Successfully installed Jinja2-2.11.1 MarkupSafe-1.1.1 Werkzeug-1.0.0 click-7.1.1 flask-1.1.1 gunicorn-20.0.4 itsdangerous-1.1.0
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 45.1M
remote: -----> Launching...
remote:        Released v3
remote:        https://mysterious-thicket-32375.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/mysterious-thicket-32375.git
 * [new branch]      master -> master
```

11. Переходим по ссылке `https://mysterious-thicket-32375.herokuapp.com/` и убеждаемся, что наше приложение успешно развернуто.
