import myHeaders
myHeaders.printp("Emoji Converter")

message = input(">")
words = message.split(' ')
print(words)
emojis = {
    ":)":   "<emoticon_smile>",
    ":(":   "<emoticon_sad>"
}

output = ''
for word in words:
    output += emojis.get(word, word) + " "
print(output)