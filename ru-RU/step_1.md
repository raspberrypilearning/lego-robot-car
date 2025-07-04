## Введение

Используй LEGO® и плату Raspberry Pi Build HAT, чтобы построить автомобиль-робот, а затем запрограммируй его, чтобы ты мог управлять им с помощью Bluetooth-соединения со своего телефона Android. Затем добавь светодиоды, чтобы ослепить своих друзей.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">Название [Bluetooth](https://ru.wikipedia.org/wiki/Bluetooth)</span> было предложено в 1997 году Джимом Кардачем из Intel. Во время этого предложения он читал исторический роман Франца Г. Бенгтссона «Длинные корабли» о викингах и датском короле 10-го века Гарольде Блютузе. Блютуз (Bluetooth) было прозвищем короля Гарольда, и он объединил датские племена в единое королевство, точно так же, как Bluetooth объединяет протоколы связи.
</p>

Ты будешь:
+ Управлять двигателями LEGO® Technic™ с помощью Raspberry Pi Build HAT
+ Использовать Bluetooth для отправки сигналов на Raspberry Pi
+ Узнаешь, как управлять светодиодами с помощью библиотеки gpiozero на Raspberry Pi

--- no-print ---

![Фотография готового бота на колесах LEGO® с Raspberry Pi и Build HAT, установленными по центру. В верхней части стека находится макетная плата с проводами, прикрепленными к светодиодам.](images/lego-bot.gif)

--- /no-print ---

Ты построишь машину с колесами. Его движение будет определяться двумя отдельно ведущими колесами, расположенными по обе стороны от автомобиля, что позволяет ему двигаться вперед, назад и разворачиваться. При желании ты можешь добавить в автомобиль светодиоды, которые будут действовать как стоп-сигналы, индикаторы или фары.

--- print-only ---

![Завершенный проект.](images/buggy.JPG)

--- /print-only ---

### Тебе понадобится

+ Компьютер Raspberry Pi с последней настольной версией операционной системы Raspberry Pi
+ Плата Raspberry Pi Build HAT
+ 2× двигателя LEGO® Technic™
+ Детали LEGO®, включая 2 колеса (мы использовали детали из [набора LEGO® Education SPIKE™ Prime](https://education.lego.com/en-gb/product/spike-prime))
+ Мобильный телефон или планшет на базе ОС Android
+ 5× батареек AA и батарейный отсек с гнездом цилиндрической формы

### Программное обеспечение

+ Библиотека Python Build HAT для управления платой Build HAT
+ Библиотека Python Blue Dot и приложение Blue Dot для Android
+ библиотека Python gpiozero


--- collapse ---
---
title: Дополнительная информация для преподавателей
---

Ты можешь скачать завершенный проект [здесь](https://rpf.io/p/ru-RU/bt-robot-car-go).

Если вы хотите напечатать этот проект, то воспользуйтесь [версией для печати](https://projects.raspberrypi.org/ru-RU/projects/bt-robot-car/print){:target="_blank"}.

--- /collapse ---

Прежде чем ты начнешь, тебе необходимо настроить твой компьютер Raspberry Pi и подключить свою плату Build HAT:

--- task ---

Установи Raspberry Pi на Cтроительную Пластину LEGO с помощью болтов и гаек M2, убедившись, что Raspberry Pi лежит на стороне пластины без «борта»:

 ![Raspberry Pi прикрученный к пурпурной Строительной Панели LEGO.](images/build_11.jpg)

--- /task ---

Установка Raspberry Pi таким образом обеспечивает легкий доступ к портам, а также к слоту для SD-карты. Строительная Платформа позволит тебе более легко подключить Raspberry Pi к основной структуре вашей панели инструментов.

--- task ---

Совмести плату Build HAT с Raspberry Pi, убедившись, что ты видишь надпись на английском `This way up`. Убедись, что все контакты GPIO закрыты платой HAT, и с усилием надави на плату. (В примере используется [проводные клеммы](https://www.adafruit.com/product/2223){:target="_blank"}, которые делают выводы длиннее)

![Изображение контактов GPIO, торчащих из верхней части платы Build HAT.](images/build_15.jpg) ![Анимация, показывающая установку платы Buildhat подходит для Raspberry Pi](images/haton.gif)

--- /task ---

Теперь ты должен подать питание на Raspberry Pi с помощью цилиндрического разъема 7,5 В на плате Build HAT, что позволит тебе использовать двигатели.

--- task ---

Если ты еще этого не сделал, настрой Raspberry Pi, следуя этим инструкциям:

[Настройка твоей Raspberry Pi](https://projects.raspberrypi.org/ru-RU/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

После загрузки Raspberry Pi открой Инструмент Настройки Raspberry Pi, нажав кнопку Меню Raspberry и выбрав «Настройки», а затем «Конфигурация Raspberry Pi».

Выбери вкладку «Интерфейсы» и настрой параметры последовательного порта, как показано ниже:

![Изображение, показывающее экран конфигурации ОС Raspberry Pi с включенным последовательным портом и отключенной последовательной консолью](images/configshot.jpg)

--- /task ---

--- task ---

Тебе также понадобится установить библиотеку Python buildhat, следуя этим инструкциям:

--- collapse ---
---
title: Установка библиотеки Python buildhat
---

Откройте окно терминала на Raspberry Pi, нажав <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.

В командной строке введи: `sudo pip3 install buildhat`

Нажми <kbd>Ввод</kbd> и дождись сообщения «установка завершена» (или «installation completed» на английском).

--- /collapse ---

--- /task ---