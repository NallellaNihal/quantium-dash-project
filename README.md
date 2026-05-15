# Quantium Dash Environment Setup

This repository contains the setup for the Quantium Dash visualization task.

## Tech Stack

- Python
- Dash
- Pandas

## Setup Instructions

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install dash pandas
pip install "dash[testing]"
```

### Run Application

```bash
python app.py
```

## Project Structure

- `app.py` → Sample Dash application
- `requirements.txt` → Python dependencies
- `data/` → Dataset folder
