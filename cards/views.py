from django.http import HttpResponse
from django.template import loader


def index(request):
    from .jpg_module import jpg_counter
    # get dict of answers
    dict_of_answers = jpg_counter.get_dict_of_answers_for_jpegs_in_the_folder(4, r"./cards/static/cards/")
    print(dict_of_answers)
    template = loader.get_template('cards/index.html')
    context = {"dict_of_answers": dict_of_answers}
    return HttpResponse(template.render(context, request))
