from pytube import Playlist


def main():
    url: str = "https://www.youtube.com/playlist?list=PLTD74k-jahHwX7ogz74-XYdxERX4AWj_8"
    try:
        playlist = Playlist(url)
        for video in playlist.videos:
            video.streams.first().download()
    except Exception as e:
        print(e)
        raise Exception('Some exception occurred.')
    print('All YouTube audio downloaded successfully.')


if __name__ == "__main__":
    main()
