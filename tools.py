import re

from connector import VKGroupAPIConnector

COUNT_PER_PAGE: int = 100


def clean_text(text: str) -> str:
    return re.sub(r'[^а-яА-Я]+', ' ', text)


def get_text_group_posts(vk_connector: VKGroupAPIConnector, object_id: int, count: int = 100) -> str:
    global COUNT_PER_PAGE
    text: str = ""
    _: int = 0

    while _ * COUNT_PER_PAGE < count:
        posts_data = vk_connector.get_group_posts_data(object_id=object_id, offset=_, count=COUNT_PER_PAGE)

        if not posts_data:
            break

        try:
            text = text + " ".join([post['text'] for post in posts_data]) + " "
        except MemoryError:
            break

        _ += 1

    return clean_text(text)
