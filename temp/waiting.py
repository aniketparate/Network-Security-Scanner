import schedule, time

# Functions setup
def job():
    print("I'm working...")

def done():
    print("I'm home...")

def meeting():
    print("I'm in a meeting...")

# schedule.every(3).seconds.do(job)
# schedule.every(1).seconds.do(meeting)
schedule.every(5).seconds.do(job)


# Task scheduling
# After every 10mins hello_world() is called.
    # schedule.every(10).seconds.do(hello_world)
# schedule.every()

# After every hour hello_world() is called.
    # schedule.every().hour.do(hello_world)

# Every day at 12am or 00:00 time hello_world() is called.
    # schedule.every().day.at("00:00").do(hello_world)

# After every 5 to 10mins in between run hello_world()
    # schedule.every(5).to(10).minutes.do(hello_world)

# Every monday hello_world() is called
    # schedule.every().monday.do(hello_world)

# Every tuesday at 18:00 hello_world() is called
    # schedule.every().tuesday.at("18:00").do(hello_world)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    schedule.run_pending()
    time.sleep(1)
    	# Checks whether a scheduled task
    	# is pending to run or not


