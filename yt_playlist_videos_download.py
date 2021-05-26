from pytube import Playlist


def main():
    url: str = # Insert the url of the playlist you want to download
    try:
        # Create a object of playlist
        playlist = Playlist(url)
        # Loop through all the videos from the playlist
        for video in playlist.videos:
            # After create a stream from each child of the parent object
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
