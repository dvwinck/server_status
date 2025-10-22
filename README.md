# Server Status Application

This is a Flask application that provides system status information through various endpoints.

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```cmd
     venv\Scripts\activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app_status.py
   ```

## Endpoints

- `/health`: Returns a simple "OK!" response
- `/info`: Returns system information (hostname, IP, OS, Python version, timestamp)
- `/status`: Returns system resource usage (CPU, memory, disk)

## Dependencies

- Flask: Web framework
- psutil: System monitoring library
