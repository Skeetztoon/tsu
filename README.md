
# Объяснение скрипта с реализацией поиска "шести рукопожатий" для предмета "Скриптовые языки"

Скрипт на Python для поиска переходов между двумя статьями Википедии с глубиной не более 5 ссылок. Основан на теории "шести рукопожатий" и анализирует только внутренние ссылки в теле статьи и блоке References.

---

Для работы скрипта необходимо установить дополнительные библиотеки с помощью команды:

~~~
pip install -r requirements.txt
~~~
---

Перед запуском необходимо указать лимит на подключения.


Для запуска использовать команду:
~~~
python six.py
~~~


---

### Обновленная версия скрипта, использующая двустронний поиск, за основу взята идея из статьи [Fast Wikipedia traversal algorithm and its applications in NLP and keyphrase extraction](https://medium.com/udemy-engineering/fast-wikipedia-traversal-algorithm-and-its-applications-in-nlp-and-keyphrase-extraction-9d6ff4c4a68b)

<img width="1177" alt="Снимок экрана 2025-06-23 в 19 00 10" src="https://github.com/user-attachments/assets/8bb65107-f0d6-4759-83f7-df31d0570708" />
