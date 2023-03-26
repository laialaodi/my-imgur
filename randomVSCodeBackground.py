import random
import os
import json


# def random_generate() -> list[str]:
#     with open('background.list', 'r', encoding='utf-8') as f:
#         background_image = f.readlines()

#     random.shuffle(background_image)
#     return_list = []
#     for filename in background_image:
#         filename = filename.strip()
#         print(
#             f'"file:///C:/Users/frank/Pictures/vscode background/{filename}",')
#         return_list.append(
#             f'file:///C:/Users/frank/Pictures/vscode background/{filename}')
#     os.system('pause')
#     return return_list
def random_generate() -> list[str]:
    with open('background.list', 'r', encoding='utf-8') as f:
        background_image = f.read().splitlines()

    random.shuffle(background_image)
    return_list = [
        f'file:///C:/Users/frank/Pictures/vscode background/{filename.strip()}' for filename in background_image]
    print('\n'.join(return_list))
    os.system('pause')
    return return_list


def modify_settings() -> None:
    with open('C:/Users/frank/AppData/Roaming/Code/User/settings.json', 'r', encoding='utf-8') as f:
        loaded_json = json.load(f)
    image_list = random_generate()
    loaded_json['background.fullscreen']['image'] = image_list
    with open('C:/Users/frank/AppData/Roaming/Code/User/settings.json', 'w', encoding='utf-8') as f:
        json.dump(loaded_json, f, ensure_ascii=False, indent=4)
    return None


if __name__ == '__main__':
    modify_settings()
