#
# Домашнее задание к лекции 3.1
# «Работа с разными форматами данных»
# Кокурникова Лилия Фаритовна, 02.03.19
#
from pprint import pprint

def count_re_news(description):

  import collections

  re_words = collections.Counter()
  for word in description:
      if len(word) > 6:
        re_words[word] += 1
  all_re_word = list(re_words.keys())
  print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов: ' + str(all_re_word[:10]))


import json
with open("newsafr.json", "r", encoding='utf-8') as datafile:
  json_data = json.load(datafile)
for i in  range(0, len(json_data["rss"]["channel"]["items"])):
  description_json = json_data["rss"]["channel"]["items"][i]["description"].split(" ")

import xml.etree.ElementTree as ET

tree = ET.parse("newsafr.xml")
root = tree.getroot()
descriptions = []
xml_items = root.findall("channel/item")

for item in xml_items:
  print(item.text)
  description = item.find("description")
  description_xml = description.text.split(" ")

print(count_re_news(description_json))
print(count_re_news(description_xml))







