Pipeline
============

Overview
-----------------
.. todo::
    Add image from Miro workflow here
    
    (time permitting) Add "Script breakdown" similar to last year's project.

.. _survey_pipeline:

Survey Pipeline
------------------------------------
.. todo:: 
    Review below text and adapt
    Add more detail on the survey pipeline
    Input and output from current pipeline
    Options and keyword arguments that can be passed to the pipeline
    How to use and tweak for future dev, other data
    Trey note - I believe this may happen for each wave? I’m not sure if we’re doing this overall of the time that we have, because that may make it more difficult


- Beginning with the individual files from the World Bank’s Harmonized Dataset, we combine them on a domain level based on the created index in collaboration with out partners
   
   * This consists of functions extracting the questions and renaming those columns that already exist on the pipeline

- We merge these individual files containing Post-Planting and Post-Harvest information from all 4 waves and rename the columns that we specifically need for our poverty indicator functions

- After, we take all those files, as well as the geolocations and add them to the ROSTER file containing all children within the survey and give them the information (on both a household and individual level?) 

- Then, run the poverty indicator functions to create the columns for each indicator and then an overall 



.. _weather_pipeline:

Weather Pipeline
------------------------------------
- Each of the temperature and precipitation data are taken from the Climate Prediction Center and read from a certain timeframe (data goes back to 1970) and is across the globe
- After, we pre-process the data for missing data, where it’s removed if the entire year has information missing, and if it’s missing for anything less then we impute previous day’s information
- Then, using Inverse Distance Weighting, we interpolate the data to a more granular level that would either map to the admin level
- Using the more granular information, we aggregate this daily data on a more seasonal level, achieving average temperatures and other information such as a drought index
    * An idea for generalizing it to admin level is having two functions that run almost identically just on different levels

.. todo::
    Input and output from current pipeline
    Options and arguments if any
    How to use and tweak for future dev, other data

.. _dash_pipeline:

Dashboard + Data Tool Pipelines
------------------------------------
- This tool should be scalable to a lot of the countries of interest, rather than just Nigeria. This means that any survey with specific geolocations would be able to track that information and output a lot of weather information regardless of source. This is the maximum added value to researchers everywhere, regardless of motive. We’re enabling Pilot Analysis. Lastly, we need to make sure we have a list of requirements that are needed for this tool to work perfectly (names of columns, where these columns are located, timeframe, country, etc.)

- This tool will also be accessed on streamlit, where any researcher should be able to upload a dataset (meeting certain requirements) and will be given back the same dataset with certain weather columns on it. 
On streamlit → we would have an upload file button, and then a download button would appear after with the data (topline research into this was done by Trey)

- Additionally, with the time range, I’m thinking about doing everything seasonally/monthly, as daily would be too risky/time consuming, in order to effectively give good information from this tool. 

- The weather portion acts as the backbone to our tool, as we take raw precipitation and temperature data from the Climate Prediction Center and transform the data to different levels and granularities (aggregate/interpolate). 

This tool’s input consists of a dataset with longitude and latitude as the first two columns as to confirm the geolocation of a particular area to gain weather information for
We also want to think about doing this not for specific households but aggregated areas like admin_1 level
Then, we would do some sanity/error checks, filter for a particular time frame, and run our weather pipeline mentioned previously to 


.. todo::
    Input and output from current pipeline
    Options and arguments if any
    How to use and tweak for future dev, other data

.. _data_outputs:

Processed data produced by pipeline
------------------------------------
Here we present the schema of the data we produce in the 'processed' folder.
We need to be very precise and exact on what datasets the pipeline is creating from the raw data. 
Especially for the weather data, as there is lot of options and ambiguity in creating weather datasets.
