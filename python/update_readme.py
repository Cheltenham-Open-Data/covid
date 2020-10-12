
 # importing modules
import helper
import random
import pathlib
import json


# setup
root = pathlib.Path(__file__).parent.parent.resolve()
with open( root / "corona.json", 'r') as filehandle:
    data = json.load(filehandle)

    total_cases = 0
    total_deaths = 0
    counter = 0
    cum_cases = data[0]['cases']['cumulative']
    cum_deaths = data[0]['deaths']['cumulative']
    last_date = data[1]['date']
    last_cum_deaths = data[1]['deaths']['cumulative']
    for item in data:
        counter += 1
        date = item['date']
        total_cases += 0 if item['cases']['daily'] == None else item['cases']['daily']
        total_deaths = 0 if item['deaths']['daily'] == None else item['deaths']['daily']

header = f"## Overall statistics\n\n Data based on {counter} records. Data might not match due to reporting/timing issues in the underlying data\n"
string1 = f"\n- The sum of the daily cases in Cheltenham is {total_cases}."
string2 = f"\n- The sum of the daily deaths in Cheltenham is {total_deaths}."
string3 = f"\n- The last recorded cumulative cases total in Cheltenham is {cum_cases}."
string4 = (f"\n- The last recorded cumulative death total in Cheltenham is {cum_deaths}"
            f" however, the on {last_date}, {last_cum_deaths} were recorded as a cumulative total")

output = header + string1 + string2 + string3 + string4


string_builder = "## Last 10 days\n\n"
for i in range(0, 10):
    string_builder += (f"- {0 if data[i]['cases']['daily'] == None else data[i]['cases']['daily']} new cases & "
    f"{0 if data[i]['deaths']['daily'] == None else data[i]['deaths']['daily']} deaths ")
    if i == 0:
        string_builder += "today"
    elif i == 1:
        string_builder += "yesterday"
    else:
        string_builder += f"on {data[i]['date']}"
    string_builder += "\n"

# processing
if __name__ == "__main__":
    all_news = ""
    readme = root / "readme.md"
    readme_contents = readme.open().read()
    final_output = helper.replace_chunk(
        readme_contents,
        "summary_marker",
        f"{output}\n\n{string_builder}"
        )
    readme.open("w").write(final_output)