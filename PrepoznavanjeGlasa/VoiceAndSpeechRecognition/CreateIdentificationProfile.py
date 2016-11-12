""" Copyright (c) Microsoft. All rights reserved.
Licensed under the MIT license.

Microsoft Cognitive Services (formerly Project Oxford): https://www.microsoft.com/cognitive-services

Microsoft Cognitive Services (formerly Project Oxford) GitHub:
https://github.com/Microsoft/ProjectOxford-ClientSDK

Copyright (c) Microsoft Corporation
All rights reserved.

MIT License:
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ""AS IS"", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import IdentificationServiceHttpClientHelper
import sys


def create_profile():
    """Creates a profile on the server.

    Arguments:
    subscription_key -- the subscription key string
    locale -- the locale string
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    creation_response = helper.create_profile('en-us')

    print('Profile ID = {0}'.format(creation_response.get_profile_id()))


def delete_profile():
    """ Deletes a profile from the server

    Arguments:
    profile_id -- the profile ID string of user to delete
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    print('Please select the profile you wish to delete:\n')

    selected_profile = input('Your choice: ')

    if selected_profile == '1':
        helper.delete_profile('842c6a50-dbc3-4aab-8ccc-6190b971b947')
        print('the profile "Goran" has been deleted')

    if selected_profile == '2':
        helper.delete_profile('970d80f8-1737-422b-be2d-c49cf140a95a')
        print('The profile "Meho" has been deleted')

    if selected_profile == '3':
        helper.delete_profile('c6101e08-45e8-4e3a-90ee-3aa795ae355e')
        print('The profile "Filip" has been deleted')

    if selected_profile == '4':
        # helper.delete_profile('c6101e08-45e8-4e3a-90ee-3aa795ae355e')
        print('There is no such profile')

    if selected_profile == '5':
        helper.delete_profile('f4d974e4-33f2-4ebe-9865-646c66b3f62f')
        print('There is no such profile')

if __name__ == "__main__":

    while True:
        # create_profile()

        delete_profile()
