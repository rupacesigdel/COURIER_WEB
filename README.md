# Courier Management System 🚚📦
A comprehensive Django-based web application to manage courier services efficiently, including bookings, sorting hubs, pickups, and delivery processes. The project integrates Google Maps for enhanced location management and uses Daytona for a streamlined development environment.

---

## Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Demo Video](#demo-video)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Daytona Integration](#daytona-integration)
  - [Google Maps Integration](#google-maps-integration)
- [Usage](#usage)
- [Contributing](#contributing)
- [Fork the repository](#fork-the-repository)
- [License](#license)
- [Acknowledgments](#acknowledgments)

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

## Project Structure
courier-management-system/
- ├── courier/
- │   ├── settings.py
- │   ├── urls.py
- │   ├── wsgi.py
- ├── templates/
- │   ├── couriers/
- │   │   ├── base.html
- │   │   ├── create_booking.html
- │   │   ├── sorting_hub.html
- │   │   └── ...
- ├── static/
- │   ├── css/
- │   ├── js/
- │   └── images/
- ├── manage.py
- └── daytona.yml

---


## Setup and Installation
1. **Clone the Repository**:
  ```sh
  git clone https://github.com/your-username/courier-management-system.git
  cd courier-management-system
  ```
2. **Install Daytona**:
Run the following command to install Daytona:

  ```sh
  curl -fsSL https://get.daytona.dev | bash
  ```
3. **Configure Daytona**:
Initialize Daytona in the project directory:
  ```sh
  daytona init
  Edit the daytona.yml file:
  
  yaml
  Copy code
  services:
    django:
      image: python:3.9
      volumes:
        - .:/app
      working_dir: /app
      environment:
        - DEBUG=True
        - SECRET_KEY=your-secret-key
        - GOOGLE_MAPS_API_KEY=your-google-maps-api-key
      ports:
        - "8000:8000"
      command: python manage.py runserver 0.0.0.0:8000
    postgres:
      image: postgres:13
      environment:
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=yourpassword
        - POSTGRES_DB=courier
      ports:
        - "5432:5432"
  ```
4. **Start the Development Environment**:
  ```sh
  daytona up
  ```
5. **Apply Migrations**:
  ```sh
  daytona exec django python manage.py migrate
  ```
6. **Create a Superuser**:
  ```sh
  daytona exec django python manage.py createsuperuser
  ```
7. **Access the Application**:
```sh  
Visit http://localhost:8000 in your browser.
```

---

## Daytona Integration
Daytona simplifies the development process by managing containerized environments.
Key Daytona commands:

**Start the Environment*8: 
  ```sh
  daytona up
  ```
*8Stop the Environment**: 
  ```sh
  daytona down
  ```
**Run a Command**: 
  ```sh
  daytona exec <service> <command>
  ```
**Check migrations**:
  ```sh
  daytona exec django python manage.py showmigrations
  ```

---

## Usage
- Create Bookings: Add new courier bookings via the booking form.
- Sort Parcels: Categorize and assign destinations to parcels in the Sorting Hub.
- Schedule Pickups: Request pickups for courier items.
- Manage Deliveries: Track and update delivery statuses.

## Contributing
- Contributions are welcome! To contribute:

## Fork the repository.
- Create a feature branch (git checkout -b feature-name).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature-name).
- Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the contributors and the open-source community for their invaluable tools and resources.
- Special appreciation to the Daytona team for simplifying the development environment setup.
- Gratitude to Google Maps API for providing interactive and reliable location services.
- A big thank you to everyone who provided feedback and helped refine this project.

---

Feel free to customize this `README.md` file according to your project's specific details and requirements.
