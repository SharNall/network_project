# Network Project

## Project Information
This project is a comprehensive Network Management System developed to handle various network operations and tasks. It provides functionalities for managing network devices, monitoring network performance, and handling network configurations. The system is designed to help network administrators efficiently manage and optimize their network infrastructure.

## Resources

- **Device Management:** Admins can add, update, and remove network devices, monitor their status, and view detailed device information.
- **Performance Monitoring:** Track network performance metrics such as bandwidth usage, latency, and error rates.
- **Configuration Management:** Manage and apply network configurations to devices, ensuring optimal network operation.
- **Alerts and Notifications:** Set up alerts for critical network events and receive notifications for any issues.

## Building, Packaging, and Running the Application

### Building and Packaging

1. **Clone the repository:**
    ```bash
    git clone https://github.com/SharNall/network_project.git
    cd network_project
    ```

2. **Set up the database:**
    - Create a database for the network management system.
    - Execute the SQL script located in the `/db` folder to create necessary tables.
    - Update the database connection details in the `dbConnection` class.

3. **Compile the project using your IDE (IntelliJ, Eclipse):**
    - Ensure all required libraries and dependencies are properly configured.

### Running the Application

1. **Run the database server and ensure the database is set up correctly.**

2. **Run the application through your IDE or via the command line using:**
    ```bash
    java -jar NetworkProject.jar
    ```
