from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
    from .translit_module import rules
    rules = rules.get_rules(file=r".\base_app\translit_module\rules.xlsx", debug='N')
    template = loader.get_template('base_app/index.html')
    context = {"rules": rules}
    return HttpResponse(template.render(context, request))


def translit_this(request, some_string):
    print("Input value", some_string)
    from .translit_module import transliteration
    from .translit_module import rules
    rules = rules.get_rules(file=r".\base_app\translit_module\rules.xlsx", debug='N')
    trans_string = transliteration.get_transliteration(some_string, rules)
    template = loader.get_template('base_app/index.html')
    context = {'normal_text': some_string, 'translit_text': trans_string, "rules": rules}
    return HttpResponse(template.render(context, request))


def normal_this(request, some_string):
    print("Input value", some_string)
    from .translit_module import transliteration
    from .translit_module import rules
    rules = rules.get_rules(file=r".\base_app\translit_module\rules.xlsx", debug='N')
    trans_string = transliteration.normalize_text(some_string, rules)
    template = loader.get_template('base_app/index.html')
    context = {'normal_text': trans_string, 'translit_text': some_string, "rules": rules}
    return HttpResponse(template.render(context, request))
