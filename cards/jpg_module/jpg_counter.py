import os
import random


def get_dict_of_answers_for_jpegs_in_the_folder(number_of_variants, folder):
    # get list of jpg_s in the folder
    try:
        list_dir = os.listdir(os.path.abspath(folder))
    except Exception as e:
        print(e)
        return {}
    list_jpg = []
    for file in list_dir:
        if '.jpg' in file:
            list_jpg.append(file)
    # convert list of jpg_s to the list of names
    list_names = []
    # list_names sorted as list_jpg
    for jpg in list_jpg:
        list_names.append(jpg.replace(".jpg", ""))
    # take randomizer
    random.seed()
    # create dict of answers
    dict_names = {}
    for name in list_names:
        key_name = name + ".jpg"
        dict_names[key_name] = []
        dict_names[key_name].append(name)
        counter = 0
        while counter < number_of_variants:
            random_name = list_names[random.randrange(0, len(list_names) - 1)]
            if (name is not random_name) and (random_name not in dict_names[key_name]):
                dict_names[key_name].append(random_name)
                counter += 1
    # randomize answers
    for key, value in dict_names.items():
        dict_names[key] = random.sample(value, len(value))
    # randomize dict
    key_list = list(dict_names)
    key_list = random.sample(key_list, len(key_list))
    rand_dict = {}
    for key in key_list:
        rand_dict[key] = dict_names[key]
    # return dict
    return rand_dict


if __name__ == "__main__":
    folder_ = os.path.dirname(os.path.abspath(__file__))
    print(get_dict_of_answers_for_jpegs_in_the_folder(3, folder_))
