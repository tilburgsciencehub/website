---
title: "Run Machine Learning Models in the Cloud with Replicate"
description: "Use Replicate's API to run models like Whisper and Flux without installing dependencies or managing GPUs"
keywords: "replicate, machine learning, cloud computing, API, whisper, flux, image generation, transcription"
date: 2026-02-03
weight: 3
author: "Albert Major"
aliases:
  - /learn/replicate
  - /ai/replicate
  - /cloud-ml
---

## The Problem

You have 50 hours of interview recordings to transcribe. Or you need illustrations for a paper. Or scanned documents to digitize.

You've heard ML models can do this. But then you look at the installation instructions: CUDA drivers, PyTorch builds, 20GB model downloads, GPU memory errors. Your laptop fan spins up just reading the requirements.

**Replicate lets you skip all of that.** You send an API request, models run on their GPUs, and you get results back. No local setup, no driver headaches — you pay by the second for what you use.

This guide covers setup, running your first model, transcribing audio with Whisper, and estimating costs for typical research workloads. Every code snippet is copy-paste ready.

---

## Getting Started

### 1. Create an account

Go to [replicate.com/signin](https://replicate.com/signin) and sign up. The account is free. You'll add a payment method before running models, but you're only charged for actual usage.

### 2. Get your API token

Go to [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens). Click **Create token**, give it a name like `research-project`, and copy it.

### 3. Set it as an environment variable

{{% codeblock %}}
```bash
export REPLICATE_API_TOKEN=r8_your_token_here
```
{{% /codeblock %}}

On Windows (PowerShell):

{{% codeblock %}}
```powershell
$env:REPLICATE_API_TOKEN = "r8_your_token_here"
```
{{% /codeblock %}}

{{% warning %}}
**Keep your token private.** Anyone with it can run models and rack up charges on your account. Never commit it to Git or paste it into shared notebooks. If exposed, revoke it immediately at [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens).
{{% /warning %}}

### 4. Install the Python client

{{% codeblock %}}
```bash
pip install replicate
```
{{% /codeblock %}}

That's the only dependency. No CUDA, no PyTorch, no driver configuration.

---

## Try It: Run a Model

The main function is `replicate.run()`. You give it a model name and inputs, it runs on their GPUs, and you get results back.

Here's the simplest example — generating an image:

{{% codeblock %}}
```python
import replicate

output = replicate.run(
    "black-forest-labs/flux-schnell",
    input={"prompt": "diagram of a neural network, technical illustration, white background"}
)

with open("output.webp", "wb") as f:
    f.write(output[0].read())
```
{{% /codeblock %}}

Three lines of real logic. No GPU required on your machine.

---

## Transcribing Audio with Whisper

Transcribing interviews is one of the most time-consuming parts of qualitative research. Whisper, developed by OpenAI, handles multiple languages and produces timestamped output.

Running Whisper locally requires a capable GPU — the large model needs 10+ GB of VRAM. On Replicate, you skip that entirely.

{{% codeblock %}}
```python
import replicate

output = replicate.run(
    "openai/whisper",
    input={
        "audio": open("interview.mp3", "rb"),
        "model": "large-v3",
        "transcription": "plain text",
        "language": "en"
    }
)

print(output["transcription"])
```
{{% /codeblock %}}

**Output formats:**

- `"plain text"` — clean transcript
- `"srt"` or `"vtt"` — subtitles with timestamps, useful for aligning text with audio segments

**Language:** Set `"language": "en"` to force English, or omit it to let Whisper auto-detect the language.

**Speaker identification:** Use `thomasmol/whisper-diarization` if you need to know who said what. It labels each segment by speaker.

**Batch processing:** For large jobs, `vaibhavs10/incredibly-fast-whisper` is optimized for throughput and costs less per minute of audio.

---

## Other Research Use Cases

The same `replicate.run()` pattern works for any model on the platform. Here are two common research workflows.

### Document Digitization (OCR)

Scanned documents, historical archives, printed forms — traditional OCR struggles with complex layouts. Models like `cuuupid/marker` combine OCR with layout analysis:

{{% codeblock %}}
```python
import replicate

output = replicate.run(
    "cuuupid/marker",
    input={"document": open("scanned_report.pdf", "rb")}
)

# Output is Markdown with tables and formatting preserved
with open("extracted.md", "w") as f:
    f.write(output)
```
{{% /codeblock %}}

### Image Analysis

Need to extract information from images? Vision-language models can describe images and answer questions about them:

{{% codeblock %}}
```python
import replicate

output = replicate.run(
    "yorickvp/llava-v1.6-34b",
    input={
        "image": open("chart.png", "rb"),
        "prompt": "What are the key trends shown in this chart?"
    }
)

print("".join(output))
```
{{% /codeblock %}}

### Browse More Models

Replicate hosts thousands of models at [replicate.com/explore](https://replicate.com/explore). Each model page shows what it does, what inputs it accepts, and the cost per run.

---

## Making Your Work Reproducible

Models on Replicate get updated. If you call a model by name, you get the latest version — which might behave differently next month.

To lock in a specific version, use the full version hash:

{{% codeblock %}}
```python
# Latest version (may change)
output = replicate.run("openai/whisper", input={...})

# Pinned version (always the same)
output = replicate.run(
    "openai/whisper:8099696689d249cf8b122d833c36a428d2d9c3a2e6bf9c4445c1b7bb2856345a",
    input={...}
)
```
{{% /codeblock %}}

Find version hashes on any model's "Versions" tab on Replicate. Record them in your project's README or requirements file so collaborators can reproduce your results exactly.

---

## Handling Long-Running Jobs

For short tasks, `replicate.run()` blocks until completion and returns the result directly. For longer jobs — hour-long audio files, large document batches — submit the job and check back later:

{{% codeblock %}}
```python
import replicate

# Submit without waiting
prediction = replicate.predictions.create(
    model="openai/whisper",
    input={
        "audio": "https://example.com/long_lecture.mp3",
        "model": "large-v3"
    }
)

print(f"Job ID: {prediction.id}")
print(f"Status: {prediction.status}")

# Check later
prediction = replicate.predictions.get(prediction.id)
if prediction.status == "succeeded":
    print(prediction.output)
```
{{% /codeblock %}}

{{% tip %}}
If your files are already hosted online (university server, cloud storage), pass the URL directly instead of uploading. It's faster.
{{% /tip %}}

---

## Quick Reference

**Install:**

{{% codeblock %}}
```bash
pip install replicate
export REPLICATE_API_TOKEN=r8_...
```
{{% /codeblock %}}

**Run a model:**

{{% codeblock %}}
```python
import replicate
output = replicate.run("model/name", input={...})
```
{{% /codeblock %}}

**Pin a version:**

{{% codeblock %}}
```python
output = replicate.run("model/name:version_hash", input={...})
```
{{% /codeblock %}}

**Async job:**

{{% codeblock %}}
```python
prediction = replicate.predictions.create(model="...", input={...})
# Later: replicate.predictions.get(prediction.id)
```
{{% /codeblock %}}

---

## See Also

- [Replicate documentation](https://replicate.com/docs) — full API reference
- [Replicate model explorer](https://replicate.com/explore) — browse available models
- [Making transcriptions with Whisper](/topics/automation/ai/transcription/whisper/) — run Whisper locally instead
- [Extract Data From APIs](/topics/collect-store/data-collection/web-scraping/extract-data-api/) — general API guide
