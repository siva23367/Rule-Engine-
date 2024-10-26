




# 3-Tier Rule Engine Application

This project is a simple 3-tier rule engine application built with FastAPI. It allows you to determine user eligibility based on configurable rules (e.g., age, department, income, spend, etc.). The system uses an Abstract Syntax Tree (AST) to represent conditional rules, allowing for dynamic creation, combination, and evaluation of these rules.

## Prerequisites

Before running this project, make sure you have the following installed:

- **Docker**: Ensure Docker is installed on your system. You can download and install it from [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).
- **Docker Compose**: Comes pre-installed with Docker Desktop. If not, you can install it separately by following the instructions here: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/).

## Running the Project

To run the project, follow these steps:

1. **Clone the repository** (if not done already):

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name
   ```

2. **Run the Docker Compose command**:

   ```bash
   docker-compose -f docker-compose.yaml up -d
   ```

   This command will start the application in detached mode.

## Accessing the Application

Once the containers are up and running, you can access the **FastAPI Swagger UI** (serving as the frontend) to interact with the API:

- Open your browser and go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Here, you can test the various routes for creating, combining, and evaluating rules.

## API Endpoints

The main API endpoints provided by the application are:

1. **Create Rule** (`POST /ast/create-rules`): Create a new rule.
2. **Combine Rules** (`POST /ast/combine-rules`): Combine multiple rules.
3. **Evaluate Rule** (`POST /ast/evaluate-rule`): Evaluate a rule against user data.

Refer to the Swagger UI documentation for detailed information about each endpoint.

## Stopping the Application

To stop the application, run:

```bash
docker-compose down
```

This command will stop and remove the containers.

## Troubleshooting

If you encounter any issues, you can check the logs by running:

```bash
docker-compose logs
```

You can also view logs for a specific service by specifying the service name:



## Additional Information

- **Dockerfile and docker-compose.yml** are required to set up the environment and services. Make sure they are correctly configured to expose the necessary ports (default: `8000`).
- The application runs on **port 8000** by default.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
# Rule-Engine-
# Rule-Engine-
