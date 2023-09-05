Resources
==========


Getting started with Geospatial Analysis
----------------------------------------
`Geographic Thinking for Data Scientists <https://geographicdata.science/book/notebooks/01_geo_thinking.html>`__ is an excellent starting for learning about geographic data science. It is a book that is written by `Dani Arribas-Bel <https://darribas.org/>`__ and `Levi John Wolf <https://www.levijohnwolf.com/>`__ for a soft technical introduction to industry standard tools for geospatial analysis.

-  Summary Notes of Part I

   -  Maps are geographical locations
   -  Much like how time isn’t just from clocks, geography isn’t from
      maps, it’s a process

      -  “For instance, most shopping malls have few (if any) residents,
         but their population density is very high at specific points in
         time, and they draw this population from elsewhere.”

   -  Geographic processes are represented using objects, fields, and
      networks.

      -  Objects are discrete entities that occupy a specific position
         in space and time.
      -  Fields are continuous surfaces that could, in theory, be
         measured at any location in space and time.
      -  Networks reflect a set of connections between objects or
         between positions in a field.

   -  The differences between these three representations are important
      to understand because they affect what kinds of relations are
      appropriate

      -  For instance, the relationships among geographical processes
         with objects can be modeled using simple distances.

   -  Data structures are digital representations that connect data
      models to computer implementations

      -  They form the middle layer that connects conceptual models to
         technology

   -  Embedding complex ideas in software helps widen the reach of a
      discipline

      -  For example, desktop GIS software in the 1990s and 2000s made
         geographic information useful to a much wider audience.

   -  What main geographic data structures should the data scientist
      care about? There are a few standard data structures that have
      been around for a long time because they are so useful

      -  In particular, we will cover three of them: geographic tables,
         surfaces (and cubes), and spatial graphs.
      -  **Geographic tables** store information about discrete objects.
         Tables are two-dimensional structures made up of rows and
         columns. Each row represents an independent object, while each
         column stores an attribute of those objects.

         -  Geographic tables are like typical data tables where one
            column stores geographic information. The tabular structure
            fits well with the object model because it clearly
            partitions space into discrete entities, and it assigns a
            geometry to each entity according to their spatial nature.
            More importantly, geographic tables can seamlessly combine
            geographic and non-geographic information

   - **Surface data structures** are used to record empirical measurements for field data models.
     - For a field (in theory), there is an infinite set of locations for which a field may be measured. In practice, fields are measured at a finite set of locations. This aim to represent continuity in space (and potentially time) is important because it feeds directly into how surface data are structured. In practice, surfaces are recorded and stored in uniform grids, or arrays whose dimension is closely linked to the geographic extent of the area they represent. In geography, we generally deal with arrays with two or more dimensions.
     - For example, a surface for air pollution will be represented as an array where each row will be linked to the measured pollutant level across a specific latitude, and each column for a specific longitude. If we want to represent more than one phenomenon (e.g., air pollution and elevation), or the same phenomenon at different points in time, we will need different arrays that are possibly connected. These multi-dimensional arrays are sometimes called data cubes or volumes.

   - **Spatial graphs** capture relationships between objects that are mediated through space. In a sense, they can be considered geographic networks, a data structure to store topologies. There are several ways to define spatial relationships between features
     - The important thing to note for now is that, whichever rules we follow, spatial graphs provide a way to encode them into a data structure that can support analytics.
     - In practice however spatial graphs are now sometimes used with grids because, as we will discuss in the following section, the connections and distinctions between data models and structures are changing very quickly
     - They are an obvious complement to geographic tables, which store information about individual observations in isolation.

     - Take the example of the streets in a city or, of the interconnected system of rivers in a catchment area. Both are usually referred to as networks (e.g., city network or river network), although in many Missing Answers what is being recorded is actually a collection of objects stored in a geographic table
     - If it is the exact shape, length and location of each segment or stream, this resembles much more a collection of independent lines or polygons that happen to "touch each other" at their ends. If what we are interested in is to understand how each segment or river is related to each other, who is connected to whom and how the individual connections comprise a broader interconnected system, then a spatial graph is a more helpful structure to use
     - This dichotomy of the object versus the graph is only one example of a larger point: the right link between a data model and data structure does not solely depend on the phenomenon we are trying to capture, but also our analytical goal.
 
-  Interactions between *conceptual* data and *computational* data

   -  First, the main conceptual mapping of data model to data structure
      is inherited from advances made in computer graphics. This
      traditional view represents fields as rasters and objects as
      vector-based tables. In this mode of analysis, there is generally
      no space for networks as a first-class geographic data structure.
      They are instead computed on the fly from a given set of objects
      or fields.

-  Computational Tools for Geographic Data Science

   -  Open Science is that the scientific process, at its core, is meant
      to be transparent and accessible to anyone
   -  Thus, transparency, accessibility, and inclusiveness are critical
      for good science.

      -  A series of recent high profile scandals have even prompted
         some to call a state of crisis. This “crisis” arises because
         the analyses that scientists conduct are difficult to repeat.
         Sometimes, it is even impossible to clearly understand the
         steps that were taken to arrive at results.

   -  We structure our approach to reproducibility in three main layers
      that build on each other.

      -  Computational Notebooks

         -  Computational notebooks are the twenty-first century sibling
            of Galileo\'s notebooks. Like their predecessors, they allow
            researchers, (data) scientists, and computational
            practitioners to record their practices and steps taken as
            they are going about their work

      -  Open Source Packaging

         -  To make notebooks an efficient medium to communicate
            computational work, it is important that they are concise
            and streamlined

            -  One way to achieve this goal is to only include the parts
               of the work that are unique to the application being
               recorded in the notebook, and to avoid duplication.

         -  Packages are modular, flexible, and reusable compilations of
            code. Unlike notebooks, they do not capture specific
            applications but abstractions of functionality that can be
            used in a variety of contexts

      -  Reproducible Platforms

         -  Additionally, a reproducible platform will also specify the
            versions of packages that are required to recreate the
            results presented in a notebook, since changes to packages
            can change the results of computations or break analytical
            workflows entirely

-  Spatial Data (With Code)

   -  geopanda is a really good package to help analyze the geometries
      and maps in data
   -  In many Missing Answers, geographic tables will have geometries of
      a single type; records will all be Point or LineString, for
      instance. However, there is no formal requirement that a
      geographic table has geometries that all have the same type.

      -  These are in terms of geographic tables

   -  Surfaces

      -  We can use the `open_rasterio` method from the xarray package
         to read in the GeoTIF files. This method returns an xarray.

-  A geographic surface will thus have two dimensions recording the
   location of cells (x and y), and at least one band that records other
   dimensions pertaining to our data.

Summary of Notes of Part II

-  Choropleth Mapping

   -  **Choropleths** are geographic maps that display statistical
      information encoded in a color palette. Choropleth maps play a
      prominent role in geographic data science as they **allow us to
      display non-geographic attributes or variables on a geographic
      map**.

      -  The word choropleth stems from the root “choro”, meaning
         “region”.

   -  Choropleth mapping thus revolves around:

      -  First, selecting a number of groups smaller than n into which
         all values in our dataset will be mapped to
      -  Second, identifying a classification algorithm that executes
         such mapping, following some principle that is aligned with our
         interest; and
      -  Third, once we know how many groups we are going to reduce all
         values in our data, which color is assigned to each group to
         ensure it encodes the information we want to reflect.

   -  Quantitative Data Classification

      -  Selecting the number of groups into which we want to assign the
         values in our data, and how each value is assigned into a group
         can be seen as a classification problem

         -  Data classification considers the problem of partitioning
            the attribute values into mutually exclusive and exhaustive
            groups. The precise manner in which this is done will be a
            function of the measurement scale of the attribute in
            question. For quantitative attributes (ordinal, interval,
            ratio scales), the classes will have an explicit ordering

      -  Skewness will have implications for the choice of choropleth
         classification scheme

   -  Equal Intervals

      -  The Freedman-Diaconis approach provides a rule to determine the
         width and, in turn, the number of bins for the classification

-  Quantiles

   -  To avoid the potential problem of sparse classes, the quantiles of
      the distribution can be used to identify the class boundaries.
      Indeed, each class will have approximately \|n/k\| observations
      using the quantile classifier
   -  While quantile classification avoids the pitfall of sparse
      classes, this classification is not problem-free. The varying
      widths of the intervals can be markedly different which can lead
      to problems of interpretation.

      -  A second challenge facing quantiles arises when there are a
         large number of duplicate values in the distribution such that
         the limits for one or more classes become ambiguous

-  Mean-Standard Deviation

   -  Our third classifier uses the sample mean and sample standard
      deviation to define class boundaries as some distance from the
      sample mean, with the distance being a multiple of the standard
      deviation

      -  This classifier is best used when data is normally distributed
         or, at least, when the sample mean is a meaningful measure to
         anchor the classification around.
      -  Ex: Clearly this is not the case for our income data as the
         positive skew results in a loss of information when we use the
         standard deviation. The lack of symmetry leads to an
         inadmissible upper bound for the first class as well as a
         concentration of the vast majority of values in the middle
         class.

-  Maximum Breaks

   -  The maximum breaks classifier decides where to set the break
      points between classes by considering the difference between
      sorted values. That is, rather than considering a value of the
      dataset in itself, it looks at how apart each value is from the
      next one in the sorted sequence

      -  Maximum breaks is an appropriate approach when we are
         interested in making sure observations in each class are
         separated from those in neighboring classes. As such, it works
         well in Missing Answers where the distribution of values is not
         unimodal

-  Boxplot

   -  The boxplot classification is a blend of the quantile and standard
      deviation classifiers

-  Etc.
-  Comparing Classification Schemes

   -  As a special case of clustering, the definition of the number of
      classes and the class boundaries pose a problem to the map
      designer
   -  The absolute deviation around class medians (ADCM) provides a
      global measure of fit which can be used to compare the alternative
      classifiers. As a complement to this global perspective, it can be
      revealing to consider how each of the observations in our data was
      classified across the alternative approaches.

-  Color

   -  Having considered the evaluation of the statistical distribution
      of the attribute values and the alternative classification
      approaches, we turn to select the symbolization and color scheme
   -  Making choropleths on geo-tables is an extension of plotting their
      geometries

-  Sequential Palettes

   -  Sequential color schemes are appropriate for continuous data where
      the origin is in one end of the series

-  Diverging Palettes

   -  A slightly different palette from the sequential one is the
      so-called “diverging” values palette. This is useful with
      continuous data when one wishes to place equal emphasis on
      mid-range critical values as well as extremes at both ends of the
      distribution

-  Qualitative Palettes

   -  Qualitative palettes encode categorical data. In this case, colors
      do not follow a gradient but rather imply qualitative differences
      between classes

-  Global Spatial Autocorrelation

   -  The notion of spatial autocorrelation relates to the existence of
      a “functional relationship between what happens at one point in
      space and what happens elsewhere”

   -  Spatial autocorrelation thus has to do with the degree to which
      the similarity in values between observations in a dataset is
      related to the similarity in locations of such observations

   -  Understanding Spatial Autocorrelation

      -  A key idea in this context is that of spatial randomness: a
         situation in which the location of an observation gives no
         information whatsoever about its value. In other words, a
         variable is spatially random if its distribution follows no
         discernible spatial pattern. Spatial autocorrelation can thus
         be defined as the “absence of spatial randomness”
      -  To get more specific, spatial autocorrelation is typically
         categorized along two main dimensions: sign and scale

         -  spatial autocorrelation can adopt two main forms: positive
            and negative

            -  The former relates to a situation where similarity and
               geographical closeness go hand-in-hand. In other words,
               similar values are located near each other, while
               different values tend to be scattered and further away

         -  For example, think of the distribution of income, or
            poverty, over space: it is common to find similar values
            located nearby wealthy areas close to other wealthy areas,
            poor population concentrated in space too

      -  Global spatial autocorrelation considers the overall trend that
         the location of values follows. In doing this, the study of
         global spatial autocorrelation makes possible statements about
         the degree of clustering in the dataset.


Some notes on `Interpolation methods<https://scikit-gstat.readthedocs.io/en/latest/userguide/kriging.html>`__


-  Spatial Interpolation

   -  The procedure of spatial interpolation is known as Kriging
   -  Similar to prediction, but Kriging is still based on the
      assumption that the variable is a random **field**

      -  Prefer the term estimation and would label the Kriging method a
         BLUE, Best Linear Unbiased Estimator
      -  The objective is to estimate a variable at a location that was
         not observed using observations from close locations

   -  It’s a best estimator, because we utilize the spatial structure
      described by a variogram to find suitable weights for averaging
      the observations at close locations

-  Using a Spatial Model

   -  A variogram describes how point observations become more
      dissimilar with distance

      -  Point distances can easily be calculated, not only for observed
         locations, but also for unobserved locations. As the variogram
         is only a function of distance, we can easily calculate a
         semi-variance value for any possible combination of point pairs
      -  Instead of making up weights, we can use the semi-variance
         value as a weight, as a first shot




LSMS-ISA Survey Overview
----------------------------

Aim of LSMS-ISA
^^^^^^^^^^^^^^^^^^^^
Living Standards Measurement Study - Integrated Surveys on Agriculture (LSMS-ISA) is a household survey project by the World Bank and partners to collect high-quality data on agriculture and household welfare in developing countries. The LSMS-ISA project is implemented in 8 countries in Sub-Saharan Africa, with the goal of generating household-level, nationally representative data that are linked to detailed information on individual plots of land.

-  Why LSMS ISA? 

   -  Official data infrastructure is weak in Sub-Saharan Africa, so World Bank and partners help in designing surveys for eight countries, with goal for open research and better outcomes.
   
   -  In some countries with pre-existing surveys, resources were reallocated and tailored to be concordant with the wider ISA survey designs.

-  ISA: These surveys are focussed on **agriculture, socioeconomic status,** and **non-farm income activities**.

-  For more about LSMS-ISA please see `LSMS website <https://www.worldbank.org/en/programs/lsms/initiatives/lsms-ISA>`__




LSMS-ISA Survey Design
^^^^^^^^^^^^^^^^^^^^^^

-  Details about the LSMS-ISA survey design:

   -  Data Collection/Sampling Procedure

      -  A Massive Sample Frame based on 2006 census conducted by
         National Population Commission (NpopC)

         -  The census includes approximately 662,000 enumeration areas
            (EAs) throughout the country.
         -  These construct the 674 Local Government Areas (LGAs), 6 of
            which are found in Federal Capital Territory (FCT), Abuja

            -  In each of the 668 EAs, 30 were “scientifically” selected

         -  40 EAs were “scientifically” selected in each of these
            remaining 6 LGAs. This gives a total of 23,280 approx 3.5%
            of total enumeration areas –> EAs selected nationally.

      -  The National Integrated Survey of Households 2007/2012 Master
         Sample Frame (NISH-MSF) was developed from the Master Frame

         -  Pooling the LGAs in the Master Frame by state; a systematic
            sample of 200 EAs were selected with equal probability
            across all LGAs within the state
         -  The NISH EAs in each state were divided into 20 “replicates”
            (groupings) of 10 EAs each

            -  The sample EAs for most national household surveys such
               as the GHS are based on a sub-sample of the NISH-MSF,
               selected as a *combination of replicates* from the
               NISH-MSF frame

         -  For the GHS-Panel, the sample is a subset of the EAs
            selected for the GHS.
         -  They essentially sampled the sample, grouped areas together,
            and then did the survey based on a subsets of the sampled
            samples ;) (but to make sure to include all states so
            certain territories were represented)

      -  Sample Framework

         -  The sample frame includes all thirty-six (36) states of the
            federation and Federal Capital Territory (FCT), Abuja
         -  Both urban and rural areas were covered and in all, 500
            clusters/EAs were canvassed and 5,000 households were
            interviewer
         -  These samples were proportionally selected in the states
            such that different states have different samples.

      -  Sample Selection

         -  The GHS Panel Survey used a two stage stratified sample
            selection process

      -  First Stage

         -  The Primary Sampling Units (PSUs) were the Enumeration Areas
            (EAs). These were selected based on probability proportional
            to size (PPS) of the total EAs in each state and FCT, Abuja
            and the total households listed in those EAs

      -  Second Stage

         -  “Systematic” selection of 10 households per EA

            -  This involved obtaining the total number of households
               listed in a particular EA, and then calculating a
               Sampling Interval (S.I) by dividing the total households
               listed by ten (10)

         -  The next step is to generate a random start ‘r’ from the
            table of random numbers which stands as the 1st selection.
            The second selection is obtained by adding the sampling
            interval to the random start
         -  For each of the next selections, the sampling interval was
            added to the value of the previous selection until the 10th
            selection was obtained.
         -  Determination of the sample size at the household level was
            based on the experience gained from previous rounds of the
            GHS, in which 10 HHs per EA are usually selected and give
            robust estimates.

   -  Weighting

      -  When a sample of households is selected for a survey, these
         households represent the entire population of the country
      -  Weighted to reflect the distribution of the full population in
         the country. A population weight was calculated for the panel
         households. This weight variable (WGHT) has been included in
         the household dataset: Section A (SECTA)

         -  When applied, this weight will *raise the sample households
            and individuals to national values* adjusting for population
            concentrations in various areas.

   -  Details about Questionnaires

      -  The survey consisted of two household questionnaires and one
         community questionnaire

         -  The first designated by ‘HOUSEHOLD QUESTIONNAIRE’ was
            administered to all households in the sample.
         -  The second questionnaire ’AGRICULTURE QUESTIONNAIRE was
            administered to all households *engaged in agriculture
            activities such as crop farming, livestock rearing and other
            agricultural and related activities*.
         -  The third Community Questionnaire was administered *to the
            community* to collect information on the socio-economic
            indicators of the community