# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from urlparse import urlparse
from urllib import urlencode

from base import Base


class TestRedirects(Base):

    def test_that_checks_redirect_using_incorrect_query_values(self, base_url):
        param = {
            'product': 'firefox-31.0',
            'lang': 'kitty_language',
            'os': 'stella'
        }
        response = self._head_request(base_url, params=param)

        assert (requests.codes.not_found == response.status_code,
                self.response_info_failure_message(base_url, param, response))

        parsed_url = urlparse(response.url)

        assert ('http' == parsed_url.scheme, 'Failed to redirect to the correct scheme. %s' %
                self.response_info_failure_message(base_url, param, response))

        assert (urlparse(base_url).netloc == parsed_url.netloc,
                self.response_info_failure_message(base_url, param, response))

        assert (urlencode(param) == parsed_url.query,
                self.response_info_failure_message(base_url, param, response))

        assert ('Unknown' != self.get_x_backend_server(response),
                'Failed, x-backend-server was not in the response object. %s' %
                self.response_info_failure_message(base_url, param, response))

    def test_that_checks_redirect_using_locales_and_os(
        self,
        base_url,
        lang,
        os
    ):
        # Ja locale has a special code for mac
        if lang == 'ja' and os == 'osx':
            lang = 'ja-JP-mac'

        param = {
            'product': 'firefox-31.0',
            'lang': lang,
            'os': os
        }

        response = self._head_request(base_url, params=param)

        parsed_url = urlparse(response.url)

        assert (requests.codes.ok == response.status_code,
                'Redirect failed with HTTP status. %s' %
                self.response_info_failure_message(base_url, param, response))

        assert ('http' == parsed_url.scheme, 'Failed to redirect to the correct scheme. %s' %
                self.response_info_failure_message(base_url, param, response))

        assert ('Unknown' != self.get_x_backend_server(response),
                'Failed, x-backend-server was not in the response object %s' %
                self.response_info_failure_message(base_url, param, response))

    def test_stub_installer_redirect_for_en_us_and_win(self, base_url, product):
        param = {
            'product': product,
            'lang': 'en-US',
            'os': 'win'
        }

        response = self._head_request(base_url, params=param)

        parsed_url = urlparse(response.url)

        assert (requests.codes.ok == response.status_code,
                'Redirect failed with HTTP status. %s' %
                self.response_info_failure_message(base_url, param, response))

        assert ('https' == parsed_url.scheme,
                'Failed to redirect to the correct scheme. %s' %
                self.response_info_failure_message(base_url, param, response))

        assert ('download-installer.cdn.mozilla.net' == parsed_url.netloc,
                'Failed by redirected to incorrect host. %s' %
                self.response_info_failure_message(base_url, param, response))

        assert ('Unknown' != self.get_x_backend_server(response),
                'Failed, x-backend-server was not in the response object %s' %
                self.response_info_failure_message(base_url, param, response))

    @pytest.mark.parametrize('product_alias', [
        {'product_name': 'firefox-beta-latest', 'lang': 'en-US'},
        {'product_name': 'firefox-latest-euballot', 'lang': 'en-GB'},
        {'product_name': 'firefox-latest', 'lang': 'en-US'},
        {'product_name': 'firefox-beta-stub', 'lang': 'en-US'},
        {'product_name': 'firefox-nightly-latest', 'lang': 'en-US'},
    ])
    def test_redirect_for_firefox_aliases(self, base_url, product_alias):
        param = {
            'product': product_alias['product_name'],
            'os': 'win',
            'lang': product_alias['lang']
        }

        response = self._head_request(base_url, params=param)

        parsed_url = urlparse(response.url)

        if not (
            product_alias['product_name'] == 'firefox-latest-euballot' and
            "download.allizom.org" in base_url
        ):
            url_scheme = 'http'
            if product_alias['product_name'] == 'firefox-beta-stub':
                url_scheme = 'https'

            assert (requests.codes.ok == response.status_code,
                    'Redirect failed with HTTP status. %s' %
                    self.response_info_failure_message(base_url, param, response))

            assert (url_scheme == parsed_url.scheme,
                    'Failed to redirect to the correct scheme. %s' %
                    self.response_info_failure_message(base_url, param, response))

            assert (parsed_url.netloc in ['download.cdn.mozilla.net', 'edgecastcdn.net',
                    'download-installer.cdn.mozilla.net', 'cloudfront.net', 'ftp.mozilla.org'],
                    'Failed, redirected to unknown host. %s' %
                    self.response_info_failure_message(base_url, param, response))

            assert ('Unknown' != self.get_x_backend_server(response),
                    'Failed, x-backend-server was not in the response object %s' %
                    self.response_info_failure_message(base_url, param, response))

            if (
                product_alias['product_name'] != 'firefox-nightly-latest' and
                product_alias['product_name'] != 'firefox-aurora-latest' and
                product_alias['product_name'] != 'firefox-latest-euballot'
            ):
                assert '/win32/' in parsed_url.path, self.response_info(response)

    def test_robotstxt_exists(self, base_url):

        url = '%s/robots.txt' % base_url
        response = self._head_request(url)

        assert requests.codes.ok == response.status_code, 'Robots.txt does not exist'
