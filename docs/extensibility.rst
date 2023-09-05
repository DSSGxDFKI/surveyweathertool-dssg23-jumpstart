Extending the codebase
======================

Floods
-------

Global Floods Database
^^^^^^^^^^^^^^^^^^^^^^^^^^

For flood data we have event (observations) across times, where each
time frame we have the rasterfiles and corresponding precipitation data
and Population Exposed Per Country Per Event. 

Crucial points:

-  On website top right (“About the data”) hand corner are 2 summary csv files from top right 
  
   -  Flood event with a measure of intensity (1, 1.5, 2), persons dead and displaced, by country and by country X year.
  
-  We can find the description of the data from here: `data
   description <https://storage.googleapis.com/gfd_metadata/README_GFD.pdf>`__

-  We can now easily relate all the weather data, particularly the flood
   data by index or date (YYYYMMDD).

-  We can read the raster (map) images.

**Summary about the data:**

The Global Flood Database is a project backed by several institutions,
with primary collaboration between **Cloud to Street and The Flood
Observatory (DFO)**. The project provides valuable information on flood
occurrences and their impacts.

1. Data Source and Methods: The database uses NASA MODIS Aqua and
   Terra satellites for its data, which provide daily images at a 250-m
   resolution. The data includes flood maps dating back to the year
   1.    These maps represent significant events documented by the DFO.
   The selection of areas to map is done by intersecting a polygon from
   the DFO flood database with global HydroSHEDS watersheds.
2. Population Exposure and Precipitation Estimates: The database
   estimates population exposure by overlaying flood maps with the
   Global Human Settlement Layer (GHSL) population data. It uses the
   PERSIANN-CDR dataset for daily precipitation estimates, calculated by
   the 95th percentile of rainfall accumulation in the mapped
   watersheds.
3. Using the Website: The database website allows users to select a
   country and then choose a specific event by its start date. Data can
   be added to the map by selecting the desired layer from the toolbar.
   It is noted that events are mapped over watersheds, which may overlap
   multiple countries. Therefore, selecting a country will display all
   events intersecting with it, even if it is not the primary coverage.
   **Users can download the map as a GeoTIFF file, which comes with a
   metadata document. The GeoTIFF contains five bands: flooded,
   duration, clear_views, clear_perc, and jrc_perm_water.**
4. Downloadable Data: Users can download the precipitation data
   displayed on the website. They can also download population-exposed
   estimates for all events, either for the entire event or by country.
   These estimates have been filtered to remove noise and isolated
   pixels.
5. Exposed and Displaced Populations: The number of exposed people is
   calculated by intersecting the observed inundated area with
   population data. The number of displaced people is taken from the DFO
   event catalogue and is often reported by the media or the government
   of the affected country. The numbers of exposed and displaced people
   can differ significantly for a variety of reasons, and some flood
   events lack data on displaced persons.
6. Casualties and Causes: The database also includes data on casualties
   and causes of flood events, as reported in the media or by government
   agencies, recorded in the Dartmouth Flood Observatory Catalogue.


International Disasters Database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The International Disasters `Database <https://www.emdat.be>`_ is a database of natural disasters. According to it, the these three highest impact flooding events in Nigeria in last decade are 2012-0366-NGA , 2018-0365-NGA, 2010-0509-NGA. These can records can also be integrated into the codebase.


.. Integrating other countries of LSMS-ISA?
.. -----------------------------------------

.. Methodological factors
.. ^^^^^^^^^^^^^^^^^^^^^^^
.. The World Bank has released combined panels for selected LSMS-ISA countries, like Nigeria and Malawi, over some waves using certain sections of the survey, for eg just the household questionnaire. These panels may not contain all the relevant factors of interest for poverty analysis. For eg. geolocations coordinates, weighting factors, which may have to pulled and merged from individual wave datasets.

.. For countries that don't have combined panels, more data engineering is required to merge the individual wave datasets.

.. Some methodological factors that need to be accounted for when using or creating longitudinal panels for any LSMS-ISA country:

.. - Attrition rates and rebalancing of respondents across waves

..   * High attrition rates reduce inference options and power from panel data

.. - Survivorship bias should be investigated prior to merging. This may be a nig issue, for eg. unhealthy people may be underrepresented over time because they are more likely to die.

.. - Non-response and missing handling

..     * Some questions only asked to certain category of individuals, eg women/child/disabled etc

..     * Some questions only asked in certain waves, eg “Conflict” only asked in Wave 3

.. - Data Cleaning rules

..     * There is a dyanmic roster of individuals in a household between waves and also between two phases of a wave.

..     * Column labels for the same question are inconsistent over different files and waves.

.. - Balanced panel creation

..     * There is periodic rebalancing in surveys. For example, in Nigeira Wave 4 there was rebalancing of households from previous waves, and only one-third of the original households from Wave 1 remain. 

..     * It may not be meaningful to merge particular domains of the questionnaire if there is a low matching rate temporally or within a wave.

.. For more in depth understanding of some of these factors, please see :ref:`survey_methodology` section.

.. How to integrate to other geo-coded surveys like DHS?
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. .. todo::       
..     Talk about DHS geodata here https://dhsprogram.com/Methodology/GPS-Data.cfm

.. Changes required in merging or data cleaning methods?
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. _extending_weather:

.. New weather sources and methods
.. --------------------------------------
.. .. todo:: 
..     Jama+Shikhar to discuss how to add completely new weather source and extreme indicator, eg. bushfire

.. Floods
.. ^^^^^^^^
.. .. todo:: 
..     Jama to discuss how Flood and methodology (and code if available) used to integrate and create flood indicators

.. Drought
.. ^^^^^^^^^^^^^^^^^^^^^
.. .. todo:: 
..     Palmers index as alternative to SPI. Discuss here

.. 'Extreme' Indicator creation
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. .. todo:: 
..     Different weather events will require new methodology for indicator creation

..     Discuss Sensitivity of 'extreme' - global vs local defintions of extreme

.. Which temperature col?
.. ^^^^^^^^^^^^^^^^^^^^^^^
.. .. todo:: 
..     Night time vs daytime? temp drop at night etc.