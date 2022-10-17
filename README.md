# Project-1
```python
Hello World! This is Marc Planas :)
```
---
## Top-10 (deathliest) activities to avoid during *'Shark Season'* 
    Climate change is not a hoax!

---
### Main objective
The aim of this project was:
1. To identify the top 10 activities (sports) in which most of the shark attacks occur and investigate their survivability.

    > ***Hypothesis:** Since surfing is a very popular sport, most of the reports will be of people practicing it. However, since surfers are very aware of their surroundings, surf might not be the most deathliest activity.*  

2. To identify a so called *'Shark Season'* based on the number of reports per month and country and investigate whether it has changed over the past years. This might give us insights on the migratory patterns of these animals.

    > ***Hypothesis:** Global warming might impact sharks' migratory events in such a way that is reflected in the number attack reports.*

An analysis on the  `sharks.csv` dataset was conducted to investigate these issues. 

---
### 1. Data cleaning
The process described below was performed in the following jupyter notebook: `my_project_cleaning_exploration.ipynb`

- Dimensions of the original dataset: `25723 rows × 24 columns`
- Almost all categories (columns) contained `~20,000 NaN` missing values.
- The dataset also contained `2392 duplicated` reports (rows). 
- Reports with `NaN` values in **all** columns and `duplicated` rows were dropped/removed, lowering the number of rows with potentially meaningful data to `6311`.

After a closer inspection, it was decided to drop some of the categories that would not be useful for the scope of the analysis and which contained repetitive information. Columns dropped were: `pdf`, `href formula`, `href`, `original order`, `Unnamed: 22`, `Unnamed: 23`, `Case Number.1` and `Case Number.2`, lowering the number of columns to `16`. 

Then, reports in which **half** of the information was missing (i. e. `NaN` values in **8** out of the **16** columns) were also dropped, since they were ruled not reliable reports. This resulted in a significantly cleaner and more trustworthy dataset, with `6302` rows. In addition, column headers were cleaned using the `strip()` method.

The resulting `(6302 x 16)` dataframe was saved as `sharks_clean.csv` and was used for further exploration and analysis. [^1]

[^1]: The dataset was also cleaned during the analysis stage when aiming at specific categories.

---
### 2. Data exploration
The process described below was performed in the following jupyter notebook: `my_project_cleaning_exploration.ipynb`

An initial exploration was conducted using the `value_counts()` method to see the distribution of values within each column.

In addition, after inspecting the number of `NaN` in each column (the lower the better - more statistically powerfull), the following categories appeared good alternatives to investigate: 
- Date/Year
- Type
- Country/Area/Location
- Activity
- Injury/Fatal (Y/N) a.k.a survivability
- Gender (Sex)

---
### 3. Data analysis
The process described below was performed in the following jupyter notebook: `my_project_analysis.ipynb`

#### 3.1. Top 10 (deathliest) activities
Starting dataset: `sharks_clean.csv`.
Outcome after cleaning and grouping: `sharks_clean_activity_fatal.csv`.

##### 3.1.1. Cleaning Activity
- Removing rows with `NaN` in activity column. Result: `df.shape = (5758, 16)`.
- Cleaning inconsistencies: `lower()`, `strip()`, `replace()`.
- Grouping activities using **RegEx:**
    - Dictionary with RegEx pattern as value.
    - Iterate over the dictionary to `replace()` group similar activities.

```python
dict_activity_regex = {
    "Board surfing" : ".*(surf).*|.*(boogie board).*|.*(body board).*",
    "Kayaking & similar" : ".*(kayak).*|.*(canoe).*|.*(rowing).*",
    "Diving" : ".*(diving).*",
    "Paddle boarding" : ".*(paddle).*",
    "Sailing" : ".*(boat).*|.*(sail).*|.*(ship).*|.*(overboard).*",
    "Snorkeling" : ".*(snorkel).*",
    "Swimming" : ".*(bathing).*|.*(swimming).*|.*(float).*",
    "Spear-fishing" : ".*(spearfishing).*",
    "Fishing" : "[\w\s]+?(fishing).*|^(fishing).*",
    "Wading" : ".*wad.*|.*(walking).*|.*(standing).*|.*(treading).*"
}

for key, value in dict_activity_regex.items():
    sharks_clean["Activity"] = sharks_clean["Activity"].str.replace(value, key, regex = True)
```

##### 3.1.2. Cleaning Fatality
- Removing rows with `NaN` in fatal column. Result: `df.shape = (5344, 16)`.
- Cleaning inconsistencies: `strip()`, `upper()`.
- Removing if value of fatal is not `Y` or `N` using filtering conditions.

##### 3.1.3. Visualization
- Countplot of top 10 activities/sports, using the fatal category as `hue`.
- Image file: `activity_fatality.jpg`

![Top deathliest activities](./images/activity_fatality.jpg)

##### Conclusions:
- Although board-related sports represent most of the reports of shark attacks, the fatality concentrates on swimmers, which have less tools to escape the attack or are less aware of their surroundings.
<br/>

#### 3.2. 'Shark Season' by Month and Country
Starting dataset: `sharks_clean.csv`.
Outcome after extracting month and cleaning both month and country: `sharks_clean_month_country.csv`.

##### 3.1.1. Extracting and cleaning Month
- The actual month of the shark attack report was extracted from the `Date` column using the **RegEx** `-(\w{3})-` and the `extract()` method to create a new `Month` column. 
- When a row did not contain that pattern, the month was filled with `NaN`. Out of the `6302` initial rows, `910` contained missing values now. I was willing to sacrifice this rows, since they either did not contain the month or the annotation was deemed unreliable (i. e. "It happened after August 1800"). 
- Rows with `NaN` in the `Month` column were removed, resulting in `5392` shark attack reports.

For visualization purposes, months were then encoded using numbers `1-12`. Otherwise they would be ordered alphabetically in the x-axis of the plot:

```python
# Creating a dictionary to store the old and new names for months:

dict_months = {"jan" : 1,
              "feb" : 2,
              "mar" : 3,
              "apr" : 4,
              "may" : 5,
              "jun" : 6,
              "jul" : 7,
              "aug" : 8,
              "sep" : 9,
              "oct" : 10,
              "nov" : 11,
              "dec" : 12              
}

# Replacing the name by value

sharks_clean.replace({"Month" : dict_months}, inplace = True)
```

##### 3.1.2. Cleaning Country
- Rows with `NaN` in Country were removed. Result: `df.shape = (5361, 17)`.
- Unique countries were checked to see inconsistencies.
- The top 3 countries (USA, Australia, South Africa) were selected as they represent most of the reports.

##### 3.1.3. Visualization: 'Shark Season'
- Defined filtering conditions for each Country.
- Report counts were plotted `groupby` month.
- Image file: `shark_season_countries.jpg`.

![Shark Season in Top 3 countries](./images/shark_season_countries.jpg)

##### Conclusions:
- *'Shark Season'* actually reflects **summer season** in the northern hemisphere (USA) and southern hemisphere (Australia, South Africa). :upside_down_face:
- Most reports are observed during summer season due to people practicing  sea-related activities.
<br/>

#### 3.3. 'Shark Season' by Country and Year
*'Shark Season'* / summer season might have looked different in the past due to:
- **Climate change / global warming**.
- Increased ease to report attacks over the years.

Starting dataframe: `sharks_clean_month_country.csv`
Outcome after cleaning the year: `sharks_clean_month_country_year.csv`

##### 3.3.1. Cleaning Year
- The `Year` column was cleaned after checking `unique()` values:
```python
try:
    sharks_clean["Year"] = sharks_clean["Year"].astype(int)
except Exception:
    sharks_clean['Year'] = sharks_clean['Year'].fillna(0).astype(int)
```
- Rows in which `Year == 0` were removed. Result: `df.shape = (5352, 17)`.

##### 3.3.2. Visualization: Worlwide reports
- Worldwide reports were visualized using a histplot.
- Image file: `shark_reports_year.jpg`.

![Shark Season in Top 3 countries](./images/shark_reports_year.jpg)

- Most reports occur since year 1900, mainly due to increased ease in documenting the attacks (probably). Thus, in order to have more powerful data (the more reports the better) it makes sense to focus in this last century.
<br/>

##### 3.3.3. Evolution of attacks in the Northern and Southern hemisphere
- Created a list of the countries in each hemisphere.
- Applied a function to rename the countries (in a new column) if they belonged to each of the lists (re-checked the `unique()` values). Data frame stored as: `sharks_clean_month_year_hemisphere.csv`.
```python
south = ["country_1", "country_2", ...]
north = ["country_3", "country_4", ...]

def hemisphere(x):
    if x.lower() in south:
        return "Southern"
    elif x.lower() in north:
        return "Northern"
    else:
        return x
```
- Created one dataframe for each hemisphere and visualized the evolution of reports `groupby` month. Each line represents a span of 20 years (1940-2018).
    - `northern.shape = (2931, 18)`. Image file: `month_year_northern.jpg`. 
    - `southern.shape = (2365, 18)`. Image file: `month_year_southern.jpg`

![Evolution in Northern](./images/month_year_northern.jpg)

![Evolution in Southern](./images/month_year_southern.jpg)
<br/>


##### 3.3.4. Visualization: Evolution of attacks in USA in the last century
- A new dataframe was created (`sharks_clean_month_year_usa.csv`) selecting only those reports belonging to USA using filtering conditions. Result: `df.shape = (2049, 17)`.
- Report were plotted `groupby` month and filtering each plot by spans of 20 years, from 1940 to 2018.
- Image file: `month_year_USA.jpg`.

![Evolution of reports in USA](./images/month_year_USA.jpg)

##### Conclusions: 
- Since the last 20-40 years concentration of attack reports seems to start earlier (from Apr) and lasts longer in time (till Oct). This could be due to:
    - Increased ease to report cases.
    - Summer season starts earlier and lasts longer due to **global warming**, leading to more attacks.
<br/>

##### 3.3.5. Visualization: Evolution of attacks in Australia in the last century
- A similar process was followed for the second country with most reports and which is located in the southern hemisphere, Australia. The dataframe was saved as: `sharks_clean_month_year_australia.csv`.
- Image file: `month_year_australia.jpg`.

![Evolution of reports in Australia](./images/month_year_australia.jpg)

##### Conclusions:
- Similar to USA, an increase in reports during *'winter'* months is observed in the last 20 years. **Global warming is not a hoax!**
- This *long summer* effect is easily seen in the northern hemisphere.
<br/>

![Global warming in the Arctic](./images/global_warming_arctic.jpg)
Further reading: [click here!](https://www.science.org/content/article/arctic-warming-four-times-faster-rest-world)
<br/>

#### 3.4. Demographics
Finally, some demographic investigation were conducted in order to visualize which age and gender accumulated more fatality reports.

##### 3.4.1. Age x Survivability
Starting dataframe: `sharks_clean_activity_fatal.csv`.
- 2180 rows with `NaN` age were removed.
- Cleaned inconsistencies: `.map(str)`, followed by `strip()`.
- **RegEx** was used to extract the age: `(\d{1,2})`.
- New `NaN` that did not follow this pattern (26) were removed.
- Ages were transformed back to `int` using `map`.
- Age distribution was plotted using a violin plot and fatality was shown in the y-axis.
- Image file: `age_fatality.jpg`.

![Age distribution and fatality](./images/age_fatality.jpg)

##### Conclusions:
- People that report shark attacks are young, since they are the ones practicing the abovementioned sports.
<br/>

##### 3.4.2. Gender x Survivability
Starting dataframe: `sharks_clean_activity_fatal.csv`.
- 362 rows with `NaN` gender were removed.
- Cleaned inconsistencies: `strip()`.
- Only those that contained a value of `M` or `F` were kept.
- Gender counts were plotted using a countplot and fatality was shown in the y-axis.
- Image file: `gender_fatality.jpg`.

![Gender and fatality](./images/gender_fatality.jpg)

##### Conclusions:
- Most shark attack reports accumulate in men. Might be interesting to visualize if this has been changing in recent years.
<br/>
