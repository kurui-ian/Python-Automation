text = "   python automation with scripts   "
cleaned = text.strip()
print(cleaned)

print(cleaned.upper())
print(cleaned.lower())
print(cleaned.title())

sentence = "I love python because python is simple"
new_sentence = sentence.replace("python", "automation")
print(new_sentence)

tags = "automation,scripting,python,files"
tag_list = tags.split(",")
print(tag_list)

joined_tags = " | ".join(tag_list)
print(joined_tags)

filename = "report_data.csv"
print(filename.startswith("report"))
print(filename.endswith(".csv"))

word = "automation"
print(word.count("a"))
print(word.find("mate"))
