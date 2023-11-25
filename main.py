import tkinter as tk
from tkinter import ttk
import threading
import json
import csv
from scrapper import IndeedJobScraper
from IAscrapped import JobDescriptionWriter

def update_progress(value):
    progress_bar['value'] = value
    root.update_idletasks()

def run_scraper():
    job_title = job_title_entry.get()
    location = location_entry.get()
    
    api_key = ""  # Remplacez par votre clé API réelle

    scraper = IndeedJobScraper(job_title, location)
    jobs = scraper.jobs
    update_progress(30)  # Mise à jour après le scraping

    writer = JobDescriptionWriter(api_key)

    for i, job in enumerate(jobs):
        job['presentation_letter'] = writer.compose_presentation_letter(job['description'])
        update_progress(30 + 30 * (i + 1) / len(jobs))  # Mise à jour pendant la génération des lettres

    with open('updated_jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'description', 'location', 'link', 'presentation_letter']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        for job in jobs:
            csv_writer.writerow(job)

    update_progress(100)  # Mise à jour lorsque tout est terminé
    status_label.config(text="Scraping and Processing Completed!")

def start_scraping_thread():
    threading.Thread(target=run_scraper).start()

# Configuration de l'interface utilisateur principale
root = tk.Tk()
root.title("Job Scraper and Letter Generator")

# Barre de progression
progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress_bar.grid(row=4, column=0, columnspan=2, pady=10)

# Widgets pour saisir le titre du job et la localisation
tk.Label(root, text="Job Title:").grid(row=0, column=0)
job_title_entry = tk.Entry(root)
job_title_entry.grid(row=0, column=1)

tk.Label(root, text="Location:").grid(row=1, column=0)
location_entry = tk.Entry(root)
location_entry.grid(row=1, column=1)

# Bouton pour démarrer le scraping
run_button = tk.Button(root, text="Run Scraper", command=start_scraping_thread)
run_button.grid(row=2, column=0, columnspan=2)

# Label pour afficher le statut
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=2)

# Démarrage de la boucle principale de l'interface utilisateur
root.mainloop()
