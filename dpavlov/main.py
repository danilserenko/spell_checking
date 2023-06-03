from deeppavlov import build_model, configs
import json
import time

def scores(TP, FP, FN, TN, beta=0.5):
    precision = TP / (TP+FP)
    recall = TP / (TP+FN)
    accuracy = (TP + TN)/(TP+FP+FN+TN)
    F_score = (1+beta**2) * (precision * recall) / (beta**2 * precision + recall)
    return precision, recall, accuracy, F_score



CONFIG_PATH = configs.spelling_correction.levenshtein_corrector_ru
# sentences = ["Я шол домой по незнакомойулице москвы.", "Двушка педа в церковно% хоре."]
model = build_model(CONFIG_PATH, download=True)
# for line in sentences:
#     print(model([line])[0], flush=True)

i = 0
with open("C:/Users/Nitro/Desktop/Папка/Диплом/evaluate/test_sample_testset.txt", "r", encoding="utf-8") as file:
    with open("test_corr_pavlov.txt", "w", encoding="utf-8") as w_file:
        for line in file:
            i += 1
            print(i)
            cor_text = model([line])[0]
            w_file.write(cor_text + "\n")

# with open("C:/Users/Nitro/Desktop/Папка/Диплом/dataset_60_40.json", "r", encoding="utf-8") as js:
#     dataset = json.load(js)
# print(len(dataset))
# str_with_mistakes = ""
# gold_words = []
# src_words = []
# pred_words = []
#
# for k, w in dataset.items():
#     gold_words.append(k)
#     str_with_mistakes += w + " "
#
# src_words = str_with_mistakes.split()
# start = time.time()
# i = 0
# for word in src_words:
#     print(i)
#     i += 1
#     pred_words.append(model([word])[0])
#     # if i > 10:
#     #     break
# print(src_words[:12])
# print(pred_words)
# print("time:", time.time() - start)
#
#
# TP = 0
# FP = 0
# FN = 0
# TN = 0
#
# for token, gold, pred in zip(src_words, gold_words, pred_words):
#     if token != pred:
#         if pred == gold:
#             TP += 1
#         else:
#             FP += 1
#             # print(f"TN: {token} - {gold} - {pred}")
#     else:
#         if pred == gold:
#             TN += 1
#         else:
#             FN += 1
#             # print(f"TN: {token} - {gold} - {pred}")
#
# print("TP:", TP, "FP:", FP, "FN:", FN, "TN:", TN)
# precision, recall, accuracy, F_score = scores(TP, FP, FN, TN, beta=0.5)
# print("precision:", precision)
# print("recall:", recall)
# print("accuracy:", accuracy)
# print("F_score:", F_score)
# print(len(gold_words))