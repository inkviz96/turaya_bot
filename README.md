
# THURAYA
### Start tg bot
nohup python3 main.py &

### Start apscheduler
nohup python3 start_scheduler.py &

### Stop tg bot
ps aux | grep main.py
kill -9 <id>

### Stop apscheduler
ps aux | grep start_scheduler.py
kill -9 <id>
rm -rf jobs.sqlite

### Add envs
export API_TOKEN="<tg_bot_token>"
export BALANCE_URL="<thuraya_api_url>"