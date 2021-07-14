import pandas as pd
import numpy as np
import matplotlib
from matplotlib import figure

# df = pd.DataFrame(
#    {
#         "Name": [
#            "Braund, Mr. Owen Harris",
#            "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#          "Sex": ["male", "male", "female"],
#   }
#  )
#
# print(df)
# print(df['Age'])
#
# ages = pd.Series([22, 35, 58], name="Age")
# print(ages)
#
# print(df["Age"].max())
# print(ages.max())
# print(df.describe())


titanic = pd.read_csv('titanic.csv')
# # print(titanic.head(10))
# # print(titanic.tail(10))
# # print(titanic.dtypes)
#
# # titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
# titanic.info()
#
# ages = titanic["Age"]
# print(type(titanic["Age"]))
# print(titanic["Age"].shape)
# age_sex = titanic[["Age", "Sex"]]
# print(type(titanic[["Age", "Sex"]]))
# print(titanic[["Age", "Sex"]].shape)
#
# above_35 = titanic[titanic["Age"] > 35]
# class_23 = titanic[titanic["Pclass"].isin([2, 3])]
# # class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
# age_no_na = titanic[titanic["Age"].notna()]

# air_quality = pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)
# print(air_quality.head(10))
# plot = air_quality.plot()
# print(plot)
# air_quality["station_paris"].plot()
# air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
# air_quality.plot.box()
# axs = air_quality.plot.area(figsize=(12, 4), subplots=True)


# air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
# air_quality["ratio_paris_antwerp"] = (
#     air_quality["station_paris"] / air_quality["station_antwerp"]
# )
# air_quality_renamed = air_quality.rename(
#     columns = {
#         "station_antwerp": "BETR801",
#         "station_paris": "FR04014",
#         "station_london": "London Westminster",
#         }
#     )
# air_quality_renamed = air_quality_renamed.rename(columns=str.lower)


titanic["Age"].mean()
titanic[["Age", "Fare"]].median()
titanic.agg(
{
"Age": ["min", "max", "median", "skew"],
"Fare": ["min", "max", "median", "mean"],
}
)
titanic[["Sex", "Age"]].groupby("Sex").mean()
titanic.groupby("Sex").mean()
titanic.groupby(["Sex", "Pclass"])["Fare"].mean()

titanic["Name"].str.lower()
titanic["Name"].str.split(",")
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
titanic[titanic["Name"].str.contains("Countess")]
titanic["Name"].str.len()
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
