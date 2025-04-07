# Space Cargo Management and Simulation System

## Overview

The Space Cargo Management and Simulation System is a comprehensive software solution designed to simulate and manage cargo operations aboard a space station. This system facilitates the placement, retrieval, rearrangement, and waste management of cargo, while also supporting time-based simulations and integrating machine learning for intelligent decision-making.

## Features

- **Cargo Placement**: Efficiently place cargo based on type, weight, and dimensions.
- **Cargo Retrieval**: Retrieve specific cargo items and manage surrounding cargo.
- **Rearrangement**: Optimize cargo arrangement for space and safety.
- **Waste Management**: Track and manage waste, including segregation and disposal.
- **Time Simulation**: Control and simulate time to observe changes in cargo and waste.
- **Machine Learning Integration**: Predict optimal cargo placement and waste classification.
- **Visualization**: Interactive visual interface for cargo management and monitoring.

## Technology Stack

- **Frontend**: React.js
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL / SQLite (for development)
- **Machine Learning**: Python (scikit-learn / PyTorch)
- **Deployment**: Docker (Docker Compose)
- **API Format**: REST APIs

## API Endpoints

### Cargo APIs
- `POST /api/place-cargo/`: Add new cargo
- `POST /api/retrieve-cargo/`: Fetch an item
- `POST /api/rearrange/`: Trigger rearrangement
- `GET /api/containers/`: Get container status

### Waste Management APIs
- `POST /api/waste/add/`: Add waste
- `POST /api/waste/process/`: Segregate waste
- `GET /api/waste/status/`: Track waste

### Time APIs
- `POST /api/simulate-time/`: Advance time
- `GET /api/time/status/`: Get current time

### Machine Learning APIs
- `POST /api/predict/placement/`: Suggest placement
- `POST /api/predict/waste-type/`: Classify waste

## Getting Started

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd space-cargo-management
   ```

2. **Set up the backend**:
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run migrations:
     ```
     python manage.py migrate
     ```
   - Start the server:
     ```
     python manage.py runserver
     ```

3. **Set up the frontend**:
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Start the development server:
     ```
     npm start
     ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.