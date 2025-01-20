# GitHub Follower Scraper

This project is an automation tool that retrieves the followers of a GitHub account using Python and Selenium. The script logs into the specified GitHub account using the provided credentials and retrieves the list of followers.

## Features
- Logs into a GitHub account with the specified username and password.
- Accesses the followers tab and scrapes all follower names.
- Supports pagination to retrieve the complete list.

## Prerequisites
Before running this project, ensure the following requirements are met:

1. Python is installed. [Download Python here](https://www.python.org/downloads/)
2. Install the Selenium library:
   ```bash
   pip install selenium
3. WebDriver (e.g., ChromeDriver) must be installed and configured appropriately. Download ChromeDriver [here](https://sites.google.com/chromium.org/driver/downloads?authuser=0).

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/username/github-follower-scraper.git
2. Open the githubUserInnfo.py file and replace the placeholders with your GitHub username and password:
   ```python
   username = "your_user_name"
   password = "your_password"
3. Run the script:
   ```python
   python github.py
   
## Important Notes

- This script is developed for **educational and research purposes only**. It is your responsibility to keep your credentials secure.
- Use this script in compliance with **GitHub's terms of service and policies**. Automated actions may result in account suspension.

## Project Structure

- `github.py`: The main automation script.
- `githubUserInnfo.py`: File containing username and password information.

## Contribute

If you wish to contribute, feel free to open a **Pull Request** or create an **Issue**.




   
 
