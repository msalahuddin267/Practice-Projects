from django_cron import CronJobBase, Schedule
import requests
import os
from .models import CronJobControl
from django.conf import settings

class DownloadImageCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # Default interval is 5 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'task_schedular.download_image_cron'  # Unique identifier

    def do(self):
        print("Starting cron job to download image...")

        # Check if CRON job is active
        config = CronJobControl.objects.first()
        if not config or not config.is_active:
            print("CRON job is inactive.")
            return

        image_url = "https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg?cs=srgb&dl=pexels-souvenirpixels-414612.jpg&fm=jpg"  # Replace with a real URL

        try:
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                # Ensure the media folder exists
                save_dir = os.path.join(settings.MEDIA_ROOT, "download")
                os.makedirs(save_dir, exist_ok=True)

                save_path = os.path.join(save_dir, "downloaded_image.jpg")
                with open(save_path, "wb") as f:
                    f.write(response.content)

                print(f"Image downloaded successfully and saved to {save_path}")
            else:
                print(f"Failed to download image. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
