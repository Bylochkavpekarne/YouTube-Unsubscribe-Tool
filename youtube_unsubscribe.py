import time
import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_youtube():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("youtube", "v3", credentials=creds)

def list_subscriptions(youtube):
    ids = []
    page_token = None
    while True:
        resp = youtube.subscriptions().list(
            part="id",
            mine=True,
            maxResults=50,
            pageToken=page_token
        ).execute()
        for item in resp.get("items", []):
            ids.append(item["id"])
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return ids

def main():
    yt = get_youtube()
    subs = list_subscriptions(yt)
    print(f"Найдено подписок: {len(subs)}")

    if not subs:
        print("Подписок нет ✅")
        return

    deleted = 0
    for sid in subs:
        try:
            yt.subscriptions().delete(id=sid).execute()
            deleted += 1
            print(f"Отписано: {deleted}/{len(subs)}")
            time.sleep(0.3)  # пауза, чтобы не словить лимит
        except Exception as e:
            print(f"Ошибка при удалении {sid}: {e}")
            time.sleep(1)

    print("✅ Все подписки удалены.")

if __name__ == "__main__":
    main()
