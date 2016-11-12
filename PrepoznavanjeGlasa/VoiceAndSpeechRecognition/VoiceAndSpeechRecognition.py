#!/usr/bin/env python
import pyaudio
import wave
import speech_recognition as sr
import IdentificationServiceHttpClientHelper
import VerificationServiceHttpClientHelper
from pylab import *


def create_identification_profile():
    """Creates a profile on the server.

    Arguments:
    subscription_key -- the subscription key string
    locale -- the locale string
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    creation_response = helper.create_profile('en-us')

    print('Profile ID = {0}'.format(creation_response.get_profile_id()))


def create_verification_profile():
    """Creates a profile on the server.

    Arguments:
    subscription_key -- the subscription key string
    locale -- the locale string
    """
    helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    creation_response = helper.create_profile('en-us')

    print('Profile ID = {0}'.format(creation_response.get_profile_id()))


def delete_identification_profile():
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
        helper.delete_profile('dcfef31e-3bb8-44bd-b7a8-c7bd78166e39')
        print('The profile "Viktorija" has been deleted')

    if selected_profile == '5':
        helper.delete_profile('1ac67c64-ca2b-4ce2-99a7-6d0dc2c086e9')
        print('The profile "Dominik" has been deleted')

    else:
        print('There is no such profile\n')


def delete_verification_profile():
    """Delete the given profile from the server

    Arguments:
    subscription_key -- the subscription key string
    profile_id -- the profile ID of the profile to reset
    """

    helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    print('Please select the profile you wish to delete:\n')

    selected_profile = input('Your choice: ')

    if selected_profile == '1':
        helper.delete_profile('2e81d1c0-3f38-4e50-b106-3c1d07cd42f1')
        print('the profile "Goran" has been deleted')

    if selected_profile == '2':
        helper.delete_profile('a46788c0-0d7d-4e13-ae13-748f351aa63f')
        print('The profile "Meho" has been deleted')

    if selected_profile == '3':
        helper.delete_profile('71b4c6a3-4510-4299-bc2e-b12a2327b04d')
        print('The profile "Filip" has been deleted')

    if selected_profile == '4':
        helper.delete_profile('fa19e8ed-9ddf-405d-9ebc-df999d452642')
        print('The profile "Viktorija" has been deleted')

    if selected_profile == '5':
        helper.delete_profile('47c9dc42-6c8b-4600-8510-a50daf760931')
        print('The profile "Dominik" has been deleted')

    else:
        print('There is no such profile\n')


def print_all_identification_profiles():
    """Print all the profiles for the given subscription key.

    Arguments:
    subscription_key -- the subscription key string
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    profiles = helper.get_all_profiles()

    print('Profile ID, Locale, Enrollment Speech Time, Remaining Enrollment Speech Time,'
          ' Created Date Time, Last Action Date Time, Enrollment Status')
    for profile in profiles:
        print('{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            profile.get_profile_id(),
            profile.get_locale(),
            profile.get_enrollment_speech_time(),
            profile.get_remaining_enrollment_time(),
            profile.get_created_date_time(),
            profile.get_last_action_date_time(),
            profile.get_enrollment_status()))


def print_all_verification_profiles():
    """Print all the profiles for the given subscription key.

    Arguments:
    subscription_key -- the subscription key string
    """
    helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    profiles = helper.get_all_profiles()

    print('Profile ID, Locale, Enrollments Count, Remaining Enrollments Count,'
          ' Created Date Time, Last Action Date Time, Enrollment Status')
    for profile in profiles:
        print('{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            profile.get_profile_id(),
            profile.get_locale(),
            profile.get_enrollments_count(),
            profile.get_remaining_enrollments_count(),
            profile.get_created_date_time(),
            profile.get_last_action_date_time(),
            profile.get_enrollment_status()))


def get_identification_profile():
    """Get a speaker's profile with given profile ID

    Arguments:
    subscription_key -- the subscription key string
    profile_id -- the profile ID of the profile to resets
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    chosen_profile = input('Please select the profile you wish to see: ')

    if chosen_profile == '1':
        profile = helper.get_profile('842c6a50-dbc3-4aab-8ccc-6190b971b947')
        print(
            'Profile ID = {0}\nLocale = {1}\nEnrollments Speech Time = {2}\nRemaining Enrollment Time = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
                profile._profile_id,
                profile._locale,
                profile._enrollment_speech_time,
                profile._remaining_enrollment_time,
                profile._created_date_time,
                profile._last_action_date_time,
                profile._enrollment_status))

    elif chosen_profile == '2':
        profile = helper.get_profile('970d80f8-1737-422b-be2d-c49cf140a95a')
        print(
            'Profile ID = {0}\nLocale = {1}\nEnrollments Speech Time = {2}\nRemaining Enrollment Time = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
                profile._profile_id,
                profile._locale,
                profile._enrollment_speech_time,
                profile._remaining_enrollment_time,
                profile._created_date_time,
                profile._last_action_date_time,
                profile._enrollment_status))

    elif chosen_profile == '3':
        profile = helper.get_profile('c6101e08-45e8-4e3a-90ee-3aa795ae355e')
        print(
            'Profile ID = {0}\nLocale = {1}\nEnrollments Speech Time = {2}\nRemaining Enrollment Time = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
                profile._profile_id,
                profile._locale,
                profile._enrollment_speech_time,
                profile._remaining_enrollment_time,
                profile._created_date_time,
                profile._last_action_date_time,
                profile._enrollment_status))

    elif chosen_profile == '4':
        profile = helper.get_profile('dcfef31e-3bb8-44bd-b7a8-c7bd78166e39')
        print(
            'Profile ID = {0}\nLocale = {1}\nEnrollments Speech Time = {2}\nRemaining Enrollment Time = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
                profile._profile_id,
                profile._locale,
                profile._enrollment_speech_time,
                profile._remaining_enrollment_time,
                profile._created_date_time,
                profile._last_action_date_time,
                profile._enrollment_status))

    elif chosen_profile == '5':
        profile = helper.get_profile('1ac67c64-ca2b-4ce2-99a7-6d0dc2c086e9')
        print(
            'Profile ID = {0}\nLocale = {1}\nEnrollments Speech Time = {2}\nRemaining Enrollment Time = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
                profile._profile_id,
                profile._locale,
                profile._enrollment_speech_time,
                profile._remaining_enrollment_time,
                profile._created_date_time,
                profile._last_action_date_time,
                profile._enrollment_status))

    else:
        print('There is no such profile\n')


def get_verification_profile():
    """Get a speaker's profile with given profile ID

    Arguments:
    subscription_key -- the subscription key string
    profile_id -- the profile ID of the profile to resets
    """
    helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    chosen_profile = input('Please select the profile you wish to see: ')

    if chosen_profile == '1':
        profile = helper.get_profile('2e81d1c0-3f38-4e50-b106-3c1d07cd42f1')
        print(
            'Profile ID = {0}\nLocale = {1}\nEnrollments Completed = {2}\nRemaining Enrollments = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
                profile._profile_id,
                profile._locale,
                profile._enrollments_count,
                profile._remaining_enrollments_count,
                profile._created_date_time,
                profile._last_action_date_time,
                profile._enrollment_status))

    elif chosen_profile == '2':
        profile = helper.get_profile('a46788c0-0d7d-4e13-ae13-748f351aa63f')
        print(
            'Profile ID = {0}\nLocale = {1}\nEnrollments Completed = {2}\nRemaining Enrollments = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
                profile._profile_id,
                profile._locale,
                profile._enrollments_count,
                profile._remaining_enrollments_count,
                profile._created_date_time,
                profile._last_action_date_time,
                profile._enrollment_status))

    elif chosen_profile == '3':
        profile = helper.get_profile('71b4c6a3-4510-4299-bc2e-b12a2327b04d')
        print(
            'Profile ID = {0}\nLocale = {1}\nEnrollments Completed = {2}\nRemaining Enrollments = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
                profile._profile_id,
                profile._locale,
                profile._enrollments_count,
                profile._remaining_enrollments_count,
                profile._created_date_time,
                profile._last_action_date_time,
                profile._enrollment_status))

    elif chosen_profile == '4':
        profile = helper.get_profile('fa19e8ed-9ddf-405d-9ebc-df999d452642')
        print(
            'Profile ID = {0}\nLocale = {1}\nEnrollments Completed = {2}\nRemaining Enrollments = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
                profile._profile_id,
                profile._locale,
                profile._enrollments_count,
                profile._remaining_enrollments_count,
                profile._created_date_time,
                profile._last_action_date_time,
                profile._enrollment_status))

    elif chosen_profile == '5':
        profile = helper.get_profile('47c9dc42-6c8b-4600-8510-a50daf760931')
        print(
            'Profile ID = {0}\nLocale = {1}\nEnrollments Completed = {2}\nRemaining Enrollments = {3}\nCreated = {4}\nLast Action = {5}\nEnrollment Status = {6}\n'.format(
                profile._profile_id,
                profile._locale,
                profile._enrollments_count,
                profile._remaining_enrollments_count,
                profile._created_date_time,
                profile._last_action_date_time,
                profile._enrollment_status))

    else:
        print('There is no such profile\n')


def enroll_identification_profile():
    """Enrolls a profile on the server.

    Arguments:
    subscription_key -- the subscription key string
    profile_id -- the profile ID of the profile to enroll
    file_path -- the path of the file to use for enrollment
    force_short_audio -- waive the recommended minimum audio limit needed for enrollment
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    enroll_selected_profile = input('Please select the profile you wish to enroll: ')

    if enroll_selected_profile == '1':
        enrollment_response = helper.enroll_profile(
            '842c6a50-dbc3-4aab-8ccc-6190b971b947',
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Goran_pass.wav',
            'true')

    elif enroll_selected_profile == '2':
        enrollment_response = helper.enroll_profile(
            '970d80f8-1737-422b-be2d-c49cf140a95a',
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Meho_pass.wav',
            'true')

    elif enroll_selected_profile == '3':
        enrollment_response = helper.enroll_profile(
            'c6101e08-45e8-4e3a-90ee-3aa795ae355e',
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Filip_pass.wav',
            'true')

    elif enroll_selected_profile == '4':
        enrollment_response = helper.enroll_profile(
            'dcfef31e-3bb8-44bd-b7a8-c7bd78166e39',
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Viktorija_pass.wav',
            'true')

    elif enroll_selected_profile == '5':
        enrollment_response = helper.enroll_profile(
            '1ac67c64-ca2b-4ce2-99a7-6d0dc2c086e9',
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Dominik_pass.wav',
            'true')

    else:
        print('There is no such profile\n')

    print('Total Enrollment Speech Time = {0}'.format(enrollment_response.get_total_speech_time()))
    print('Remaining Enrollment Time = {0}'.format(enrollment_response.get_remaining_speech_time()))
    print('Speech Time = {0}'.format(enrollment_response.get_speech_time()))
    print('Enrollment Status = {0}'.format(enrollment_response.get_enrollment_status()))


def enroll_verification_profile():
    """Enrolls a profile on the server.

    Arguments:
    subscription_key -- the subscription key string
    profile_id -- the profile ID of the profile to enroll
    file_path -- the path of the file to use for enrollment
    """
    helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    enroll_selected_profile = input('Please select the profile you wish to enroll: ')

    if enroll_selected_profile == '1':
        enrollment_response = helper.enroll_profile(
            '2e81d1c0-3f38-4e50-b106-3c1d07cd42f1',
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Goran_pass.wav')

    elif enroll_selected_profile == '2':
        enrollment_response = helper.enroll_profile(
            'a46788c0-0d7d-4e13-ae13-748f351aa63f',
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Meho_pass.wav')

    elif enroll_selected_profile == '3':
        enrollment_response = helper.enroll_profile(
            '71b4c6a3-4510-4299-bc2e-b12a2327b04d',
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Filip_pass.wav')

    elif enroll_selected_profile == '4':
        enrollment_response = helper.enroll_profile(
            'fa19e8ed-9ddf-405d-9ebc-df999d452642',
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Viktorija_pass.wav')

    elif enroll_selected_profile == '5':
        enrollment_response = helper.enroll_profile(
            '47c9dc42-6c8b-4600-8510-a50daf760931',
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Dominik_pass.wav')

    else:
        print('There is no such profile\n')

    print('Enrollments Completed = {0}'.format(enrollment_response.get_enrollments_count()))
    print('Remaining Enrollments = {0}'.format(enrollment_response.get_remaining_enrollments()))
    print('Enrollment Status = {0}'.format(enrollment_response.get_enrollment_status()))
    print('Enrollment Phrase = {0}'.format(enrollment_response.get_enrollment_phrase()))


def reset_identification_enrollments():
    """Reset enrollments of a given profile from the server

    Arguments:
    subscription_key -- the subscription key string
    profile_id -- the profile ID of the profile to reset
    """

    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    selected_profile = input('Please select the profile you wish to reset: ')

    if selected_profile == '1':
        helper.reset_enrollments('842c6a50-dbc3-4aab-8ccc-6190b971b947')
        print('the profile "Goran" has been successfully reset')

    elif selected_profile == '2':
        helper.reset_enrollments('970d80f8-1737-422b-be2d-c49cf140a95a')
        print('The profile "Meho" has been successfully reset')

    elif selected_profile == '3':
        helper.reset_enrollments('c6101e08-45e8-4e3a-90ee-3aa795ae355e')
        print('The profile "Filip" has been successfully reset')

    elif selected_profile == '4':
        helper.reset_enrollments('dcfef31e-3bb8-44bd-b7a8-c7bd78166e39')
        print('the profile "Viktorija" has been successfully reset')

    elif selected_profile == '5':
        helper.reset_enrollments('1ac67c64-ca2b-4ce2-99a7-6d0dc2c086e9')
        print('The profile "Dominik" has been successfully reset')

    else:
        print('There is no such profile\n')


def reset_verification_enrollments():
    """Reset enrollments of a given profile from the server

    Arguments:
    subscription_key -- the subscription key string
    profile_id -- the profile ID of the profile to reset
    """

    helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    selected_profile = input('Please select the profile you wish to reset: ')

    if selected_profile == '1':
        helper.reset_enrollments('2e81d1c0-3f38-4e50-b106-3c1d07cd42f1')
        print('the profile "Goran" has been successfully reset')

    elif selected_profile == '2':
        helper.reset_enrollments('a46788c0-0d7d-4e13-ae13-748f351aa63f')
        print('The profile "Meho" has been successfully reset')

    elif selected_profile == '3':
        helper.reset_enrollments('71b4c6a3-4510-4299-bc2e-b12a2327b04d')
        print('The profile "Filip" has been successfully reset')

    elif selected_profile == '4':
        helper.reset_enrollments('fa19e8ed-9ddf-405d-9ebc-df999d452642')
        print('the profile "Viktorija" has been successfully reset')

    elif selected_profile == '5':
        helper.reset_enrollments('47c9dc42-6c8b-4600-8510-a50daf760931')
        print('The profile "Dominik" has been successfully reset')

    else:
        print('There is no such profile\n')


def record_new_file():
    """Record new .wav audio file and save it the current folder

    Arguments:
    """
    CHUNK = 1024
    FORMAT = pyaudio.paInt16  # paInt8
    CHANNELS = 1
    RATE = 16000  # sample rate
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = input("Please enter name for newly created file: ") + ".wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)  # buffer

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)  # 2 bytes(16 bits) per channel

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def show_waveform_and_spectrogram():
    """Show the waveform and spectrogram of the selected audio file with all the speaker's voice characteristics

    """
    selected_file = input('Please select the audio file you wish to visualize: ')

    spf = wave.open('C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/' + selected_file + '.wav', 'r')
    sound_info = spf.readframes(-1)
    sound_info = fromstring(sound_info, 'Int16')
    f = spf.getframerate()

    subplot(211)
    plot(sound_info)
    title('Waveform and Spectrogram of ' + selected_file + '.wav')

    subplot(212)
    specgram(sound_info, Fs=f, scale_by_freq=True, sides='default')

    show()
    spf.close()


def identify_file():
    """Identify an audio file on the server.

    Arguments:
    subscription_key -- the subscription key string
    file_path -- the audio file path for identification
    profile_ids -- an array of test profile IDs strings
    force_short_audio -- waive the recommended minimum audio limit needed for enrollment
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    identify_selected_file = input('Please enter the name of the desired sample to identify: ')

    profile_IDs = ['842c6a50-dbc3-4aab-8ccc-6190b971b947',
                   '970d80f8-1737-422b-be2d-c49cf140a95a',
                   'c6101e08-45e8-4e3a-90ee-3aa795ae355e',
                   'dcfef31e-3bb8-44bd-b7a8-c7bd78166e39',
                   '1ac67c64-ca2b-4ce2-99a7-6d0dc2c086e9']

    if identify_selected_file == 'Goran_pass':

        identification_response = helper.identify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Goran_pass.wav',
            profile_IDs,
            'true')

        if identification_response.get_identified_profile_id() == '842c6a50-dbc3-4aab-8ccc-6190b971b947':
            print('The sample voice is identified as that of Goran Horvat!')

    elif identify_selected_file == 'Meho_pass':
        identification_response = helper.identify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Meho_pass.wav',
            profile_IDs,
            'true')

        if identification_response.get_identified_profile_id() == '970d80f8-1737-422b-be2d-c49cf140a95a':
            print('The sample voice is identified as that of Zlatko Mehanović!')

    elif identify_selected_file == 'Filip_pass':
        identification_response = helper.identify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Filip_pass.wav',
            profile_IDs,
            'true')

        if identification_response.get_identified_profile_id() == 'c6101e08-45e8-4e3a-90ee-3aa795ae355e':
            print('The sample voice is identified as that of Filip Crnko!')

    elif identify_selected_file == 'Viktorija_pass':
        identification_response = helper.identify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Viktorija_pass.wav',
            profile_IDs,
            'true')

        if identification_response.get_identified_profile_id() == 'dcfef31e-3bb8-44bd-b7a8-c7bd78166e39':
            print('The sample voice is identified as that of Viktorija Sabo!')

    elif identify_selected_file == 'Dominik_pass':
        identification_response = helper.identify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Dominik_pass.wav',
            profile_IDs,
            'true')

        if identification_response.get_identified_profile_id() == '1ac67c64-ca2b-4ce2-99a7-6d0dc2c086e9':
            print('The sample voice is identified as that of Dominik Smiljanić!')

    else:
        print('There is no such file\n')

    print('Confidence = {0}'.format(identification_response.get_confidence()))


def verify_file():
    """Verify an audio file on the server.

    Arguments:
    subscription_key -- the subscription key string
    file_path -- the audio file path for verification
    profile_id -- profile ID to test the audio file with
    """
    helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(
        '359a42dd1486427daf6141db26af54c6')

    verify_selected_file = input('Please enter the name of the desired sample to verify: ')

    if verify_selected_file == 'Goran':

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Goran_pass.wav',
            '2e81d1c0-3f38-4e50-b106-3c1d07cd42f1')
        print('\n*Verifying Goran_pass.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Goran_test_pass.wav',
            '2e81d1c0-3f38-4e50-b106-3c1d07cd42f1')
        print('\n*Verifying Goran_test_pass.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Goran_test_fail.wav',
            '2e81d1c0-3f38-4e50-b106-3c1d07cd42f1')
        print('\n*Verifying Goran_test_fail.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

    elif verify_selected_file == 'Meho':
        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Meho_pass.wav',
            'a46788c0-0d7d-4e13-ae13-748f351aa63f')
        print('\n*Verifying Meho_pass.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Meho_test_pass.wav',
            'a46788c0-0d7d-4e13-ae13-748f351aa63f')
        print('\n*Verifying Meho_test_pass.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Meho_test_fail.wav',
            'a46788c0-0d7d-4e13-ae13-748f351aa63f')
        print('\n*Verifying Meho_test_fail.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

    elif verify_selected_file == 'Filip':
        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Filip_pass.wav',
            '71b4c6a3-4510-4299-bc2e-b12a2327b04d')
        print('\n*Verifying Filip_pass.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Filip_test_pass.wav',
            '71b4c6a3-4510-4299-bc2e-b12a2327b04d')
        print('\n*Verifying Filip_test_pass.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Filip_test_fail.wav',
            '71b4c6a3-4510-4299-bc2e-b12a2327b04d')
        print('\n*Verifying Filip_test_fail.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

    elif verify_selected_file == 'Viktorija':
        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Viktorija_pass.wav',
            'fa19e8ed-9ddf-405d-9ebc-df999d452642')
        print('\n*Verifying Viktorija_pass.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Viktorija_test_pass.wav',
            'fa19e8ed-9ddf-405d-9ebc-df999d452642')
        print('\n*Verifying Viktorija_test_pass.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Viktorija_test_fail.wav',
            'fa19e8ed-9ddf-405d-9ebc-df999d452642')
        print('\n*Verifying Viktorija_test_fail.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

    elif verify_selected_file == 'Dominik':
        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Dominik_pass.wav',
            '47c9dc42-6c8b-4600-8510-a50daf760931')
        print('\n*Verifying Dominik_pass.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Dominik_test_pass.wav',
            '47c9dc42-6c8b-4600-8510-a50daf760931')
        print('\n*Verifying Dominik_test_pass.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

        verification_response = helper.verify_file(
            'C:/Users/ghorv/Desktop/Zavrsni/PrepoznavanjeGlasa/Testing/Dominik_test_fail.wav',
            '47c9dc42-6c8b-4600-8510-a50daf760931')
        print('\n*Verifying Dominik_test_fail.wav*\n')
        print('Verification Result = {0}'.format(verification_response.get_result()))
        print('Confidence = {0}'.format(verification_response.get_confidence()))
        print('----------------------------------------------')

    else:
        print('There is no such file\n')


def recognition():
    while more:
        rec = sr.Recognizer()
        key = 'close program'
        with sr.Microphone() as source:
            audio = rec.listen(source)
        try:
            output = rec.recognize_google(audio)

            print(output)

            if output == key:
                return output

        except sr.UnknownValueError:
            print("error")
            exit()


if __name__ == "__main__":

    more = True

    print('1. Create an identification profile\n'
          '2. Create a verification profile\n'
          '3. Delete an identification profile\n'
          '4. Delete a verification profile\n'
          '5. List all identification profiles\n'
          '6. List all verification profiles\n'
          '7. Identification profile information\n'
          '8. Verification profile information\n'
          '9. Enroll identification profile\n'
          '10. Enroll verification profile\n'
          '11. Reset identification profile\n'
          '12. Reset verification profile\n'
          '13. Identify speaker\n'
          '14. Verify speaker\n'
          '15. Record new sample\n'
          '16. Show profile wave form and spectrogram\n'
          '17. Speech recognition\n\n')

    while more:

        selected_option = input('Please select an option: ')

        if selected_option == '1':
            selected_option = ''
            create_identification_profile()

        elif selected_option == '2':
            selected_option = ''
            create_verification_profile()

        elif selected_option == '3':
            selected_option = ''
            delete_identification_profile()

        elif selected_option == '4':
            selected_option = ''
            delete_verification_profile()

        elif selected_option == '5':
            selected_option = ''
            print_all_identification_profiles()

        elif selected_option == '6':
            selected_option = ''
            print_all_verification_profiles()

        elif selected_option == '7':
            selected_option = ''
            get_identification_profile()

        elif selected_option == '8':
            selected_option = ''
            get_verification_profile()

        elif selected_option == '9':
            selected_option = ''
            enroll_identification_profile()

        elif selected_option == '10':
            selected_option = ''
            enroll_verification_profile()

        elif selected_option == '11':
            selected_option = ''
            reset_identification_enrollments()

        elif selected_option == '12':
            selected_option = ''
            reset_verification_enrollments()

        elif selected_option == '13':
            selected_option = ''
            identify_file()
        elif selected_option == '14':
            selected_option = ''
            verify_file()

        elif selected_option == '15':
            selected_option = ''
            record_new_file()

        elif selected_option == '16':
            selected_option = ''
            show_waveform_and_spectrogram()

        elif selected_option == '17':
            selected_option = ''
            recognition()

        else:
            more = False
            break
