def translate_txt(text):
    if '_' in text:
        return trans_snake_to_camel(text)
    else:
        return trans_camel_to_snake(text)

def trans_snake_to_camel(snake_str):
    words = snake_str.split('_')
    result = ""
    for x in words:
        result += x.capitalize()
    return result

def trans_camel_to_snake(camel_str):
    snake_str = ""
    for i, char in enumerate(camel_str):
        if char.isupper():
            if i > 0:
                snake_str += "_"
            snake_str += char.lower()
        else:
            snake_str += char
    return snake_str

print(translate_txt(input('введите текст')))
