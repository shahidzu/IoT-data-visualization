import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

def visualize_iot_data(csv_file):
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(csv_file, parse_dates=['timestamp'])
    
    # Extracting timestamp and sensor readings
    timestamp = df['timestamp']
    temperature = df['temperature']
    humidity = df['humidity']
    
    # Create the figure and axes for plotting
    fig, ax1 = plt.subplots()
    
    # Plot temperature data
    ax1.plot(timestamp, temperature, color='tab:red', label='Temperature (°C)')
    ax1.set_xlabel('Timestamp')
    ax1.set_ylabel('Temperature (°C)', color='tab:red')
    ax1.tick_params(axis='y', labelcolor='tab:red')
    
    # Create a second y-axis for humidity data
    ax2 = ax1.twinx()
    ax2.plot(timestamp, humidity, color='tab:blue', label='Humidity (%)')
    ax2.set_ylabel('Humidity (%)', color='tab:blue')
    ax2.tick_params(axis='y', labelcolor='tab:blue')
    
    # Formatting the date on the x-axis
    date_format = DateFormatter('%Y-%m-%d %H:%M:%S')
    ax1.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    
    # Combine the legends from both axes
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')
    
    # Show the plot
    plt.title('IoT Data Visualization')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    csv_file = "iot_data.csv"
    visualize_iot_data(csv_file)
