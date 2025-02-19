VocalizeHub is a Django-based web application called VocalizeHub that takes text input, uses the Web Speech API to read it aloud, and provides controls for pausing, resuming, and adjusting the speech rate.
**Features**
1.Convert text to speech
2.Adjustable speech rate (0.5x to 2x)
3.Play, pause, and resume functionality
4.Estimated duration display

vocalizehub/
│
├── manage.py                # Entry point for running the Django project
├── vocalizehub/             # Main project directory
│   ├── settings.py          # Global settings for the project
│   ├── urls.py              # URL routing for the entire project
│   └── wsgi.py              # WSGI entry point for deployment
│
├── speechify/               # App responsible for TTS functionality
│   ├── __init__.py          # Marks this directory as a Python package
│   ├── admin.py             # Admin interface configurations (if needed)
│   ├── apps.py              # App configuration file
│   ├── models.py            # Database models (if needed)
│   ├── views.py             # Handles HTTP requests for TTS
│   ├── urls.py              # URL routing specific to Speechify
│   └── templates/           # HTML templates specific to Speechify
│       └── home.html        # Main page for VocalizeHub

By keeping Speechify as a separate directory, all files related to TTS are grouped together.
This includes:
views.py: Defines how HTTP requests are processed for TTS.

urls.py: Maps URLs to views for TTS endpoints.

templates/: Contains HTML templates specific to TTS.



**How It Works**
Workflow:
Initialization:
The application initializes by loading available voices from the Web Speech API.
It automatically selects the "Microsoft BrianMultilingual Online" voice at index 105.

User Interaction:
The user clicks "Play" to start reading the text aloud.
The user can pause or resume playback using dedicated buttons.
The user adjusts the speech speed using a slider.

Speech Synthesis:
The Web Speech API converts text into speech using the selected voice and speed settings.

Dynamic Updates:
The application dynamically updates the estimated duration based on word count and speed changes.

Requirements
Python 3.9 or higher
Modern web browser with JavaScript enabled

Installation

Clone the repository:
git clone https://github.com/yourusername/vocalizehub.git
cd vocalizehub

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
venv\Scripts\activate


Start the web server:
python manage.py runserver
