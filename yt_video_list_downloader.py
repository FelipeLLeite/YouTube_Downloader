from pytube import YouTube


def main():
    # Insert the url of the video you want to download
    url_list: list = [
        "https://www.youtube.com/watch?v=99XzyUgDvVI",
        "https://www.youtube.com/watch?v=g2zX1GOBjo8",
    ]
    for url in url_list:
        try:
            # Create a object of YouTube
            video = YouTube(url)
            # The streams parameter, according to pytube official documentation,
            # "Interface to query both adaptive (DASH) and progressive streams."
            # Now we can call the first() method. This method return:
            # "the first result of this query or None if the result doesn’t contain any streams."
            # To finalize is to download the video that exist in the streams parameter in the
            # video obj (Youtube instance)
            video.streams.first().download()
        except Exception as e:
            # If any Exception occurs
            print(e)
            raise Exception('Some exception occurred.')
    print('Everything downloaded successfully.')


if __name__ == "__main__":
    main()
