# Script-Excecution-tkinter-App-Django-Mqtt

This project introduces a comprehensive and user-centric Python Script Management System, empowering developers with a streamlined approach to creating, managing, executing, and tracking Python scripts. The system comprises two essential components: a Tkinter desktop application and a Django web application. These components collaboratively communicate and share data through a unified database, creating a harmonious ecosystem for script management and execution.

## Features:

1. Tkinter Desktop App:
   The heart of the system lies in the Tkinter desktop application, which offers a user-friendly interface for effortless script management
   and execution. Developers can perform the following actions:
    - Create, Edit, and Delete Scripts: Seamlessly craft new scripts, modify existing ones, or remove outdated ones, all within an intuitive interface.
    - Script Execution: The app provides a dedicated play button for executing scripts locally. This real-time execution ensures that - developers can swiftly validate their code changes.
    - Execution Tracking: Detailed execution logs are captured, including output, start and completion times, and execution duration. This valuable information helps developers diagnose issues and measure script performance.
    - Subprocess Integration: Python scripts are executed locally using the Subprocess module, ensuring accurate execution and robust performance.
    - Database Management: The app utilizes the Pewee Object-Relational Mapping (ORM) library for efficient and reliable database management, ensuring optimal data organization and retrieval.

2. Django Web App:
  The Django web application serves as an extension of the desktop app, providing a web-based interface for script management and execution   tracking. Key functionalities include:

  - Real-Time Data Synchronization: Changes made to scripts (creation, updates, deletions) in the Tkinter app are instantly propagated to the Django app via MQTT messaging, ensuring seamless data consistency across platforms.
  - Web Interface: Developers can access, review, and manage their scripts through an intuitive web interface, enhancing accessibility and collaboration.
  - Script Execution Logs: Execution logs from the Tkinter app are seamlessly synchronized with the Django app, allowing developers to review past executions and troubleshoot any encountered issues.

## Database Schema:

- Script Table:
  
  Script Name: A user-defined name for the script.
  Script Body: The content of the Python script.

- ExecutionLog Table:
  
  script (foreign key): Establishes a link to the associated script.
  output: Captures the output generated during script execution.
  execution_started_at: Timestamp indicating the start of script execution.
  execution_completed_at: Timestamp indicating the completion of script execution.
  execution_time: Duration of script execution in seconds.

## Technology Stack:

- Tkinter: Building the feature-rich desktop application for script management and execution.
- Django: Developing the web application interface for remote access and data visualization.
- Subprocess: Ensuring reliable and secure execution of Python scripts locally.
- Pewee ORM: Efficiently managing the database and facilitating data interactions.
- MQTT: Enabling real-time data synchronization and communication between the Tkinter and Django apps.

<br>
<img width="519" alt="Screenshot 2023-08-16 at 9 20 26 PM" src="https://github.com/NikhilSaraogi/Script-Excecution-tkinter-Django-Mqtt/assets/35253854/ee5bd89c-417d-488d-8409-79198e949638">
<img width="494" alt="Screenshot 2023-08-16 at 9 21 10 PM" src="https://github.com/NikhilSaraogi/Script-Excecution-tkinter-Django-Mqtt/assets/35253854/c97c43f8-1385-4ee1-b11a-a001009894e1">
<img width="1407" alt="Screenshot 2023-08-16 at 9 22 13 PM" src="https://github.com/NikhilSaraogi/Script-Excecution-tkinter-Django-Mqtt/assets/35253854/749b1bc1-a4c2-451b-a575-367b113f20df">
<br>

## Conclusion:

This Python Script Management System revolutionizes the way developers handle Python scripts, combining the convenience of a desktop app with the accessibility of a web interface. With a seamless data flow, real-time synchronization, and robust execution tracking, developers can confidently manage, execute, and monitor their scripts, enhancing productivity and code quality.



