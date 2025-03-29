# DeepTrace

## Overview
DeepTrace is an **asynchronous web crawler** designed for scraping data from websites on the **Tor (`.onion`)** and **I2P (`.i2p`)** networks. Additionally, it features an **NLP-based hate speech classification** system for analyzing extracted text data.

---

## Features

### Asynchronous Web Crawling
- Concurrent crawling of **Tor** and **I2P** websites using `asyncio` and `aiohttp`.
- Data is saved as **HTML** files in the `archive/` directory.
- **CSV log (`data.csv`)** tracks URLs and timestamps.
- **Avoids redundant crawling** by storing temporary URLs in `temp/scraped.txt`.

### Randomization & Security
- Uses random **User-Agents** for enhanced anonymity.
- Implements **secure random strings** for various purposes.

### NLP-Based Hate Speech Analysis
- Utilizes a **pre-trained NLP model**: `Hate-speech-CNERG/dehatebert-mono-english`.
- Performs **automated hate speech classification** on extracted text.

### User-Friendly CLI Interface
- `main.py` provides an **interactive menu** for:
  - **Starting** web crawling on **Tor, I2P, or both**.
  - **Checking the Tor IP Address**.

### Continuous Background Processing
- Runs a **background thread** (`run_process_files_continuously`) for **automated file processing**.

---

## Prerequisites
To use this project, you need:
- **Python 3.10.x** (recommended)
- Install dependencies using:
  ```sh
  pip install -r requirements.txt
