import requests


class VKGroupAPIConnector:
    def __init__(self, access_token, version='5.131'):
        self.access_token = access_token
        self.version = version
        self.base_url = 'https://api.vk.com/method/'

    def _make_request(self, method, params) -> dict:
        url = self.base_url + method
        params['access_token'], params['v'] = self.access_token, self.version
        try:
            response = requests.get(url, params=params)
            data = response.json()
        except (ValueError, requests.JSONDecodeError) as _e:
            return {'error': _e}
        return data

    def get_object_id_by_link(self, link: str) -> int:
        data = self._make_request(
            method='utils.resolveScreenName', params={'screen_name': link.split('/')[-1], }
        )

        if not data or 'error' in data or 'response' not in data:
            return 0

        object_id, object_type = data['response']['object_id'], data['response']['type']
        return -object_id if object_type == 'group' or object_type == 'public' else object_id

    def get_group_posts_data(self, object_id: int, offset: int = 0, count: int = 100) -> list:
        data = self._make_request(
            method='wall.get', params={'owner_id': object_id, 'count': count, 'offset': offset}
        )

        if not data or 'error' in data or 'response' not in data:
            return []

        return data['response']['items']

    def get_post_comments_data(self, object_id: int, post_id: int, count: int = 50):
        data = self._make_request(
            method='wall.getComments', params={'owner_id': object_id, 'post_id': post_id, 'count': count, }
        )

        if not data or 'error' in data or 'response' not in data:
            return []

        return data['response']['items']


if __name__ == "__main__":
    token = input('Enter VK API access token: ')
    vk_connector = VKGroupAPIConnector(access_token=token)
    obj_id = vk_connector.get_object_id_by_link('https://vk.com/informatika_gia')
    posts_data = vk_connector.get_group_posts_data(object_id=obj_id)
    print(vk_connector.get_post_comments_data(object_id=obj_id, post_id=posts_data[0]['id']))
