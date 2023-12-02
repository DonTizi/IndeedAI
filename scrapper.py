import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

class IndeedJobScraper:
    def __init__(self, job_title, location, json_filename='jobs.json', csv_filename='jobs.csv'):
        self.job_title = job_title
        self.location = location
        self.json_filename = json_filename
        self.csv_filename = csv_filename
        self.jobs = []
        self.scrape_jobs()
        self.save_to_json()
        self.save_to_csv()

    def scrape_jobs(self):
        # Initialiser le WebDriver
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)
        self.browser.get("https://emplois.ca.indeed.com/")
        self.browser.implicitly_wait(1)

        # Remplir les champs de recherche
        self.browser.find_element(By.ID, "text-input-what").send_keys(self.job_title)
        where_element = self.browser.find_element(By.ID, "text-input-where")
        where_element.clear()
        where_element.send_keys(self.location)
        where_element.send_keys(Keys.ENTER)

        # Attendre le chargement des résultats
        self.browser.implicitly_wait(10)

        # Extraire les informations des emplois
        job_cards = self.browser.find_elements(By.CLASS_NAME, "job_seen_beacon")

        for job_card in job_cards:
            title = job_card.find_element(By.CLASS_NAME, "jobTitle").text
            job_link = job_card.find_element(By.TAG_NAME, "a").get_attribute('href')

            # Ouvrir le lien de l'offre d'emploi dans un nouvel onglet
            self.browser.execute_script(f"window.open('{job_link}');")
            self.browser.switch_to.window(self.browser.window_handles[1])

            # Récupérer la description complète
            try:
                self.browser.implicitly_wait(5)
                description = self.browser.find_element(By.ID, "jobDescriptionText").text
            except NoSuchElementException:
                description = "Description non disponible"

            # Fermer l'onglet de l'offre d'emploi et revenir à la liste principale
            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])

            # Ajouter les informations au tableau des emplois
            job_info = {"title": title, "description": description, "location": self.location, "link": job_link}
            self.jobs.append(job_info)

        # Fermer le navigateur après avoir parcouru toutes les offres
        self.browser.quit()

    def save_to_json(self):
        with open(self.json_filename, 'w') as jsonfile:
            json.dump(self.jobs, jsonfile, indent=4)

    def save_to_csv(self):
        with open(self.csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['title', 'description', 'location','link'])
            writer.writeheader()
            for job in self.jobs:
                writer.writerow(job)


