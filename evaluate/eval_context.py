# with open("C:/Users/Nitro/Desktop/Папка/Диплом/yandex/test_corr.txt", "r", encoding="utf-8") as corrected_file:
#     with open("C:/Users/Nitro/Desktop/Папка/Диплом/yandex/test_corr_new.txt", "w",
#               encoding="utf-8") as right_file:
#         for line in corrected_file:
#             if line != "\n":
#                 # print(line.strip())
#                 right_file.write(line.strip() + "\n")

with open("C:/Users/Nitro/Desktop/Папка/Диплом/dpavlov/test_corr_pavlov.txt", "r", encoding="utf-8") as corrected_file:
    with open("C:/Users/Nitro/Desktop/Папка/Диплом/evaluate/corrected_sample_testset.txt", "r", encoding="utf-8") as right_file:
        with open("C:/Users/Nitro/Desktop/Папка/Диплом/evaluate/test_sample_testset.txt", "r", encoding="utf-8") as test_file:
            cor_my_lines = corrected_file.readlines()
            corrected_lines = right_file.readlines()
            test_lines = test_file.readlines()

total_count = 0
total_error = 0
origin_error = 0

for line_my, line_cor, test_line in zip(cor_my_lines, corrected_lines, test_lines):
    temp_error = 0
    for my_word, cor_word, test_word in zip(line_my.strip().split(), line_cor.strip().split(), test_line.strip().split()):
        total_count += 1
        if cor_word != test_word:
            origin_error += 1
        if my_word != cor_word:
            temp_error += 1
    temp_error = 2 if temp_error >= 5 else temp_error
    total_error += temp_error

print(origin_error / total_count * 100)
print(total_error / total_count * 100)
print(100 - total_error / origin_error * 100)

