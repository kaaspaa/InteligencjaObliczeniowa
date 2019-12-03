import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori
import csv

with open("pre.csv", "r") as file:
    df = csv.reader(file, delimiter=',',
                    quotechar='"', quoting=csv.QUOTE_MINIMAL
                    )
    df = [x[0].split(',') for x in df]
    print(df[0])
    print(len(df[5]))

    # generating apriori model
    final_rule = apriori(df, min_support=0.005, min_confidence=0.8)
    # grouping all the rules into a list
    final_result = list(final_rule)

    df = pd.DataFrame(columns=('Items', 'Antecedent', 'Consequent', 'Support', 'Confidence', 'Lift'))

    Support = []
    Confidence = []
    Lift = []
    Items = []
    Antecedent = []
    Consequent = []

    for RelationRecord in final_result:
        for ordered_stat in RelationRecord.ordered_statistics:
            Support.append(RelationRecord.support)
            Items.append(RelationRecord.items)
            Antecedent.append(ordered_stat.items_base)
            Consequent.append(ordered_stat.items_add)
            Confidence.append(ordered_stat.confidence)
            Lift.append(ordered_stat.lift)

    df['Items'] = list(map(set, Items))
    df['Antecedent'] = list(map(set, Antecedent))
    df['Consequent'] = list(map(set, Consequent))
    df['Support'] = Support
    df['Confidence'] = Confidence
    df['Lift'] = Lift
    df.sort_values(by="Lift", ascending=False, inplace=True)
    print(df.columns)
    plt.ylabel('Lift values')
    names = []
    values = []

    for i in range(0, 8):
        names.append("R".join(str(i * 10)))
    for i in range(0, 8):
        values.append(df.values[i * 10][5])
    for i in range(0, 8):
        print(df.values[i * 10])
    plt.bar(names, values)
    plt.show()
