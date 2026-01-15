#!/usr/bin/env python3
"""
Daily screenshot scheduler
Runs the screenshot job every day at 8:00 AM (Asia/Shanghai timezone)
"""
import logging
import time
import schedule
from datetime import datetime

from src import app, now


def run_screenshot_job():
    """Run the screenshot job and log results"""
    current_time = now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"{'='*50}")
    logging.info(f"Starting scheduled screenshot job at {current_time}")
    logging.info(f"{'='*50}")

    try:
        result = app.run()
        if result == 0:
            logging.info(f"✅ Job completed successfully at {now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            logging.error(f"❌ Job failed with exit code {result}")
    except Exception as e:
        logging.error(f"❌ Job failed with exception: {e}", exc_info=True)


def main():
    """Main scheduler loop"""
    logging.info("="*60)
    logging.info("Daily Screenshot Scheduler Started")
    logging.info(f"Current time: {now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info("Job scheduled for: 08:00 AM (Asia/Shanghai)")
    logging.info("="*60)

    # Schedule the job for 8:00 AM every day
    schedule.every().day.at("09:35").do(run_screenshot_job)

    # Run immediately once at startup (optional - comment out if not needed)
    # logging.info("Running job once at startup for testing...")
    # run_screenshot_job()

    # Keep running
    logging.info("Scheduler is running. Waiting for next scheduled job...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    main()