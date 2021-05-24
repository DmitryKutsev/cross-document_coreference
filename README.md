
# Извлечение кросс-текстовой анафоры из русскоязычного пользовательского контента в медицинской сфере.

# Cross-document anaphora extraction from medicine-related content generated by Russian users.

## Вступление.

Извлечение данных из пользовательского медицинского контента - важная задача,
позволяющая решить, или упростить решение для множества задач в медицине. Такие
задачи, как извлечение отзывов, и иной информации о препаратах, или проведение
диагностики на имеющихся данных о лечении заболеваний, дополняют методики лечения.
На основе обработанных данных составляются рекомендательные и консалтинговые
системы, помогающие врачам поставить диагноз, или подобрать наиболее подходящий
препарат.
Разрешение анафоры - важная составляющая для большинства систем извлечения
данных из текстов. Анафора - зависимость между интерпретацией какой-то
одной сущности в тексте от другой, встретившейся в том же тексте ранее.
Упоминание, встретившееся первым, называют антецедентом, а следующее за ним
упоминание того же объекта - анафором. Отношения между антецедентом и анафором
можно назвать кореферентными.

Например:

  ```А кто принимал респеридон расскажите плз как у вас с либидо, было ли сильноеснижение или нет? А также очень интересно как влияет он на депрессивную составляющую..?```

Здесь местоимение “он” является анафором, и ссылается на антецедент, респеридон.

Существует близкая к разрешению анафоры задача - разрешение кореференции. Различие заключается в том, что в случае с анафорой мы рассматриваем конкретный анафор,
и подбираем для него подходящий антецедент, в случае же с разрешением кореференции мы собираем все упоминания какой-либо сущности в один кластер.

Например:

`Admin сказал(а) 19.9.2006, 0:29:
Обсуждаем препарат Тиаприд 
Может ли тиаприд вызвать головокружение, принимаю его 2й месяц?`

`Лилу сказал(а) 27.4.2008, 10:23:
Знаю, что тиапридал применяется при алкоголизме для купирования агрессивности.
Есть ли у кого-нибудь опыт применения этого препарата у пожилых людей?`
  
Здесь можно объединить Тиаприд и Тиапридал в один кластер, так как они ссылаются на один и тот же препарат.
Разрешение анафоры можно рассматривать так же как подзадачу к разрешению кореференции, кластеризовав все найденные в текстах упоминания, что так же затрагивается подробнее в этой работе.

Нахождение кореференциальных связей может применяться во множестве систем,
помимо медицинских. Например, системы машинного перевода, извлечение
именованных сущностей, классификация событий, и многие другие. 



## Типы анафоры и процесс разрешения.

Самый распостраненный тип анафоры подразумевает связи местоимения (реже существительного) с именованной сущностью, 
или упоминанием этой сущности. Такой тип анафоры называют прономинальной.

Существуют связи, в которых и анафор, и антецедент являются существительными (или, в некоторых случаях, именными группами существительного), например:

  `- “Знаю, что тиапридал применяется при алкоголизме для купирования агрессивности.
Есть ли у кого-нибудь опыт применения этого препарата у пожилых людей?”`

Различают также анафоры, находящиеся внутри одного предложения, и анафоры, члены
которых находятся в разных предложениях (интрасентенциальные, и
интерсентенциальные).
В основном в системах разрешения анафоры в качестве анафора рассматривают только именные группы существительных. Хотя бывают случаи,
когда в качестве антецедента выступают глагольные группы, целые предложения, или участки дискурса[1]. Также большинство исследований рассматривает анафоры с кореферентными связями в пределах нескольких предложений одного текста. 
Сами системы разрешения анафоры можно разделить на правиловые системы [5], системы на основе алгоритмов машинного обучения[7, 8], и гибридные системы[3].
Правиловые системы отбирают подходящих кандидатов в антецеденты на основании допусков и ограничений, например согласование по гендеру и числу, со-зависимость в синтаксическом дереве и т.д.[9].

Набор признаков для систем машинного обучения зачастую выглидит аналогично признакам, которые учитываются в правилах rule-based подходов:
  - морфологические признаки (род, число, падежб часть речи)
  - синтаксические (контекст, зависимости главного слова именной/прономинальной группы)
  - семантические (эмбеддинги контекста)
  - дистанционные (дистанция между словами, предложениями)

В исследованиях кореференции явно прослеживается разделение на кросс-текстовую кореференцию, и кореференцию в рамках одного текста. В кросс-текстовых методах документы расположены независимо, у них разные авторы, и соответственно отсутствует линейный порядок событий и упоминаемых сущностей. Лексически расходящиеся выражения могут быть связанными, и наоборот, лексически похожие не иметь таких связей.

В отличии от кореференции, редко можно встретить исследования кросс-текстовой анафоры, в связи с тем, что, как и было упомянуто ранее, большинство работ рассматривают связки антецедент - анафор в рамках нескольких предложений.
В случае с пользовательским контентом, этот термин приобретает актуальность, так как сообщения на форумах имеют различных авторов и зачастую могут 
содержать в себе рассуждения на совершенно различные темы, разрывая линейность текста.
В данной работе под термином "текст" мы будем иметь ввиду один(??) пользовательский пост на форуме, и искоть кореферентные связи между анафором и антецедентом 
между постами.

## Обзор предыдущих работ
  
В основе работ по разрешению кореференции часто лежат вероятностные статистические модели (Charniak 1998), в качестве классификаторов используются (если рассматривать классические методы машинного обучения), такие модели, как деревья решений или логистическая регрессия.

Здесь можно выделить два основных подхода - бинарная классификация и ранжирование. Основное различие заключается в том, что при определении антецедента, ранжирование учитывает уже имеющиеся в одном классе с анафорой антецеденты, а бинарная классификация рассматривает только один конкретный антецедент и одну анафору, не учитывая других связей при принятии решения.
В качестве классификаторов используются (если рассматривать классические методы машинного обучения), такие модели, как Деревья решений или Логистическая регрессия. Также в последнее время част встречаются модели на основе алгоритмов глубокого обучения, таких как LSTM, BERT и ELMO[10, 11, 12]*как-то сделать тут референс получше*.

Встречается множество исследований [Lee et al. (2012), Barhom S. (2019)], описывающих разрешение кросс-текстовой кореференции, в то время как разрешение анафоры, в основном, описывается с учетом дистанции в несколько предложений между анафором и антецедентом.
Исследования по снятию кореференции и анафоры часто путают, но различия имеются. Под разрешением кореференции в основном имеют ввиду кластеризацию именованных сущностей, или событий в одном или нескольких текстах, когда под разрешением анафоры подразумевают связь между анафором(в основном, как упоминалось выше, прономинальной или номинативной именной группы) и антецедентом(в основном номинативные именные группы).
Эти задачи можно слить в одну, если после разрешения анафоры слить в классы все пары антецедент-анафор, ссылающиеся на одну и ту же сущность в рамках текста, корпуса, или, как иногда выражаются, в рамках реального мира.

Обработка текста является важной деталью при решении задач компьютерной лингвистики методами машинного обучения. В исследовании
[15], например, описывается замена местоимений(личные, рефлексивные, и релятивные) на их антецеденты в процессе обработке текста для обучения модели(так так же используется модель  fastText ля векторизации). Для первичного разрешения анафоры используется инструмент An@phora(http://ling.go.mail.ru/anaphora). Затем в тех предложениях, где сработало разрешение анафоры, анафор заменяется на антецедент. Модель обучается на парах предложений, с заменой и без. В случае отсутствия антецедента, местоимение отсеивается, как стоп-слово. В результате, при формировании эмбеддингов слов и контекста, модель, обученная на таких парах предложений, лучше различает векторную близость анафора и антецедента.

## Сбор и подготовка данных.

Данные для обучения классификаторов были взяты с форумов (https://neuroleptic.ru/,  https://mneploho.net/forum/1002-1, https://www.hv-info.ru/ и http://www.rakpobedim.ru), и размечены как вручную, так  иавтоматически.

При скачивании тексты разделялись на топики (символом "TOPIC") и посты (разметкой "-----").

В качестве синтаксического парсера использовалась модель библиотеки spacy (https://spacy.io/models/ru, ru_core_news_md).

Морфологическим анализатором служила библиотека pymorphy2 (https://pymorphy2.readthedocs.io/en/stable/).

Для векторизации окружения и контекста используется предобученная модель fastText, разработанная компанией Facebook, в дистрибутиве библиотеки Gensim (open source software released under the GNU LGPLv2.1 license) для языка Python.
В процессе токенизации текст разбивался иерархически на топики, посты, предложения, и токены.
Разбиение на топики и посты реализовывалось автоматически по разметке, определенной при скачивании текстов. Такенизация на предложения и токены осуществлялась с помощью библиотеки NLTK (https://www.nltk.org , Natural Language Toolkit).

При обработке определялось, присутствует ли в посте цитирование какого-то из предыдущих постов топика с помощью улючевых слов 'сказал(а)', ') писал:', 'писал(а): ↑'.
Описание датафрейма.

Датафрейм содержит следующую информацию:
  - TOKEN - строковое представление всех токена в тексте. 
  - TOKEN_VECT - изначально fastText-вектор токена, после обработки в эту колонку помещается значение косинусного расстояния до семантической оси токенов(см. дальше расчет сем. осей).
  - IS_ANSWER - бинарый признак, 1 или 0. Один значит, что в посте есть цитирование, ноль - наоборот.
  - TOPIC_NUM - номер топика
  - POST_NUM - номер поста внутри топика (каждый новый топик счетчик сбрасывается и посты считаются с начала)
  - SENT_NUM - номер предложения внутри топика.
  - TOKEN_NUM - номер токена внутри топика.
  - ANIMACY - признак одушевленности/неодушевленности (парсер pymorphy2).
  - CASE - падеж (парсер pymorphy2).
  - GENDER - пол (парсер pymorphy2).
  - PERSON - лицо (парсер pymorphy2).
  - POS - часть речи (парсер pymorphy2).
  - DEPENDENCY - тип синтаксической зависимости (парсер Spacy).
  - HEAD - главное слово в синсинтаксическом дереве (парсер Spacy).
  - HEAD_ANIMACY - признак одушевленности/неодушевленности гавного слова (парсер pymorphy2).
  - HEAD_CASE - падеж главного слова (парсер pymorphy2).
  - HEAD_GENDER - пол главного слова(парсер pymorphy2).
  - HEAD_POS - часть речи главного слова(парсер pymorphy2).
  - HEAD_VECT - fastText-вектор главного слова токена, после обработки в эту колонку помещается значение косинусного расстояния до семантической оси главных слов(см. дальше расчет сем. осей).
  - SENT_VECT - fastText-вектор главного слова всего предложения, после обработки в эту колонку помещается значение косинусного расстояния до семантической оси предложений(см. дальше расчет сем. осей).
  - HEAD_CHILDS_VECT - fastText-вектор всех зависимых слов для главного слова токена.
  - NER - размеченное значение сущности. 1 - название препарата, именованная сущность. 2 - номинативный анафор, такие слова как "препарат", или"лекарство". 3- прономинальный анафор, например "он", "него", "его". 0 - нет кореферентной связи с медицинскими препаратами.
  - COREFERENCE_CLUSTER - номер антецедента, начиная с начала топика. В случае, если входящий токен является антецедентом - ему присваивается собственный номер. Если это анафор, то ему присваивается номер его антецедента.

Названия препаратов (например, "серковель", "сиозсин", и тд) размечались, как класс "1" в столбце NER. В столбце "COREFERENCE_CLUSTER"  присваивался собственный номер индекса. 

Из антецедентов рассматривались только номинативные и прономинальные группы. В прономинальных группах, размечались только личные местоимения единственного числа.
В номинативные группы входили существительные, такие как "препарат" и "лекарство".
Так как антецедентов в течении топика, как правило, встречалось несколько, кандидаты рассматривались в следующем порядке приоритезации:
  - В одном предложении.
  - В одном посте.
  - В заглавном сообщение топика.
  - В соседних постах.
 
Цитаты можно не рассматривать, как исключительный случай, потому что они входят в состав поста на всех трех форумах.

## Метод семантических осей.
Обычно в методах ранжирования для разрешения анафоры и кореференции в качестве признаков рассчитывается косинусная дистанция между анафором и потенциальным антецедентом. Для этого необходимо расчитать попарно близости каждой пары, и провести сравнение скорингов.
Для ускорения процесса, и упрощения анализа зависимостей, я решил применить метод семантических осей, описанный в [14] (глава 20.4.1 Semantic Axis Methods).

Для каждого из значений TOKEN_VECT, HEAD_CHILDS_VECT, SENT_VECT, HEAD_VECT расчитывались сидовые множества. Как правило, в первом посте каждого топика содержится название препарата, и тема для обсуждения. В общем случае это модерируемое сообщение, написанное по шаблону:
  - "Обсуждаем препарат анальгин(производитель Фарма-инк)."
Из каждого первого предложения топика(на данный момент размечено 5 топиков) извлекался анафор, его главное слово, и зависимые слова. Для каждого знаения отдельно берется вектор, и так же векторизуется все предложение. 
Формула расчета каждого из сидовых множеств:

![f1]

Здесь ![f2] - результирующий вектор сидового множества, ![f3] - вектор токена, предложения,главного слова, или зависимых слов главного слова, а ![f4] - количество топиков.

Значения TOKEN_VECT, HEAD_CHILDS_VECT, SENT_VECT, HEAD_VECT для каждого токена считаются по формуле:

![f5]

## Описание моделей
В задаче разрешения анафоры используется широкий набор инструментов. Это методы, основанные на наборах правил, классическом машинном обучении, их комбинации, а так же методы глубокого обучения. В нашей задаче в качестве бэйзлайна мы будем использовать правиловый алгоритм, затем подключим алгоритмы машинного обучения.

Учитывая специфику русского языка, а так же иерархичности текста в социальных форумах, связанных с медицинской тематикой, можно проследить ряд закономерностей, по которым был реализован алгоритм из правил по выбору подходящего антецедента. Алгоритм состоит из следующих шагов:

`(я сделаю потом нормальный алгоритм, его интуюцию и блок-схему, но пока опишу словами)`

  - Извлекаются индексы всех топиков датасета.
  - Ведется итерация по всем индексам, для каждого:
     * Извлекается количество постов в топике, и предложений в каждом посте.
     * Итерация идет по каждому предложению поста, для каждого:
         * Извлекаются все анафоры в предложении.
         * Извлекаются все антецеденты в предложении.
         * Если анафоров нет, берется следующее предложение.
         * Если анафоры есть:
             * Проверяется наличие антецедентов в предложении, первым берется самый дальний от анафора(первый с начала предложения), проверяется соответствие по числу. Если ни один из кандидатов не соответствует по числу, анафору присваивается нулевой класс.
             * Если антецедентов нет в предложении, рассматриваются все антецеденты, встречающиеся в предыдущих предложениях поста. В этом случае берется ближайший к анафору антецедент, и так же проверяется на соответствие по числу. В случае несоответствия, присваивается нулевой класс.
             * Если антецедентов нет в посте, берется самый верхний кандидат начиная с начала топика, как правило это заглавное сообщение темы. 
         


## Метрики оценки системы

Работы по оценке систем анафоры и кореференции используют различные критерии. При расчете метрик часто разделяют типы местоимений. Например оцениваются только личные, посессивные и рефлексивные местоимения, а так же учитывается максимальное растояние между анафором и антецедентом[17].

К сожалению, не тек много исследований описывают рассчет ошибок систем разрешения анафоры для русского языка. В 2014 году был проведен форум U-EVAL-2014: Evaluating anaphora and coreference resolution for Russian, посвященный оценке систем разрешения анафоры и кореференции для русских текстов. Участникам форума высылался набор данных, на котором они использовали свои системы.

Отдельно оценивались разрешение анафоры и кореференция.
Для оценки разрешения анафоры использовались метрики: recall, precision и F-measure (полнота, точность, и F-мера).

Для оценки разрешения кореференции: MUC, B3, CEAF и F-measure.

данная работа посвящена в первую очередь разрешению анафоры, поэтому рассмотрим более подробно оценку систем для разрешения именно анафоры.
метрика precision рассчитывается по формуле:

![f6]

где ![f7] - пары антецедент - анафор, распознанные системой верно, а ![f8] - все пары, распознанные системой, как имеющие анафорическую связь.

Соответственно, формула для критерия recall выглядит и расшифровывается следующим образом:

![f9]


где ![f10] - пары антецедент - анафор, распознанные системой верно, а ![f11] - пары, имеющие анафорическую связь, но не распознанные системой, или распознанные ошибочно, и пары, распознанные верно.

И, наконец, Ф-мера:

![f12]

где ![f13] и ![f14]  - точность и полнота.

## Результаты работы моделей
`coming soon`

## Дискуссия
`coming soon`

## Выводы
`coming soon`

-----
[1] http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.29.6235&rep=rep1&type=pdf
ANAPHORA RESOLUTION: THE STATE OF THE ART, Ruslan Mitkov

Hirst, Graeme. 1981.Anaphora in natural language understanding. Berlin Springer Verlag,
1981.

[2] https://www.aclweb.org/anthology/W16-0711.pdf
Error analysis for anaphora resolution in Russian: new challenging issues
for anaphora resolution task in a morphologically rich language
Svetlana Toldova Ilya Azerkovich Anna Roytberg

[3] http://www.dialog-21.ru/media/3913/gureenkovaoaetal.pdf
Complex Approach towards
Algoritm Learning for Anaphora
Resolution in Russian Language
Gureenkova O. A.,
Batura T. V. ,
Kozlova A. A.,
Svischev A. N.

[4] https://arxiv.org/pdf/1805.10163.pdf
Context-Aware Neural Machine Translation Learns Anaphora Resolution
Elena Voita
University of Amsterdam, Netherlands
Pavel Serdyukov
Rico Sennrich

[5] http://www.dialog-21.ru/media/4829/inshakovaes-167.pdf
AN ANAPHORA RESOLUTION SYSTEM FOR RUSSIAN BASED ON ETAP-4 LINGUISTIC PROCESSOR1 Inshakova E. S

[6] https://www.aclweb.org/anthology/J13-4004.pdf
Jurafsky D., Lee H., Chang A., Peirsman Y., Chambers N., Surdeanu M. (2013), Deterministic Coreference Resolution Based on Entity-Centric, Precision-Ranked
Rules, Association for Computational Linguistics, Vol. 39, N 4, pp. 885–916.


[7] http://www.dialog-21.ru/digests/dialog2014/materials/pdf/Kamenskaya%D0%9C%D0%90.pdf
Kamenskaya М. А., Khramoin I. V., Smirnov I. V. (2014), Data-driven Methods
for Anaphora Resolution of Russian, Computational Linguistics and Intellectual Technologies: Papers from the Annual International Conference “Dialogue”
(2014), Issue 13 (20), pp. 241–250.

http://www.dialog-21.ru/digests/dialog2014/materials/pdf/ProtopopovaEV.pdf
[8] Protopopova E. V., Bodrova A. A., Volskaya S. A., Krylova I. V., Chuchunkov A. S.,
Alexeeva S. V., Bocharov V. V., Granovsky D. V. (2014), Anaphoric Annotation and
Corpus-Based Anaphora Resolution: An Experiment, Computational Linguistics
and Intellectual Technologies: Papers from the Annual International Conference
“Dialogue” (2014), Issue 13 (20), pp. 562–571

[9] http://www.dialog-21.ru/media/4829/inshakovaes-167.pdf
An anaphora resolution system for Russian based on ETAP-4 linguistic processor

[10] https://arxiv.org/pdf/1706.02256.pdf [Submitted on 7 Jun 2017 (v1), last revised 21 Jul 2017 (this version, v2)] A Mention-Ranking Model for Abstract Anaphora Resolution Ana Marasović, Leo Born, Juri Opitz, Anette Frank

[11] https://arxiv.org/pdf/2004.07898.pdf
[Submitted on 16 Apr 2020 (v1), last revised 24 Jun 2020 (this version, v3)] Bridging Anaphora Resolution as Question Answering Yufang Hou

[12] https://www.aclweb.org/anthology/2021.eacl-main.116.pdf ChEMU-Ref: A Corpus for Modeling Anaphora Resolution in the Chemical Domain
Biaoyan Fang, Christian Druckenbrodt, Saber A Akhondi, Jiayuan He, Timothy Baldwin, Karin Verspoor

[13] Speech and Language Processing. Daniel Jurafsky & James H. Martin. Copyright © 2020. All
rights reserved. Draft of December 30, 2020. глава про разрешение кореференции
https://web.stanford.edu/~jurafsky/slp3/21.pdf

[14] https://web.stanford.edu/~jurafsky/slp3/20.pdf 20.4.1 Semantic Axis Methods
Speech and Language Processing. Daniel Jurafsky & James H. Martin. Copyright © 2020. All rights reserved. Draft of December 30, 2020. CHAPTER 20 Lexicons for Sentiment, Affect, and Connotation

[15] https://publications.hse.ru/mirror/pubs/share/folder/omioiyt0dk/direct/196474574.pdf Koslowa O., Kutuzov A.
Improving Distributional Semantic Models Using Anaphora Resolution during Linguistic Preprocessing

[16]  https://www.aclweb.org/anthology/W16-0711.pdf Error analysis for anaphora resolution in Russian: new challenging issues for anaphora resolution task in a morphologically rich language
Svetlana Toldova, Ilya Azerkovich, Alina Ladygina, Anna Roitberg, Maria Vasilyeva

[17] C. Barbu. 2002. Error analysis in anaphora resolution.
In LREC.
[17] https://www.researchgate.net/publication/292851003_RU-EVAL-2014_Evaluating_anaphora_and_coreference_resolution_for_Russian U-EVAL-2014: Evaluating anaphora and coreference resolution for Russian


[f1]: http://chart.apis.google.com/chart?cht=tx&chl=E_sid=\frac{\sum_n^i{E\imath}}{n}
[f2]: http://chart.apis.google.com/chart?cht=tx&chl=E_sid
[f3]: http://chart.apis.google.com/chart?cht=tx&chl=Ei
[f4]: http://chart.apis.google.com/chart?cht=tx&chl=n
[f5]: http://chart.apis.google.com/chart?cht=tx&chl=score_w=cos(E_w,E_sid)
[f6]: http://chart.apis.google.com/chart?cht=tx&chl=P=\frac{M}{S}
[f7]: http://chart.apis.google.com/chart?cht=tx&chl=M
[f8]: http://chart.apis.google.com/chart?cht=tx&chl=S
[f9]: http://chart.apis.google.com/chart?cht=tx&chl=R=\frac{M}{G}
[f10]: http://chart.apis.google.com/chart?cht=tx&chl=M
[f11]: http://chart.apis.google.com/chart?cht=tx&chl=G
[f12]: http://chart.apis.google.com/chart?cht=tx&chl=Fscore=\frac{2PR}{P+R}
[f13]: http://chart.apis.google.com/chart?cht=tx&chl=P
[f14]: http://chart.apis.google.com/chart?cht=tx&chl=R

