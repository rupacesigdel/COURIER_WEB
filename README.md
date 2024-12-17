<h1 align="center" >
  Python/Django - Courier Management System 🚚📦
</h1>

[COURIER_WEB](https://github.com/rupacesigdel/COURIER_WEB.git) is a  comprehensive Django-based web application to manage courier services efficiently, including bookings, sorting hubs, pickups, and delivery processes. The project integrates Google Maps for enhanced location management and uses Daytona for a streamlined development environment.

---

## Contents
- [Features](#features)
- [Demo Video](#demo-video)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Demo Video
[Watch the demo video](https://github.com/user-attachments/assets/9f5d865a-2582-49c8-a07b-02e896bcfff1)

---
## Features
- User-Friendly Interface: Simplified management of courier-related tasks with an intuitive design.
- Bookings: Create and manage bookings for parcels.
- Sorting Hub: Classify and organize parcels by categories and destinations.
- Pickups: Schedule parcel pickups for specific addresses.
- Last-Mile Delivery: Track and update parcel delivery statuses.
- Google Maps Integration: Interactive location selection for precise destinations.
- Responsive Design: Works seamlessly on desktops, tablets, and mobile devices.
- Environment Management with Daytona: Simplifies development and deployment with pre-configured containerized environments.

## Tech Stack
- Frontend: HTML5, CSS3, Bootstrap
- Backend: Python 3.9+, Django Framework
- Database: PostgreSQL / SQLite
- Environment Management: Daytona (Containerized)
- API: Google Maps API
- Version Control: Git


## Prerequisites
- Python 3.9+ installed on your system.
- Docker and Docker Compose installed.
- Google Maps API Key for location-based services.
- Daytona installed for environment management

## Google Maps Integration
- Setup:
- Go to the Google Cloud Console.
- Enable the Maps JavaScript API.
- Get the API key and set it in the GOOGLE_MAPS_API_KEY environment variable.

---

## Daytona
- Works with any Git platform: GitHub, GitLab, Bitbucket.
- Compatible with any IDE: Vim, VS Code, JetBrains IDEs.
- Runs anywhere: Localhost, AWS, Azure, GCP, Digital Ocean.
- Flexible and efficient for modern development workflows.

## Installation

1. **Create the Daytona Environment**:
Initialize the project directly with Daytona:
  ```sh
    daytona create https://github.com/rupacesigdel/COURIER_WEB.git
  ```
2. **Create the .env file:**
- Get the API key and set it in the GOOGLE_MAPS_API_KEY environment variable.

3. **Run the Application: Start the Django server:**:
   ```sh
   python manage.py runserver
   ```
4. **Access the Application**:
Open your browser and navigate to:
```sh
http://localhost:8000
```

---


## Usage
- Create Bookings: Add new courier bookings via the booking form.
- Sort Parcels: Categorize and assign destinations to parcels in the Sorting Hub.
- Schedule Pickups: Request pickups for courier items.
- Manage Deliveries: Track and update delivery statuses.

## Contributing
- Fork the repository.
- Create a Feature Branch: git checkout -b feature-name
- Commit Your Changes: git commit -m 'Description of changes'
- Push the Branch: git push origin feature-name
- Open a Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the contributors and the open-source community for their invaluable tools and resources.
- Special appreciation to the Daytona team for simplifying the development environment setup.
- Gratitude to Google Maps API for providing interactive and reliable location services.
- A big thank you to everyone who provided feedback and helped refine this project.

---

Feel free to customize this `README.md` file according to your project's specific details and requirements.
