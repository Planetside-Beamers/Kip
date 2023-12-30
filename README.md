# Kip - PlanetSide 2 Data Dashboard

Kip is a Python application designed to fetch, process, and display data from PlanetSide 2, offering real-time insights and aggregate statistics for players and events. This project focuses on creating a dashboard and OBS overlays for displaying player stats and other game-related data.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Fetch and process general character data via REST API.
- Log real-time event data from PlanetSide 2 through a WebSocket stream.
- Future capabilities for a dashboard and OBS overlays.

## Getting Started

### Prerequisites
- Python 3.8+
- Dependencies listed in `requirements.txt`.

### Installation
1. **Clone the Repository**
```
git clone https://github.com/your-username/Kip.git
```

2. **Setup a Virtual Environment (Optional but Recommended)**
```
python -m venv venv
source venv/bin/activate # For Unix or MacOS
venv\Scripts\activate # For Windows
```

3. **Install Dependencies**
```
pip install -r requirements.txt
```

4. **Environment Variables**
- Set `PS2_API_KEY` in your environment to your PlanetSide 2 API key.

## Usage
- **Fetching Character Data**
Run the `example_usage` function in `rest_api_service.py` to fetch and process character data.
- **WebSocket Stream**
Execute `websocket_service.py` to start listening to the PlanetSide 2 WebSocket stream.

## Project Structure
- `models/`: ORM classes for database models.
- `controllers/`: Business logic for processing data.
- `services/`: External interactions like WebSocket and REST API calls.
- `views/`: (Future Development) Components for the dashboard and overlays.
- `requirements.txt`: List of project dependencies.

## Contributing
Contributions to Kip are welcome! Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the [LICENSE] - see the LICENSE.md file for details.

## Contact
Email - [Cygnus](mailto:cygnus@cygnusxone.com)
Discord - CygnusXUno

