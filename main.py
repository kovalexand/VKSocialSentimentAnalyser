from analyzer import TextClusteringAnalyzer
from connector import VKGroupAPIConnector
from tools import get_text_group_posts

token = 'vk1.a.7THUxa02YyK0ya9O3uDBFhzZYU-t80DdAkdAXFQDZkVC7rU3BZD-RKUZPvfiE1tmDDbBH7DKSMc7xbjBbhMST2DiUGxcNWWDTbD_129m_pBEPVHer5vTTkSCzFK55iLRtT7KH7yR2_N0_uTyf87LiWBZtNmwrjna2kOcpWnTepBOqvpbl6o0YACbFLC_u6-CHaN-jRXMoy7NGSnUYTesGw'

vk_connector = VKGroupAPIConnector(access_token=token)
object_id = vk_connector.get_object_id_by_link('https://vk.com/rock_music_on')
text = get_text_group_posts(vk_connector=vk_connector, object_id=object_id, count=300)
analyzer = TextClusteringAnalyzer(oai_api_key='')
print(analyzer.determine_texts_topic(text=text))
