from pytube import YouTube


def downloader(link, file_name):
    try:
        yt = YouTube(link)
        downolad = yt.streams.get_highest_resolution()
        downolad.download(filename=f"{file_name}.mp4")
    except:
        print('Something went wrong...')
    else:
        print('Successfully')


def main():
    link = input('Enter url to download: ')
    file_name = input('Enter filename: ')
    downloader(link, file_name)


if __name__ == '__main__':
    main()