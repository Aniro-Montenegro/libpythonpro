from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': '79Aniro', 'id': 20999767,
         'avatar_url': 'https://avatars.githubusercontent.com/u/20999767?v=4', 'gravatar_id': '',
         }
    github_api.requests.get=Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('79Aniro')
    assert 'https://avatars.githubusercontent.com/u/20999767?v=4' == url
