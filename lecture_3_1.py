# Домашнее задание к лекции 3.1
# «Работа с разными форматами данных»
# Кокурникова Лилия Фаритовна, 10.03.19

def count_re_news(description):
  import collections

  re_words = collections.Counter()
  for word in description:
    if len(word) > 6:
        re_words[word] += 1
  all_re_word = list(re_words.keys())
  return print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов: ' + str(all_re_word[:10]))


import json

with open("newsafr.json", "r", encoding='utf-8') as datafile:
  json_data = json.load(datafile)
items = json_data["rss"]["channel"]["items"]

all_news_json = []
i = 0
while i < len(items):
    all_news_json = all_news_json + json_data["rss"]["channel"]["items"][i]["description"].split(" ")
    i += 1

import xml.etree.ElementTree as ET

tree = ET.parse("newsafr.xml")
root = tree.getroot()
all_news_xml = []
xml_items = root.findall("channel/item")

for item in xml_items:
  description = item.find("description")
  description_xml = description.text.split(" ")
  all_news_xml = all_news_xml + description_xml


print(count_re_news(all_news_xml))
print(count_re_news(all_news_json))






