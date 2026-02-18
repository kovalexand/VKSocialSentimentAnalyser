from analyzer import TextClusteringAnalyzer
from connector import VKGroupAPIConnector
from tools import get_text_group_posts

token = ''

vk_connector = VKGroupAPIConnector(access_token=token)
object_id = vk_connector.get_object_id_by_link('https://vk.com/rock_music_on')
text = get_text_group_posts(vk_connector=vk_connector, object_id=object_id, count=300)
analyzer = TextClusteringAnalyzer(oai_api_key='')
print(analyzer.determine_texts_topic(text=text))
