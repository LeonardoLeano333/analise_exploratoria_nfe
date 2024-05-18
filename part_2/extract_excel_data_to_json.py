from datetime import datetime
import pandas as pd


def write_output_files(data: str, file_name: str, output_path="output"):
    with open(f"output/{file_name}", "w") as file:
        file.write(data)


def generate_jsons_from_excel(excel_path="input/sample.xls", output_path="output", timestamp_suffix="%Y_%m_%d_%H_%M"):

    excel_data: pd.DataFrame = pd.read_excel(excel_path, sheet_name=None)
    now = datetime.now()

    for sheet_name, df in excel_data.items():
        file_name = sheet_name + "_" + now.strftime(timestamp_suffix) + ".json"
        json_data = df.to_json(orient="records")
        write_output_files(json_data, file_name, output_path=output_path)


if __name__ == "__main__":
    generate_jsons_from_excel()
