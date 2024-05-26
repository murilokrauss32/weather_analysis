import matplotlib.pyplot as plt
import logging

def plot_average_pressure(average_pressures):
    try:
        cities = list(average_pressures.keys())
        pressures = list(average_pressures.values())

        plt.figure(figsize=(10, 5))
        plt.bar(cities, pressures, color='blue')
        plt.xlabel('Cities')
        plt.ylabel('Average Pressure')
        plt.title('Average Pressure over the Last 15 Days')
        plt.show()
    except Exception as e:
        logging.error(f"Error in plot_average_pressure: {e}")

def plot_relationships(relationships):
    try:
        for city, correlation in relationships.items():
            fig, ax = plt.subplots(figsize=(8, 6))
            cax = ax.matshow(correlation, cmap='coolwarm')
            plt.title(f'Correlation Matrix for {city}', pad=20)
            fig.colorbar(cax)

            # Set ticks and labels
            ax.set_xticks(range(len(correlation.columns)))
            ax.set_yticks(range(len(correlation.columns)))
            ax.set_xticklabels(correlation.columns, rotation=45, ha='left')
            ax.set_yticklabels(correlation.columns)

            plt.tight_layout()
            plt.show()
    except Exception as e:
        logging.error(f"Error in plot_relationships: {e}")

def plot_rankings(rankings):
    try:
        fig, ax = plt.subplots(figsize=(10, 5))
        for city, rank_dict in rankings.items():
            for days, rank in rank_dict.items():
                ax.bar(f"{city} - {days} days", rank)

        ax.set_xlabel('City and Days')
        ax.set_ylabel('Max Pressure')
        ax.set_title('Max Pressure Rankings')
        plt.xticks(rotation=90) 
        plt.tight_layout()
        plt.show()
    except Exception as e:
        logging.error(f"Error in plot_rankings: {e}")
