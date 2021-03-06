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

class IdentificationEnrollmentResponse:
    """This class encapsulates the enrollment response."""

    _TOTAL_SPEECH_TIME = 'enrollmentSpeechTime'
    _REMAINING_SPEECH_TIME = 'remainingEnrollmentSpeechTime'
    _SPEECH_TIME = 'speechTime'
    _ENROLLMENT_STATUS = 'enrollmentStatus'

    def __init__(self, response):
        """Constructor of the EnrollmentResponse class.

        Arguments:
        response -- the dictionary of the deserialized python response
        """
        self._total_speech_time = response.get(self._TOTAL_SPEECH_TIME, None)
        self._remaining_speech_time = response.get(self._REMAINING_SPEECH_TIME, None)
        self._speech_time = response.get(self._SPEECH_TIME, None)
        self._enrollment_status = response.get(self._ENROLLMENT_STATUS, None)

    def get_total_speech_time(self):
        """Returns the total enrollment speech time"""
        return self._total_speech_time

    def get_remaining_speech_time(self):
        """Returns the remaining enrollment speech time"""
        return self._remaining_speech_time

    def get_speech_time(self):
        """Returns the speech time for this enrollment"""
        return self._speech_time

    def get_enrollment_status(self):
        """Returns the enrollment status"""
        return self._enrollment_status
