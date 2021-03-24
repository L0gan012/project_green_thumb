import database as db

from graph import graph

def main():

    cur = db.create_cursor("./plant_data")

    db.add_plant(cur)

    #moisture = graph("Moisture Over Time", "Time (days)", "Moisture level", plants)
    #temp = graph("Temp Over Time", "Time (Days)", "Temp. (Degrees F)", plants)

    #moisture.show_graph()

main()