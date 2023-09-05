Methodology
===========
One of the key ingredients involved in this project is the methodology for creating extreme weather indicators from the raw weather data and then combining these with survey datasets. This process is described in depth in on this page.

Some methodological considerations from the survey perspective are also discussed here.

.. todo::
  Weahter section should have: How Climate change -> extreme weather?

  How merge Weather + Survey?

  Clean up

  Subheadings could include how we constructed weather indicators, how SPU index etc works

  When to use which kind of granularities? Household waehter vs Admin level vs national

  We have a LOT to talk about in this space, since Weather was our novel contribution, and we thought a lot about this

  Justify: Why we did method A as opposed to other methods B, C etc

.. _weather_methodology:

Weather methodologies
------------------------------------

Heatwaves & Heavy Rainfall Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. We download weather for grid over country. Talk about resolutions etc here

The Heatwave Duration Index defines the occurrence of a heatwave when the daily maximum temperature of more than two consecutive days exceeds the average maximum temperature by  5 °C or 0 °C as adopted by the MOC and IPCC respectively. This method efficiently discerns heatwaves by comparing temperatures to historical averages, aiding in heat-related risk assessment and adaptation planning. The indexing  is done in two main steps - 

1. compute the daily averaging thresholds, and  

2. identifying and quantifying the weather events.

The same definition is also adopted for the `heavy rainfall <https://en.wikipedia.org/wiki/Precipitation_types>`_ with the respective indexing deltas of 15mm and 0mm for MOC and IPCC respectively.


Droughts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Standardized Precipitation Index (SPI) is a drought quantification metric, commonly used for monitoring precipitation anomalies. It is dimensionless and scale independent metric, and can help identify the onset, magnitude, duration, and recovery of drought conditions.

It can be interpreted like below:

- SPI > 2         : Extremely Wet

- 1.5 < SPI ≤ 2   : Moderately Wet

- 1 < SPI ≤ 1.5   : Wet

- -1 ≤ SPI ≤ 1    : Neutral (Near Normal)

- -1.5 ≤ SPI < -1 : Dry

- -2 ≤ SPI < -1.5 : Moderately Dry

- SPI < -2        : Extremely Dry

The function for this is available in the codebase as `calculate_SPI`. Algorithm steps are:

- Gather long-term precipitation data.

- Calculate the rolling sum or average for a given time scale (e.g., 3 months).

- Fit the rolling sums to the gamma distribution to get the shape and scale parameters.

- Calculate the cumulative probability for each precipitation value using the gamma distribution.

- Convert the cumulative probability to SPI by applying the inverse of the standard normal cumulative distribution function (quantile function).

Implementations can be found in the code repo.



.. Interpolation
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. Discuss interpolation methods here. Discuss what new methods we provide and which we call from a library.
.. Discuss other interpolation methods that we could have used but did not use.

.. Combining weather data with survey data
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. Once we have the interpolated grid points for weather data time series, we did weighted avg to calc the weather for exact household. 
.. From that, we calculated the weather and survey indicators.


.. "Extreme" Weather indicators calculation
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. Put in context how/why we went from climate change to 'extreme' indicators (Because thats what we can observe and do analysis with!)

.. How are weather indicators calculated? What are the assumptions? What are the limitations?

.. List 'extreme' indicators we currently using 1,2,3..

.. How are they calculated?

Correlation Matrix Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Correlation analysis assesses the linear relationship strength and direction between two quantitative variables, yielding a correlation coefficient (-1 to 1) - implying weak or no, neutral and strong correlation. By understanding the correlation between different regions, one can get insights. For example, if two regions have a strong positive correlation, it implies that the weather patterns in those regions are similar. Implementation is provided in the code repository `get_correlation_matrix` 

DBSCAN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Density-Based Spatial Clustering of Applications with Noise (DBSCAN) is an algorithm that identifies high-density regions in data space separated by regions of lower density. Unlike many clustering algorithms, DBSCAN doesn't require specifying the number of clusters beforehand.

The key advantage of using DBSCAN for time series data is its ability to identify regions (or time periods) that display similar patterns or trends over time, regardless of their magnitude. 

The method is used in the repo in the `time_series_clustering` function and can be utilized to cluster regions based on their time series data. Regions in the same cluster display similar patterns or trends over time.

Dynamic Time Warping (DTW)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The dynamic time warping ( DTW) algorithm is able to find the optimal alignment between two time series. It is often used to determine time series similarity, classification, and to find corresponding regions between two time series. 

The DTW algorithm calculates the optimal (least cumulative distance) alignment between two time series. So, a higher DTW distance between two time series implies that the time series are less similar because it requires a larger "effort" to align them. Conversely, a lower DTW distance implies that the two time series are more similar. Therefore, if we plot as a heatmap, darker colors (lower values) would correspond to more similar weather patterns, while lighter colors (higher values) indicate less similar weather patterns.

The implementation of DTW is also in the repo as `compute_dtw`, which itself is a wrapper around the fastdtw package implementation.

.. _survey_methodology:

Survey methodologies
------------------------------------

Population level estimates from survey level observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Using survey weights for population level estimates from a survey is an art. It can be a tedious and time consuming process to recalibrate weights. Also, since every research question can require its own customised sub-sample from the survey data, it is left to the researcher to decide how to combine the survey weights to get the best population level estimates for that particular research question. Survey weights for each of the LSMS-ISA datasets are usually provided in the main 'demographic' file (aka cover file) from each wave. Further documentation on how the survey weights were calculated can be found in the 'Weighting' section of LSMS-ISA survey `documentation <https://microdata.worldbank.org/index.php/catalog/3557/study-description>`__.

Survey geocodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Historically, for technological and privacy reasons, geographic coordinates were not collected in household surveys. However this trend is changing and newer surveys have started collecting geo coordinates information. For privacy reasons, these are usually obfuscated to within a +-X km radius, as it the case with LSMS-ISA. There is also clustering of several households into one (lat,lon) point. Both of these features of publicly available household geocoordinates have to be taken into account when using them for analysis.

In case of LSMS-ISA, we can use the given (randomly obsfucated) geocoordinates to find the nearest weather grid points, and take the inversely distance weighted average for the appr. We then use the weather time series data from that gridpoint to calculate the weather indicators for that household for given temporal resolutions. 

Given an administrative level shapefile, the set of households which fall inside the administrative boundary can be used to calculate the administrative level indicators for that administrative boundary.

Geocoordinates from the DHS survey are available `here < https://dhsprogram.com/Methodology/GPS-Data.cfm>`_.

Non-response bias
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In case of surveys, there is a possibility of non-response bias, where some households or individuals may not respond to survey questions. The survey data can also be 'missing' for a variety of reasons. In case of systematic non-responses, the survey data may not be representative of the population at large. This has to be analysed prior to using the datasets for statistical analysis. Non-response bias can be corrected (eg by recalibrating weighting factors) 

Alternative methodologies can also be used to bypass some non-response issues. For example, Principal Components Analysis on the entire survey dataset may reveal six features which collectively explain 90% of the variance in poverty index. This kind of analysis could be useful when dealing with lots of missingness or non-response in the survey data.

Survivorship Bias
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Households may drop out of the survey over time, so a larger balanced longitudinal panel will have some survivorship bias. This has to be analysed prior to using the data for analysis. In case there is systematic dropout of households, survivorship corrections will need to be applied for accurate and high statistical power analysis.

Creating 'balanced' longitudinal panels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Previous attempts at making a balanced panel from Wave 1-4 created massive amounts of missingness because of the granularity difference between some of the files, the participant retention from other poverty domains, and a lack of uniform primary keys.  In other words, some of the files only operate on a household level and exponentially increase missing data when combined with files on an individual level. Additionally, the indicators on an individual level have different amounts of participants, and concatenating those files leads to a massive amount of missingness. 

Due to this, a 'single' uniform balanced panel across all domains and waves (with the goal of extending to future waves) is not possible.

Crosslinking multiple survey and official statistics sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
Every survey has a carefully though about questionnaire which is designed to collect data on a specific set of variables. Some demographic variables usually overlap, but there is usually a lot of variation in the variables collected by different surveys. Eg, the DHS survey has a specific focus on health, nutrition and poverty, while the LSMS-ISA survey has a specific focus on agriculture and incomes. 

To get a wholistic picture of the population, surveys and official statistics sources could be cross-linked and augmented together at appropriate granularity levels. For example, The World Bank Global Subnational Poverty `Atlas <https://datacatalog.worldbank.org/search/dataset/0042041>`_ has official statistics on domain level poverty at the subnational level (usually STATE level). This can be cross-linked with the LSMS-ISA survey data, especially for domains in which the survey is lacking (like health) to get a more complete picture of the population.

.. Data filtering rules
.. ^^^^^^^^^^^^^^^^^^^^^^



.. Other methodological discussions
.. ------------------------------------







.. the his can then be merged with the LSMS-ISA data to get a more complete picture of the population.


.. However, there is a possibility that the survey may not collect data on a specific variable of interest. For example, the LSMS-ISA survey does not collect data on household income. In such cases, it is possible to cross-link the survey data with other sources of data to get a more complete picture of the population. For example, the LSMS-ISA survey can be cross-linked with the DHS survey to get a more complete picture of the population. This can be done by using the household geocoordinates to find the nearest DHS cluster, and then using the DHS cluster ID to find the DHS survey data for that cluster. 

.. sampling scheme and 

.. In case of multiple surveys, there is a possibility of cross-linking the datasets to get a more complete picture of the population. For example, the LSMS-ISA survey can be cross-linked with the DHS survey to get a more complete picture of the population. This can be done by using the household geocoordinates to find the nearest DHS cluster, and then using the DHS cluster ID to find the DHS survey data for that cluster. This can then be merged with the LSMS-ISA data to get a more complete picture of the population.



.. Discuss most probable alternate methods that can be used in lew of what we have in current codebase.
.. This includes things like alternative measures to create heatwave/drought indices, etc
.. Can and if DHS or other survey data be used with this codebase? If so, how?

.. Also future things that we envision should be done, could have been done, or will have to be done later (the broad research area can be 10y long project) but weren't done during the 12 weeks.

.. Eg. 3D framework for thinking about (Poverty, Weather, Time), Causality + Simpsons paradox and how it can be mitigated when using this codebase



.. .. _data_prep:

.. Data preparation
.. ----------------


.. .. _evaluation:

.. Evaluation
.. ----------


.. .. _label_transform:

.. Label transformation
.. --------------------



.. .. _xai:

.. Explainable ML pipeline
.. -----------------------
