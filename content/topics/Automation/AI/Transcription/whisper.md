---
title: "Making transcriptions using OpenAI's Whisper"
description: "Guidance page for using Whisper for translations and transcriptions"
keywords: "openai, whisper, translations, transcriptions"
date: 2023-06-06
weight: 2
author: "Ana Bianca Luca"
authorlink: "https://tilburgsciencehub.com/contributors/anabiancaluca/"
aliases:
  - /learn/whisper
  - /ai/transcriptions
---

## What is Whisper?

Whisper, developed by OpenAI, is an automatic speech recognition model. It can recognize multilingual speech, translate speech and transcribe audios. It has been trained on 680k hours of diverse multilingual data. Whisper is an API with two endpoints: `transcriptions` and `translations`. Specifically, it can transcribe audio in any of its 98 trained languages, and it can translate the audios in English only (for now).


## Getting started

Unlike ChatGPT, Whisper cannot be used from the browser, but has to be installed locally. It can be used either in Python or from the command line and the setup and usage is very easy. You can upload audio files under 25MB that have the following types: mp3, mp4, mpeg, mpga, m4a, wav or webm.

### Installation

Whisper is compatible with versions 3.8-3.11 of Python, so make sure you have the right version. To install Whisper simply use the following command in the `cmd`:

```
pip install -U openai-whisper
```

{{% tip %}}
If you encounter errors during this command, you may need an additional tool named [`rust`](https://www.rust-lang.org/learn/get-started). If errors persist, check Whisper's [guide](https://github.com/openai/whisper#setup) 

{{% /tip %}}

Additionally, it requires a command line tool called [`ffmpeg`](https://ffmpeg.org/). To install it we only need one additional line:

```
#for Windows using Chocolatey(https://chocolatey.org/)
choco install ffmpeg

#for Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg

#for Mac using Homebrew (https://brew.sh/)
brew install ffmpeg

#for Ubuntu
sudo apt update && sudo apt install ffmpeg

#for Linux
sudo pacman -S ffmpeg
```

### Python usage
To transcribe an audio file we simple give the file as an input to the API:

{{% codeblock %}}

```python
import openai
audio_file= open("/path/audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

```
{{% /codeblock %}}

The output is a json file of the transcribed text.

To translate a file into English we just use `openai.Audio.translate` instead of the above command.

{{% codeblock %}}
```python
import openai
audio_file= open("/path/audio.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)

```
{{% /codeblock %}}

Alternatively, we can use the following code which also allows to select which model to use for processing the audio file.

{{% tip %}}
There are five models that can be used for audio processing, which differ in terms of parameters used, language, memory required and computational speed. An overview of these models is available [here](https://github.com/openai/whisper#available-models-and-languages).

{{% /tip %}}


{{% codeblock %}}
```python
import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```
{{% /codeblock %}}

It can also detect the language of the audio:

{{% codeblock %}}
```python
import whisper

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("audio.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
```
{{% /codeblock %}}

{{% tip %}}
The maximum size of the accepted audio files is 25MB. If you have longer files, you can split it into smaller parts of maximum 25MB. It is best to split the files at the end of sentences, not in the middle of them since this can lead to losing the context. One tool to do this is [PyDub Python package](https://github.com/jiaaro/pydub).

{{% /tip %}}

{{% codeblock %}}
```python
from pydub import AudioSegment

song = AudioSegment.from_mp3("example.mp3")

# PyDub handles time in milliseconds
ten_minutes = 10 * 60 * 1000

first_10_minutes = song[:ten_minutes]

first_10_minutes.export("example_10.mp3", format="mp3")
```
{{% /codeblock %}}

{{% tip %}}
To improve the accuracy of the transcriptions you can use [prompts](https://platform.openai.com/docs/guides/speech-to-text/prompting). Depending on the given style of the prompt, the model will try to replicate it and deliver a specific style of text (eg. using acronyms, punctuation, filler words).
{{% /tip %}}

### Command line usage

To transcribe more files at the same time using one of the five models using:
```
whisper audio.mp4 audio.mp3 audio.wav --model medium
```
We can also mention the language to perform the transcription:
```
whisper japanese.wav --language Japanese
```

To translate a file we can use:
```
whisper japanese.wav --language Japanese --task translate
```


## See also
[Whisper open source code](https://github.com/openai/whisper)

[Whisper documentation](https://platform.openai.com/docs/guides/speech-to-text/prompting)
