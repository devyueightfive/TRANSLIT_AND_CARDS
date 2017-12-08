from .rules import  get_rules
from .transliteration import normalize_text, get_transliteration

if __name__ == '__main__':
    rules = get_rules()
    # print(rules)
    text = input('Input some russian text: ')
    trans_text = get_transliteration(text, rules)
    print(trans_text)
    norm_text = normalize_text(trans_text, rules)
    print(norm_text)
