from celery import shared_task
from phone_form.data_access.repository import import_csv_data, truncate_table
from ..update_data import get_download_links, download_file
import os
from celery.utils.log import get_task_logger

url = "https://opendata.digital.gov.ru/registry/numeric/downloads"
proj_path = os.getcwd()
path_to_csvs = os.path.join(proj_path, "phone_form", "downloads")


logger = get_task_logger(__name__)


@shared_task
def update_data():
    logger.info("Task ran")
    truncate_table()
    logger.info("Table truncated")
    download_links = get_download_links(url)
    logger.info("Got download links")
    for num, link in enumerate(download_links):
        download_file(link, num)
    logger.info("Csv's successfully updated")
    csvs = os.listdir(path_to_csvs)
    for csv in csvs:
        logger.info(f"Importing data from {csv}")
        import_csv_data(os.path.join(path_to_csvs, csv))
    logger.info("Data successfully imported")
    logger.info("Task ended")
