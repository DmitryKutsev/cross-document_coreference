# cross-document_coreference
First steps to make my research in HSE computational linguistics master program. Theme of the diploma is Cross-document coreference resolution in social networks.

Извлечение кросс-текстовой анафоры из русскоязычного пользовательского
контента в медицинской сфере.

Cross-document anaphora extraction from medicine-related content generated by
Russian users.

Вступление.
Извлечение данных из пользовательского медицинского контента - важная задача,
позволяющая решить, или упростить решение для множества задач в медицине. Такие
задачи, как извлечение отзывов, и иной информации о препаратах, или проведение
диагностики на имеющихся данных о лечении заболеваний, дополняют методики лечения.
На основе обработанных данных составляются рекомендательные и консалтинговые
системы, помогающие врачам поставить диагноз, или подобрать наиболее подходящий
препарат.
Разрешение анафоры - важная составляющая для большинства систем извлечения
данных из текстов. Строго говоря, анафора - зависимость между интерпретацией какой-то
одной сущности в тексте от другой, встретившейся в том же тексте ранее.
Упоминание, встретившееся первым, называют антецедентом, а следующее за ним
упоминание того же объекта - анафором. Отношения между антецедентом и анафором
можно назвать кореферентными.
Например:
“А кто принимал респеридон расскажите плз как у вас с либидо, было ли сильное
снижение или нет? А также очень интересно как влияет он на депрессивную
составляющую..?”
Здесь местоимение “он” является анафором, и ссылается на антецедент, респеридон.
Нахождение кореференциальных связей может применяться также во множестве систем,
помимо медицинских. Например, системы машинного перевода, извлечение
именованных сущностей, классификация событий, и многие другие задачи могут
использовать в своих алгоритмах разрешение анафоры.
При исследовании анафоры в первую очередь подразумевают исследование связи
местоимения(реже существительного) с именованной сущностью, или упоминанием этой
сущности. Такой тип анафоры называют прономинальной.

Есть связи, в которых и анафор, и антецедент являются существительными, например:
“Знаю, что тиапридал применяется при алкоголизме для купирования агрессивности.
Есть ли у кого-нибудь опыт применения этого препарата у пожилых людей?”
Иногда различают анафоры, находящиеся внутри одного предложения, и анафоры, члены
которых находятся в разных предложениях(интрасентенциальные, и
интерсентенциальные).
