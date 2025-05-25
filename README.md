# Sedona Experiments

## Set-up

Code in `sedona_experiments/src/get_data.ipynb`

1. Create virtual environment by running `bash init_venv.sh` then `source venv/bin/activate` in terminal.
    * **NOTE:** Java should be installed (check with `java -version`).
2. Copy data for experiments into `sedona_experiments/unprocessed_data`
    * Data info:
        * 2 meter temperature
        * 5 years (2019 - 2023), hourly temporal resolution
        * Greenland, 0.25 spatial resolution

3. ??? Split data into daily .nc files ??? Need to do this anymore???

## Import data to Sedona
Code in `sedona_experiments/src/sedona_queries.ipynb`

1. Open 5 years of Greenland .nc with xarray
2. Convert to pandas DataFrame
3. Create Sedona object
4. Create columns in object etc..

<!-- ### Get Variable



### Timeseries

### Heatmap

### Find area

### Find time

## Run experiments -->


<!-- ### FOR MERRA 2 NOT SEDONA
Execution time	get variable	find time	heatmap
3H, 0.5x0.625			
day, 1 x 1.25			
year, 2 x 2.5			 -->