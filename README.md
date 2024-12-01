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

- Ensure Python 3.12 is installed.
- Clone the repository and navigate into it.
    ```bash
    git clone https://github.com/Taanviir/get-top-roles.git
    cd get-top-roles/
    ```
- Set up virtual environment (optional but recommended):
   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
- Install the required Python packages using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

---

### **Usage**

1. Start the Flask server.
    ```bash
    python backend/app.py
    ```
2. Open the website at `http://localhost:5000`.
3. Enter a valid student ID (`1` or `2` in the mock data) in the input box and press "Fetch Roles" or hit the **Enter** key.
4. View the list of recommended roles.
5. If the JSON alone is preferred then open the following link:
   - Open a browser and visit: `http://127.0.0.1:5000/get-top-roles?student_id=1`.
   - Or use curl to interact with the API endpoint:
       ```
       curl "http://127.0.0.1:5000/get-top-roles?student_id=1"
       ```
   - You should see JSON data like:
     ```json
     {
         "student_id": "1",
         "student_name": "Alice",
         "top_roles": ["Developer", "Data Scientist", "UX Designer", "Analyst", "Product Manager"]
     }
     ```

---

### **Tests**

The `tests.py` file in the `backend` directory can be used to validate the API functionality. Use the following command to run the tests:

```bash
python backend/tests.py
```

---

### **Mock Data**

The following student data is available in the backend:

| **Student ID** | **Name** | **Top Roles** |
|-----------------|----------|---------------|
| 1               | Alice    | Developer, Data Scientist, UX Designer, Analyst, Product Manager |
| 2               | Bob      | Marketing Specialist, Sales Executive, HR Manager, Copywriter, Event Planner |
