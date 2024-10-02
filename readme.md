# Web Application with Traefik Reverse Proxy

This project sets up a web application using Flask, Docker, and Traefik as a reverse proxy. The `webapp` directory contains the Flask application, while the `traefik` directory contains configuration files for Traefik, including the static and dynamic configurations.

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

1. **Start the Flask Web Application**:

   Navigate to the `webapp` directory and run the following command to build and start the Flask app:

   ```bash
   docker-compose up -d
   ```

2. **Start Traefik**:

   Navigate to the `traefik` directory and run the following command to start the Traefik reverse proxy:

   ```bash
   docker-compose up -d
   ```

   This will start Traefik in detached mode.

3. **Access the Application**:

   - The web application will be accessible on `http://machine1:5000` and `http://machine2:5000`.
   - Traefik will route requests made to `http://localhost:80` to the appropriate web application instance.
   - The Traefik dashboard is accessible at `http://localhost:8080`.

## Traefik Configuration

- **Static Configuration (`traefik.yml`)**:
  - Defines the entry point `web` for HTTP traffic on port 80.
  - Configures the file provider to load dynamic routing from `dynamic.yml`.
  - Enables the Traefik API dashboard.

- **Dynamic Configuration (`dynamic.yml`)**:
  - Defines a router for the web application, forwarding traffic to the web application service based on the prefix `/`.
  - Load balances requests across two instances of the Flask app running on different servers (`http://machine_1:5000` and `http://machine_2:5000`).



## License

This project is licensed under the MIT License.