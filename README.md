# IndeedAI
Indeed AI solution to find your job

# Job Scraping, Cover Letter, and CV Personalization Application

This application is a comprehensive tool for job seekers, designed to scrape job listings from Indeed, automatically generate personalized cover letters, and tailor CVs for each job listing using the OpenAI API. It enhances job application efforts by ensuring that both cover letters and CVs are optimally aligned with the specific requirements of each job.

## Features

- Scrapes job listings from Indeed based on job title and location.
- Automatically generates personalized cover letters for each scraped job listing.
- Personalizes CVs for each job listing to align with the job's specific requirements and to highlight the applicant's relevant skills and experiences, increasing the likelihood of securing interviews.
- Saves scraped data, generated letters, and personalized CVs to CSV files.

## Installation

To use this application, ensure the following dependencies are installed:

- Python 3
- Selenium
- Tkinter (usually included with Python)
- OpenAI (requires an API key)

## Setup

1. Clone this repository to your local machine using `git clone https://github.com/RayaneMelDz/IndeedAI.git`.
2. Install the necessary dependencies using `pip install -r requirements.txt`.

## Usage

1. Launch the application by running `python main.py` in your terminal.
2. Enter the desired job title and location in the GUI.
3. Click on "Run Scraper" to start the scraping, letter generation, and CV personalization process.
4. The results, including personalized cover letters and CVs, will be saved to a CSV file in the same directory as the application.

## Project Structure

- `main.py`: Main script to launch the GUI application.
- `scrapper.py`: Module for scraping job listings.
- `IAscrapped.py`: Module for generating cover letters and personalizing CVs with OpenAI.

## Important Notes

- Ensure not to publicly publish your OpenAI API key.
- Respect the terms of use of websites when scraping.
- This application is a project example and should not be used for commercial purposes without proper permission.

## Contributions

Contributions to this project are welcome. Please follow standard practices for open-source contributions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
