Data
====================

LSMS-ISA Survey
------------------------------------
For this study, Living Standard Measurement Study - Integrated Survey on Agriculture (LSMS-ISA) `data <https://www.worldbank.org/en/programs/lsms>`_ is sourced from the World Bank Data Catalogue. This survey primarily focusses on agricultural indicators, but also captures demographic, educational, and health information at the community, household, and individual level. 

The project used data for Nigeria. There are four waves of `data <https://microdata.worldbank.org/index.php/catalog/5835/study-description>`_ available, between 2010-2019. A unified panel for Nigeria is also available in the Data Catalogue, which concatenates some of demographic data from the individual waves together.

LSMS-ISA survey is also done for the following countries: Ethiopia, Malawi, Niger, Nigeria, Tanzania, and Uganda, Burkina Faso, Mali. The data is available for download in Stata, SPSS, and CSV formats, but this repository used the Stata files because they are more data engineered for ready analysis. The data is available in the `World Bank Microdata Library <https://microdata.worldbank.org/index.php/home>`_, and can be integrated with this project.

For further details on integerating other LSMS-ISA countries or surveys with this project, see 'Extending the Codebase' section.

Poverty Index
----------------
.. .. todo:: 
..   Trey - have a review. 
  
..   How are poverty indicators calculated? What are the assumptions? What are the limitations?
   
..   Fill in the exact formula for the poverty index.

..   Gernot note: the poverty index needs to be defined and explained how the 6 domains are defined, which questions go in which domain etc

This project focussed on multidimensional child poverty, which is defined as a child who is deprived in at least one of the dimensions of poverty. The dimensions of poverty proposed by various indices include health, education, standard of living, nutrition, water, sanitation, housing, information, protection from violence, and participation.

- As a proof of concept, the UNICEF definition of child poverty was used. This can be found `here <https://data.unicef.org/resources/child-poverty-profiles-understanding-internationally-comparable-estimates/>`__

    - UNICEF definition encompasses 6 dimensions of poverty: nutrition, health, water, sanitation, housing, education. 

    - For each of the six indicators that we have, we define a deprivation severity score (0, 1 or 2) and average it to get the overall poverty index.

    - Theory suggests to equally weight each domain when creating a poverty index score.

The UNICEF definition of multidimensional child poverty is survey-agnostic, and has to be adapted for usage with the LSMS-ISA surveys. Eg. the LSMS-ISA survey does not collect quality data on anthropometrics which are components in the UNICEF index. Therefore, the UNICEF definition was adapted to use the available data from the LSMS-ISA survey. 

The below table illustrates the mapping between the UNICEF domain and definition, and how it was adapted to work for the LSMS-ISA survey.

.. list-table:: UNICEF and adapted multidimensional child poverty definitions
   :widths: 25 50 50
   :header-rows: 1

   * - Indicator Domain
     - UNICEF Definition
     - LSMS Adapted Definition
   * - Housing
     - Number of separate rooms the members of the household occupy
     - Same as UNICEF
   * - Education
     - Level of education. If they ever attended school.
     - If they can read or write in any language. If they ever attended school
   * - Water
     - How far away the water source is
     - Same as UNICEF
   * - Sanitation
     - Kind of toilet facility the household uses. If the toilet facility is shared
     - Same as UNICEF
   * - Nutrition
     - Height & Weight for calculating stunting
     - Days without any (or not enough) food
   * - Health
     - Immunizations (Age 1-3). Medical Consultation (Age 3-5). Contraception (Age 15-17)
     - Same as UNICEF

.. _weather_data_sources:

Weather data sources
------------------------------------
.. .. todo:: 
..    Getting the Weather Data - See last year inspiration for a CLI script which can be one-run download with keyword options.

Precipitation
^^^^^^^^^^^^^^^^^^^^^^^
NASA collects a variety of satellite-based atmospheric measurements and provides several precipitation datasets at various resolutions and time intervals. In this project, Integrated Multi-satellitE Retrievals for GPM (IMERG) precipitation estimates were used. The data is available globally at 0.1° x 0.1° resolution for every half-hour beginning June 2000 to the delayed present. 


Daily precipitation data is created by averaging the non-missing precipitation values in every 0.1° grid box for a specific day of the year, over a range of years. It is suggested to use the Final Run (instead of the Late and Early runs) on the website.

.. .. todo:: 
..    NASA EarthData. Copy/adapt from report

..    describe and reference website for downloading, format, how data are stored etc

Temperature 
^^^^^^^^^^^^^^^^^^^^^^^^^^
The historical weather events satellite dataset from the Copernicus has hourly 2m air temperature reanalysis data available at 0.25° x 0.25° resolution between 2006 and 2018. 

Using linear interpolation, we enhance the temperature to an increased resolution of 0.1°x 0.1° and then average the non-missing values in every 0.1° grid box for a specific day of the year, over a range of years.


.. .. todo:: 
..    ERA5 (ECMWF). Copy/adapt from report

..    describe and reference website for downloading, format, how data are stored etc

.. Floods
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. todo:: 
..    describe and reference website for downloading, format, how data are stored etc

..    Concise and adapt from Flood text currently in Appendix section

