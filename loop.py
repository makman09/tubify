from pydub import AudioSegment
from pydub.utils import mediainfo
from mutagen.id3 import ID3
import eyed3

from .utility import timestamp_to_milliseconds

def splice_audio(file_path, start, end):
    """
        Splice audio to specified selection
    """
    audio = AudioSegment.from_mp3(file_path)

    # Pull thumbnail
    tags = ID3(file_path)
    thumbnail = tags.get("APIC:").data

    # Pull any other tags from og audio file
    tags = mediainfo(file_path).get('TAG', {})

    # Get start and and end paramters
    # to pull the audio splice of interest
    start = timestamp_to_milliseconds(start)
    end = timestamp_to_milliseconds(end)

    spliced = audio[start:end]
    spliced.export(
        file_path,
        format="mp3",
        tags=tags
    )

    audiofile = eyed3.load(file_path)
    audiofile.tag.images.set(3, thumbnail, 'image/jpeg')
    audiofile.tag.save()