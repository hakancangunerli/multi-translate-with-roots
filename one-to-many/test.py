from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("https://translate.astian.org/")

user_input = str(input("Enter text to translate:"))

list = ["de", "fr", "es"]
for i in range(len(list)):
    print(lt.translate(user_input, "en", list[i]))

