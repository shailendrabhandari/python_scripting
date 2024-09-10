
# Currency Converter Project

This is a simple currency converter project that fetches real-time exchange rates and allows users to convert currency amounts using the CurrencyLayer API.

## Prerequisites
- Python 3.x installed on your system.
- Internet connection (for fetching live exchange rates).

## Steps to Set Up and Run the Project

### 1. Create a Virtual Environment
A virtual environment helps manage dependencies for your project. Follow these steps to set up a virtual environment:

1. Open a terminal or command prompt.
2. Navigate to your project directory:
   ```bash
   cd path_to_your_project
   ```

3. Create a virtual environment (name it `venv`):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. You should see the virtual environment activated, indicated by a `(venv)` prefix in your terminal.

### 2. Install Dependencies
The project uses two primary dependencies: `requests` for making HTTP requests and `pytest` for testing.

1. Install the dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

2. After installing, the `requests` and `pytest` libraries will be available in your virtual environment.

### 3. Run the Currency Converter Program

1. Navigate to the `src` folder where the main script (`project.py`) is located:
   ```bash
   cd src
   ```

2. Run the program:
   ```bash
   python project.py
   ```

3. You will be prompted to input the following:
   - **Currency code to convert from** (e.g., `USD`).
   - **Currency code to convert to** (e.g., `EUR`).
   - **Amount** to convert (e.g., `100`).

4. The program will fetch real-time exchange rates and display the converted amount.

### 4. Run Unit Tests (Optional)
Unit tests have been written using `pytest`. To verify that everything works correctly:

1. Navigate to the `tests` folder:
   ```bash
   cd tests
   ```

2. Run the tests:
   ```bash
   pytest test_project.py
   ```

3. If all tests pass, you'll see an output indicating that everything is working properly.

### 5. Deactivate the Virtual Environment (Optional)
When you're done working on the project, deactivate the virtual environment by typing:
```bash
deactivate
```

## Project Structure

```
your_project/
├── src/
│   └── project.py         # Main project script
├── tests/
│   └── test_project.py    # Test script for pytest
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```


