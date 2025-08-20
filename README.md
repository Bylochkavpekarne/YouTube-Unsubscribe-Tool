# YouTube-Unsubscribe-Tool

What you will need in advance

A personal Google account (regular @gmail.com). If you have a work/school account, the administrator may restrict access to the API.

Any modern browser (Chrome/Edge/Firefox).

Python installed on your PC (if you haven't installed it yet, you can do so later).

1) Create a project in Google Cloud Console

Open: https://console.cloud.google.com/

At the top left, click on the project selector (usually labeled “Select project”).

Click “New project.”

Fill in:

Project name: for example, YouTube Unsubscribe Tool.

Organization/Location: if it is a personal account, you can leave “No organization.”

Click “Create.”

After creation, make sure that this project is selected in the header.

2) Enable YouTube Data API v3

In the left menu, go to: APIs & Services → Library.

In the search bar, enter: YouTube Data API v3.

Open the API page and click “Enable.”

If you see “Manage” instead of the “Enable” button, it means that the API is already enabled.

3) Configure the OAuth consent screen

Google requires you to configure the “Consent Screen” even if you are only using the API for yourself.

Go to: APIs & Services → OAuth consent screen.

Select the user type:

External — for a personal account (recommended).

Internal is only available for Google Workspace domains.

Click Create.

Fill in the App information:

App name: for example, YouTube Unsubscribe Tool.

User support email: your Gmail.

(Optional) Logo and links — you don't have to fill this in.

App domain — you can skip this (for a personal project).

Developer contact information — your Gmail (required).

Click Save and continue.

(Optional) Add Scopes (access areas)

You don't need to add anything at the “Scopes” step — the script will request the necessary scope during authorization.
But if you want, add:

https://www.googleapis.com/auth/youtube.force-ssl (this is the main scope for reading/deleting subscriptions).

Click Save and continue.

Add test users

In the “Test users” step, click Add users.

Enter your Google email address (the one you used to subscribe to YouTube).

Click Save and continue → Return to the panel.

Note: In Testing mode, you can add up to 100 test users.
Refresh tokens for the test application have a limited lifespan (usually up to 7 days). If you log out after a week, simply log in again when you run the script.

4) Create an OAuth client ID (Desktop App)

Go to: APIs and Services → Credentials.

Click Create Credentials → OAuth client ID.

Application type: select Desktop app.

Name: for example, YouTube Unsubscribe Desktop.

Click Create.

In the window that appears, click Download JSON. The file will be named something like this:

client_secret_1234567890-abcdef.apps.googleusercontent.com.json

5) Rename and place client_secret.json next to the script

Create a folder for the project (for example, C:\YouTubeUnsub\).

Put your Python script (youtube_unsubscribe.py) in it.

Rename the downloaded JSON to client_secret.json (or leave the original name and correct the file name in the code).

As a result, the folder should contain:

youtube_unsubscribe.py

# My Telegram

https://t.me/Bylochka_V_Pekarne
client_secret.json

requirements.txt

