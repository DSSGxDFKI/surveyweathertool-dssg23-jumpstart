Getting started
===============
.. todo::
    This is the 5mins version of things. It references other in-depth pages.

.. _installing:

Installing the project
----------------------
1. Install Docker
    - Docker is a containerization platform that allows you to run applications in an isolated environment. This means that you can run applications without having to worry about dependencies and other issues that may arise from running the application on your local machine.

    - To install Docker, follow the instructions for your operating system here: https://docs.docker.com/get-docker/

2. Clone the repository
    - To clone the repository, run the following command in your terminal:

.. code-block:: console

   (.venv) $ git clone https://git.opendfki.de/dssgxdfki/dssg23-unicef.git

This will create a folder called *dssg23-unicef* in your current directory. This folder contains all the code needed to run the project.

3. Download the data
    - Download all the raw datasets required to run the project in the exact same file heirarchy as described and shown in the instructions on sourcing the survey data and weather data. Further information on which datasets to download, and how to store them is available in :ref:`getting-started:Getting-Survey-data`. Let the absolute path to the top level of the data directory be **/path/to/data**.

4. Build docker
    - In a terminal, navigate to the `dssg23-unicef` folder and run the following command to build the Docker container:

.. code-block:: console

   (.venv) $ docker build -t <your-image-name> .

Replace the `<your-image-name>` with a name of your choice. This may take a few minutes to complete the first time you run it.

5. Run docker
    - Once the image is built, run the Docker container by running the following command:

.. code-block:: console

   (.venv) $ docker run  -v <path/to/repo>:/app -v </path/to/data>:/app/data -t <your-image-name>

The `-v` parameter attaches a volume to the container. Adapt the <path/to/repo> and </path/to/data> as per your local configuration.

6. Run pipeline and dashboard.
    - Once the container is running, the code pipeline will run automatically. A dashboard will also be created and can be accessed (by default)at http://localhost:8501.
   
Folder structure for the data
-------------------------------------------
Please create the following empty folder structure in your local machine. This is where the data will be stored.

.. code-block:: console

    data
    ├── processed
    │   ├── survey
    │   |   └── nigeria
    │   ├── survey_weather
    │   └── weather
    │       ├── era5_temperature
    │       ├── flood_data
    │       ├── interpolated_weather
    │       └── nasa_historical_precipitation
    └── raw
        ├── nga_admin
        ├── survey
            └── nigeria

The `processed` folder is the destination for  final outputs from the pipeline, best used for further statistical analysis. The `raw` data folder contains the freshly downloaded, and some stages of intermediate processed data.

Broadly, there is a division between `survey` and `weather` with files relating to each store under those directories. 

`precipitation` and `temperature` folders contain the raw time series data for these weather observations.

For geospatial analysis, shapefiles (in .geojson format) for any country or administrative sub-division of interest will be required. This is to be stored inside `raw/shapefiles` directory.

Getting Survey data
-------------------
Nigeria LSMS-ISA (combined) survey data is available in the `World Bank Data Catalog <https://microdata.worldbank.org/index.php/catalog/5835>`_ . Links to the Nigerian Survey Data (General Household Survey) are available below:

#.  `Wave 1 (2010-2011) <https://doi.org/10.48529/y9e2-b753>`__

#.  `Wave 2 (2012-2013) <https://doi.org/10.48529/kxpy-aa72>`__

#.  `Wave 3 (2015-2016) <https://doi.org/10.48529/7xmj-q133>`__

#.  `Wave 4 (2018-2019) <https://doi.org/10.48529/1hgw-dq47>`__

#.  Concatenated demographics `data <https://microdata.worldbank.org/index.php/catalog/5835/study-description>`__  from all 4 waves

Executive data reports are also available for each wave. For example `Final Report <https://microdata.worldbank.org/index.php/catalog/3557/download/47679>`__ from Nigeria Wave 4.

Please create a new account on the website, accept the license and download conditions for all the datasets and download **Stata** format of the data.

.. note:: 
    The data is available in multiple formats, including CSV, Stata and SPSS files. The Stata format is used in this repository because it has data type information, and the data encoding includes the metadata which makes it easier to understand the levels taken by a particular column without reference or joining to the Metadata documentation. Eg. The column for **state** will have the values encoded as `1 = Abia`, `2 = Adamawa` in the STATA version, but in the CSV version it will just be `1` and `2`.

Once you have downloaded the four waves and the Unified Panel 2010-2019, store them under `raw/survey/nigeria`. The final directory structure should look like:

.. code-block:: console

    data
    └── nigeria 
        ├── raw
        │   └── survey
        │       ├── metadata
        │       ├── NGA_2010-2019_NUPD_v01_M_Stata
        │       ├── NGA_2010_GHSP-W1_v03_M_STATA
        │       ├── NGA_2012_GHSP-W2_v02_M_STATA
        │       ├── NGA_2015_GHSP-W3_v02_M_Stata
        │       └── NGA_2018_GHSP-W4_v03_M_Stata12

Getting weather data
--------------------
Currently, two weather datasets are integrated into the codebase, precipitation and temperature.

Precipitation
^^^^^^^^^^^^^

For precipitation, we source the data from NASA Earthdata (IMERG). 

1. Go to `this link <https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDF_06/summary?keywords=%22IMERG%20final%22>`_ to the data source page where you can find the Subset/Get data button. 
   
2. On clicking the button, you will see a popup window with options to subset the data as per your requirements. We recommend using the download method as Get File Subsets using the GES DISC Subsetter. You will also see options to subset the date and region (both using a bounding box or coordinates). Since we are sourcing precipitation data, we chose the variable "HQprecipitation". 

3. Once all the filters are set, on clicking the get data button, we will see a list of download links and download instructions. Please make sure you agree to the terms and conditions on the page and add the script provided in the download instructions on your local computer.

4. On running *wget* on the download files list, we get the daily data for the chosen time frame and location. 

5. Once the required data has been downloaded, stored it inside the `raw/weather/precipitation/1_raw_nc` directory.

.. code-block:: console

    data
    ├── nigeria
        └── raw
            └── weather
                ├── precipitation
                │   ├── 1_raw_nc

6.  The pipeline can be run as per the instructions on the repository.

Temperature
^^^^^^^^^^^
For temperature, we source the data from Copernicus (ERA5). 

1. `This is the link <https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form>`_ to the hourly data from 1940 to present.

2. Choose the variable 2m temperature as it is more accurate than surface temperature. Here too, similar to precipitation, there are options to select year, month, day, hour and geographical area. 

3. Select the format as NetCDF and click on show API request. Then you should see a code snippet that you can run to get the data. 

4. Once you have the NC file, store it inside the `raw/weather/temperature/1_raw_nc` directory.

.. code-block:: console

    data
    ├── nigeria
        └── raw
            └── weather
                └── temperature
                    ├── 1_raw_nc

5. The pipeline can be run as per the instructions.

Getting shapefiles
^^^^^^^^^^^^^^^^^^
It is important to have the shapefiles for the country or administrative sub-division (as well as for some weather events like floods, earthquakes) to be able to effectively do geospatial based analysis.

Usually, the National Bureau of Statistics or Meteorological Department websites will provide them for a given country. The World Bank also provides some State-level shapefiles in the Global subnational Poverty Atlas `here <https://datacatalog.worldbank.org/search/dataset/0042041>`_

The Nigeria shape files used in the project were downloaded from `The Humanitarian Data Exchange <https://data.humdata.org/dataset/geoboundaries-admin-boundaries-for-nigeria?>`_.

..     describe how to run pipeline to create poverty index and outcome and where data is stored in which format

.. Weather indicators
.. -------------------
..     describe how to run pipeline to create weather indicators and outcome and where data is stored in which format

.. Dashboard
.. ----------------
..     describe how to access the dashboard and link to the dashboard and ist documentation

..     Here we describe the commands needed to run the dashboard and view locally - COPY from dashboard page

..     Here we describe the how to use the data tool - COPY from dashboard page
