# CodePulse: Competitive Programming Tracker

CodePulse is a Django-based web application that tracks and analyzes your Competitive Programming (CP) journey. It leverages the Codeforces API, Chart.js, and Google Gemini AI to provide users with performance tracking and personalized topic recommendations.

---

## Features

- **User Accounts**: Manage profiles and access personalized dashboards.
- **Performance Tracking**: Analyze Codeforces performance using data fetched via the Codeforces API.
- **Recommendation System**: Receive recommended CP topics and resources based on your performance.
- **Visualization**: Interactive charts using Chart.js for better data insights.
- **Integrated AI**: Google Gemini AI for topic recommendations.

---

## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite3
- **Frontend**: HTML, CSS, Chart.js
- **API Integration**: Codeforces API, Google Gemini AI
- **Other Tools**: `requests` for API calls

---

## Installation

Follow these steps to set up and run CodePulse locally:

### Prerequisites

1. Python (>=3.8)
2. Virtual Environment (optional but recommended)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nehal21-hash/CodePulse.git
   cd CodePulse
   ```

2. **Set Up Virtual Environment** (optional)
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Usage

1. Create an account or log in with your existing credentials.
2. Enter your Codeforces handle to track your performance.
3. View personalized topic recommendations and improve your skills.
4. Explore the visual charts to analyze your progress.

---

## Contributing

We welcome contributions from the community! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeatureName`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeatureName`.
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Codeforces API](https://codeforces.com/apiHelp)
- [Chart.js](https://www.chartjs.org/)
- [Google Gemini AI](https://ai.google/)

---

Happy coding and best of luck with your Competitive Programming journey!
