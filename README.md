# Sedona Experiments

## Set-up

Code in `sedona_experiments/src/get_data.ipynb`

1. Create virtual environment by running `bash init_venv.sh` then `source venv/bin/activate` in terminal.
    * **NOTE:** Java should be installed (check with `java -version`).
2. Copy data for experiments into `sedona_experiments/unprocessed_data`.
    * Data info:
        * 2 meter temperature
        * 5 years (2019 - 2023), hourly temporal resolution
        * Greenland, 0.25 spatial resolution

3. Split data into daily `.parquet` files. Stores files in `sedona_experiments/processed_data`.

## Import data to Sedona, SQL query Sedona

Code in `sedona_experiments/src/sedona_queries.ipynb` :

1. Read in parquet files into a Spark DataFrame.
2. Create geometry column for spatial queries.
3. Register DataFeame as a temporal view

**Polaris queries:**

* *Get Variable*

* *Timeseries*

* *Heatmap*

* *Find area*

* *Find time*

## Run experiments

Code can be found in `..`

**Pseudo code:** Get the query execution time for each experiment:

1. Impact of Changing Spatial and Temporal Resolution (old Figure 5)

        for hour,day, year:
            for spatial resolution 0.25, 0.5, 1.0:
                run get variable queries

        for 0.5, 1.0 degrees:
            for temporal resolution hour, day, month, year:
                run get variable queries (sans the ones performed above)

2. Impact of result size (old figure 6)

        for resolution pairs {(0.25,H), (0.25,Y), (0.5,M), (1.0,H), (1.0,Y)}:
            for percent of Greenland 1, 25, 50, 100:
                run get variable queries (sans the ones performed for Experiment 1)

3. Heatmap Query Perfoncace

        for spatial resolution 0.25, 1.0:
            for time span 1, 2.5, 5:
                run heatmap queries

4. Find Time Query Performance

        for temporal resolution hour, month, year
            for filter values 205, 240, 275, 310
                run find time queries