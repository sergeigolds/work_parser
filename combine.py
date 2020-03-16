import json


def combine():
    with open('cvonline.json', encoding='utf8') as fo:
        data1 = json.load(fo)

    with open('cvkeskus.json', encoding='utf8') as fo:
        data2 = json.load(fo)

    merged = data1 + data2

    with open("data.json", "w", encoding='utf8') as fo:
        json.dump(merged, fo, ensure_ascii=False, indent=4)
