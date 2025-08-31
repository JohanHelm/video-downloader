from yt_dlp import YoutubeDL
from threading import Thread


def get_urls(urls_file):
    with open(urls_file, 'r', encoding='utf-8') as file:
        return file.readlines()


def download_video(url):
    ydl_opts = {"paths":
                    {'home':
                         "/home/pp/PycharmProjects/video-downloader/output",
                     'temp': "/home/pp/PycharmProjects/video-downloader/parts"},
                "quiet": True,
                }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)


def spawn_threads(urls):
    threads = []
    for url in urls:
        threads.append(Thread(target=download_video, args=(url, ), daemon=True))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':

    urls = get_urls("downs_2.txt")
    spawn_threads(urls)

