# get-top-roles: Backend endpoint to get recommended roles

---

#### **Overview**

This application demonstrates a simple backend endpoint `/get-top-roles` to fetch and display the top 5 recommended roles for a student based on their ID. It uses a Flask backend to serve mock data and an HTML/JavaScript frontend to fetch and display the results.

A simple frontend was made in `index.html` to visually interact with the API endpoint.

---

### **Technologies Used**

1. **Backend**:
   - Flask (Python)
   - Flask-CORS (for handling Cross-Origin Resource Sharing)

2. **Frontend**:
   - HTML
   - JavaScript
   - CSS

---

### **Setup Instructions**

#### Prerequisites

- Python 3.12.3 installed
- Clone the repository and navigate into it

#### Backend Setup

1. Install the required Python packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask server:
   ```bash
   python backend/app.py
   ```

3. The backend will be running at `http://127.0.0.1:5000`.

#### Frontend Setup

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Open `index.html` in any modern web browser (e.g., Chrome, Edge).

---

### **Tests**

The `tests.py` file in the `backend` directory can be used to validate the API functionality. Use the following command to run the tests:

```bash
python backend/tests.py
```

---

### **Usage**

1. Start the Flask server.
2. Open the `index.html` file in the browser.
3. Enter a valid student ID (`1` or `2` in the mock data) in the input box and press "Fetch Roles" or hit the **Enter** key.
4. View the list of recommended roles.

---

### **Mock Data**

The following student data is available in the backend:

| **Student ID** | **Name** | **Top Roles** |
|-----------------|----------|---------------|
| 1               | Alice    | Developer, Data Scientist, UX Designer, Analyst, Product Manager |
| 2               | Bob      | Marketing Specialist, Sales Executive, HR Manager, Copywriter, Event Planner |

---

### **Error Handling**

1. **Missing Student ID**:
   - Error: *"Please enter a student ID"*

2. **Invalid Student ID**:
   - Error: *"No data found for student: [ID]"*

3. **Server Errors**:
   - Displays generic error messages returned from the backend.
