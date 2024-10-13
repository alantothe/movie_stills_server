# Movie Stills Server

This Django project serves as a backend for managing and serving movie stills.


## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/movie_stills.git
   cd movie_stills
   ```

2. Create a virtual environment:
   ```
   python3 -m venv movie_stills_env
   ```

3. Activate the virtual environment:
   ```
   source movie_stills_env/bin/activate  # On Unix or MacOS
   # movie_stills_env\Scripts\activate.bat  # On Windows
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python3 manage.py migrate
   ```

6. Run the development server:
   ```
   python3 manage.py runserver
   ```

