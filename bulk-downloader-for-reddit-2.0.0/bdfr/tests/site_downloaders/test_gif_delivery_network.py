#!/usr/bin/env python3
# coding=utf-8

from unittest.mock import Mock

import pytest

from bdfr.resource import Resource
from bdfr.site_downloaders.gif_delivery_network import GifDeliveryNetwork


@pytest.mark.online
@pytest.mark.parametrize(('test_url', 'expected'), (
    ('https://www.gifdeliverynetwork.com/regalshoddyhorsechestnutleafminer',
     'https://thumbs2.redgifs.com/RegalShoddyHorsechestnutleafminer.mp4'),
    ('https://www.gifdeliverynetwork.com/maturenexthippopotamus',
     'https://thumbs2.redgifs.com/MatureNextHippopotamus.mp4'),
))
def test_get_link(test_url: str, expected: str):
    result = GifDeliveryNetwork._get_link(test_url)
    assert result == expected


@pytest.mark.online
@pytest.mark.parametrize(('test_url', 'expected_hash'), (
    ('https://www.gifdeliverynetwork.com/maturenexthippopotamus', '9bec0a9e4163a43781368ed5d70471df'),
    ('https://www.gifdeliverynetwork.com/regalshoddyhorsechestnutleafminer', '8afb4e2c090a87140230f2352bf8beba'),
))
def test_download_resource(test_url: str, expected_hash: str):
    mock_submission = Mock()
    mock_submission.url = test_url
    test_site = GifDeliveryNetwork(mock_submission)
    resources = test_site.find_resources()
    assert len(resources) == 1
    assert isinstance(resources[0], Resource)
    resources[0].download(120)
    assert resources[0].hash.hexdigest() == expected_hash
