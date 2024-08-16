# Zoho User Tracker

This project is a Django-based application for tracking user activation and deactivation logs from Zoho Projects. It allows you to sync users from Zoho, update user statuses, and view the activation/deactivation history.

## Features

- **Sync Users from Zoho Projects**: Fetch and store user details such as name, email, status, and access type.
- **Track Activation/Deactivation Events**: Log every activation or deactivation event with timestamps.
- **View User Logs**: View a detailed history of user status changes.
- **Easy Integration**: Connects to Zoho Projects API using OAuth2 for secure access.

## Technology Stack

- **Backend:** Django
- **Database:** SQLite (can be switched to PostgreSQL)
- **Zoho Integration:** Zoho Projects API (OAuth2)
- **Frontend:** Django templates (optional), or REST API endpoints

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Zoho Projects account
- Zoho API credentials (Client ID, Client Secret, and OAuth2 token)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/zoho-user-tracker.git
    cd zoho-user-tracker
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:  
   Create a `.env` file in the project root and add the following variables:
    ```env
    ZOHO_CLIENT_ID=your_zoho_client_id
    ZOHO_CLIENT_SECRET=your_zoho_client_secret
    ZOHO_REDIRECT_URI=your_redirect_uri
    ZOHO_ACCESS_TOKEN=your_oauth2_access_token
    ```

5. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Run the server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the app**:  
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### Usage

1. **Sync Users from Zoho**:
   - Make a GET request to: `/users/sync-users/`
   - This will fetch users from Zoho Projects and store them in your database.

2. **Update User Status**:
   - Make a POST request to: `/users/update-user-status/`
   - Example request body:
     ```json
     {
       "user_id": "zoho_user_id_here",
       "status": "active"  # or "deactivated"
     }
     ```

3. **View User Logs**:
   - Make a GET request to: `/users/user-logs/<str:user_id>/`
   - This will return the activation/deactivation history for the specified user.

### Project Structure

