# Задание 3
# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.


text = "Статья — это жанр журналистики, в котором автор ставит задачу проанализировать общественные ситуации, процессы, явления, прежде всего с точки зрения закономерностей, лежащих в их основе. В статье автор рассматривает отдельные ситуации как часть более широкого явления. Автор аргументированно пишет о своей точке зрения.В статье выражается развернутая обстоятельная аргументированная концепция автора или редакции по поводу актуальной социологической проблемы. Также в статье журналист обязательно должен интерпретировать факты (это могут быть цифры, дополнительная информация, которая будет правильно расставлять акценты и ярко раскрывать суть вопроса).Отличительным аспектом статьи является её готовность. Если подготавливаемый материал так и не был опубликован (не вышел в тираж, не получил распространения), то такой труд относить к статье некорректно. Скорее всего данную работу можно назвать черновиком или заготовкой. Поэтому целью любой статьи является распространение содержащейся в ней информации"

my_dict = {}
text_list = text.lower().split()
text_list_new = [''.join(filter(str.isalpha, a)) for a in text_list]

while '' in text_list_new:
    text_list_new.remove('')

for word in text_list_new:
    my_dict.setdefault(word, text_list_new.count(word))

num_words = 1
while num_words <= 10:
    num_words += 1
    max_key = max(my_dict,  key=my_dict.get)
    print(f'{max_key:>5}  =  {my_dict[max_key]}')
    my_dict.pop(max_key)