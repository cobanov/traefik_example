# Basic Load Balancing Example with Traefik

This project is a simple template for setting up a basic load balancing environment using Flask (or anything) as the web application and Traefik as the reverse proxy. It demonstrates how to distribute traffic across multiple instances of a web application using Docker and Traefik's load balancing capabilities.

## Project Structure

```plaintext
/webapp
├── app.py                 # Flask application
├── Dockerfile             # Dockerfile for the Flask app
└── docker-compose.yml     # Docker Compose file for the Flask app

/traefik
├── traefik.yml            # Traefik static configuration
├── dynamic.yml            # Traefik dynamic routing and service configuration
└── docker-compose.yml     # Docker Compose file for running Traefik
```

## Running the Project

**Start the Flask Web Application**:

Navigate to the `webapp` directory and run the following command to build and start the Flask app:

```bash
docker-compose up -d
```

**Start Traefik**:

Navigate to the `traefik` directory and run the following command to start the Traefik reverse proxy:

```bash
docker-compose up -d
```

This will start Traefik in detached mode.

**Access the Application**:

- The web application will be accessible on `http://machine1:5000` and `http://machine2:5000`.
- Traefik will route requests made to `http://localhost:80` to the appropriate web application instance.
- The Traefik dashboard is accessible at `http://localhost:8080`.

## Traefik Configuration

**Static Configuration (`traefik.yml`)**:
- Defines the entry point `web` for HTTP traffic on port 80.
- Configures the file provider to load dynamic routing from `dynamic.yml`.
- Enables the Traefik API dashboard.

**Dynamic Configuration (`dynamic.yml`)**:
- Defines a router for the web application, forwarding traffic to the web application service based on the prefix `/`.
- Load balances requests across two instances of the Flask app running on different servers (`http://machine_1:5000` and `http://machine_2:5000`).



## License

This project is licensed under the MIT License.