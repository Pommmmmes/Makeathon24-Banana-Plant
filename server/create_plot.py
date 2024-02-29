import numpy as np
import matplotlib.pyplot as plt
import datetime

def plot_soil_moisture(last_7_days_moisture: int):
    today = datetime.date.today()
    dates = [str(today - datetime.timedelta(days=i)) for i in range(6, -1, -1)]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, last_7_days_moisture, marker='o', linestyle='-')
    plt.title('Daily Soil Moisture of Last 7 Days')
    plt.xlabel('Date')
    plt.ylabel('Moisture (%)')
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('./templates/images/new_plot.png')




last_7_days_moisture = (10, 20, 30, 80, 10, 100, 50)
plot_soil_moisture(last_7_days_moisture)


# soil moisture 0-100% dry-moist
