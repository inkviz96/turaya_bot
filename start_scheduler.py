import asyncio
import logging
from periodic_tasks import scheduler
from handlers.utils import check_balances, check_data


if __name__ == "__main__":
    logging.info("Start scheduler...")
    scheduler.add_job(check_balances, "interval", minutes=5)
    scheduler.add_job(check_data, "interval", minutes=5)
    scheduler.start()
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
