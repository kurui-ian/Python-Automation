text = "     This is my sample text for string manipulation in python   "
cleaned = text.strip()
print(cleaned)


lowercase = cleaned.lower()
print(lowercase)

uppercase = cleaned.upper()
print(uppercase)

Tittle = cleaned.title()
print(Tittle)

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

