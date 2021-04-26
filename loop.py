from pydub import AudioSegment
from pydub.utils import mediainfo


def shorten_audio(file_path, duration):
    """
        Shorten the audio located at file_path
        to duaration specified as an integer seconds
        that is less than total audio length
    """
    audio = AudioSegment.from_mp3(file_path)

    # Pull any tags from og audio file
    # TODO - doesn't bring over audio thumbnail art
    tags = mediainfo(file_path).get('TAG', {})

    spliced = audio[:duration*1000]
    spliced.export(
        file_path,
        format="mp3",
        tags=tags
    )
