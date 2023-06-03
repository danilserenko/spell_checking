# -*- coding: utf-8 -*-
from pyaspeller import YandexSpeller

corrector = YandexSpeller(lang="ru")

i = 0
with open("C:/Users/Nitro/Desktop/Папка/Диплом/evaluate/test_sample_testset.txt", "r", encoding="utf-8") as file:
    with open("test_corr_pavlov.txt", "w", encoding="utf-8") as w_file:
        for line in file:
            i += 1
            print(i)
            cor_text = corrector.spelled_text(line)
            w_file.write(cor_text + "\n")
            # if i > 10:
            #     break

# cor_text = corrector.spelled_text()
# print(cor_text)
