'''
read in data to pandas and return pandas arrays. Import using:

from dataReader import farrow_and_weaning_data_reader, death_weights_data_reader


param: farrowing_data_file_path     =       directory path to farrowing data file
'''

import pandas as pd


def farrow_and_weaning_data_reader(farrowing_data_file_path="C:/Users/charl/GitHub/jsr_pigs/Farrowing Data.xlsx"):
    farrow_and_weaning_df = pd.read_excel(farrowing_data_file_path, sheet_name="Farrow and Weaning Data")
    return farrow_and_weaning_df


def death_weights_data_reader(farrowing_data_file_path="C:/Users/charl/GitHub/jsr_pigs/Farrowing Data.xlsx"):

    # PS Weaned for 2020 03 18 & 2020 04 01 have typos on excel (no 0 for month), uncorrected to keep data unchanged
    labels = ["Weaned 20200527a", "Weaned 20200205a", "Weaned 20200226", "Weaned 20200101", "Weaned 20200415a",
              "Weaned 20200311", "Weaned 20200610", "Weaned 20200122", "Weaned 20200205b", "Weaned 20200527b",
              "Weaned 20200415b", "Weaned 20200429", "Weaned 20200304", "Weaned 20200624", "Weaned 2020318",
              "Weaned 20200708", "Weaned 2020401", "Weaned 20200219"]
    death_weights_dfs_set = pd.read_excel(farrowing_data_file_path, sheet_name=labels)
    death_weights_df = pd.DataFrame()
    for sheet in death_weights_dfs_set:
        
        # get data (from table) and farm name (from top left cell)
        raw_data = death_weights_dfs_set[sheet].to_numpy()
        top_left_cell = death_weights_dfs_set[sheet].iloc[0].keys()[0]

        # create frame
        sheet_df = pd.DataFrame(data=raw_data[1:], columns=["Date Sold", "Number Sold", "Total Weight", "Average Weight",
                                                            "Dead Weights", "P2"])

        sheet_df["Farm"] = top_left_cell

        # amending line 18 mistake
        if sheet == "Weaned 2020318":
            sheet_df["Weaning Date"] = "20200318"
        elif sheet == "Weaned 2020401":
            sheet_df["Weaning Date"] = "20200401"
        else:
            sheet_df["Weaning Date"] = sheet[7:]

        # add data to end
        frames = [death_weights_df, sheet_df]
        death_weights_df = pd.concat(frames)

    return death_weights_df