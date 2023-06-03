import jamspell
import time
import json
import random


def scores(TP, FP, FN, TN, beta=0.5):
    precision = TP / (TP+FP)
    recall = TP / (TP+FN)
    accuracy = (TP + TN)/(TP+FP+FN+TN)
    F_score = (1+beta**2) * (precision * recall) / (beta**2 * precision + recall)
    return precision, recall, accuracy, F_score

corrector = jamspell.TSpellCorrector()

# Load Language model -
# argument is a downloaded model file path
corrector.LoadLangModel("/media/sf_Common_folder/model_1m.bin")
with open("/media/sf_Common_folder/dataset_60_40.json", "r") as js:
    dataset = json.load(js)
print(len(dataset))
str_with_mistakes = ""
gold_words = []
src_words = []
pred_words = []
# start = time.time()
for k, w in dataset.items():
    gold_words.append(k)
    str_with_mistakes += w + " "

src_words = str_with_mistakes.split()
start = time.time()
for word in src_words:
    pred_words.append(corrector.FixFragment(word))
print("time:", time.time() - start)
# pred_str = corrector.FixFragment(str_with_mistakes)
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



