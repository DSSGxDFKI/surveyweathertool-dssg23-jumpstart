
|MIT license| |Documentation Status| |made-with-python|

Analysing Impact of Climate Change on Child Poverty
==================================================

As a part of the Data Science for Social Good Fellowship (DSSGx) Kaiserslautern 2023, team 'jmpst' researched and created data pipelines for future multivariate statistical analyses on the impacts of extreme weather events on child poverty and developed an extensible data dashboard for visualization.

Data Science for Social Good
-----------------------------
Data Science for Social Good (DSSG) Fellowship trains aspiring data scientists to work on data science projects with social impact in an ethical manner. The 2023 edition of the Fellowship was held in person by the Rheinland-Pfälzische Technische Universität Kaiserslautern-Landau (RPTU) and Deutsches Forschungsinstitut für Künstliche Intelligenz (DFKI).

The project was run in partnership with `Save the Children UK <https://www.savethechildren.org.uk/>`_, `Oxford Dept of Social Policy and Intervention <https://www.spi.ox.ac.uk/>`_, and `UNICEF <https://www.unicef.org/>`_.

Problem
-------
Extreme weather events disproportionately impact millions of children living in poverty around the world. Multi-dimensional child poverty as per UNICEF definitions consists of six domains beyond monetary income, which are: Housing, Education, Health, Nutrition, Sanitation, and Water. The UNICEF poverty index measures the lack of these public and private material resources for children.

Extreme weather events are weather phenomena at the extremes of historical distributions, and/or rare for a particular geography or time. The impacts of extreme weather events on households and communities are both direct (e.g., decrease in income due to drought) and indirect (e.g., repercussions of reduced income on health, education, decisions). Extreme climate events are already impacting children across the world, especially in settings where government services are either absent or weak. Research is required to analyze and quantify the effect of these impacts.

Goal
----
The goal of this project is to reduce the entry barrier for research and analysis of extreme weather impacts on child poverty and well-being, and to provide an extensible framework for researchers and concerned citizens to analyze the same.

Solution
--------
We created a `data dashboard <https://dssg23-surveyweathertool.streamlit.app/>`_ which allows users to explore and visualize extreme weather and poverty datasets. The dashboard also allows users to upload geographical coordinates and receive weather time series for those locations. We also created data and feature engineering pipelines for LSMS-ISA surveys and extreme weather data.

.. image:: /docs/_static/bivariate_map.png
   :alt: Bivariate Map
   :align: center

About the Project
------------------
In this project, longitudinal and geocoded survey data was linked with weather datasets to analyze the impact of specific 'extreme' weather events, such as heatwaves, heavy rainfall and droughts, on multidimensional child poverty and well-being.

As a proof of concept, the project specifically focused on survey and weather data from the country of Nigeria. The project is set up in a modularized manner to allow for easy integration of other LSMS-ISA countries (such as Nigeria, Ethiopia, Malawi, Tanzania, and Uganda), other geo-linked surveys, such as `DHS <https://dhsprogram.com>`_ or `MICS <https://mics.unicef.org/surveys>`_, as well as other 'extreme' weather indicators.

Data
----
The Living Standards Measurement Study - Integrated Surveys on Agriculture (LSMS-ISA) data is collected by the World Bank for eight African countries and is available on the `World Bank Microdata Library <https://microdata.worldbank.org/index.php/catalog/lsms>`_.

There are several options for long and short-term temperature and precipitation data, with different pros and cons. The project presently uses `ERA5 <https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5#:~:text=ERA5%20is%20the%20fifth%20generation,land%20and%20oceanic%20climate%20variables.>`_ temperature data available from the `COPERNICUS <https://cds.climate.copernicus.eu/cdsapp#!/home>`_ project. NASA Earthdata `IMERG <https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDF_06/summary?keywords=%22IMERG%20final%22>`_ is used for sourcing the precipitation data.

From these raw weather datasets, we support analysis of three extreme weather events:


1. Heatwaves


2. Heavy rainfall


3. Droughts

Dashboard
---------
The `dashboard <https://streamlit.io/cloud>`_ allows visualization of extreme weather and poverty indicators. It also allows users to upload geographical coordinates and receive weather data for those locations.

Getting Started
---------------

1. Install Docker
    - Docker is a containerization platform that allows you to run applications in an isolated environment. This means that you can run applications without having to worry about dependencies and other issues that may arise from running the application on your local machine.

    - To install Docker, follow the instructions for your operating system here: https://docs.docker.com/get-docker/

2. Clone the repository
    - To clone the repository, run the following command in your terminal:

.. code-block:: console

   (.venv) $ git clone https://github.com/DSSGxDFKI/surveyweathertool-dssg23-jumpstart.git

This will create a folder called `surveyweathertool-dssg23-jumpstart` in your current directory. This folder contains all the code needed to run the project.

3. Download the data
    - Download all the raw datasets required to run the project in the exact same file heirarchy as described and shown in the instructions on sourcing the survey data and weather data. Further information on which datasets to download, and how to store them is available in :ref:`docs/getting-started`. Let the absolute path to the top level of the data directory be `/path/to/data`.

4. Build docker
    - In a terminal, navigate to the repository folder and run the following command to build the Docker container:

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
   
People
------
The package was developed during DSSGxGermany 2023, in partnership with Save the Children, University of Oxford, and  UNICEF. We thank the Rheinland-Pfälzische Technische Universität Kaiserslautern-Landau (RPTU) and Deutsches Forschungszentrum für Künstliche Intelligenz (DFKI) for funding the project. We also thank DFKI and University of Kaiserslautern for hosting the project. 

We thank the project staff for their guidance and support:

- `Julia Ostheimer - Project Technical Mentor <https://github.com/JOPloume>`_
 
- Gernot Schreider - Project Manager
 
- Stefanie Osewalt - Program Assistant
 
- Andrea Sipka - Program Manager
 
- Sebastian Vollmer - Program Director

Fellows working on the project:

- Jama Hussein Mohamud
 
- Prahitha Moova
 
- `Shikhar Mishra <https://github.com/smishr>`_

- Trey Roark

- Moshood Yekini


References
----------
Data attribution for the sources used in the project are available in the Code Documentation.

In case you utilise the project in your work, Bibtex citation is available below:

.. code-block:: console

    dssg_rptu_2023,
    author = {Jama Hussein Mohamud, Prahitha Moova, Shikhar Mishra, Trey Roark, Moshood Yekini},
    copyright = {2023 Data Science for Social Good (RPTU and DFKI)},
    title = {Analysing Impact of Climate Change on Child Poverty},
    organization={ { Rheinland-Pfälzische Technische Universität Kaiserslautern-Landau (RPTU) }, {Deutsches Forschungszentrum für Künstliche Intelligenz (DFKI) } },
    year = {2023},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://git.opendfki.de/dssgxdfki/dssg23-unicef.git}}

The project is released under the MIT License.

Copyright (c) 2023 Data Science for Social Good (RPTU and DFKI)

.. |MIT license| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/

.. |Documentation Status| image:: https://readthedocs.org/projects/ansicolortags/badge/?version=latest
   :target: https://surveyweathertool-dssg23-jumpstart.rtfd.io/

.. |made-with-python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/
