from pyaspeller import YandexSpeller
import json
import time
import random

def scores(TP, FP, FN, TN, beta=0.5):
    precision = TP / (TP+FP)
    recall = TP / (TP+FN)
    accuracy = (TP + TN)/(TP+FP+FN+TN)
    F_score = (1+beta**2) * (precision * recall) / (beta**2 * precision + recall)
    return precision, recall, accuracy, F_score


speller = YandexSpeller(lang="ru")

with open("C:/Users/Nitro/Desktop/Папка/Диплом/dataset_60_40.json", "r", encoding="utf-8") as js:
    dataset = json.load(js)
print(len(dataset))
str_with_mistakes = ""
gold_words = []
src_words = []
pred_words = []

for k, w in dataset.items():
    gold_words.append(k)
    str_with_mistakes += w + " "

src_words = str_with_mistakes.split()
start = time.time()
i = 0
for word in src_words:
    print(i)
    i += 1
    pred_words.append(speller.spelled(word))
# pred_str = speller.spelled(str_with_mistakes)
print("time:", time.time() - start)
# pred_words = pred_str.split()

TP = 0
FP = 0
FN = 0
TN = 0

for token, gold, pred in zip(src_words, gold_words, pred_words):
    if token != pred:
        if pred == gold:
            TP += 1
        else:
            FP += 1
    else:
        if pred == gold:
            TN += 1
        else:
            FN += 1

print("TP:", TP, "FP:", FP, "FN:", FN, "TN:", TN)
precision, recall, accuracy, F_score = scores(TP, FP, FN, TN, beta=0.5)
print("precision:", precision)
print("recall:", recall)
print("accuracy:", accuracy)
print("F_score:", F_score)
print(len(gold_words))


