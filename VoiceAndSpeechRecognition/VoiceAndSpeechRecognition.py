#!/usr/bin/env python
import pyaudio
import wave
import time
import pygame
import speech_recognition as sr
import IdentificationServiceHttpClientHelper
import VerificationServiceHttpClientHelper
from pylab import *
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.ttk import Treeview

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

file_name = ''
subscription_key = '359a42dd1486427daf6141db26af54c6'

ident_profile_IDs = ['842c6a50-dbc3-4aab-8ccc-6190b971b947',
                     '970d80f8-1737-422b-be2d-c49cf140a95a',
                     'c6101e08-45e8-4e3a-90ee-3aa795ae355e',
                     'dcfef31e-3bb8-44bd-b7a8-c7bd78166e39',
                     '1ac67c64-ca2b-4ce2-99a7-6d0dc2c086e9',
                     '00d5ef46-33b7-42b7-8a0c-a03546ed4113',
                     '87f77063-2f37-4a9c-a317-9eb61a2737eb',
                     '9fa54e07-87b7-4ceb-aefb-10d83fa00524',
                     '4a4b05b7-2641-4787-b927-1910a9bbeb28',
                     '594720fe-0e08-476d-9a2c-5c5061a303e1']

veri_profile_IDs = ['2e81d1c0-3f38-4e50-b106-3c1d07cd42f1',
                    'a46788c0-0d7d-4e13-ae13-748f351aa63f',
                    '71b4c6a3-4510-4299-bc2e-b12a2327b04d',
                    'fa19e8ed-9ddf-405d-9ebc-df999d452642',
                    '47c9dc42-6c8b-4600-8510-a50daf760931',
                    '232862c5-32e7-4bfc-818c-65a013ec22de',
                    'ed764992-cd5c-4804-9c73-bbb4f290a6a3',
                    'fd6d220e-6522-4cbc-91ee-eb45349fb67e',
                    '0fa1273f-312c-4a8e-afbc-949f01b07ff8',
                    'be20eb01-274b-415a-b3d4-74c45afda9a2']

labels = ['Goran Horvat',
          'Zlatko Mehanović',
          'Filip Crnko',
          'Viktorija Sabo',
          'Dominik Smiljanić',
          'Marko Gregurović',
          'Gabriel Ilić',
          'Stjepan Maričević',
          'Dino Džafović',
          'Fran Goldner']


def print_all_identification_profiles():
    """Print all the identification profiles for the given subscription key."""

    table = tk.Tk()
    table.title("List of identification profiles")
    IdentTable(table)
    table.mainloop()


def print_all_verification_profiles():
    """Print all the verification profiles for the given subscription key."""

    table = tk.Tk()
    table.title("List of verification profiles")
    VeriTable(table)
    table.mainloop()


def enroll_identification_profile():
    """Enrolls an identification profile on the server."""

    profile_enrollment = tk.Tk()
    profile_enrollment.title("Identification profile enrollment")
    EnrollIdentificationProfile(profile_enrollment)
    profile_enrollment.mainloop()


def enroll_verification_profile():
    """Enrolls a verification profile on the server."""

    profile_enrollment = tk.Tk()
    profile_enrollment.title("Verification profile enrollment")
    EnrollVerificationProfile(profile_enrollment)
    profile_enrollment.mainloop()


def reset_identification_enrollments():
    """Reset enrollments of a given identification profile from the server"""

    profile_reset = tk.Tk()
    profile_reset.title("Identification profile reset")
    ResetIdentificationProfile(profile_reset)
    profile_reset.mainloop()


def reset_verification_enrollments():
    """Reset enrollments of a given verification profile from the server"""

    profile_reset = tk.Tk()
    profile_reset.title("Verification profile reset")
    ResetVerificationProfile(profile_reset)
    profile_reset.mainloop()


def record_new_file():
    """Record new .wav audio file and save it the desired folder"""

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000  # sample rate
    RECORD_SECONDS = 20
    WAVE_OUTPUT_FILENAME = filedialog.asksaveasfilename() + '.wav'

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)  # buffer

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)  # 2 bytes(16 bits) per channel

    messagebox.showinfo(title="Sample completed", message="Recoding complete!")

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
    """Show the waveform and spectrogram of the selected audio file with all the speaker's voice characteristics"""
    filename = filedialog.askopenfilename()
    spf = wave.open(filename, 'r')
    sound_info = spf.readframes(-1)
    sound_info = fromstring(sound_info, 'Int16')
    f = spf.getframerate()

    subplot(211)
    plot(sound_info)
    title('Waveform and Spectrogram of ' + filename + '\n')

    subplot(212)
    specgram(sound_info, Fs=f, scale_by_freq=True, sides='default')

    show()
    spf.close()


def identify_file():
    """Identify an audio file on the server."""

    file_ident = tk.Tk()
    file_ident.title("Speaker identification")
    FileIdentification(file_ident)
    file_ident.mainloop()


def verify_file():
    """Verify an audio file on the server."""

    file_veri = tk.Tk()
    file_veri.title("Speaker verification")
    FileVerification(file_veri)
    file_veri.mainloop()


def recognition():
    """Listens for speech, recognises it and returns spoken text as messagebox"""
    rec = sr.Recognizer()
    key = 'close program'
    with sr.Microphone() as source:
        audio = rec.listen(source, 10)
    try:
        output = rec.recognize_google(audio)

        messagebox.showinfo(title="Speech recognition output", message='"' + output + '"')

        if output == key:
            return

    except sr.UnknownValueError:
        messagebox.showerror(title="Error", message="Error!")
        exit()


def verify_credentials():
    """Verifies if the user has the correct password for admin access"""
    pygame.mixer.pre_init(16000, 16, 2, 4096)
    pygame.mixer.init()
    pygame.mixer.music.load("credentials_needed.wav")
    pygame.mixer.music.play()
    time.sleep(1)

    rec = sr.Recognizer()
    login = "super secret password"

    with sr.Microphone() as source:
        audio = rec.listen(source, 5)
    try:
        output = rec.recognize_google(audio)

        if output == login:
            pygame.mixer.music.load("login_success.wav")
            pygame.mixer.music.play()

            credentials = tk.Tk()
            credentials.title("Admin menu")
            AccessAdminMenu(credentials)
            credentials.mainloop()

        else:
            pygame.mixer.music.load("login_fail.wav")
            pygame.mixer.music.play()

    except sr.UnknownValueError:
        messagebox.showerror(title="Error", message="Error!")


class VoiceAndSpeechRecognition(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="app_logo.ico")
        tk.Tk.wm_title(self, "Voice and Speech Recognition application")

        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        speaker_identification_menu = tk.Menu(menubar, tearoff=0)

        ident_profiles_menu = tk.Menu(menubar, tearoff=0)
        speaker_identification_menu.add_cascade(label="Profiles", menu=ident_profiles_menu)
        ident_profiles_menu.add_command(label="Show all profiles", command=print_all_identification_profiles)
        ident_profiles_menu.add_command(label="Enroll profile", command=enroll_identification_profile)
        ident_profiles_menu.add_command(label="Reset profile", command=reset_identification_enrollments)

        speaker_identification_menu.add_command(label="Identify speaker", command=identify_file)
        menubar.add_cascade(label="Speaker identification", menu=speaker_identification_menu)

        speaker_verification_menu = tk.Menu(menubar, tearoff=0)

        veri_profiles_menu = tk.Menu(menubar, tearoff=0)
        speaker_verification_menu.add_cascade(label="Profiles", menu=veri_profiles_menu)
        veri_profiles_menu.add_command(label="Show all profiles", command=print_all_verification_profiles)
        veri_profiles_menu.add_command(label="Enroll profile", command=enroll_verification_profile)
        veri_profiles_menu.add_command(label="Reset profile", command=reset_verification_enrollments)

        speaker_verification_menu.add_command(label="Verify speaker", command=verify_file)
        menubar.add_cascade(label="Speaker verification", menu=speaker_verification_menu)

        voice_samples_menu = tk.Menu(menubar, tearoff=0)
        voice_samples_menu.add_command(label="Record new sample", command=record_new_file)
        voice_samples_menu.add_command(label="Load sample", command=show_waveform_and_spectrogram)
        menubar.add_cascade(label="Voice samples", menu=voice_samples_menu)


        speech_recognition_menu = tk.Menu(menubar, tearoff=0)
        speech_recognition_menu.add_command(label="Start listening", command=recognition)
        menubar.add_cascade(label="Speech recognition", menu=speech_recognition_menu)

        admin_menu = tk.Menu(menubar, tearoff=0)
        admin_menu.add_command(label="Login", command=verify_credentials)
        menubar.add_cascade(label="Admin menu", menu=admin_menu)

        exit_menu = tk.Menu(menubar, tearoff=0)
        exit_menu.add_command(label="Exit", command=exit)
        menubar.add_cascade(label="Exit", menu=exit_menu)

        tk.Tk.config(self, menu=menubar)


class IdentTable(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky=(tk.N, tk.S, tk.W, tk.E))
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    def CreateUI(self):
        tv_ident = Treeview(self)
        tv_ident['show'] = 'headings'
        tv_ident['columns'] = (
        'profile_id',
        'profile_name',
        'enrollment_speech_time',
        'remaining_enrollment_speech_time',
        'created_date_time',
        'enrollment_status')

        tv_ident.heading("profile_id", text='Profile ID', anchor='w')
        tv_ident.column("profile_id", anchor="w", width=250)
        tv_ident.heading('profile_name', text='Profile name')
        tv_ident.column('profile_name', anchor='center', width=120)
        tv_ident.heading('enrollment_speech_time', text='Total length')
        tv_ident.column('enrollment_speech_time', anchor='center', width=100)
        tv_ident.heading('remaining_enrollment_speech_time', text='Time remaining')
        tv_ident.column('remaining_enrollment_speech_time', anchor='center', width=100)
        tv_ident.heading('created_date_time', text='Created on')
        tv_ident.column('created_date_time', anchor='center', width=100)
        tv_ident.heading('enrollment_status', text='Status')
        tv_ident.column('enrollment_status', anchor='center', width=100)
        tv_ident.grid(sticky=(tk.N, tk.S, tk.W, tk.E))
        self.treeview_ident = tv_ident
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def LoadTable(self):
        helper_ident = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(subscription_key)

        ident_profiles = helper_ident.get_all_profiles()

        for profile in ident_profiles:

            if profile.get_profile_id() == ident_profile_IDs[0]:
                profile_name = labels[0]
            elif profile.get_profile_id() == ident_profile_IDs[1]:
                profile_name = labels[1]
            elif profile.get_profile_id() == ident_profile_IDs[2]:
                profile_name = labels[2]
            elif profile.get_profile_id() == ident_profile_IDs[3]:
                profile_name = labels[3]
            elif profile.get_profile_id() == ident_profile_IDs[4]:
                profile_name = labels[4]
            elif profile.get_profile_id() == ident_profile_IDs[5]:
                profile_name = labels[5]
            elif profile.get_profile_id() == ident_profile_IDs[6]:
                profile_name = labels[6]
            elif profile.get_profile_id() == ident_profile_IDs[7]:
                profile_name = labels[7]
            elif profile.get_profile_id() == ident_profile_IDs[8]:
                profile_name = labels[8]
            elif profile.get_profile_id() == ident_profile_IDs[9]:
                profile_name = labels[9]


            self.treeview_ident.insert('', 'end', values=(profile.get_profile_id(),
                                                          profile_name,
                                                          profile.get_enrollment_speech_time(),
                                                          profile.get_remaining_enrollment_time(),
                                                          profile.get_created_date_time(),
                                                          profile.get_enrollment_status()))


class VeriTable(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky=(tk.N, tk.S, tk.W, tk.E))
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    def CreateUI(self):
        tv_veri = Treeview(self)
        tv_veri['show'] = 'headings'
        tv_veri['columns'] = (
        'profile_id',
        'profile_name',
        'enrollments_count',
        'remaining_enrollments_count',
        'created_date_time',
        'enrollment_status')

        tv_veri.heading("profile_id", text='Profile ID', anchor='w')
        tv_veri.column("profile_id", anchor="w", width=250)
        tv_veri.heading('profile_name', text='Profile name')
        tv_veri.column('profile_name', anchor='center', width=120)
        tv_veri.heading('enrollments_count', text='Enrollments count')
        tv_veri.column('enrollments_count', anchor='center', width=100)
        tv_veri.heading('remaining_enrollments_count', text='Remaining enrollments')
        tv_veri.column('remaining_enrollments_count', anchor='center', width=100)
        tv_veri.heading('created_date_time', text='Created on')
        tv_veri.column('created_date_time', anchor='center', width=100)
        tv_veri.heading('enrollment_status', text='Status')
        tv_veri.column('enrollment_status', anchor='center', width=100)
        tv_veri.grid(sticky=(tk.N, tk.S, tk.W, tk.E))
        self.treeview_veri = tv_veri
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def LoadTable(self):
        helper_veri = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(subscription_key)

        veri_profiles = helper_veri.get_all_profiles()

        for profile in veri_profiles:

            if profile.get_profile_id() == veri_profile_IDs[0]:
                profile_name = labels[0]
            elif profile.get_profile_id() == veri_profile_IDs[1]:
                profile_name = labels[1]
            elif profile.get_profile_id() == veri_profile_IDs[2]:
                profile_name = labels[2]
            elif profile.get_profile_id() == veri_profile_IDs[3]:
                profile_name = labels[3]
            elif profile.get_profile_id() == veri_profile_IDs[4]:
                profile_name = labels[4]
            elif profile.get_profile_id() == veri_profile_IDs[5]:
                profile_name = labels[5]
            elif profile.get_profile_id() == veri_profile_IDs[6]:
                profile_name = labels[6]
            elif profile.get_profile_id() == veri_profile_IDs[7]:
                profile_name = labels[7]
            elif profile.get_profile_id() == veri_profile_IDs[8]:
                profile_name = labels[8]
            elif profile.get_profile_id() == veri_profile_IDs[9]:
                profile_name = labels[9]

            self.treeview_veri.insert('', 'end', values=(
            profile.get_profile_id(),
            profile_name,
            profile.get_enrollments_count(),
            profile.get_remaining_enrollments_count(),
            profile.get_created_date_time(),
            profile.get_enrollment_status()))


class EnrollIdentificationProfile(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        global file_name

        profile_enroll = ttk.Label(parent, text="Please choose a profile you wish to enroll", font=NORM_FONT)
        profile_enroll.pack(fill=tk.BOTH)
        file_enroll = ttk.Label(parent, text="Please choose a file to enroll", font=NORM_FONT)
        profiles_cmb = ttk.Combobox(parent, state="readonly")
        profiles_cmb.pack(fill=tk.BOTH)
        file_enroll.pack(fill=tk.BOTH)
        profiles_cmb['values'] = [labels[0],
                                  labels[1],
                                  labels[2],
                                  labels[3],
                                  labels[4],
                                  labels[5],
                                  labels[6],
                                  labels[7],
                                  labels[8],
                                  labels[9]]

        name_txt = ttk.Entry(parent, textvariable=file_name)
        name_txt.pack(fill=tk.BOTH)
        browse_btn = ttk.Button(parent, text="...", command=lambda: self.browseClick(name_txt))
        browse_btn.pack(fill=tk.BOTH)

        enroll_profile_btn = ttk.Button(parent, text="Enroll profile", command=lambda: self.buttonClick(profiles_cmb.selection_get(), name_txt.get()))
        enroll_profile_btn.pack(fill=tk.BOTH)

    def browseClick(self, fn):
        file_name = filedialog.askopenfilename()
        fn.delete(0, tk.END)
        fn.insert(0, file_name)

    def buttonClick(self, selection, path):
        helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(subscription_key)

        profile_index = labels.index(selection)

        if  selection == labels[profile_index]:
            enrollment_response = helper.enroll_profile(ident_profile_IDs[profile_index], path)
            messagebox.showinfo(title="Success", message="Profile " +
                                                         selection + " successfully enrolled!\n\nTotal enrollment speech time: " +
                                                         str(enrollment_response.get_total_speech_time()) + "\nRemaining enrollment time: " +
                                                         str(enrollment_response.get_remaining_speech_time()) + "\nEnrollment status: " +
                                                         str(enrollment_response.get_enrollment_status()))


class EnrollVerificationProfile(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        global file_name

        profile_enroll = ttk.Label(parent, text="Please choose a profile you wish to enroll", font=NORM_FONT)
        profile_enroll.pack(fill=tk.BOTH)
        file_enroll = ttk.Label(parent, text="Please choose a file to enroll", font=NORM_FONT)
        profiles_cmb = ttk.Combobox(parent, state="readonly")
        profiles_cmb.pack(fill=tk.BOTH)
        file_enroll.pack(fill=tk.BOTH)
        profiles_cmb['values'] = [labels[0],
                                  labels[1],
                                  labels[2],
                                  labels[3],
                                  labels[4],
                                  labels[5],
                                  labels[6],
                                  labels[7],
                                  labels[8],
                                  labels[9]]

        name_txt = ttk.Entry(parent, textvariable=file_name)
        name_txt.pack(fill="both")
        browse_btn = ttk.Button(parent, text="...", command=lambda: self.browseClick(name_txt))
        browse_btn.pack(fill=tk.BOTH)

        enroll_profile_btn = ttk.Button(parent, text="Enroll profile", command=lambda: self.buttonClick(profiles_cmb.selection_get(), name_txt.get()))
        enroll_profile_btn.pack(fill=tk.BOTH)

    def browseClick(self, fn):
        file_name = filedialog.askopenfilename()
        fn.delete(0, tk.END)
        fn.insert(0, file_name)

    def buttonClick(self, selection, path):
        helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(subscription_key)

        profile_index = labels.index(selection)

        if  selection == labels[profile_index]:
            enrollment_response = helper.enroll_profile(veri_profile_IDs[profile_index], path)
            messagebox.showinfo(title="Success", message="Profile " +
                                                         selection + " successfully enrolled!\n\nTotal enrollments: " +
                                                         str(enrollment_response.get_enrollments_count()) + "\nRemaining enrollment: " +
                                                         str(enrollment_response.get_remaining_enrollments()) + "\nEnrollment status: " +
                                                         enrollment_response.get_enrollment_status() + "\nEnrollment phrase: " +
                                                         enrollment_response.get_enrollment_phrase())


class ResetIdentificationProfile(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        profile_choice = ttk.Label(parent, text="Please choose a profile you wish to reset", font=NORM_FONT)
        profile_choice.pack(fill=tk.BOTH)
        profiles_cmb = ttk.Combobox(parent, state="readonly")
        profiles_cmb.pack(fill=tk.BOTH)
        profiles_cmb['values'] = [labels[0],
                                  labels[1],
                                  labels[2],
                                  labels[3],
                                  labels[4],
                                  labels[5],
                                  labels[6],
                                  labels[7],
                                  labels[8],
                                  labels[9]]

        reset_profile_btn = ttk.Button(parent, text="Reset profile", command=lambda: self.buttonClick(profiles_cmb.selection_get()))
        reset_profile_btn.pack(fill=tk.BOTH)

    def buttonClick(self, selection):
        helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(subscription_key)

        profile_index = labels.index(selection)

        if  selection == labels[profile_index]:
            helper.reset_enrollments(ident_profile_IDs[profile_index])
            messagebox.showinfo(title="Success", message="Profile " + selection + " successfully reset!")


class ResetVerificationProfile(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        profile_choice = ttk.Label(parent, text="Please choose a profile you wish to reset", font=NORM_FONT)
        profile_choice.pack(fill=tk.BOTH)
        profiles_cmb = ttk.Combobox(parent, state="readonly")
        profiles_cmb.pack(fill=tk.BOTH)
        profiles_cmb['values'] = [labels[0],
                                  labels[1],
                                  labels[2],
                                  labels[3],
                                  labels[4],
                                  labels[5],
                                  labels[6],
                                  labels[7],
                                  labels[8],
                                  labels[9]]

        reset_profile_btn = ttk.Button(parent, text="Reset profile", command=lambda: self.buttonClick(profiles_cmb.selection_get()))
        reset_profile_btn.pack(fill=tk.BOTH)

    def buttonClick(self, selection):
        helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(subscription_key)

        profile_index = labels.index(selection)

        if selection == labels[profile_index]:
            helper.reset_enrollments(veri_profile_IDs[profile_index])
            messagebox.showinfo(title="Success", message="Profile " + selection + " successfully reset!")


class FileIdentification(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        global file_name

        identify_selected_file = ttk.Label(parent, text="Please choose a file you wish to identify", font=NORM_FONT)
        identify_selected_file.pack()
        name_txt = ttk.Entry(parent, textvariable=file_name)
        name_txt.pack(fill=tk.BOTH)
        browse_btn = ttk.Button(parent, text="...", command=lambda: self.browseClick(name_txt))
        browse_btn.pack(fill=tk.BOTH)

        identify_btn = ttk.Button(parent, text="Identify file", command=lambda: self.buttonClick(name_txt.get()))
        identify_btn.pack(fill=tk.BOTH)

    def browseClick(self, fn):
        file_name = filedialog.askopenfilename()
        fn.delete(0, tk.END)
        fn.insert(0, file_name)

    def buttonClick(self, file):

        helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(subscription_key)

        identification_response = helper.identify_file(file, ident_profile_IDs)
        if identification_response.get_identified_profile_id() == '00000000-0000-0000-0000-000000000000':
            messagebox.showinfo(title="Profile not found!", message="There was no match!")
        else:
            profile_index = ident_profile_IDs.index(identification_response.get_identified_profile_id())

        if identification_response.get_confidence() != "High":
            messagebox.showinfo(title="Profile not found!", message="There was no match!")

        elif identification_response.get_identified_profile_id() == ident_profile_IDs[profile_index]:
            messagebox.showinfo(title="Profile identified", message="The sample voice is identified as that of " + labels[profile_index] + "!\nConfidence = " + identification_response.get_confidence())


class FileVerification(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        global file_name

        verify_selected_file = ttk.Label(parent, text="Please choose a file you wish to verify", font=NORM_FONT)
        verify_selected_file.pack()
        name_txt = ttk.Entry(parent, textvariable=file_name)
        name_txt.pack(fill=tk.BOTH)
        browse_btn = ttk.Button(parent, text="...", command=lambda: self.browseClick(name_txt))
        browse_btn.pack(fill=tk.BOTH)

        profile_choice = ttk.Label(parent, text="Please choose a profile you wish to verify", font=NORM_FONT)
        profile_choice.pack(fill=tk.BOTH)
        profiles_cmb = ttk.Combobox(parent, state="readonly")
        profiles_cmb.pack(fill=tk.BOTH)
        profiles_cmb['values'] = [labels[0],
                                  labels[1],
                                  labels[2],
                                  labels[3],
                                  labels[4],
                                  labels[5],
                                  labels[6],
                                  labels[7],
                                  labels[8],
                                  labels[9]]

        verify_btn = ttk.Button(parent, text="Verify file", command=lambda: self.buttonClick(name_txt.get(), profiles_cmb.selection_get()))
        verify_btn.pack(fill=tk.BOTH)

    def browseClick(self, fn):
        file_name = filedialog.askopenfilename()
        fn.delete(0, tk.END)
        fn.insert(0, file_name)

    def buttonClick(self, file, selection):

        helper = VerificationServiceHttpClientHelper.VerificationServiceHttpClientHelper(subscription_key)

        profile_index = labels.index(selection)

        if selection == labels[profile_index]:
            verification_response = helper.verify_file(file, veri_profile_IDs[profile_index])
            messagebox.showinfo(title="Profile verified", message="*Verifying " + file + " *\n\nVerification Result = " + verification_response.get_result() + "\nConfidence = " + verification_response.get_confidence())


class AccessAdminMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        secret_message = ttk.Label(parent, text="Something super secret here!", font=LARGE_FONT, width=100)
        secret_message.pack(fill=tk.BOTH)


if __name__ == "__main__":
    app = VoiceAndSpeechRecognition()
    app.geometry("1280x720")
    app.mainloop()
