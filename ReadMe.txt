Файл 103.xlsx
Я создал этот файл для расшифровки пакетов, пердаваемых с применением протокола ГОСТ 60870-5-103.

Файлы Draft_2.py, Draft_3.py, Draft_10.py
Коллега сделал библиотеку на Python, но не написал для нее документацию.
Чтобы пользоваться данной библиотекой, я сделал несколько файлов, с помощью которых проверял работспособность библиотеки и дополнял нужными комментариями.

Work.postman_collection.json
Коллекция методов (Postman) была создана для замены ручного ввода многочисленных параметров через веб-интерфейс перед ручными тестами.
Применение позволило избежать многочисленных ошибок при ручном вводе на подготовительном этапе.

TEST.postman_collection.json
Коллекция методов (Postman) создавалась по мере необходимости для работы или в учебных целях. 

prot_events_to_txt.py
Скрипт был сделан для преобразования лога в читаемый(более привычный) формат.

Test current input.py
Скрипт был создан для отслеживания состояния виртуального канала.

Translation_conflicts_v_01.py
Скрипт просматривает лог событий, фильтрует критические сообщения и проверяет появились (или нет) критические сообщения за последний час за последний час.
Данный скрипт запускается автоматически каждый час на Jenkins.