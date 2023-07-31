from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler(
    {
        "apscheduler.jobstores.default": {
            "type": "sqlalchemy",
            "url": "sqlite:///jobs.sqlite",
        },
        "apscheduler.executors.processpool": {
            "type": "processpool",
            "max_workers": "5",
        },
        "apscheduler.job_defaults.coalesce": "false",
        "apscheduler.job_defaults.max_instances": "3",
        "apscheduler.timezone": "UTC",
    }
)
