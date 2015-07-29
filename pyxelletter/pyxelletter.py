import json

import requests


class LetterNotFoundException(Exception):
    """
    Exception when file not found
    """
    pass


class Pyxelletter(object):

    def __init__(self, username, password):
        """
        :param username: Username (email) registered with in Pixelletter
        :param password: Password registered with in Pixelletter
        """
        self.username = username
        self.password = password

        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

        self.api_url = "https://api.pixelletter.de/v1/"

    def _make_get_request(self, path):
        r = self.session.get(self.api_url + path)
        if r.status_code == 200:
            return r.text
        else:
            return None

    def _make_delete_request(self, path):
        r = self.session.delete(self.api_url + path)
        return r.text

    def _make_post_request(self, path, data=None, files=None):
        r = self.session.post(self.api_url + path, data=data, files=files)
        if r.status_code == 200:
            return r.text
        else:
            return None

    def send_letter(self, file_path, destination='DE', duplex=True, color=False, user_transaction=None,
                    test_environment=False):
        """
        Send pdf-File
        :param file_path: path, where the file is located
        :param destination: country code of the destination country
        :param duplex: send letter in duplex
        :param color: send letter with color or black/white
        :param user_transaction: custom transaction id
        :param test_environment: Enable Test-Mode
        :return: Letter-ID if letter was sended successfully, else None
        """
        try:
            files = {'file': open(file_path, 'rb')}
        except IOError:
            raise LetterNotFoundException('File does not exist in specified path: {}'.format(file_path))

        data = {
            'settings[destination]': destination,
            'settings[simplex]': 'NONE' if duplex else 'ALL',
            'settings[color]': 'ALL' if color else 'NONE',
            'settings[user_transaction]': user_transaction,
            'settings[test_environment]': test_environment
        }
        send_req = self._make_post_request('letters', data=data, files=files)

        if send_req:
            return json.loads(send_req)['id']

        return None

    def get_letters(self):
        """
        Get an overview of all letters
        :return: List of all letters. Empty List if request failed.
        """
        letter_request = self._make_get_request("letters")

        if letter_request:
            return json.loads(letter_request)['orders']

        return []

    def get_letter_as_pdf(self, pixelleter_id):
        """
        Get specified letter by letter ID
        :param pixelleter_id: ID of the letter
        :return: PDF-Letter-Unicode-String if successful else None
        """
        pdf_letter = self._make_get_request('letters/{}.pdf'.format(pixelleter_id))

        if pdf_letter:
            return pdf_letter

        return None

    def get_letter_as_image(self, pixelletter_id):
        """
        Get specified letter as image
        :param pixelletter_id: ID of the letter
        :return: JPG-Letter-Unicode-String if successful else None
        """
        image_letter = self._make_get_request('letters/previews/{}_1.jpg'.format(pixelletter_id))

        if image_letter:
            return image_letter

        return None

    def cancel_letter(self, pixelletter_id):
        """
        Cancel specified letter
        :param pixelletter_id: ID of the letter
        :return: True if canceled, else False
        """
        cancel_request = self._make_delete_request('letters/{}'.format(pixelletter_id))
        status = json.loads(cancel_request)['status']

        if status == 200:
            return True

        return False