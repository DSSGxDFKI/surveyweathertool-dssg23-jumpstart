Categories
^^^^^^^^^^

\*All dimensions are treated equally, without any weights (for several
reasons)

\*In combination from the LSMS indicators given by the brief/World Bank
and UNICEFs own categorization

Weather Information/Findings
----------------------------

.. _general-notes-1:

**General Notes**
~~~~~~~~~~~~~~~~~

-  **Disaster magnitude scale and value** : The “intensity”of a specific
   disaster (the unit is automatically linked to the disaster type)
-  **Earthquake** : Richter Scale **Flood** : Km² (area covered)
   **Drought** : Km² (area covered) **Extreme Temperature** : °C
   (minimum or maximum value) **Epidemic** : Number of Vaccinated **Wild
   fire** : Km2 (area covered) **Storm** : kph (speed of wind)

**Defining Extreme**
~~~~~~~~~~~~~~~~~~~~

“Extreme weather events are ‘weather phenomena at the extremes of
historical distributions and are rare for a particular place and/or
time’. They include severe flooding, drought, heat waves, and cyclones.
The impacts of extreme weather events on households and communities are
both direct (eg, decrease in income due to drought) and indirect (eg,
repercussions of reduced income on health, education, decisions).” →
Partner Brief

**Flood Data:**
~~~~~~~~~~~~~~~

For flood data we have event (observations) across times, where each
time frame we have the rasterfiles and corresponding precipitation data
and Population Exposed Per Country Per Event

Crucial points:

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

1. Data Source and Methods: The database uses NASA’s MODIS Aqua and
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
3. Using the Website: The database’s website allows users to select a
   country and then choose a specific event by its start date. Data can
   be added to the map by selecting the desired layer from the toolbar.
   It’s noted that events are mapped over watersheds, which may overlap
   multiple countries. Therefore, selecting a country will display all
   events intersecting with it, even if it’s not the primary coverage.
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

**Weather datasets (order of priority)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+------------------------------------------------------+---+---+
| *         | Login                                                | W | C |
| *Source** |                                                      | e | o |
|           |                                                      | a | m |
|           |                                                      | t | m |
|           |                                                      | h | e |
|           |                                                      | e | n |
|           |                                                      | r | t |
|           |                                                      | e | s |
|           |                                                      | v |   |
|           |                                                      | e |   |
|           |                                                      | n |   |
|           |                                                      | t |   |
+===========+======================================================+===+===+
| Global    | none                                                 | f |   |
| Flood     |                                                      | l |   |
| `Databas  |                                                      | o |   |
| e <https: |                                                      | o |   |
| //global- |                                                      | d |   |
| flood-dat |                                                      | s |   |
| abase.clo |                                                      |   |   |
| udtostree |                                                      |   |   |
| t.ai/>`__ |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
| Inte      |                                                      |   |   |
| rnational |                                                      |   |   |
| Disaster  |                                                      |   |   |
| `DB       |                                                      |   |   |
|  <https:/ |                                                      |   |   |
| /www.emda |                                                      |   |   |
| t.be/>`__ |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
| ALL       | Every “extreme” weather event, (enough to be         |   |   |
|           | labelled natural disaster)NO COMMERCIAL USE or       |   |   |
|           | reproductionSince 1900 natural+manmade disasters     |   |   |
|           | with >10 deathsReally good classification and        |   |   |
|           | magnitude systemHave variety of events, we can       |   |   |
|           | subset by geography and typeIncludes lat long as     |   |   |
|           | well, and human/economic impact numbers              |   |   |
+-----------+------------------------------------------------------+---+---+
| CHIRPS    |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
| `IPAC     |                                                      |   |   |
| <https:// |                                                      |   |   |
| www.icpac |                                                      |   |   |
| .net/open |                                                      |   |   |
| -data-sou |                                                      |   |   |
| rces/>`__ |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
| **d       |                                                      |   |   |
| roughts** |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
| **heat    |                                                      |   |   |
| wave      |                                                      |   |   |
| s/extreme |                                                      |   |   |
| temp      |                                                      |   |   |
| erature** |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
| **crop    |                                                      |   |   |
| failures/ |                                                      |   |   |
| changes   |                                                      |   |   |
| in crop   |                                                      |   |   |
| yields**  |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
| **c       |                                                      |   |   |
| yclones** |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
| **wi      |                                                      |   |   |
| ldfires** |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
| **air     |                                                      |   |   |
| po        |                                                      |   |   |
| llution** |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+
|           |                                                      |   |   |
+-----------+------------------------------------------------------+---+---+

Pipeline Formation
------------------

**Resources**
~~~~~~~~~~~~~

-  “Harmonising” multiple rounds of surveys `into one
   dataframe <https://stackoverflow.com/questions/73110117/how-to-combine-multiple-survey-rounds-into-one-panel-data-r>`__
-  Template code/workflow for survey analysis (using R survey, but
   workflow remains same) - `ASDfree <http://asdfree.com/>`__
-  Poverty and inequality metrics/indices using survey data - `online
   recipe/guidebook <https://guilhermejacob.github.io/context/2-poverty.html#poverty>`__

.. _notes-1:

**Notes**
~~~~~~~~~



Aisha’s Geospatial Data Workshop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Get the shape file and specifically look at Geometry
-  Also, the administrative values. ADM1 is how they decided to divide
   it, like district
-  Double check projections are the same

   -  Aisha’s on mattermost, so ask her questions there

-  \*Most notes are on the Google Collaborations



**Weekly**
==========

Week 1: 6/16-23/2023 - Exploratory Phase
----------------------------------------

**(6/16) Initial Brainstorming**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  JMPST?
-  First two days should be spent understanding the project

   -  Exploration but with structure

-  Scope the time to check solution feasibility
-  Given the broad scope, establishing and keeping in mind the partner
   is imperative

   -  Does this go beyond data infrastructure and feature selection?

-  Delegation of tasks can be done in many ways

   -  I.e. independently, paired, grouped, etc.
   -  This is not to say we won’t work as a group checking each other’s
      work, but more to understand we can’t all do everything together

-  *Organization* is key
-  Goals

   -  Here’s what the partner talks about in the brief

” **More research into the causal impacts of extreme weather events on
children is needed to support child climate resilience in the future**.
It will be essential for this research **to disentangle the degree to
which extreme weather events impact child poverty** and wellbeing,
versus vulnerable children being more likely to live in areas worst
affected by extreme weather events – often not through their choice. It
will also be key to distinguish the impacts of distinct climate events
(inc. flooding, drought, wildfires) across a wider range of poverty and
wellbeing indicators. So far, **studies’ exclusive focus on monetary
poverty** means that we are still unclear of the effects of extreme
climate events on child poverty. Evidence is also needed across a
**wider range of countries,** where due to distinct geographies, the
impacts of climate events on children may differ.”

” **1.** How do extreme weather events impact child poverty and
wellbeing? How do these impacts differ in response to more intense and
frequent events?

**2.** Does access to social assistance/social protection moderate the
potential poverty and wellbeing effects of extreme weather? What other
factors also moderate these effects?

**3.** What do we know about the role of public service provision on
child poverty and child wellbeing when facing extreme weather events?”

-  Look at people in the references of these papers, look for similar
   solutions/projects

   -  Look at questions on miro

-  Partner Brief Notes

   -  Objectives

      -  

         1. Harmonization of Data Engineering

      -  

         2. Open Source Weather

         -  How are we finding the cross sections with these and survey
            data

   -  A LOT OF potential time scale issues given all the different
      issued surveys, weather events, etc.

      -  

         3. Find

      -  Data Infrastructure

-  Why are we doing this

   -  On an individual basis, can we take the weather events and poverty
      and harmonize them across different geographical locations, times,
      etc.

Next Week’s Plan
^^^^^^^^^^^^^^^^

-  

   1. Research and Read ourselves ( **Focus on bigger picture** )

   -  A. Goals, objectives, partner needs, etc. all need to happen
      because at the moment we’re looking at potential data and
      solutions and we’re just assuming we’re all on the same page about
      the problem at hand
   -  B. How to articulate the questions to the partner to get a
      sufficient reply

-  

   2. Collaborate to understand what the problem is, goals, where the
      data is gonna come from, the partner, etc.

**(6/19) Plan for Partner Call**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our first partner Call is Thursday from 2-3:30pm!

**Requirements** for progress report on Wednesday!

-  What happened and progress

   -  Presenting the name of the team
   -  Attitude, what is the attitude we want to have in our team

      -  Short Sentence

   -  Any experience that you have with data/data exploration

-  Then identify the central questions for the partner (5pm today)

   -  A list, not extensive and vague, but basics and understandings
      that we can send up front
   -  Ask conformational questions, about our understanding of certain
      tasks and concepts

Notes

-  Data harmonization is an understanding of combining certain datasets
   towards a certain goal

   -  We understand that this is a problem of linking climate change and
      child poverty

-  We’re essentially creating a data set full of relevant features in
   regards to climate weather events and child poverty?
-  We shouldn’t be afraid to ask for assistance with each other and look
   to that of which we’re all good at

Stakeholders (Scouting for Team Meeting)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  William Rudgard -

   -  Oxford, Department of Social Policy and Intervention
   -  Youth outcomes and transformations

-  Oliver Fiala

   -  Save The Children
   -  Dev economist, child inequality, health, nutrition etc
   -  Previously done DSSG Warwick
   -  

-  Enrique Delamonica

   -  UNICEF, Nigeria
   -  Senior statistics/data guru and Multi dimensional poverty expert
   -  https://blogs.worldbank.org/opendata/measuring-povertys-multiple-dimensions-new-guidance-countries-developing-multidimensional
   -  https://www.crop.org/Fellows/2014-2018/Enrique-Delamonica.aspx

-  Hernando gruesco hutado

   -  Oxford, Department of Social Policy and Intervention
   -  ML + econometrics, Bayesian + causality person
   -  Website - https://sites.google.com/cornell.edu/hernando-grueso
   -  Paper - Unveiling the Causal Mechanisms within Multidimensional
      Poverty
      https://assets.researchsquare.com/files/rs-1882302/v1_covered.pdf?c=1659459651

**(6/20) Morning Team Meeting**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Take a deeper dive into the project → Moshood, Jama, Shikar

   -  Start scoping out certain topics
   -  Starting with the information we were given
   -  Ex: Data provided, LSMS-IA surveys, etc.

-  Sift through the outside resources

   -  Gernot also gave resources

-  Look into last year’s project → Prahitha, Trey

   -  Either in group’s or individually

-  Creating the repository, creating the online workspace

Gernot: “Don’t spend too much time on scientific papers, they might not
be directly relevant. It’s a risk of a rabbit hole.”

\*Note: Data dictionary should be apart of final report

**(6/20) Last Year’s Project Takeaways (Prahitha & Trey)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **More different than our project than perceived**
-  They redefined what poverty means

   -  Rather than monetarily, they focused on 6 major components

.. image:: RackMultipart20230825-1-239u6w_html_e4bd89a33e65e7b6.png

-  Since we’re also adding weather data into the mix, we should use
   these six criterion as a **foundation** , not strict rule of thumb
   when defining child poverty, adding certain features when necessary
-  Prevalence and severity

   -  This is what they were analyzing and predicting

-  Data

   -  `MICS <https://dhsprogram.com/Data/>`__\ and
      `DHS <https://dhsprogram.com/Data/>`__\ are also potential surveys
      to work with if LSMS_ISA is insufficient, were used in last years
      project
   -  `Other data
      sources <https://github.com/DSSGxUK/s22_savethechildren#script-breakdown>`__

      -  Data is not provided, so if necessary, may need to contact
         Warwick or the involved project members

   -  Only for Nigeria

-  Model Building

   -  They build a model to predict said multidimensional poverty in
      particular areas
   -  Deep learning through autoencoding

      -  Utilizing Uber’s H3 Hexagonal Hierarchical Spatial Index

-  Issues

   -  Unfinished package without results nor clear methodology

Recommendations
^^^^^^^^^^^^^^^

-  Focus on creating a perfect and/or malleable public data set
   accessible by everyone

   -  Ex: Future years of the survey and/or more extreme weather events
   -  Focus on usability

      -  Not necessarily creating dashboards, but showing how this
         dataset/collection can be used

   -  Keeping it organized, meaning potentially separating by extreme
      weather event

-  Define our terms clearly

   -  “Extreme weather event” and “Child poverty”

      -  Clearly outlining conditions

-  Organization, especially among datasets, is key

   -  Coordinating with the notebooks and code

-  Come up with harmonizations across space and time
-  Start small and then cross-apply to different countries

**(6/20) Tasks for future Meeting**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Clarify resources available from last years project → Prahitha & Trey
-  Key Questions

   -  What features do we want to use?

      -  Both in Weather and LSMS_ISA Survey Data

         -  We’re gonna have to use our own methods such as corr plots
            in order to decipher which features are the most important

   -  How do we want to collectivize it?

      -  Dataset(s)? How extensive do we want this dataset/solution to
         be?
      -  To optimize feasibility and usability

-  Understand the data we have

   -  Both the features within and the lack of certain features

-  Develop some understanding of child poverty

   -  Are we using our own definitions

-  What is “extreme” weather

   -  We have precipitation data, but at what point do we consider
      extreme
   -  Quantifying “extreme”

**(6/21) Weekly Update Presentation**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Last Week

   -  What have you worked on?/What was accomplished?

      -  Gaining a deeper understanding of the topic (better than
         before), researching the possible datasets
      -  Preparation for the partner call
      -  First email was sent with array of questions regarding the
         project

         -  First meeting is Tomorrow 2-3:30pm

      -  Read and pulled from last year’s project at the University of
         Warwick to find anything we can cross-reference with this topic

-  Next Week

   -  What will you work on?

      -  Exploring datasets specifically in Nigeria, as we’ve decided to
         start with this country then expand that if time and resources
         permit

         -  Understanding the different information these datasets
            provide
         -  Keeping in mind transferability and scalability across
            countries

   -  What do you plan to accomplish

      -  Defining vague terms in the problem statement such as “extreme”
         and “child poverty” to the partner’s asking
      -  Start solidifying/deciding which features from recommended
         datasets we want to use in our analysis

-  Which issues are blocking you?

   -  Vague understandings of words within the objective; we haven’t had
      a chance to ask the partner what they’d like these criteria to
      look like

      -  I.e. “Extreme” weather events or “child poverty”

-  What asks do you have?

   -  We’d like to have more transparency from last year’s project
      regarding multidimensional poverty to utilize this as a foundation
      for our understanding.

**(6/21) Goals (Shikar, Prahitha, Trey)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  What does each file (in the links on the partner brief) mean/refer to
-  How they are related

   -  Similarities and Differences
   -  Both to each other and the LSMS-ISA table

-  Features of interest/disinterest
-  Each dataset, organize almost a library of data dictionaries
-  Start with Wave 1 and then cross-apply learnings to other waves

Literature Notes
^^^^^^^^^^^^^^^^

-  DFKI grant/proposal

   -  West and sub saharan africa is a major application geography
   -  Focussed on “events” studies, with angles from survival analysis
      and time series, modelling and ML
   -  Preprocessing and data infrastructure for future research
   -  Spatio-temporal modelling with NNs
   -  Social good angle - eg open sourcing for all scientific community
   -  Active learning surveys, bayesian + surveys

-  Oxford researchers

   -  Impact of climate risks on youth in (select) African countries
   -  Interested in extreme weather events

      -  Droughts, floods, and deadly storms

   -  
   -  Distangling confounding factors of impact

      -  Causal related

**(6/21) Weather Data Findings (Moshood, Jama)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Global Flood Database**

   -  Great website
   -  2 summary csv files from top right “About the data”

      -  Flood event with a measure of intensity (1, 1.5, 2), persons
         dead and displaced, by country and by country X year

   -  Lots of focus on maps

      -  May be rabbit hole to go too deep on maps for just floods

**(6/21) Decisions/Important Notes/Resources**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  EventStudies → Package for looking at events with lots of cool stuff

   -  R package - https://github.com/xKDR/eventstudies
   -  Julia package - https://github.com/xKDR/EventStudies.jl/tree/main

-  We should:

   -  Create an “intensity” vector for each record in the survey
      datasets from a given weather event
   -  Find/decide a common binning level that allows easy merging
      between survey dataset and weather categorisation.
   -  Create a vector for each weather event for the entire survey

-  Weather events do not look at administrative boundaries

   -  Some level of discretisation required
   -  This binning should still preserve the signal for research later.

.. _tasks-for-future-meeting-1:

**(6/21) Tasks for future Meeting**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Develop a template for weekly update presentations

Sebastian notes and questions

-  Current systems of categorisation/intensity are vague, sometimes
   politically/agenda guided.
-  WB preprocessing scripts!!
-  Resilience - ??
-  Andrea - child poverty & WELLBEING? - what is wellbeing
-  Verification and Augmentation via indirect measures

**(6/22) Goals: Data Exploration**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Find a structure for data (both survey and weather)

   -  Slight organization

-  Consolidate a solution task list, tangible to show our process
-  Finalize survey data

Shikhar task list

-  Get logins for all the surveys/datasets
-  Look into harmonisinsation meaning from Malawi -

WB Data access template -

Data Science for Social Good (DSSG) is a summer programme hosted by the
German Research Centre for Artificial Intelligence
(`www.dfki.de <http://www.dfki.de/>`__), which links socially-minded
organizations with data scientists to solve real-world problems and
produce insights or tools that the organizations can use in their own
work to tackle issues relating to public health, social welfare,
transparency and the environment. This year’s DSSG is held in
Kaiserslautern in Germany by the Data Science and its Applications group
of the DFKI.

One project stream is partnered with Save The Children, who are
interested in studying the ‘Causal impacts of extreme weather events on
child poverty’. In this project, DSSG fellows will use data from the
Malawi household surveys, as well as from other sources, to fit
spatio-temporal models to estimate the effects of events such as floods
or extreme weather events on multidimensional poverty indicators in
children, and to ask the questions:

Research questions

1. How do extreme weather events impact multidimensional poverty and
   monetary poverty for children? What role do intensity and frequency
   of such events play?
2. Does social assistance/social protection mediate the potential
   poverty effects of extreme weather events? What other factors
   determine the poverty effects for children?
3. What do we know about the role of public service provision on
   individual child poverty when facing weather shocks?

The target for predictions will be a range of measures including
nutrition, health, education, housing, water and sanitation, as well as
monetary poverty. Discrete events may be defined as moving above or
below certain established thresholds over time). Weather data will be
linked with, among others, the Global Flood Database, to investigate the
effect of flooding (their intensity of frequency) and to see if this has
a disproportionate effect on certain areas. Existing literature suggests
that areas experiencing poverty feel the effects of flooding and weather
events more strongly than richer areas or those with more developed
infrastructure. In this project we focus specifically on indicators of
poverty in children.

Research methods: regression analyses of poverty indicators, accounting
for repeated measures, spatio-temporal correlations, confounding and
mediating factors, uncertainty and prior knowledge through e.g. Bayesian
hierarchical methods.

Outputs will include one or more reports at the end of the summer
school, and, where applicable, reproducible code for implementing
similar analyses on future datasets in Malawi and other countries,
providing Save The Children and other organizations the ability to
expand their understanding to future datasets, countries, indicators and
climate-related risks as data becomes available.

**(6/23) Goals: Data Wrangling**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Start Data Wrangling

   -  Filtering for a couple of unnecessary questions

\*Firmly root design in requirements → DOCUMENT EVERYTHING

Week 2: 6/26-30/2023 - Data Exploration Part 2: Electric Boogaloo
-----------------------------------------------------------------

**(6/26) Rescoping Priorities**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  (PRIO 1) Find out exactly how partner will use the outcome of the
   data infrastructure

   -  Which skills do the users of the outcome have?
   -  How will they analye with their skills correlations/causality?
   -  Which tools and tech stacks do they have?
   -  How should it look like? - GUI filter tool, dashboard, Excel-File

-  Define Foundation Definition for “child poverty”, “well-being” and
   “extreme”

   -  Create visualizations for basic understanding

      -  (Trey) can draft a definition based on partner notes, last
         year’s project, and any other relevant information

   -  Find exact columns/features of exact data sources that are linked
      to the different dimensions of the definitions
   -  Categorize features in LSMS indicator categories

-  Develop a simple run-through of the project (prototype/mock solution)

   -  Source data from different data sources together
   -  Clean this data and preprocess it (apply data science expertise)
   -  Output this in a single file
   -  Data Science Add-on:

      -  E.g. provide visualizations (EDA)
      -  E.g. simple predictive model
      -  E.g. Analyze Feature Importances of the different features
         (once data is sourced & merged)

-  Do Deep Dive in all possible data sources & Decide on most important
   ones further one

   -  Precipitation, temperature
   -  Clarify this in this week in ourselves: Do we need the satellite
      data?
   -  Which other alternative data sources could be useful? → and are
      these open-source

**(6/27) Goals**
~~~~~~~~~~~~~~~~

-  Andrea, Julia, Sebastian, etc. are working out the scope of the
   project (shoutout ;))

-  What is Infrastructure, Extreme and Child Poverty? Meaning of life…:)

-  “A single file, whatever format that’s in, that has weather data
   that’s linked or that we can overlay and bring the survey data
   together” → William

   -  “A protocol for how these data can be brought together *&
      analyzed*”
   -  Just focused on expandability

EM-DAT visualisation notes

Could focus study on these three highest impact flooding events in
Nigeria in last decade. 2012-0366-NGA , 2018-0365-NGA, 2010-0509-NGA

= == ============= === ==== ===== ============ ====
0 40 2012-0366-NGA NGA 2012 Flood 7,000,867.00 4.02
= == ============= === ==== ===== ============ ====
1 93 2018-0365-NGA NGA 2018 Flood 1,922,332.00 0.86
2 3  2010-0509-NGA NGA 2010 Flood 1,500,200.00 0.59
= == ============= === ==== ===== ============ ====

2012 Nigeria floods - biggest in 40y
https://en.wikipedia.org/wiki/2012_Nigeria_floods

2018 Nigeria floods - https://reliefweb.int/disaster/fl-2018-000120-nga

Shikhar Notes

.. _goals-1:

**(6/29) Goals**
~~~~~~~~~~~~~~~~

-  Focus Area #2: Begin documenting the methodology behind understanding
   this spatial engineering

   -  So basically make a guide for how to do what we’re doing for both
      the team and the partner

      -  After finish your bigger issue, then figure out how to share
         that deliverable and methodology with the team

Shikhar Notes on Focus Area 3, Wk3, due diligence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

--------------

title: “Focus Area 3 Week 3”

title-block-banner: true

date: 2023-06-29

date-format: short

author-title: “Shikhar Mishra”

format:

html:

code-fold: true

jupyter: python3

--------------

.. code:: {python}


   import pandas as pd

   import numpy as np

   ## Pandas options for seeing things better

   # pd.get\_option('display.max\_columns')

   pd.set\_option('display.max\_columns', 30)

   # pd.get\_option('display.precision')

   pd.set\_option('display.precision', 2)

   pd.set\_option('display.float\_format', '{:,.2f}'.format)

Focus 3 Notes
=============

Focus area 3: Developing the data product facilitating certain analysis
features (Focus: Application Development & Data Science)

From rescope doc
----------------

pointers from Sebastian, Andrea, and Julia in Monday Wk3 meeting

\* Inspiration:

\*
`This <https://climatechange.europeandatajournalism.eu/en/germany/rheinhessen-pfalz/kaiserslautern-kreisfreie-stadt/kaiserslautern-stadt>`__
EDJ net project on localising climate change. Main
`page <https://climatechange.europeandatajournalism.eu>`__.
Methodological
`note <https://medium.com/european-data-journalism-network/glocal-climate-change-2071830aa640>`__.

-  Commercial: `Maxar <https://www.maxar.com/products/climatedesk>`__

-  GeoSuite: ESRI/ArcGIs

\* What could it look like???

\* Phenotype Project UK
`link <https://phenotypes.healthdatagateway.org>`__

\* Challenges & Tasks:

-  Do a due diligence check → which tools are already out there, what
   not?

-  Decide on the tech stack to be used

-  Extend the pipeline with taking the preprocessed data that was able
   to be combined for a certain granularity and for a certain use case
   and visualize this data in a defined user interface

-  Think about a way to package the application

-  Think about how users can interact with the application

-  Think about which analysis on top of that data makes sense

-  Have the code as maintainable and precise as possible

\* Motivation behind

\* Enable the general public/journalists etc. to inform themselves about
temporal developments regarding climate change effects on child poverty

(1) Related User Stories:

“As a citizen, I want to know how my children are affected, compared to
children in similar regions”.

“As a local journalist, I want to inform the public about the regional
differences in outcomes”

(2) Evaluate if there are interesting insights to be gained by comparing
    areas of “different speed” of climate change. Eg., does the baseline
    heat
    `matter <https://www.nature.com/articles/s41598-020-58638-8>`__?

\* Outputs:

\* Frontend application that makes it possible for a user to visualize
the sourced data layers and trigger of analysis on top of that data?

Stata Repository
================

Summary
-------

\* Naive search with “lsma isa” on github points to few repositories

\* UW Seattle has several github packages for data engineering
(“harmonising”) the LSMS-ISA datasets into a ready to use .dta (STATA)
files. They use these final files for students doing Policy studies
research etc.

\* Websites are here: for
`Methodology <https://github.com/EvansSchoolPolicyAnalysisAndResearch/335_Agricultural-Indicator-Curation>`__
and justification behind each of 163 features from LSMS-ISA.

\* Final .dta
`files <https://github.com/EvansSchoolPolicyAnalysisAndResearch/335_Data-Dissemination/tree/master>`__
are on this repository

\* Their focus is primarily on the agriculture related indicators, but
some income and demographics are also created.

\* they dont cover all the waves or the countries, but this entire
project is a good starting point to use into our work

\* Most important file to look first is their “summary” file

\* Our end goal use could be guided by their final product .dta files,
from which you can immediately start SQL style querying and
“split-apply-combine” analysis. See below

\* Not a single line of data engineering to be written, which is great!

.. code:: {python}


   harmonised\_repo = pd.read\_stata("/Users/shikharmishra/Work/dssg/dssg23-unicef/notebooks/EM\_DAT\_explore/Nigeria\_GHS\_W1\_household\_variables.dta", convert\_categoricals=False)

.. code:: {python}


   harmonised\_repo.describe()

.. code:: {python}


   harmonised\_repo.groupby(["lga"]).agg({"total\_income" : np.mean})

.. code:: {python}


   harmonised\_repo.groupby(["ea"]).agg({"total\_income" : np.mean}).sort\_values("total\_income",ascending=False)

\* Along with engineered data files, they also release summary
statistics for each of their engineered columns for each wave and
country that they used.

\* Code is in STATA .do files, is very intense and long. I dont think
DSSG fellows should adapt it for this project. However, we could use it
as a guidance for some mutually common indicators of interest.

\* The authors of the repo (who seem to be policy analysts/ dev
economics types) methodologically justify why/why not an indicator is
constructed for particualar WAVE X COUNTRY.

\* We should steal their formulas for some indicators, like Total Income
= :math:`\Sigma` Incomes from 5 different sources.

Other repos
-----------

\* Seasonal-Hunger-Malawi -
`code <https://github.com/EvansSchoolPolicyAnalysisAndResearch/337_Seasonal-Hunger-Malawi>`__

Concrete Deliverables
=====================

Exact files/outputs to be included in GitLab repo for handover

\* Data Dictionary for LSMS-ISA

\* Ideally both human and machine readible

\* excel/csv format knowledge base for files accross surveys and waves

\* Currently done at a file level, not at column level

\* “Helper” package (in python)

\* Sebastian liked this idea of helper utility/package that can be open
sourced out of our work

\* Time is challenge

\* Also need to be encapsulating and abstracting away all code/work
generated in the team on a regular basis

\* GUI tool

\* Bit like EM-DAT drag and drop and download data for Survey X Weather
for given years, time and countries. This could be good starting point

\* Maybe extension with geospatial UI, click and unclick for layers of
required features

Thoughts on tools to be used
============================

\* CSV since it is most popular

\* Also Feather as it is most efficient and data engineered for both R
and Python

Documentation of python
=======================

\* Sphinx - You should now populate your master file
/Users/shikharmishra/Work/dssg/wk3/dssg23-unicef/docs/index.rst and
create other documentation source files. Use the Makefile to build the
docs, like so: make builder. where “builder” is one of the supported
builders, e.g. html, latex or linkcheck.

Technical Note
~~~~~~~~~~~~~~

Fix the Python: Select Interpreter to your desired Python so every VS
code extension uses the same python environment and runs Quarto
effectively

Week 3: 7/3-7/2023 - Design Phase
---------------------------------

**(7/3) Weekly Planning**
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Review of Last week

   -  Focus Task #1

      -  Implementation of combining all files across waves

         -  Data dictionary filter parameter for relevant files
         -  Aggregation with timestamp and geolocation

   -  Focus Task #2

      -  Visualizations of weather data set on a spatial set is
         understood

         -  Can take a band and gauge certain geography’s features with
            it

   -  Focus Task #3

      -  Reviewed STATA, wrote paragraph

         -  It’s logistics and how they constructed Columns

      -  Looked at demo and scalability
      -  EM-DAT → front-end

-  This Week

   -  Finalize the Use Case Exploration

      -  Focus Task #1 - Prahitha & Moshood

         -  Begin/Investigate the new harmonized set with smaller
            columns, analyze, and scale up
         -  Investigate specific columns and criterion according to
            UNICEF guidelines (in email)
         -  Investigate the new harmonized panel data (2010-2019)

      -  Focus Task #2 - Trey & Jama

         -  Look more into the literature and methods approaching less
            visual combinations and more logistical (tabular)

            -  Which columns do we add to the data (e.g. severity from
               floods)

         -  Finalize which data sources are important

            -  Roping in the satellite data/images into this analysis

               -  Find out if it’s even needed
               -  Look into Hernando’s stuff for this

      -  Focus Task #3 - Shikhar

         -  Finalize due diligence check

   -  Overall the whole team

      -  Finish Vision & Scope document
      -  Shift gears into making decisions rather than focusing on
         understanding the last couple of things
      -  Plan the iterations to come!

**(7/3) Project Planning (Team Debrief)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  

   1. Data Preparation

   -  Survey
   -  Climate

      -  Temperature
      -  Flood/Precipitation

   -  \*Task: Building tabular data on a smaller scale → Small csv file

      -  Sub-task - Find some indicators (~ 20 columns)
      -  Sub-task - Merge together
      -  Sub-task - Data Cleaning
      -  Sub-task - HH level visualizations

-  

   2. Combine into a single dataframe

   -  Subtask - Household + Climate (Factors e.g. Severity, etc.)
   -  Subtask - Merge based on distance threshold
   -  \*Task - Prepare Presentations

-  

   3. Machine-Learning & Understanding time effects

-  

   4. Model building, simple but scalable

   -  Focus on readability, usability, and feasibility
   -  \*Goal: Taking our solution and using it for cross-country
      analysis

-  

   5. Front-end

-  \*NOTE: We have to go through all these tasks with a small subset,
   create that MVP of the front-end with JUST Nigeria and floods and
   then expand upon that and run through this process with more stuff

**(7/3) Merging Data Notes (Jama, Prahitha, Trey)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The latitude and longitude of the data for each household is slightly
   duplicated because within each enumeration area, a couple of points
   were chosen as anonymous points to plot to confide specific
   locations, and so some of them are plotted to a single point. It’s a
   weird intersection between an enumeration area and household-specific
   information
-  Severity calculation

   -  Girl what is this LMAO
   -  It seems to be both severity of the event at that moment AND/OR
      recurrence of this severity in a previous year range

.. image:: RackMultipart20230825-1-239u6w_html_6bde9deef23febc0.png

`Table <https://data.unicef.org/resources/child-poverty-profiles-understanding-internationally-comparable-estimates/>`__\ ^
(Brief Note)

-  Severity is a bootleg column, because it starts with 1.0, which
   assumes significant structural damage has occurred, and anything
   outside of the flood area has this value, which isn’t possible

   -  We need to *classify an area of affected and not affected*, and
      then within that calculate the severity
   -  

**(7/5) Daily Planning**
~~~~~~~~~~~~~~~~~~~~~~~~

-  Focus Area #1

   -  Come up with one solution that emphasizes efficiency

-  Focus Area #2

   -  Data source *all* of the desired
   -  There’s no scalable solution to each of the extreme climate
      events, make sure to display that extra effort needing to be put
      in for other weather events

      -  Consider when doing the planning
      -  Wants an overview table with all the extreme weather events,
         whether or not we found sources for them, and how we can
         use/measure them/combine them

         -  ^^^^^ Imperative

      -  Note that raw satellite image data is harder and not feasible
         to work with

         -  It’s a different game, we don’t have the time or the
            resources to work with this

      -  The households are not precise, but anonymity
      -  Potential Legal Trouble with this household pinpoints

-  Could have a bivariate map that shows area affected by climate
   vs. area affected by poverty
-  The plan

   -  We’d like to take relevant features/questions from the LSMS survey
      & Indicators, cross/merge that with climate data across several
      sources in order to create an accessible and usable front end that
      many can use for individual research and policy analyzing

.. _daily-planning-1:

**(7/6) Daily Planning**
~~~~~~~~~~~~~~~~~~~~~~~~

-  Finalize Source Sheet for partner to share with them (link)

**(7/6) Next Week Planning**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  \*Priority of next week is planning the architecture and what the
   final product will look like in the long run! (Have a dedicated
   issue)

Week 4: 7/10-14/2023 - Iteration 1
----------------------------------

.. _weekly-planning-1:

**(7/10) Weekly Planning**
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Look to github for this
-  Majorly, we’re reorganizing and planning out the next iterations and
   how we envision the final product to look. This lead to a
   restructuring of the github into epics and issues with that, and
   looking towards a more vertical slicing approach to our data product.

**(7/10) Vision & Scope Workspace (Mainly for Trey ;))**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Potential Deletions
^^^^^^^^^^^^^^^^^^^

In Solution:

Extract Transform Load (ETL) Data Pipeline

The data infrastructure pipeline offers the value of primarily
harmonizing paired indicator-domains to indicators using the LMS-ISA
Survey Data. The minimum viable product will focus on Nigeria with
scalable implementation to accommodate other countries of interest
captured in the LMS-ISA Survey Dataset Catalogue.

Additionally, the product will integrate relevant weather datasets which
are aligned with countries of interest and which aid the study of the
impact of weather events with related indicators from the survey data on
child poverty and well-being.

-  Product backlog (features/functional requirements)

   -  In the GitLab tasks going with the functionality we’re providing

      -  Detail down the functionality into userStories, and that is the
         foundation of the coding that you have to implement
      -  Separate them as separate issues so you can work
      -  independently on them

Prelim notes on solutions

-  

   (P) click/select and time to create visualizations based on the
       filters

   -  Get a front-end template, and add our JSON data and filter it
      based on the JSON data

-  

   (S) Library of functions (proper documentation/documentation page
       (“to-do manual”)) once you’ve downloaded the world bank dataset

   -  Expect a locally
   -  created database that spits out several dataframes from the format
      the user chooses
   -  SQL database

-  

   (S) Make some of those features in a simpler way on a webpage

-  Data privacy considerations

   -  Legal problems with publication of any personal information by the
      World Bank

-  Risks/Challenges

   -  Along with considerations

-  Come to some decisions that provide the lines drawn in the sand
   within the scope so we’re sufficiently secure that what they define
   they will accept from us

**(7/11) Daily Planning/Updates**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  (Julia) Streamlit *should* be what we use for the UI that’s easy and
   free to host after

Streamlit Notes
^^^^^^^^^^^^^^^

In iteration 1, the minimum deliverables we have defined are:

-  **Modularized Code** : Depending on your discussed granularity in the
   team, the tasks of the envisioned End-to-End Workflows are being
   modularized in scripts and further in each script in individual
   functions.
-  **pipeline.py** : To not commit early on to a specific workflow
   orchestration tool, we simply make a pipeline ourselves by importing
   the individual task scripts and their functions and construct them
   together in pipeline.py.
-  **Simple data product** : To focus on vertical slicing, we envision
   presenting a first data product deliverable at the end of iteration
   1. As both projects envision some sort of web app: To keep the web
   development part simplistic, we can achieve this with Streamlit (see
   example implementation).
-  **Unit Tests** : Already in iteration 1 we want to implement quality
   mechanisms. One such is implementing unit tests to test user-defined
   functions (see tests/ for examples).

**(7/12) Post-Presentation Planning/Updates**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Start looking rather into the mean aggregate, the climate aspect:

   -  Maybe the increase in temperature/precipitation over the past
      couple of decades?

**(7/12) Streamlit Notes (Thanks Alex & Diego)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Import streamlit package

Streamlit app gallery

Streamlit documentation

Folium as a map has a lot of promising widgets with

Awesome streamlit (check Mattermost)

**(7/14) Miro Workboard Notes (Shoutout Julia <3)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  We need to get creative and figure out a way to forward fill or
   impute some information for certain timestamps around the extreme
   weather events that we see since the survey is really only taken
   every two years

Week 5: 7/17-21/2023 - Iteration 1 Part 2: Electric Boogaloo
------------------------------------------------------------

.. _weekly-planning-2:

**(7/17) Weekly Planning**
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Finalize “combination” of survey and household data together and push
   to the dashboard

   -  Potential issue with combining into 1 csv file → Shikhar

      -  Look at later

-  Wrap up where we left off last week

   -  Survey Data Preparation

      -  Running into computational cost problems
      -  Waiting on other file for geographical and weight data

         -  No weights have been gathered yet\*

   -  Weather Data

      -  Lots of visualizations done, and Trey will review that draft
         merge request from Jama

   -  Dashboard Stuff

      -  Made a blank webpage
      -  Will maybe create mockup on Figma
      -  Dummy Data (subset) will be used on Streamlit

-  Major Takeaway: Finish up what is unfinished from last week, and
   prepare the dashboard and a mockup that can be reviewed by the
   partner

**(7/19) Daily Planning/Notes from Presentation**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Gernot talked about assigning one question per poverty index category
   for right now, and evolving it later

   -  Also that we could talk about the population density

-  Seth’s Comments

   -  Thinking about time that we’re given for the survey and
      cross-applying it with the weather
   -  20 extra columns with key weather indicators (weather in the past
      90 days) or other stuff

-  Sebastian’s Comments

   -  CHANGE in precipitation, not just in a particular time instance
   -  Climate velocity, how the velocity of climate change is measured
      (how to measure the speed of climate and to measure that in a few
      numbers)
   -  Not just a singular day matters, instead of average of temp but
      heatwaves are how many days do they have more than 40 degrees
      Celsius
   -  Effect of climate on the survey

**(7/19) Poverty Index Development**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `Reference
   Table <https://hdr.undp.org/content/2023-global-multidimensional-poverty-index-mpi#/indicies/MPI>`__
   for indicators and their weights

-  Other option from
   `Oxford <https://ophi.org.uk/multidimensional-poverty-index/>`__

.. image:: RackMultipart20230825-1-239u6w_html_7b5e6af24b33e51.png

.. image:: RackMultipart20230825-1-239u6w_html_5b3ae70a959d8bf.png

→ Files taken for each category:

-  Health:

   -  nup_phx_mod_o.dta: Mortality
   -  nup_pp_mod_s.dta, nup_ph_mod_s.dta, nup_pp_mod_t.dta: Household
      consumption (Nutrition)

-  Education:

   -  nup_pp_mod_c.dta, nup_ph_mod_c.dta, (nup_phx_mod_c.dta)

-  Living Standards:

   -  nup_pp_mod_n.dta, (nup_pp_mod_n1.dta, nup_phx_mod_k): Household
      Assets
   -  nup_pp_mod_v.dta, nup_ph_mod_v.dta: Housing & Electricity &
      Drinking Water & Sanitation & Cooking Fuel

→ Big concerns with files

-  Living Standards

   -  nup_pp_mod_v.dta

      -  \*Only across waves 3 & 4

   -  nup_ph_mod_v.dta

      -  \*Only across waves 1 & 2

   -  nup_pp_mod_n1.dta

      -  Has all four waves but only for the asset portion of the survey

   -  nup_phx_mod_k

      -  \*Only for waves 1 & 2

   -  nup_pp_mod_c.dta

      -  \*Only for waves 1 & 2

   -  nup_ph_mod_c.dta

      -  Has for all four waves and has all of the information but
         aggregation may need to happen with this file

   -  nup_phx_mod_c.dta

      -  \*Only for waves 1 & 2

   -  nup_pp_mod_t.dta

      -  \*Only for wave 3

   -  nup_phx_mod_o.dta

      -  \*Only has waves 1,2, & 3 in post harvest but does have a lot
         of mortality information

→ Big World Bank issues and findings

-  These are only contained in post-planting/harvest because the
   questions were omitted from per say, the post-planting part, and only
   in the post-harvest questionnaire

   -  We (Prahitha & Trey) looked at the questionnaire documents, and
      found some sections were only included in certain periods

-  This means that we would be able to calculate a poverty index for a
   household in a post-planting time frame, but would not for a
   post-harvest with the information we are given.

   -  I guess not huge issue, however leaves a lot of analysis to be
      desired

**(7/20) Daily Planning/Notes**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visualization Idea (Shoutout Gernot)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the visual styling of the UN/STC for the final presentation,
pictures and big fonts

Visualization idea: We have poverty (On the lower side) and extreme
weather (dropping/raining/pushing it down) somehow

**(7/20) Iteration 2 Planning**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have been thinking on areas to cover in iteration 2 (perhaps with
some overflow into iteration 3). We also got feedback on iteration one
prototype and analysis from all the three partners. Based on that we
feel, in order of priority, next areas to tackle are:

1. Survey only - engineering and analysis
2. Survey x Weather - engineering and analysis

——-

1. Weather only - engineering and analysis
2. Data Pipeline and Dashboard

Survey x Weather
^^^^^^^^^^^^^^^^

-  ’ **Meaningfully’ merging all the datasets**

   -  

      (1) Merge temperature and precipitation datasets to survey roster
          file

      -  Note Survey is at static time, weather is over time.

   -  

      (2) Merge flood data to survey roster file

      -  Different technique than temp/precip

   -  

      (3) Merge (1) + (2)

-  Feasibility - of temp+precip+flood+survey together??

   -  Expected final dataset from this process is at the appropriate
      ‘granularity’ for further ‘natural experiment’ studies

-  Spatial Analysis of Survey x Weather: investigate the geographic
   distribution of the interaction between poverty and temp/precip, and
   how this distribution changes over time.

   -  *Multivariate Analysis*: Some questions could include: how do
      changes in precipitation affect population migration patterns or
      poverty levels? Are there other variables (such as population
      density, local economy, infrastructure, etc.) that mediate this
      relationship?

      -  Start thinking in terms of bivariate maps

   -  *Population level census data*:

      -  How best to utilise this here? Many interesting variables
         require denominators to make sense

Survey
^^^^^^

-  ‘Meaningfully’ merging the different survey sub-datasets:

   -  

      (1) LEFT JOIN Survey roster file ← ‘normalised tables’ for all
          sub-datasets

      -  Note overlaps and matching rates
      -  Each of these can be done modularly, so we dont introduce any
         new NAs by coercing

   -  

      (2) Merge all the domains for two ‘balanced’ panels

      -  Eg ~4500 HH in Wv1-3 ~1400 HH in Wv1-4,
      -  Andrea: Start with Wv1-3 panel

   -  Use (2) as input to Survey x Weather merging

-  Exploratory data analysis of survey

   -  Data quality concerns with columns used as inputs for poverty
      indicators
   -  Zooming into the ‘child’ in child poverty

      -  The poverty index partners said to use is only for Age < 18. So
         we need to verify

-  Poverty Index

   -  Feature engineering raw questionnaire columns into ‘indicators’
      required for poverty index calculation
   -  [STRIKEOUT:Other derivative statistics of interest like in UN
      report (headcount ratios, poverty cutoffs, intensity of
      poverty)]\ Already too much for iteration two!
   -  Partners are primarily interested in the (very low and simplistic)
      benchmark of UNICEF poverty -

-  Survey Data Normalisation

   -  How to store data in format such that no ‘missing’ introduced
   -  How to merge meaningfully

-  “Balanced” panel creation - feasible combinations for specific use
   Missing Answers and questions
-  Survey weights

   -  are currently not in the combined panel data we are using. These
      have to be pulled and combined from individual wave data, similar
      to geo_coordinates
   -  Expected csv Header: [<lowest_level_of_weights>, weights_wv1,
      …weights_wv4, weights_combined?]
   -  Weight calibration for the combined panel should be done for
      balanced observations only. This is a v precise task (lots for
      minute multiplications and divisions)

-  Spatial analysis of survey data for poverty trends

   -  Similar to weather analysis done
   -  Are similar children ‘poor’ poverty ‘indicators’

-  Population level Census data & statistics (ground truths for Nigeria)
   best ways to 1) utilise 2) validate our results

   -  Population growth - correlations with survey and poverty findings

Dashboard & Visualisations
^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Important visuals for all of the above

-  ‘Bivariate maps’: Start with engineered poverty index ‘indicators’
   overlaid with nigeria temperature and precip

Weather
^^^^^^^

-  Floods

   -  Integrating floods to Survey data (at household level)
   -  Go from processed raster satellite image

-  Improve current algorithms for correlation/spatial analysis
-  Time-Series Analysis: As you have data across different waves, we
   could examine how certain trends evolve over time. This includes
   looking at how weather conditions, population data, and poverty
   change over time and their interdependencies.
-  What is extreme?

**(7/20) Poverty Index Bafoonery (Shoutout to the partner call)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Based on the Brief note from UNICEF

6 indicators

\*weird note, nup_phx_mod_flap_a_roster_b.dta → hb_19 has a column
called “what is the **correct** age?!”

**Location of columns (from harmonized dataset) (make sure to get pp &
ph when necessary)**:

-  Shelter (Dwelling rooms): on household ID

   -  For “how many separate rooms do the members of your household
      occupy?”

      -  nup_pp_mod_v.dta → hv_13 (Waves 3 & 4)
      -  nup_ph_mod_v.dta → hv_13 (Waves 1 & 2)

   -  For “how many people in your household” to create a people to
      household ratio:

      -  Any file using individual ID, we can just aggregate

-  Sanitation: on household ID

   -  For questions regarding sanitation facility

      -  nup_pp_mod_v.dta → hv50 & hv_51 (hv_87 & hv_89)
      -  nup_ph_mod_v.dta → hv50 & hv_51 (hv_87 & hv_89)

-  Water: on household ID

   -  For how far away the water source is (1-way)

      -  nup_pp_mod_v.dta → hv_48a & hv_48b
      -  nup_ph_mod_v.dta → hv_48a & hv_48b

   -  For water sources

      -  nup_pp_mod_v.dta → hv_74 & hv_47b
      -  nup_ph_mod_v.dta → hv_47b

-  Nutrition (will require a bit of calculation): on individual ID

   -  For international references of stunting to be imputed

      -  Link:
         https://www.who.int/tools/growth-reference-data-for-5to19-years/indicators/height-for-age

   -  For height and weight:

      -  nup_phx_mod_d.dta → hd_60_1 & hd_60_2 & hd_60_3
      -  nup_phx_mod_d.dta → hd_59_1 & hd_59_2 & hd_59_3

-  Education: on individual ID

   -  ifre.search(r’nup_pp_mod_c.dta’, filename):
   -  education_cols=education_cols+[‘hc_17’, ‘hc_10’]
   -  rename_dict= {‘hc_03’: ‘age_5y_older’, ‘hc_07’:
      ‘ever_attended_school’, ‘hc_17’: ‘currently_in_school’, ‘hc_10’:
      ‘education_level’}
   -  Is this child under 5?

      -  nup_pp_mod_c.dta → hc_03
      -  nup_ph_mod_c.dta → hc_03

   -  Ever attended school?

      -  nup_pp_mod_c.dta → hc_07
      -  nup_ph_mod_c.dta → hc_07

   -  Currently in school?

      -  nup_pp_mod_c.dta → hc_17
      -  nup_ph_mod_c.dta → hc_17

   -  Level of education?

      -  nup_pp_mod_c.dta → hc_10
      -  nup_ph_mod_c.dta → hc_10

-  Health

   -  Immunization records (*Lots of missing)

      -  nup_phx_mod_e.dta → he_10 & he_11 & he_12
      -  nup_phx_mod_e.dta → he_08

   -  For health consultation

      -  nup_phx_mod_d.dta → hd_09a

   -  Contraception

      -  nup_phx_mod_d.dta → hd_45
      -  nup_phx_mod_d.dta → hd_44

**(7/21) Iteration 2 Planning Review (Shoutout Andrea)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Be able to set your own weather thresholds would be a useful mechanic

   -  How many days above x temperature
   -  Not necessarily extreme but kills your crops

      -  Since this is a huge driver of poverty

-  DON’T share til week 12
-  Elevation/coverage (vegetation)

   -  Maybe start to integrate
   -  (i.e.) vegetation helps a lot with protecting from extreme
      temperatures so it could be interesting to look at with this

      -  Already in the survey

-  Don’t prioritize:

   -  “what is extreme”
   -  Wave 4
   -  Postpone weights

-  Do prioritize

   -  A way to integrate flood into the pipeline

-  Look to prioritizing list made by Andrea above (mwah thanks Andrea)
-  Julia: we should add unit tests

Week 6: 7/24-28/2023 - Iteration 2 Part 1
-----------------------------------------

.. _weekly-planning-3:

**(7/24) Weekly Planning**
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Focus more on in-depth analysis instead of making it engineering
   focused
-  

EMAIL Notes:

Dear all,

Thanks for sharing this vision and scope document. It fits well with our
expectations and will contribute significantly to moving our work
forward in this area!

Having a tool for visualising area level changes in climate and child
poverty and development outcomes will really help to make our work more
accessible to policymakers. **[This line refers to the dashboard
prototype with visualisation we have made. Cool]**

For maximum added value, it will be really important that the final tool
allows us to upload a list of geocoded locations (for instance from
surveys such as the LSMS-ISA), run an algorithm, and then download an
updated survey dataset with linked climate information (flood affected,
intensity, timing since last event etc.). **[There is no ‘tool’ here.
Dashboard is for visualising and EDA of trends. Pipeline run() function
is just what they need to transform raw data -> ready data for analysis.
If they really want a Windows ’’]**

This feature will be key for our undertaking for future ‘causal’
analyses of the impact of climate variation and extreme weather events
on children’s lives. So that applied researchers like ourselves can
easily use it, could the tool be written in R. **[I think R is out of
scope and non-negotiable. What we can guarantee is that the data output
from our Python code will be in R readable format (csv, parquet, feather
… take your pick)]**

There are a few other asks:

1. To help with expansion of this work to other LSMS-ISA countries,
   please could you make sure that any climate features you use are also
   present in the other LSMS-ISA countries. **[Jama says that’s what we
   are doing, so no need to worry here]**
2. To speed up the cleaning of LSMS-ISA surveys in the future, could you
   write out a summary of the necessary steps for this process in a word
   document. **[This is planned for the final report in Wk11-12. But do
   they want this right now??]**
3. Finally, this tool should be scalable to a wide variety of geocoded
   datasets that we are likely to use the in the future – like the
   Demographic and Health Surveys, and Multiple Indicator Cluster
   Surveys. **[We cant take any guarantee this. Firstly, data wrangling
   for surveys is very specific to each data. As we noted before, even
   within the waves, columns naming scheme is inconsistent. While they
   can follow the high level methodology, any code will still need
   porting and changing filename and paths for any other survey. Last
   mention of DHS was when they said that it cant be used for
   longitudinal analysis! What they really need here is a Jr research
   assistant who can do this porting for them in future]**

Lastly, we would emphasise that you get in touch with us as early as
possible when issues in the LSMS-ISA cleaning process come-up. We’re
on-hand to provide feedback to that.

Let us know if you have any questions.

Best,

Oliver, Enrique, Hernando, and Will

**(7/27) Morning Meeting (Partner call prep)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Review the email that william sent

   -  The visualization dashboard tool is good for policymakers and I
      think that’s our push for the project
   -  They want both a similar and different push. Similar to
      `this <https://github.com/meteostat/meteostat-python/tree/master>`__
      library → shoutout Julia, they want to be able to put locations of
      household as input and receive several columns of weather
      information, which I (Trey) think is doable, feasible, and useful
      for this project

-  Preparation for the partner call



Week 7: 7/31-8/4 - Iteration 2 Part 2: Revenge of the 2’s
---------------------------------------------------------

.. _weekly-planning-4:

**(7/31) Weekly Planning**
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Wrap up missing report
-  Moshood, Prahitha, and Trey will review the new strategy into merging
   that effectively rids the problem of solvable missingness
-  Figure out the columns that we can derive from the raw temperature
   data

   -  More useful and meaningful areas
   -  Brainstorm this

-  What questions can substitute and compensate for the missing data
-  Iteration 3 Planning:

   -  Which workflow orchestration tool would be best for the weather
      query tool we’re making for the dashboard

-  Investigate the “open source” library

   -  What can it provide, and what is the data source
   -  Does it provide all the data for all the countries we want to
      provide

**Creating powerful weather indicators**

I have ideas on how to create more powerful ‘weather’ indicators,
especially when you want to use them together with survey for
experimental study in tabular format. From the weather time series of
temp+precip, lets find patterns in frequency & amplitude of deviations
from long term trend.
`link <https://www.sciencedirect.com/science/article/pii/S0012825218303726>`__
to a resource with some ideas. For example, lets check if temperature TS
at an appropriate geographical level (EA or region as a starting point)
is stationary or not, after accounting for seasonality etc. If there is
a trend zoom into the trend and find patterns. Use heatwave information
we know eg 2013 heatwave from day M to N. There should be elevated
temperatures between those days. At the aggregate level find the average
duration and magnitude of anomalies in weather. This can help defined
new indicators like ``#Number of Days HH impacted by T\>T_threshold``

**(7/28-31) Missingness Report Column Decisions**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\*Look to Andrea’s message as well for some deliverables as well

**Shelter** :

Given -> Overcrowding: Separate rooms: sysmiss -> 89 (ph), 26 (pp)

Other possible questions -> From the housing sections of the harmonized
data

(nup_ph_mod_v.dta)

-  The outer walls of the dwelling are made of what material (hv_10):
   sysmiss -> 80
-  The roof of the dwelling is made of what material (hv_11): sysmiss ->
   69
-  The floor of the dwelling is made of what material (hv_12): sysmiss
   -> 73

(nup_pp_mod_v.dta)

-  The outer walls of the dwelling are made of what material (hv_10):
   sysmiss -> 25
-  The roof of the dwelling is made of what material (hv_11): sysmiss ->
   22
-  The floor of the dwelling is made of what material (hv_12): sysmiss
   -> 22

**Sanitation** :

Given -> Access to toilet facility of any kind

**Current columns are the best and have the least amount of missing
data** (hv_50, hv_51)

(nup_ph_mod_v.dta)

-  Kind of toilet facility the household uses (hv_50): sysmiss -> 95
-  Is this toilet facility shared (hv_51): sysmiss -> 2377

(nup_ph_mod_v.dta)

-  Kind of toilet facility the household uses (hv_50): sysmiss -> 25
-  Is this toilet facility shared (hv_51): sysmiss -> 6378

**Water** :

Given -> No/improved access to water sources

**Current columns are the best indicators**

(nup_pp_mod_v.dta)

-  For how far away the water source is (1-way)

   -  hv_48a (sysmiss -> 5084) & hv_48b (unit -> 5983)

-  For water sources

   -  hv_47b (sysmiss -> 43)

(nup_ph_mod_v.dta)

-  For how far away the water source is (1-way)

   -  hv_48a (sysmiss -> 238) & hv_48b (unit -> 1127)

-  For water sources

   -  hv_47b (sysmiss -> 268)

**Nutrition** :

Given -> Children under 5 + Stunting (3/2 SDs)

Other possible questions -> From the food security sections of the
harmonized data

(nup_phx_mod_d.dta): individual level

-  Height

   -  hd_60_1 (sysmiss -> 93681) & hd_60_2 & hd_60_3

-  Weight

   -  hd_59_1 (sysmiss -> 93688) & hd_59_2 & hd_59_3

(nup_pp_mod_s.dta): household level

-  Have you been faced with a situation where you did not have enough
   food

   -  hs_05 (sysmiss -> 170)

      -  hs_06_1 to hs_06_24: when did you experience this incident
      -  hs_07_1 to hs_07_3: what were the causes of this situation

-  How many meals are taken per day in hh

   -  By children between 5 and 15: hs_2b1 (sysmiss -> 16094)
   -  By adults 15 years or older: hs_02a (sysmiss -> 248)

-  How many days had no food in hh

   -  hs_01g (sysmiss -> 5375)

-  How many days had to rely on less preferred foods

   -  hs_01a (sysmiss -> 5326)

-  How many days had to limit variety of foods eaten

   -  hs_01b (sysmiss -> 5296)

-  How many days had to rely on limit portion size at meal times

   -  hs_01c (sysmiss -> 5311)

-  How many days had to reduce the number of meals

   -  hs_01d (sysmiss -> 5334)

(nup_ph_mod_s.dta): household level

-  Have you been faced with a situation where you did not have enough
   food

   -  hs_05 (sysmiss -> 45)

      -  hs_06_1 to hs_06_24: when did you experience this incident
      -  hs_07_1 to hs_07_3: what were the causes of this situation

-  How many meals are taken per day in hh

   -  By children between 5 and 15: hs_02b1 (sysmiss -> 15991)
   -  By adults 15 years or older: hs_02a (sysmiss -> 109)

-  How many days had no food in hh

   -  hs_01g (sysmiss -> 5144)

-  How many days had to rely on less preferred foods

   -  hs_01a (sysmiss -> 5112)

-  How many days had to limit variety of foods eaten

   -  hs_01b (sysmiss -> 5099)

-  How many days had to rely on limit portion size at meal times

   -  hs_01c (sysmiss -> 5112)

-  How many days had to reduce the number of meals

   -  hs_01d (sysmiss -> 5129)

**Education** :

Given -> About attending school

(nup_pp_mod_c.dta): individual level

-  Is the child under 5 (hc_03 -> 23385)

   -  Can also use age maybe? (ha_07 in the roster -> 11523)

-  Ever attended school (hc_07 -> 3708)
-  Currently in school (hc_17 -> 15923)
-  Level of education (hc_10 -> 15967)

(nup_ph_mod_c.dta): individual level

-  Is the child under 5 (hc_03 -> 52726)

   -  Can also use age maybe? (ha_07 in the roster -> 11523)

-  Ever attended school (hc_07 -> 48447)
-  Currently in school (hc_12 (w4) -> 78356, hc_13 (w1) -> 96674, hc_16
   (between waves 3 and 4 -> 59874)
-  Level of education (hc_10 -> 59713)

Other possible questions -> From the education section of the harmonized
data

(nup_pp_mod_c.dta): individual level

-  Can you read and write in any language (hc_06 -> 3658)

(nup_ph_mod_c.dta): individual level

-  Can you read and write in any language (hc_06 -> 48454)

**Health:**

Given ->

(nup_phx_mod_e.dta): individual level

Immunizations: 12-35 months

-  he_10 -> 41935 (for the overall data and not filtered for 12-35
   months)
-  he_08 -> 41912 (for the overall data and not filtered for 12-35
   months)

(nup_phx_mod_d.dta): individual level

Medical treatment: 36-59 months

-  hd_09a -> 90903 (for the overall data and not filtered for 36-59
   months)

Contraception: 15-17 years:

-  hd_44 -> 67233 (for the overall data and not filtered for 15-17
   years)
-  hd_45 -> 103891 (for the overall data and not filtered for 15-17
   years)

Other possible questions -> From the health section of the harmonized
data

(nup_phx_mod_d.dta): individual level

Money spent on OTC meds in the last 4 weeks

-  hd_16 -> 1374

If they have consulted a health practitioner in the last 4 weeks

-  hd_03 -> 335

**(7/31) Missingness Report**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previous attempts at making a balanced panel from Wave 1-4 create
massive amounts of missingness because of the granularity difference
between some of the files, the participant retention from other poverty
domains, and a lack of uniform primary keys. In other words, some of the
files only operate on a household level and exponentially increase
missing data when combined with files on an individual level.
Additionally, the indicators on an individual level have different
amounts of participants, and concatenating those files leads to a
massive amount of missingness.

Due to this, a uniform balanced panel across all domains and waves is
not possible. Moving forward, we’ve decided to create three different
files based on child poverty domain level. One contains 3 different
indicators as they were located in the same data file. These files are
as follows:

-  housing.pickle → Contains Shelter, Sanitation, and Water
-  education.pickle
-  nutrition.pickle

Our reformed index we recommend based on the available LSMS-ISA survey
data can be seen in reference [2].

The files we use to calculate the percentages combine the post-planting
(PP) and post harvest (PH) harmonized file(s) from the `World Bank’s
Uniform
Panel <https://microdata.worldbank.org/index.php/catalog/5835/study-description>`__.
After sub-setting them based on Wave and Visit, we calculated the
percentage of missingness out of the number of applicable observations
in that Wave. These applicable observations are the number of child
records taken at that time.

Listed below are tables containing the six domains from the UNICEF
poverty index, the missing data percentage within each of the column
we’re using, and the recommendations moving forward:

**Shelter, Sanitation, and Water Missingness** :

All indicator questions were found in the same two files
(`nup_pp_mod_v.dta <https://microdata.worldbank.org/index.php/catalog/5835/data-dictionary/F47?file_name=nup_pp_mod_v.dta>`__
&
`nup_ph_mod_v.dta <https://microdata.worldbank.org/index.php/catalog/5835/data-dictionary/F48?file_name=nup_ph_mod_v.dta>`__)
that were merged together. Within these files, as seen in the table
below, the questions we’re using for Wave 1 and 2, are only asked in the
Post-Harvest period and only Post-Planting in Waves 3 & 4.

Shelter Indicator Questions:

→ How many separate rooms do the members of your household occupy?

→ We created a number of people within a house column using the
individual IDs for each unique household ID. This column had no
missingness

→ Additionally, we created a room-to-person ratio to determine this
indicator. This has the same amount of missing information as
num_separate_rooms.

Sanitation Indicator Questions:

→ What kind of toilet facility do members of your household actually
use?

→ Is this toilet facility for the use of HH Members only or shared among
other households?

Water Indicator Questions:

→ How long does it take (1-way) to walk to the water source? (Time
Amount)

→ How long does it take (1-way) to walk to the water source? (Time Unit)

→ What is your main source of drinking water for the household during
the rainy season?

File Statistics:

Total observations [rows] in combined file: 38654

Houses with a Child (Applicable rows): 19376 (50.13%)

**Table 1: Shelter, Sanitation, and Water Observations & Missingness**

+----------+-----+--------------+-----+--------------+--------------+
| **Column | *   | **(Wave 2)** | *   | **(Wave 4)** | **Total**    |
| Name**   | *(W |              | *(W |              |              |
|          | ave |              | ave |              |              |
|          | 1   |              | 3   |              |              |
|          | )** |              | )** |              |              |
+==========+=====+==============+=====+==============+==============+
| **Obsv   | **  | **4789**     | **  | **5047**     | **19376**    |
| (Rows)** | 492 |              | 461 |              |              |
|          | 9** |              | 1** |              |              |
+----------+-----+--------------+-----+--------------+--------------+
| *        | **P | **PH**       | **P | **PH**       | **PP**       |
| *Visit** | P** |              | P** |              |              |
+----------+-----+--------------+-----+--------------+--------------+
| **Obsv** | **  | **4929**     | **  | **4789**     | **4611**     |
|          | 0** |              | 0** |              |              |
+----------+-----+--------------+-----+--------------+--------------+
| nu       | N/A | 42 Missing   | N/A | 47 Missing   | 26 Missing   |
| m_separa |     | An           |     | An           | An           |
| te_rooms |     | swers(0.85%) |     | swers(0.98%) | swers(0.56%) |
+----------+-----+--------------+-----+--------------+--------------+
| shar     | N/A | 1088 Missing | N/A | 1289 Missing | 1331 Missing |
| ed_sanit |     | Ans          |     | Ans          | Ans          |
|          |     | wers(22.07%) |     | wers(26.92%) | wers(28.86%) |
+----------+-----+--------------+-----+--------------+--------------+
| sa       | N/A | 58 Missing   | N/A | 37 Missing   | 25 Missing   |
| nit_type |     | An           |     | An           | An           |
|          |     | swers(1.18%) |     | swers(0.77%) | swers(0.54%) |
+----------+-----+--------------+-----+--------------+--------------+
| time_    | N/A | 154 Missing  | N/A | 84 Missing   | 37 Missing   |
| to_water |     | An           |     | An           | An           |
|          |     | swers(3.12%) |     | swers(1.75%) | swers(0.80%) |
+----------+-----+--------------+-----+--------------+--------------+
| wate     | N/A | 791 Missing  | N/A | 336 Missing  | 936 Missing  |
| r_time\_ |     | Ans          |     | An           | Ans          |
| unit     |     | wers(16.05%) |     | swers(7.02%) | wers(20.23%) |
+----------+-----+--------------+-----+--------------+--------------+
| drink    | N/A | 204 Missing  | N/A | 64 Missing   | 43 Missing   |
| _water\_ |     | An           |     | An           | An           |
| source   |     | swers(4.14%) |     | swers(1.34%) | swers(0.93%) |
+----------+-----+--------------+-----+--------------+--------------+

\*PP → Post-Planting

\*PH → Post-Harvest

\*N/A → observations indicates these questions were not asked during
this visit

Looking at the table above, we believe the UNICEF definition and
indicator questions are the best suited for the LSMS-ISA survey. All of
these questions we’ve adapted utilize the least amount of missingness as
compared to other potential questions we’ve researched. However,
sanitation does have the most amount of missingness out of the three.

**Nutrition Missingness** :

For the UNICEF-defined Nutrition indicator, the information was found in
only one
file(`nup_phx_mod_d.dta <https://microdata.worldbank.org/index.php/catalog/5835/data-dictionary/F51?file_name=nup_phx_mod_d.dta>`__),
which only asked for height and weight in the Post-Harvest period. Under
the current definition of poverty under the Nutrition domain, it focuses
on Stunting for ages 0-5 compared to an international reference metric,
using a combination of height, weight, and age [1]. However, as
indicated by the table below, height and weight have a significant
amount of missingness. As a result, we would recommend using some other
information for the child poverty index under the UNICEF definition. We
recommend using some combination of the questions listed here:

→ Have you been faced with a situation where you did not have enough
food?

→ How many days had no food in the household?

These questions have significantly less missing information and would be
more useful for analysis of a “deprived” nutrition indicator. Table 2
below shows the height and weight information we would use if we
continued with the UNICEF definition of Nutrition, given on an
individual level:

File Statistics:

Total observations [rows] in file: 107,668

Child (0-17) record: 53515 (49.70%)

0-5 age rows (Applicable Rows): 17334

**Table 2: UNICEF Defined Nutrition Indicator Observations &
Missingness**

+---------+-------+------------------+-------+------------------+-----+
| *       | **    | **(Wave 2)**     | **    | **(Wave 4)**     | **T |
| *Column | (Wave |                  | (Wave |                  | ota |
| Name**  | 1)**  |                  | 3)**  |                  | l** |
+=========+=======+==================+=======+==================+=====+
| **Obsv  | **14  | **13493**        | **12  | **13157**        | **5 |
| (       | 007** |                  | 858** |                  | 351 |
| Rows)** |       |                  |       |                  | 5** |
+---------+-------+------------------+-------+------------------+-----+
| **      | *     | **PH**           | *     | **PH**           | **P |
| Visit** | *PP** |                  | *PP** |                  | P** |
+---------+-------+------------------+-------+------------------+-----+
| *       | **0** | **14007**        | **0** | **13493**        | **  |
| *Obsv** |       |                  |       |                  | 0** |
+---------+-------+------------------+-------+------------------+-----+
| Height  | N/A   | 10458 Missing    | N/A   | 10343 Missing    | N/A |
|         |       | Answers(74.66%)  |       | Answers(76.65%)  |     |
+---------+-------+------------------+-------+------------------+-----+
| Weight  | N/A   | 10471 Missing    | N/A   | 10339 Missing    | N/A |
|         |       | Answers(74.76%)  |       | Answers(76.62%)  |     |
+---------+-------+------------------+-------+------------------+-----+

\*PP → Post-Planting

\*PH → Post-Harvest

\*N/A → observations indicates these questions were not asked during
this visit

From a different set of questionnaires
(`nup_pp_mod_s.dta <https://microdata.worldbank.org/index.php/catalog/5835/data-dictionary/F41?file_name=nup_pp_mod_s.dta>`__
&
`nup_ph_mod_s.dta <https://microdata.worldbank.org/index.php/catalog/5835/data-dictionary/F42?file_name=nup_ph_mod_s.dta>`__),
on a household level, are where we have the two questions previously
mentioned we’d like to use for analysis. These missing values are given
in Table 3 below.

File Statistics

Total observations [rows] in combined file: 38654

Houses with a Child: 38521 (99.66%)

**Table 3: LSMS-ISA Adapted Nutrition Definition Observations &
Missingness**

+------------+--------------+--------------+--------------+------+----+
| **Column   | **(Wave 1)** | **(Wave 2)** | **(Wave 3)** | **(  | *  |
| Name**     |              |              |              | Wave | *T |
|            |              |              |              | 4)** | ot |
|            |              |              |              |      | al |
|            |              |              |              |      | ** |
+============+==============+==============+==============+======+====+
| **Obsv     | **9836**     | **9486**     | **9173**     | *    | *  |
| (Rows)**   |              |              |              | *100 | *3 |
|            |              |              |              | 26** | 85 |
|            |              |              |              |      | 21 |
|            |              |              |              |      | ** |
+------------+--------------+--------------+--------------+------+----+
| **Visit**  | **PP**       | **PH**       | **PP**       | **   | ** |
|            |              |              |              | PH** | PP |
|            |              |              |              |      | ** |
+------------+--------------+--------------+--------------+------+----+
| **Obsv**   | **4996**     | **4840**     | **4697**     | **47 | ** |
|            |              |              |              | 89** | 45 |
|            |              |              |              |      | 91 |
|            |              |              |              |      | ** |
+------------+--------------+--------------+--------------+------+----+
|            |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| situati    | 59           |              |              |      |    |
| on_no_food |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 5            |              |              |      |    |
| Answ       |              |              |              |      |    |
| ers(1.18%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 107          |              |              |      |    |
| Answ       |              |              |              |      |    |
| ers(0.10%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 40           |              |              |      |    |
| Answ       |              |              |              |      |    |
| ers(2.28%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 4            |              |              |      |    |
| Answ       |              |              |              |      |    |
| ers(0.84%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 0            |              |              |      |    |
| Answ       |              |              |              |      |    |
| ers(0.08%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 0            |              |              |      |    |
| A          |              |              |              |      |    |
| nswers(0%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 0            |              |              |      |    |
| A          |              |              |              |      |    |
| nswers(0%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | **215**      |              |              |      |    |
| A          |              |              |              |      |    |
| nswers(0%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| num\_      | 222Missing   | 124Missing   | 102Missing   | 41   |    |
| da         | An           | An           | An           |      |    |
| ys_no_food | swers(4.44%) | swers(2.56%) | swers(2.17%) |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 4            |              |              |      |    |
| Answ       |              |              |              |      |    |
| ers(0.86%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 0            |              |              |      |    |
| Answ       |              |              |              |      |    |
| ers(0.08%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 0            |              |              |      |    |
| A          |              |              |              |      |    |
| nswers(0%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | 0            |              |              |      |    |
| A          |              |              |              |      |    |
| nswers(0%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+
| Missing    | **493**      |              |              |      |    |
| A          |              |              |              |      |    |
| nswers(0%) |              |              |              |      |    |
+------------+--------------+--------------+--------------+------+----+

\*PP → Post-Planting

\*PH → Post-Harvest

As shown above, the missingness is significantly less than using the
demographic information with the UNICEF-specific definition, and better
for longitudinal analysis. The thresholds are malleable, however the
updated definition is shown in the adapted table at the end of this
report [2]. As a result, we would recommend moving forward with these
questions.

**Education Missingness** :

In terms of the education indicator, UNICEF defines it on an individual
level, based upon different age groups. Currently, it depends on whether
or not they’ve ever attended school, are currently in school, and their
level of education. The particular questions from the files
(`nup_pp_mod_c.dta <https://microdata.worldbank.org/index.php/catalog/5835/data-dictionary/F2?file_name=nup_pp_mod_c.dta>`__
&
`nup_ph_mod_c.dta <https://microdata.worldbank.org/index.php/catalog/5835/data-dictionary/F3?file_name=nup_ph_mod_c.dta>`__)
we chose to model the UNICEF definition are as follows:

→ What is the highest education level completed?

→ Have you ever attended school?

As a quick note, the currently in school questions are more difficult to
model as these surveys ask year specific questions. For example, “were
you currently in school for the 2018/2019 year?”, which has a lot of
missingness, and would require some time sorting for us to analyze it
anyway.

If we want to use the columns with the least amount of missingness, we
recommend using whether they have ever attended school *and* their
literacy ability, which are given by the following questions in the same
files:

→ Have you ever attended school?

→ Can you read and write in any language?

File Statistics:

Total observations [rows] in combined file: 148,113

Child (0-17) record: 69563 (46.97%)

0-5 age rows: 18204

Applicable (6-17) Rows (Applicable Rows): 51359

**Table 4: Education Indicator Observations & Missingness**

+----------+------------+------------+------------+------------+---+
| **Column | **(Wave    | **(Wave    | **(Wave    | **(Wave    | * |
| Name**   | 1)**       | 2)**       | 3)**       | 4)**       | * |
|          |            |            |            |            | T |
|          |            |            |            |            | o |
|          |            |            |            |            | t |
|          |            |            |            |            | a |
|          |            |            |            |            | l |
|          |            |            |            |            | * |
|          |            |            |            |            | * |
+==========+============+============+============+============+===+
| **Obsv   | **15554**  | **17523**  | **9142**   | **9140**   | * |
| (Rows)** |            |            |            |            | * |
|          |            |            |            |            | 5 |
|          |            |            |            |            | 1 |
|          |            |            |            |            | 3 |
|          |            |            |            |            | 5 |
|          |            |            |            |            | 9 |
|          |            |            |            |            | * |
|          |            |            |            |            | * |
+----------+------------+------------+------------+------------+---+
| *        | **PP**     | **PH**     | **PP**     | **PH**     | * |
| *Visit** |            |            |            |            | * |
|          |            |            |            |            | P |
|          |            |            |            |            | P |
|          |            |            |            |            | * |
|          |            |            |            |            | * |
+----------+------------+------------+------------+------------+---+
| **Obsv** | **8721**   | **6833**   | **8692**   | **8831**   | * |
|          |            |            |            |            | * |
|          |            |            |            |            | 0 |
|          |            |            |            |            | * |
|          |            |            |            |            | * |
+----------+------------+------------+------------+------------+---+
| le       | 1546       | 6561       | 1602       | 8676       | N |
| vel_of_e | Missing    | Missing    | Missing    | Missing    | / |
| ducation | Answe      | Answe      | Answe      | Answe      | A |
|          | rs(17.73%) | rs(96.02%) | rs(18.43%) | rs(98.24%) |   |
+----------+------------+------------+------------+------------+---+
| ever     | 48 Missing | 6517       | 26 Missing | 8647       | N |
| _attende | Answ       | Missing    | Answ       | Missing    | / |
| d_school | ers(0.55%) | Answe      | ers(0.30%) | Answe      | A |
|          |            | rs(95.38%) |            | rs(97.92%) |   |
+----------+------------+------------+------------+------------+---+
| 3        | N/A        | 0 Missing  | **15,241** |            |   |
| Missing  |            | A          |            |            |   |
| Answer   |            | nswers(0%) |            |            |   |
| s(0.03%) |            |            |            |            |   |
+----------+------------+------------+------------+------------+---+
| rea      | 35 Missing | 6519       | 28 Missing | 8647       | N |
| d_write_ | Answ       | Missing    | Answ       | Missing    | / |
| language | ers(0.40%) | Answe      | ers(0.32%) | Answe      | A |
|          |            | rs(95.40%) |            | rs(97.92%) |   |
+----------+------------+------------+------------+------------+---+

\*PP → Post-Planting

\*PH → Post-Harvest

\*N/A → observations indicates these questions were not asked during
this visit

Similarly, Table 4 above shows the literacy rate column has
significantly less missingness than the level of education. Thus, moving
forward, we should use the literacy question instead.

**Health Missingness** :

Lastly, looking at the health, the information based on the current
definition (immunizations) in the data was only taken for Waves 1 and 2,
so there’s isn’t any data for other waves in the post-harvest-only file
(`nup_phx_mod_e.dta <https://microdata.worldbank.org/index.php/catalog/5835/data-dictionary/F52?file_name=nup_phx_mod_e.dta>`__),
seen in Table 5 below. The questions in these files regarding the health
indicator from UNICEF are as follows:

→ Was this person immunized against DPT 1?

→ Was this person immunized against DPT 2?

→ Was this person immunized against DPT 3?

→ Was this person immunized against Measles?

File Statistics:

Total observations [rows] in file: 43940

Child (0-17) record: 22623 (51.49%)

1-3 age rows (Applicable Rows): 2543 (5.79%)

**Table 5: UNICEF Health Indicator Definition Observations & Missingness
(Age 1-3 condition only)**

+--------+-----------+---------------+-----------+---------------+----+
| **     | **Missing | **Missing     | **Missing | **Missing     | *  |
| Column | (Wave     | (Wave 2)**    | (Wave     | (Wave 4)**    | *T |
| Name** | 1)**      |               | 3)**      |               | ot |
|        |           |               |           |               | al |
|        |           |               |           |               | ** |
+========+===========+===============+===========+===============+====+
| **Obsv | **1289**  | **1254**      | **0**     | **0**         | ** |
| (R     |           |               |           |               | 25 |
| ows)** |           |               |           |               | 43 |
|        |           |               |           |               | ** |
+--------+-----------+---------------+-----------+---------------+----+
| **V    | **PP**    | **PH**        | **PP**    | **PH**        | ** |
| isit** |           |               |           |               | PP |
|        |           |               |           |               | ** |
+--------+-----------+---------------+-----------+---------------+----+
| **     | **0**     | **1289**      | **0**     | **1254**      | *  |
| Obsv** |           |               |           |               | *0 |
|        |           |               |           |               | ** |
+--------+-----------+---------------+-----------+---------------+----+
| DPT_1  | N/A       | 929Missing    | N/A       | 1000Missing   | N  |
|        |           | An            |           | An            | /A |
|        |           | swers(72.07%) |           | swers(79.74%) |    |
+--------+-----------+---------------+-----------+---------------+----+
| DPT_2  | N/A       | 928Missing    | N/A       | 999Missing    | N  |
|        |           | An            |           | An            | /A |
|        |           | swers(72.00)% |           | swers(79.66%) |    |
+--------+-----------+---------------+-----------+---------------+----+
| DPT_3  | N/A       | 929Missing    | N/A       | 1000Missing   | N  |
|        |           | An            |           | An            | /A |
|        |           | swers(72.07%) |           | swers(79.74%) |    |
+--------+-----------+---------------+-----------+---------------+----+
| M      | N/A       | 925Missing    | N/A       | 1000Missing   | N  |
| easles |           | An            |           | An            | /A |
| Immun  |           | swers(71.76%) |           | swers(79.74%) |    |
+--------+-----------+---------------+-----------+---------------+----+

\*PP → Post-Planting

\*PH → Post-Harvest

\*N/A → observations indicates these questions were not asked during
this visit

In a separate file
(`nup_phx_mod_d.dta <https://microdata.worldbank.org/index.php/catalog/5835/data-dictionary/F51?file_name=nup_phx_mod_d.dta>`__),
we acquired the questions for the UNICEF Definition for ages 3-5 and
15-17 about healthcare and contraception. These questions are as
follows:

→ Where did this person’s medical consultation take place?

→ Do you currently use family planning?

→ What type of family planning do you currently use?

File Statistics:

Total observations [rows] in file: 107668

Child (0-17) records: 53515 (49.70%)

3-5 age rows (Applicable rows): 6379

15-17 age rows (Applicable rows): 7342

Non-Applicable: 39794

**Table 6: UNICEF Health Indicator Definition Observations & Missingness
(Age 3-5 condition only)**

+-------------+-----------+-----------+-----------+-----------+----+
| **Column    | **Missing | **Missing | **Missing | **Missing | *  |
| Name**      | (Wave     | (Wave     | (Wave     | (Wave     | *T |
|             | 1)**      | 2)**      | 3)**      | 4)**      | ot |
|             |           |           |           |           | al |
|             |           |           |           |           | ** |
+=============+===========+===========+===========+===========+====+
| **Obsv      | **1930**  | **1629**  | **1332**  | **1488**  | ** |
| (Rows)**    |           |           |           |           | 63 |
|             |           |           |           |           | 79 |
|             |           |           |           |           | ** |
+-------------+-----------+-----------+-----------+-----------+----+
| **Visit**   | **PP**    | **PH**    | **PP**    | **PH**    | ** |
|             |           |           |           |           | PP |
|             |           |           |           |           | ** |
+-------------+-----------+-----------+-----------+-----------+----+
| **Obsv**    | **0**     | **1930**  | **0**     | **1629**  | *  |
|             |           |           |           |           | *0 |
|             |           |           |           |           | ** |
+-------------+-----------+-----------+-----------+-----------+----+
| consul      | N/A       | 1648      |           |           |    |
| tation_type |           |           |           |           |    |
+-------------+-----------+-----------+-----------+-----------+----+
| Missing     | N/A       | 1374      |           |           |    |
| Answ        |           |           |           |           |    |
| ers(85.39%) |           |           |           |           |    |
+-------------+-----------+-----------+-----------+-----------+----+
| Missing     | N/A       | 1056      |           |           |    |
| Answ        |           |           |           |           |    |
| ers(84.35%) |           |           |           |           |    |
+-------------+-----------+-----------+-----------+-----------+----+
| Missing     | N/A       | 1090      |           |           |    |
| Answ        |           |           |           |           |    |
| ers(79.28%) |           |           |           |           |    |
+-------------+-----------+-----------+-----------+-----------+----+
| Missing     | **5168**  |           |           |           |    |
| Answ        |           |           |           |           |    |
| ers(73.25%) |           |           |           |           |    |
+-------------+-----------+-----------+-----------+-----------+----+

\*PP → Post-Planting

\*PH → Post-Harvest

\*N/A → observations indicates these questions were not asked during
this visit

**Table 7: UNICEF Health Indicator Definition Observations & Missingness
(Age 15-17 condition only)**

+------------+-----------+---------------+-----------+-----------+----+
| **Column   | **Missing | **Missing     | **Missing | **Missing | *  |
| Name**     | (Wave     | (Wave 2)**    | (Wave     | (Wave     | *T |
|            | 1)**      |               | 3)**      | 4)**      | ot |
|            |           |               |           |           | al |
|            |           |               |           |           | ** |
+============+===========+===============+===========+===========+====+
| **Obsv     | **1735**  | **1868**      | **1909**  | **1830**  | ** |
| (Rows)**   |           |               |           |           | 73 |
|            |           |               |           |           | 42 |
|            |           |               |           |           | ** |
+------------+-----------+---------------+-----------+-----------+----+
| **Visit**  | **PP**    | **PH**        | **PP**    | **PH**    | ** |
|            |           |               |           |           | PP |
|            |           |               |           |           | ** |
+------------+-----------+---------------+-----------+-----------+----+
| **Obsv**   | **0**     | **1735**      | **0**     | **1868**  | *  |
|            |           |               |           |           | *0 |
|            |           |               |           |           | ** |
+------------+-----------+---------------+-----------+-----------+----+
| family     | N/A       | 45Missing     | N/A       | 36        |    |
| _plan_flag |           | A             |           |           |    |
|            |           | nswers(2.59%) |           |           |    |
+------------+-----------+---------------+-----------+-----------+----+
| Missing    | N/A       | 1909          |           |           |    |
| Answ       |           |               |           |           |    |
| ers(1.93%) |           |               |           |           |    |
+------------+-----------+---------------+-----------+-----------+----+
| Missing    | N/A       | 1830          |           |           |    |
| Ans        |           |               |           |           |    |
| wers(100%) |           |               |           |           |    |
+------------+-----------+---------------+-----------+-----------+----+
| Missing    | **3820**  |               |           |           |    |
| Ans        |           |               |           |           |    |
| wers(100%) |           |               |           |           |    |
+------------+-----------+---------------+-----------+-----------+----+
| family     | N/A       | 1614Missing   | N/A       | 1745      |    |
| _plan_type |           | An            |           |           |    |
|            |           | swers(93.02%) |           |           |    |
+------------+-----------+---------------+-----------+-----------+----+
| Missing    | N/A       | 1909          |           |           |    |
| Answe      |           |               |           |           |    |
| rs(93.42%) |           |               |           |           |    |
+------------+-----------+---------------+-----------+-----------+----+
| Missing    | N/A       | 1830          |           |           |    |
| Ans        |           |               |           |           |    |
| wers(100%) |           |               |           |           |    |
+------------+-----------+---------------+-----------+-----------+----+
| Missing    | **7098**  |               |           |           |    |
| Ans        |           |               |           |           |    |
| wers(100%) |           |               |           |           |    |
+------------+-----------+---------------+-----------+-----------+----+

\*PP → Post-Planting

\*PH → Post-Harvest

\*N/A → observations indicates these questions were not asked during
this visit

As shown in Tables 5-7, all these health questions from the LSMS-ISA
survey have a massive amount of missingness and won’t have much
explanatory analysis when building a poverty index. After investigating
the other potential questions, they either have no explanatory power in
terms of health, or also have a massive amount of missing data. As a
result, we would recommend not using health as an indicator.

In conclusion, we’ve adapted the UNICEF definition to adhere more to the
available information in the LSMS-ISA survey [2]. As indicated by the
missingness, switching to the recommended guidelines and questions we’ve
researched will help with more explanatory power when creating a poverty
index.

**Appendix** :

[1] UNICEF Child Poverty Thresholds/Definition

+------+-------------+------------------------------+-----------------+
| *    | **Unit of   | **Severe Deprivation         | **Moderate      |
| *Dim | Analysis**  | Definition**                 | Deprivation     |
| ensi |             |                              | Definition      |
| on** |             |                              | (includes       |
|      |             |                              | severe          |
|      |             |                              | deprivation)**  |
+======+=============+==============================+=================+
| She  | Children    | Children living in a         | Children living |
| lter | under 17    | dwelling with five or more   | in a dwelling   |
|      | years of    | persons per sleeping room.   | with three or   |
|      | age         |                              | more persons    |
|      |             |                              | per sleeping    |
|      |             |                              | room.           |
+------+-------------+------------------------------+-----------------+
| Sa   | Children    | Children with no access to a | Children using  |
| nita | under 17    | toilet facility of any kind  | improved        |
| tion | years of    | (i.e. open defecation, or    | facilities but  |
|      | age         | pit latrines without slabs,  | shared with     |
|      |             | hanging latrines, or bucket  | other           |
|      |             | latrines, etc).              | households      |
+------+-------------+------------------------------+-----------------+
| W    | Children    | Children with no access to   | Children using  |
| ater | under 17    | waterfacilities of any kind  | improved water  |
|      | years of    | (i.e. usingsurface water or  | sources but     |
|      | age         | unimproved facilities such   | more than 15    |
|      |             | as. non-pipedsupplies).      | minutes away    |
|      |             |                              | (30 minutes     |
|      |             |                              | roundtrip)      |
+------+-------------+------------------------------+-----------------+
| N    | Children    | Stunting (3 standard         | Stunting (2     |
| utri | under 5     | deviationsbelow the          | standard        |
| tion | years of    | international                | deviations      |
|      | age         | referencepopulation)         | below the       |
|      |             |                              | international   |
|      |             |                              | reference       |
|      |             |                              | population).    |
+------+-------------+------------------------------+-----------------+
| E    | Children    | Children who have never been | Children who    |
| duca | between     | toschool.                    | are not         |
| tion | 5-14 years  |                              | currently       |
|      | of age      |                              | attending       |
|      |             |                              | school.         |
+------+-------------+------------------------------+-----------------+
|      |             |                              |                 |
+------+-------------+------------------------------+-----------------+
| Chil | Children    | Children who are not         |                 |
| dren | who have    | currently attending          |                 |
| bet  | not         | secondary school (or did not |                 |
| ween | compl       | complete secondary school).  |                 |
| 1    | etedprimary |                              |                 |
| 5-17 | school.     |                              |                 |
| y    |             |                              |                 |
| ears |             |                              |                 |
| of   |             |                              |                 |
| age  |             |                              |                 |
+------+-------------+------------------------------+-----------------+
| He   | Children    | Children who did not         | Children who    |
| alth | 12-35months | receiveimmunization against  | received less   |
|      | old         | measles norany dose of DPT.  | than 4 vaccines |
|      |             |                              | (out of measles |
|      |             |                              | and three       |
|      |             |                              | rounds of DPT). |
+------+-------------+------------------------------+-----------------+
|      |             |                              |                 |
+------+-------------+------------------------------+-----------------+
| Chil | Children    | Children with severe cough   |                 |
| dren | with severe | and fever who did not        |                 |
| 36-  | cough       | receiveprofessional medical  |                 |
| 59mo | andfever    | treatment.                   |                 |
| nths | who         |                              |                 |
| old  | received no |                              |                 |
|      | treatmentof |                              |                 |
|      | any kind.   |                              |                 |
+------+-------------+------------------------------+-----------------+
|      |             |                              |                 |
+------+-------------+------------------------------+-----------------+
| Chil | Unmet       | Unmet contraceptive needs    |                 |
| dren | co          | (using only traditional      |                 |
| 15   | ntraceptive | methods)                     |                 |
| -17y | needs.      |                              |                 |
| ears |             |                              |                 |
| old  |             |                              |                 |
+------+-------------+------------------------------+-----------------+

\*Table from (Insert source)

[2] LSMS-ISA-Adapted UNICEF Child Poverty Thresholds/Definition

+---+------+-------------------------------------+---------------------+
| * | **   | **Severe Deprivation Definition**   | **Moderate          |
| * | Unit |                                     | Deprivation         |
| D | of   |                                     | Definition          |
| i | An   |                                     | (includes severe    |
| m | alys |                                     | deprivation)**      |
| e | is** |                                     |                     |
| n |      |                                     |                     |
| s |      |                                     |                     |
| i |      |                                     |                     |
| o |      |                                     |                     |
| n |      |                                     |                     |
| * |      |                                     |                     |
| * |      |                                     |                     |
+===+======+=====================================+=====================+
| S | Chil | Children living in a dwelling with  | Children living in  |
| h | dren | five or more persons per sleeping   | a dwelling with     |
| e | u    | room.                               | three or more       |
| l | nder |                                     | persons per         |
| t | 17   |                                     | sleeping room.      |
| e | y    |                                     |                     |
| r | ears |                                     |                     |
|   | of   |                                     |                     |
|   | age  |                                     |                     |
+---+------+-------------------------------------+---------------------+
| S | Chil | Children with no access to a toilet | Children using      |
| a | dren | facility of any kind (i.e. open     | improved facilities |
| n | u    | defecation, or pit latrines without | but shared with     |
| i | nder | slabs, hanging latrines, or bucket  | other households    |
| t | 17   | latrines, etc).                     |                     |
| a | y    |                                     |                     |
| t | ears |                                     |                     |
| i | of   |                                     |                     |
| o | age  |                                     |                     |
| n |      |                                     |                     |
+---+------+-------------------------------------+---------------------+
| W | Chil | Children with no access to          | Children using      |
| a | dren | waterfacilities of any kind         | improved water      |
| t | u    | (i.e. usingsurface water or         | sources but more    |
| e | nder | unimproved facilities such as.      | than 15 minutes     |
| r | 17   | non-pipedsupplies).                 | away (30 minutes    |
|   | y    |                                     | roundtrip)          |
|   | ears |                                     |                     |
|   | of   |                                     |                     |
|   | age  |                                     |                     |
+---+------+-------------------------------------+---------------------+
| N | Chil | If the number of days without any   | If the individual   |
| u | dren | food in the household exceeds 1     | has faced a         |
| t | u    |                                     | situation where     |
| r | nder |                                     | there wasn’t enough |
| i | 17   |                                     | food in the         |
| t | y    |                                     | household           |
| i | ears |                                     |                     |
| o | of   |                                     |                     |
| n | age  |                                     |                     |
+---+------+-------------------------------------+---------------------+
| E | Chil | If the individual has never         | If the individual   |
| d | dren | attended school & cannot read or    | has never attended  |
| u | 5-17 | write in any language               | school              |
| c | y    |                                     |                     |
| a | ears |                                     |                     |
| t | of   |                                     |                     |
| i | age  |                                     |                     |
| o |      |                                     |                     |
| n |      |                                     |                     |
+---+------+-------------------------------------+---------------------+

Brought to you by JMPST Team members Trey & Prahitha

**(8/2) After-presentation notes**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Sebastian

   -  Predict missingness or not just looking at vertical missingness →
      non-response bias
   -  Get spatial clustering among survey *and* weather data
   -  Look at how other people characterize climate change
   -  Don’t bin on regional level, make sure to be specific and granular

      -  Think more city-rural divide

Julia notes:

@channel

\**I made some notes of the most important inputs in today’s Weekly
Update:*\*

-  \**No. 1 Focus:*\* Combine weather with survey data!! :handshake:

-  Focus on weather feature engineering :sun_behind_rain_cloud:

-  How to bring features in that reflect climate change? —> e.g. climate
   change velocity (checking some resources, eg. `this
   one <https://www.nature.com/articles/nature08649>`__)

-  Further check how people measure climate change —> inspire the
   feature engineering with this

-  Backlog Idea: Checking for missingness & bias in a survey dataset in
   an automated way

-  Besides how much is missing, what could be the root cause of the
   missingness?

-  Bias: thinking about non-response bias

-  Checking how representative a sample is

The idea to further investigate missingness & bias in a survey dataset
is very useful and could be a great feature for the pipeline to actually
check this for any dataset. However, we in the staff also just discussed
that it would be best to shift the focus now away from specifically the
LSMS dataset to focus on weather feature engineering and the combination
with a survey data set to look further into similar regions, correlation
analysis etc.

.. _section-1:

**(8/2) Plan (For Gernot) (Gernot please be proud)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**1) Spatial- temporal analysis on combined Weather+survey data (2ppl)**

**1.1) Spatial- temporal analysis at [hh survey, regional levels]**

Use current weather features we have

-  pd.merge(survey_data, weather_data, how = ‘left’)

-  Heatwaves + survey

-  Heavy rain + survey

-  Drought + survey

   -  SPI

-  Bivariate maps

   -  Pick combinations of two variables
   -  Build on top of dashboard

What methods to apply?

-  Four methods as done previously in Weather (Clustering, TWD,
   Correlation matrix,LISA)
-  Find patterns in regions + survey question
-  Relationship between <weather> and <poverty>

**2.2) Analysis at different geographic levels**

-  Repeat above at regional level
-  Also check if EA/state level is better or worse?
-  Do different weather regions have similar climate change
   characteristics.

**2) Weather feature engineering**

**2.1**

-  Due diligence - Check how people measure climate change?

   -  Velocity of climate change? [idea of investigating the rate of
      weather events, how often their occurrence]

https://www.nature.com/articles/nature08649

-  inspire the feature engineering with this

-  How to bring features in that reflect climate change?

   -  Constructing columns
   -  Verify based on due diligence check.

-  Time series analysis on weather TS

   -  Do time series things - like
      https://otexts.com/fpp2/stationarity.html
   -  Helps define the ‘extreme’, eg T> T(3 months rolling avg)
   -  Series differencing
   -  Finding seasonal patterns changes over time
   -  Do the baby/naive things first like here
      https://www.sciencedirect.com/science/article/pii/S0012825218303726

-  Methodological comparisons

-  

**MISC work**

-  Partner email request - General fn (geo_coords) -> [weather_columns]

   -  External python API
   -  Assume it works for Temp+precip for any coord in Nigeria (uses
      interpolation method) - Done

-  .. rubric:: Docker
      :name: docker

-  Pipeline

   -  JUUUULIA!!!!
   -  Resolve Filepaths -> from constants.py create filepaths.py

-  Github Tasks

   -  GERNOOOOOT!!!

**Backlog Idea: Representativeness and non-response in Survey**

-  How representative is the balanced panel vs

-  

Checking for missingness & bias in a survey dataset in an automated way

-  Besides how much is missing, what could be the root cause of the
   missingness?

-  Bias: thinking about non-response bias

-  Checking how representative a sample is

Week 8: 8/7-8/11 - Iteration 3 Part 1
-------------------------------------

**(8/7) Professor Flaxman Notes**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  UNICEF and STC met for a video call which started the brunt of this
   project
-  If it’s not a specific geocode, because of some of the other surveys
   such as cluster, the geocodes aren’t available for the survey, so all
   we know are admin one, and so how would this work if we were only
   provided with Admin 1 rather than a specific geolocation.
-  Find out the formula for this SPI so that it’s easily knowable and it
   makes sense
-  What about time specific information, are we doing some specific
   month or day
-  Take existing research methods and build upon them cause they’re
   theory and then change the method based on what you can utilize it
   best for
-  Ask more difficult questions and technical questions
-  Non-response bias

   -  Does it really matter if we’re trying to predict whether or not
      they’re deprived, if I did principal components analysis, six
      features and 90% of the variance is explained by a linear
      combination of them
   -  Could be useful having a lot of missingness

-  Put together anthropometrics from DHS
-  Distribution of weight for age (malnourished), height-for-age
   (Stunting), and weight-for-height

   -  Based on a standardized growth chart that changed based on what
      other surveys did

      -  For example, it wanted to see if breastfeeding was the best
         thing for children

   -  Taking the growth chart, and if 2 standard deviations off from
      that specific point then it’s considered stunting, and those
      thresholds push children into the more extreme cases

-  Stunting Data

   -  Mix & DHS always do it for the survey
   -  DHS has geocodes
   -  Mix does not, it’ll be admin 1, but can use any of those sources
      wherever it is, smooth that out with the DHS clusters
   -  Census might have a lot of that
   -  In this missingness, there may be different phases of missingness,
      and also geographically, 60% only for this

-  What are they looking for

   -  Care at the high level, this is child poverty, this is the
      constructed index and what people are using, and the causal of
      climate and poverty, and if they find out it’s most associated
      with a specific index, then they could use it

-  Zimbabwe nutrition survey (food consumption)

   -  At the admin 2 level asking demographics and the World Bank is
      like… really great data party

-  See if the geography changes across the timeline

   -  Outcome variables stunting, income variables demographics
   -  Income level post-stratification, lower income, lower education →
      stunting
   -  Now give the model a set of people, then do it for several sources

-  Andrew Gellmen and colleagues (Wang), using Xbox data and logged into
   and specified voted on Obama and Rodney, and then did multilevel
   regression post-stratification
-  Non-ignorable missingness, use the framework, Bradley et. al Big
   Paradox (send Sebastian an email)

   -  You need some sort of benchmark like a Census
   -  Their case the benchmark was COVID vaccine in 2021 which compared
      a facebook survey and another one to the administrative data,
      which told them there’s bias from the facebook and census but the
      old school one was fine, doesn’t reveal other features but it can
      be inferred…
   -  Look at the weights and calculate deff
   -  50% missing 50% not, are those two distributions of populations
      totally different, can still recover but are they different

-  Don’t change from geolocations, nice to think about the surveys that
   don’t have geolocations
-  Connecting 120 years on malaria prevalence, children aged 2-5, paper
   that discussed geocoded data, Snow et al. 2017, on medarchive
   (Carlson) which connects climate to Malaria, climate attribution
   models

   -  What can we forecast for the next 50 years for malaria

-  Anything that you do, if it’s reproducible, well documented code and
   write-ups, it will be useful, because they’ll continue to work on
   what you worked on

   -  If they can run your code and continue on it, then they will
   -  \*Which to me means that the pipeline, data accessibility,
      dashboard, and geo locations to weather information
   -  Foresee a very nice writeup and tool, that says here’s survey
      data, timestamp, here are a starting list of climate features, try
      these starting lineups that can be refined, and maybe some of them
      say flooding wasn’t measured correctly then you can change it
   -  Go to interface, point and click, latitude, longitude, etc.
   -  A write up of that will be very useful for that, especially for
      anyone, reviewers saying this is very interesting for this.

-  Actually getting enough signal for the rare cases that longitudinal
   is having

   -  Difficult to see things that may be helpful

-  Focus on a tool that would be helpful to all the social scientists
   who know geolocations, or just the centroid (given just admin levels)
   then bam
-  Climate Change

   -  Someone has used this (definition of flooding and extreme
      temperature), make it modular, here is the feature that I want you
      to extract from the weather data
   -  Carlson paper talked about the definition of drought, flood, and
      for temperature they were using averages (b/c it was motivated by
      the malaria)

      -  \*In the mattermost

   -  Malaria prevalence has gone down in the past years, is that
      because of climate change?

-  Check the soundness of your statistics
-  There isn’t a standing secretariat who maintains it, so it either has
   to be UNICEF (who doesn’t really have the capacity, but could), could
   be STC, could be Academics, idk

   -  Don’t just run themselves, have GitHub actions, but some people
      will need to know why it broke, and some other errors, etc.
   -  Make sure it’s public, somewhat automated, could that human do it
      (paid by Sebastian or Oxford LMAO)

-  One of you could be paid as a RA for them to maintain it
-  Characterizing climate change in a geo-spatial manner

   -  Sensitivity analysis, rural regions comparison
   -  Spatial similarity studies

-  US → Getting out of prison and giving the opportunity to move
   neighborhoods, but people weren’t actually moving but saying (1990s)

   -  Work on “synthetic controls” → I’ve got this city, and then I’ve
      got another city that’s kind of like it, create a fake version of
      this city by averaging a couple of others
   -  Natural experiments do go back to those things, like rainfall,
      etc.

      -  Where they used rain to see what restaurants people were eating
         at

-  If you have measurements of child growth what’s the association
   between
-  **The tool is DSSG, so to illustrate the tool, USE IT (big brain this
   is → me thinks)**

   -  Child growth is a good one, child poverty, etc
   -  6 dimensions then you could write the association of them, see how
      association changes among
   -  Then you’ll learn something about those 6 dimensions
   -  Don’t worry about non-significant responses

.. _weekly-planning-5:

**(8/7) Weekly Planning**
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Clean up GitHub

**(8/7) Weather Columns**
~~~~~~~~~~~~~~~~~~~~~~~~~

What specific weather columns do we want to attach to the geolocations?
We’re given a specific timeframe and these are the columns we would give
them:

-  Average seasonal temp/precip
-  Drought index (SPI)
-  Historical Data gathering
-  Column building
-  Severity Checks/Columns
-  Climate Check
-  Correlation Analysis
-  Weather API/something similar

**(8/7) Pipeline Plan/Architecture Documentation**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\*Refer to the Miro Workflow Board to find visualizations of this

Here’s a brief overview of each of the sections and the functions within
them:

**Survey**

The survey portion of this pipeline speaks to the analysis we’re doing
and the available data we’re utilizing to calculate a poverty index
(Based upon a collaborated UNICEF-adapted definition). We want to make
sure this portion of the pipeline is reproducible and documented well.

This also works as a best test to our tool, given the LSMS-survey data
has geolocations to the house cluster points

Procedure:

-  Beginning with the individual files from the World Bank’s `Harmonized
   Dataset <https://microdata.worldbank.org/index.php/catalog/5835/study-description>`__,
   we combine them on a domain level based on the created index in
   collaboration with out partners

   -  This consists of functions extracting the questions and renaming
      those columns that already exist on the pipeline

-  We merge these individual files containing Post-Planting and
   Post-Harvest information from all 4 waves and rename the columns that
   we specifically need for our poverty indicator functions

   -  Also already on the pipeline

-  After, we take all those files, as well as the geolocations and add
   them to the ROSTER file containing all children within the survey and
   give them the information (on both a household and individual level?)
-  Then, run the poverty indicator functions to create the columns for
   each indicator and then an overall

   -  \*I believe this may happen for each wave? I’m not sure if we’re
      doing this overall of the time that we have, because that may make
      it more difficult

**Weather**

The weather portion acts as the backbone to our tool, as we take raw
precipitation and temperature data from the Climate Prediction Center
and transform the data to different levels and granularities
(aggregate/interpolate).

Emphasizing reproducibility, this needs to be generalizable to different
countries, whether we use the library Julia recommended, or our
interpolation methods we’re currently using.

Procedure:

-  Each of the temperature and precipitation data are taken from the
   Climate Prediction Center and read from a certain timeframe (data
   goes back to 1970) and is across the globe
-  After, we pre-process the data for missing data, where it’s removed
   if the entire year has information missing, and if it’s missing for
   anything less then we impute previous day’s information
-  Then, using Inverse Distance Weighting, we interpolate the data to a
   more granular level that would either map to the admin level
-  Using the more granular information, we aggregate this daily data on
   a more seasonal level, achieving average temperatures and other
   information such as a drought index

   -  An idea for generalizing it to admin level is having two functions
      that run almost identically just on different levels

**Tool**

This tool should be scalable to a lot of the countries of interest,
rather than just Nigeria. This means that any survey with specific
geolocations would be able to track that information and output a lot of
weather information regardless of source. This is the maximum added
value to researchers everywhere, regardless of motive. We’re enabling
Pilot Analysis. Lastly, we need to make sure we have a list of
requirements that are needed for this tool to work perfectly (names of
columns, where these columns are located, timeframe, country, etc.)

This tool will also be accessed on streamlit, where any researcher
should be able to upload a dataset (meeting certain requirements) and
will be given back the same dataset with certain weather columns on it.

On streamlit → we would have an upload file button, and then a download
button would appear after with the data (topline research into this was
done by Trey)

Additionally, with the time range, I’m thinking about doing everything
seasonally/monthly, as daily would be too risky/time consuming, in order
to effectively give good information from this tool.

Procedure:

-  This tool’s input consists of a dataset with longitude and latitude
   as the first two columns as to confirm the geolocation of a
   particular area to gain weather information for

   -  \*We also want to think about doing this not for specific
      households but aggregated areas like admin_1 level

-  Then, we would do some sanity/error checks, filter for a particular
   time frame, and run our weather pipeline mentioned previously to

(I imagine the pipeline will be even more specific, but this is where my
current knowledge lies)

**(8/8) Data Requirements/Notes for Data Enhancement Tool**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

“Lat”

“Long”

“Date”

Minimum 1 other column → Representing other survey data they have

Could filter on LSMS dashboard for wave and visit, so that the weather
information reflects those points as well as the snapshot of the survey
data they wanted to look at

Maybe trim the columns

\*Also consider the idea longitude and latitude may be on a particular
point so we have to be careful

\*Unit tests to check (input and precipitation) → certain features like
date are correct, no missing, etc.

**(8/9) Testing other weather data sources**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Meteostat
^^^^^^^^^

Get the API Key (Note the limits)

-  Get data for a country and compute the weather indicators on the fly
   (additional columns include aggregates, and/or extreme values for
   that month/year) -> Profiling each step

   -  streamlit dashboard -> select country/region + date (range) ->
      get_data() -> additional_columns() -> compute_SPI() ->
      compute_heatwave_indicator() -> compute_heavy_rain_indicator()

-  Get data for the world and precompute all the weather indicators.
   Then, only show the data for the selected regions on Streamlit ->
   Profiling each step

   -  get_data() -> additional_columns() -> compute_SPI() ->
      compute_heatwave_indicator() -> compute_heavy_rain_indicator() ->
      streamlit dashboard -> select country/region + date (range) ->
      filter the precomputed weather indicators for the user inputted
      country & date

**(8/9) Standardized Precipitation Index (SPI)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SPI is a measure that was formulated to understand and quantify
precipitation anomalies, irrespective of scale. This scale independence
is what makes the SPI a versatile tool in drought monitoring. It is
utilized to identify the onset, magnitude, duration, and recovery of
drought conditions.

**Calculation:**

1. Data Collection: The first step involves collecting precipitation
   data for a given location over a significant period (typically, at
   least 30 years).
2. Time Scale: SPI can be calculated for different time scales ranging
   from 1 month to 48 months or more. This flexibility allows it to
   monitor both short and long-term drought conditions.
3. Calculation of the Rolling Sum: For a given time scale (e.g., 3
   months), calculate the rolling sum or average of precipitation.
4. Fitting a Probability Distribution: The rolling sums are then fit to
   a probability distribution. Typically, the gamma distribution is
   chosen due to its ability to represent skewed datasets, like
   precipitation.
5. Transformation to a Standard Normal Distribution: Once the cumulative
   probability of the observed precipitation value is determined using
   the gamma distribution, it is transformed into the Standard Normal
   Distribution (mean = 0 and standard deviation = 1). This
   transformation yields the SPI value.

**Interpretation:**

SPI values can be interpreted as follows:

-  SPI > 2: Extremely Wet
-  1.5 < SPI ≤ 2: Moderately Wet
-  1 < SPI ≤ 1.5: Wet
-  -1 ≤ SPI ≤ 1: Neutral (Near Normal)
-  -1.5 ≤ SPI < -1: Dry
-  -2 ≤ SPI < -1.5: Moderately Dry
-  SPI < -2: Extremely Dry

Implementation Steps:

-  Gather long-term precipitation data.
-  Calculate the rolling sum or average for a given time scale (e.g., 3
   months).
-  Fit the rolling sums to the gamma distribution to get the shape and
   scale parameters.
-  Calculate the cumulative probability for each precipitation value
   using the gamma distribution.
-  Convert the cumulative probability to SPI by applying the inverse of
   the standard normal cumulative distribution function (quantile
   function).
-  Implementations can be found in the code repo.

**(8/9) Correlation Analysis Methods**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Correlation Matrix**

Correlation analysis is a statistical method used to evaluate the
strength and direction of a linear relationship between two quantitative
variables. The result of the analysis is a correlation coefficient,
which can range from -1 to 1. A value close to 1 implies a strong
positive correlation: as one variable increases, the other also tends to
increase. A value close to -1 implies a strong negative correlation: as
one variable increases, the other tends to decrease. A value close to 0
implies a weak or no linear correlation between the variables.

By understanding the correlation between different regions, one can get
insights like:

-  Regions that tend to have similar weather patterns.
-  Regions that tend to have opposite weather patterns.

Implementation is provided in the code repo.

1. **Time Series Clustering with DBSCAN**

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is
an algorithm that identifies high-density regions in data space
separated by regions of lower density. Unlike many clustering
algorithms, DBSCAN doesn’t require specifying the number of clusters
beforehand.

The key advantage of using DBSCAN for time series data is its ability to
identify regions (or time periods) that display similar patterns or
trends over time, regardless of their magnitude.

**Key Concepts:**

**Core Point:** In DBSCAN, a point is a core point if it has more than a
specified number of points (min_samples) within a specified radius
(eps).

**Border Point:** A point which is within the radius of a core point but
doesn’t have enough points within its own radius to be a core point.

**Noise Point:** Points that aren’t classified as core or border points.

**Implementation Steps in the Function** :

**Pivot the Data** : Convert the dataframe into a time series format
where each row represents a region, each column represents a time
period, and cell values represent the time series values.

**Standardize the Data:** Time series data are standardized to have a
mean of 0 and a standard deviation of 1. This ensures that all time
series are on the same scale and that the clustering is based on
patterns and not on the absolute values.

**Apply DBSCAN** : The DBSCAN algorithm is applied to the standardized
time series data.

Label Clusters: Each time series (or region) is labeled with a cluster
label. Noise points are labeled with -1.

**Merge Results** : The cluster labels are then merged back into the
original dataframe to assign each row (representing an observation for a
region at a specific time) its corresponding cluster label.

The code is provided in the repo and can be utilized to cluster regions
based on their time series data. Regions in the same cluster display
similar patterns or trends over time.

1. **Dynamic Time Warping (DTW)**

The dynamic time warping (DTW) algorithm is able to find the optimal
alignment between two time series. It is often used to determine time
series similarity, classification, and to find corresponding regions
between two time series.

The DTW algorithm calculates the optimal (least cumulative distance)
alignment between two time series. So, a higher DTW distance between two
time series implies that the time series are less similar because it
requires a larger “effort” to align them. Conversely, a lower DTW
distance implies that the two time series are more similar. Therefore,
if we plot as a heatmap, darker colors (lower values) would correspond
to more similar weather patterns, while lighter colors (higher values)
indicate less similar weather patterns.

The implementation of DTW is also in the repo.Use it with care.

**A Note of Caution on Using the Provided Methods:**

While the methodologies provided—Standardized Precipitation Index (SPI),
Correlation Analysis, DBSCAN Clustering, and Dynamic Time Warping
(DTW)—offer powerful techniques for time series analysis, it’s
imperative that anyone using should use it with caution and have good
understanding before utilizing them. The success and accuracy of these
methods are deeply rooted in the structure and nature of the input data.
Particularly, when adapting these methods for different granularities of
analysis, such as at the regional or household levels, it’s essential to
ensure that the data is appropriately structured and representative of
the level of analysis in focus. Inaccurate or misaligned data can lead
to misleading or erroneous results.

**(8/9) HeatWave Index Method**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the course of defining what extreme weather events (for temperature
and precipatation), we settled for the Heat Wave Index rather than the
simplistic approach of taking a certain benchmark - say above 35 degree
celsius or 50 mm for temperature and precipitation respectively. The
reason for this choice is that, the heatwave index is data-driven in
accounting the its daily averaging threshold with seasonality. Beyond
differencing the daily temperatures/precipation from their daily
averaging thresholds to identify the “extremas” (WMO and IPCC), the
severity impact of such events taking into consideration if such is
experienced for 3 or more consecutive days.
`Guide <https://docs.google.com/presentation/d/1UrH9qzpFQUadyON5kJF4xkLfFBmtUWeE/edit#slide=id.p4>`__

Implementation wise, we considered the geographical interpolation of the
location of the weather event data sources to the countries of interest-
presently Nigeria and proceeded with geographical granularity to its
downstream.

**(8/10) Notes to Pick up on next week**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Fixed -1 and -2 to NA’s
-  For some reason, when adding them together, the entire column is
   NA’s?
-  Still trying to figure out the counting columns to take the average
   part

Week 9: 8/14-8/18 - Iteration 3 Part 2 - Productive Vibes
---------------------------------------------------------

.. _weekly-planning-6:

**(8/14) Weekly Planning**
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Check the spreadsheet
-  Also, follow up email with partners
-  Thinking about how we’re going to make quantities for averages of the
   regions without excluding extreme weather events within the regions

Weather Sources
^^^^^^^^^^^^^^^

`Precipitation <https://gpm.nasa.gov/data/directory>`__
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

IMERG provides precipitation estimates globally at 0.1°×0.1° every
half-hour beginning June 2000 to the delayed present. This IMERG Daily
Climatology product is derived from the daily precipitation data by
averaging the non-missing precipitation values in every 0.1° grid box
for a specific day of the year, over a range of years. It is suggested
to use the Final Run (instead of the Late and Early runs) on the
website.

Level 2: Horizontal resolution: 5x5 km

-  IMERG Final Run GES DISC: https://gpm.nasa.gov/node/3328
-  

Temperature
'''''''''''

**(8/14) Streamlit Integration Work/Notes (Trey)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The Pages folder has to be on the same level the home page folder
-  The page configuration has to be the first code read
-  File names are how they appear on the app

When trying to run the docker file using the home page as our Entry
Point, it doesn’t configure the multiple pages for some reason, and I
tried running multiple commands in the dockerfile but that wound up in a
dead end too.

-  I’ll ask Julia/Alex and default to expanding the weather tool

   -  Update: Julia and I can make it work on local machine but not on
      the virtual environment on the server, which is weird

Shifting to expanding the weather tool to more columns

Weather stations data used by CPC:
https://ftp.cpc.ncep.noaa.gov/cadb_v2/library/StationLibrary_Global.png