# Page with LSMS-ISA Dashboard Visualizations

import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
from src.dashboard.utils import (
    filter_survey,
    filter_weather,
    load_data_from_google_drive,
    preprocess_weather_data
)
from src.weather.weather_pipeline import (
    aggr_monthly,
    combine_map_weather,
    aggr_yearly,
    aggr_seosonal_nigeria,
)
from src.weather.utils import read_shape_file
from src.weather.create_visuals import (
    generate_choropleth,
    generate_interactive_time_series,
    generate_bivariate_map,
    plot_poverty_index,
)

from src.weather.weather_pipeline import plot_heatmap_grid_on_map
from src.weather.constants import (
    TEMPERATURE_FILE,
    PRECIPITATION_FILE,
    TEMPERATURE_INDICATORS,
    PRECIPITATION_INDICATORS,
    NIGERIA_SHAPE_PATH_FILE,
    LSMS_SURVEY_FILE,
    JOINED_WEATHER_DATA_FILE
)
from src.survey.constants import SURVEY_FINAL_PATH
from src.weather_x_survey.weather_survey import combine_with_poverty_index
from src.dashboard.utils import parse_command_arguments

# Parse the arguments passend when running the streamlit run command
datalocation, computation = parse_command_arguments()

print(f"datalocation: {datalocation} with type {type(datalocation)}")
print(f"datalocation: {computation} with type {type(computation)}")

# Page Configuration
st.set_page_config(page_title="LSMS-ISA Dashboard", page_icon="📈")

# Page Aesthetics and Text
st.markdown("# LSMS-ISA Dashboard")
st.sidebar.header("LSMS-ISA Dashboard")
st.markdown(
    """This page illustrates the 
    [Living Standards Measurement Survey - Integrated Survey on Agriculture (LSMS-ISA)](https://www.worldbank.org/en/programs/lsms/initiatives/lsms-ISA#:~:text=The%20Living%20Standards%20Measurement%20Study,and%20smallholder%20agriculture%20in%20Africa.), 
    conducted by the World Bank for Nigeria 
    and the analysis our team has done within it. 
    You may select up to two features to visualize together.
    Select some filters on the sidebar to visualize some weather information and/or 
    the poverty index to explore!"""
)

# Add filters/input widgets with tooltips
st.sidebar.markdown("Select Filters:")

year_list = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
year_choice_dropdown = st.sidebar.selectbox("Year", year_list, help="Year Selection")
# Time Aggregation Choice Widget
time_list = ["Yearly", "Seasonaly", "Monthly", "Survey-Dependent"]
time_choice_dropdown = st.sidebar.selectbox(
    "Time Aggregation", time_list, help="Time Aggregation Selection"
)

season_choice = None
month_choice_dropdown = None
wave_choice = 1
possible_selections = 2
disable_dropdown = True
poverty_legend = "0: Not Deprived, 1: Moderately Deprived, 2: Severely Deprived"

# Use forms and submit button to batch input widgets
with st.sidebar.form(key="columns_in_form"):
    if "Seasonaly" in time_choice_dropdown:
        level = "season"
        # Season choice widget
        season_list = ["Wet (April-September)", "Dry (October-March)"]
        season_choice_dropdown = st.selectbox(
            "Season", season_list, help="Season Selection"
        )
        # Rename Season after selection
        if "Wet (April-September)" in season_choice_dropdown:
            season_choice = "Wet"
        else:
            season_choice = "Dry"
    elif "Monthly" in time_choice_dropdown:
        level = "month"
        # Month choice widget
        month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        month_choice_dropdown = st.selectbox(
            "Month", month_list, help="Month Selection"
        )
    elif "Yearly" in time_choice_dropdown:
        level = "year"
    else:
        level = "year"
        possible_selections = 1
        disable_dropdown = False
        # Wave choice widget for Survey
        wave_list = ["Wave 1 (2010-2011)", "Wave 2 (2012-2013)", "Wave 3 (2015-2016)"]
        wave_choice_dropdown = st.selectbox(
            "Wave", wave_list, help="Survey Wave Selection"
        )
        # Rename Wave after selection
        if "Wave 1 (2010-2011)" in wave_list:
            wave_choice = 1
        elif "Wave 2 (2012-2013)" in wave_list:
            wave_choice = 2
        else:
            wave_choice = 3

    # Weather Event widget
    weather_events_list = [
        None,
        "Precipitation (mm)",
        "Temperature (°C)",
        "Drought",
        "Heavy Rain",
        "Heat Wave",
    ]
    weather_dropdown = st.multiselect(
        "Weather Event",
        weather_events_list,
        max_selections=possible_selections,
        default=["Precipitation (mm)"],
        help="Please choose up to 2 weather events to investigate",
    )

    # Poverty Index widget
    poverty_index_list = [
        None,
        "Overall Poverty",
        "Housing Poverty",
        "Health Poverty",
        "Nutrition Poverty",
        "Sanitation Poverty",
        "Education Poverty",
        "Water Poverty",
    ]
    poverty_index_dropdown = st.selectbox(
        "Poverty Indicators",
        poverty_index_list,
        help="Overall Poverty Index Selection",
        disabled=disable_dropdown,
    )

    # Admin choice for granularity
    admin_list = ["Admin 1 - State level", "Admin 2 - Region/City Level"]
    admin_choice_dropdown = st.selectbox(
        "Admin Level", admin_list, help="Administration Level Selection"
    )
    # Rename Admin after selection
    if "Admin 2 - Region/City Level" in admin_choice_dropdown:
        admin_choice = "admin2Pcod"
    else:
        admin_choice = "admin1Pcod"

    submitted = st.form_submit_button("Apply Filters")

if submitted:
    st.toast("Weather data is being read and preprocessed", icon="⌛")
    with st.spinner("Weather data is being read and preprocessed..."):
        # Read Data for Dashboard (Once and st.caches it)
        nigeria_shape_df = read_shape_file(data_path=NIGERIA_SHAPE_PATH_FILE)

        if datalocation == "gdrive" and computation == "low_resource":
            weather_data = load_data_from_google_drive(
                file_to_load=JOINED_WEATHER_DATA_FILE
            )
            weather_data_df = pd.read_parquet(weather_data)
            weather_data_df = preprocess_weather_data(weather_data_df)

        elif datalocation == "gdrive" and computation == "high_resource":
            precipitation_indicators_data = load_data_from_google_drive(
                file_to_load=PRECIPITATION_FILE
            )
            precipitation_indicators = pd.read_parquet(precipitation_indicators_data)
            temperature_indicators_data = load_data_from_google_drive(
                file_to_load=TEMPERATURE_FILE
            )
            temperature_indicators = pd.read_parquet(temperature_indicators_data)

        elif datalocation == "local" and computation == "high_resource":
            precipitation_indicators = pd.read_parquet(PRECIPITATION_INDICATORS)
            temperature_indicators = pd.read_parquet(TEMPERATURE_INDICATORS)

    st.toast("Survey data is being read and preprocessed", icon="⌛")
    with st.spinner("Survey data is being read and preprocessed..."):
        if datalocation == "gdrive":
            lsms_survey_data = load_data_from_google_drive(
                file_to_load=LSMS_SURVEY_FILE
            )
        else:
            lsms_survey_data = SURVEY_FINAL_PATH
        survey_data_df = pd.read_pickle(lsms_survey_data).reset_index()
        target_epsg = 4326

    if disable_dropdown == True:
        poverty_index_dropdown = None

    if computation == "low_resource":
        dict_value_cols = {
            "Precipitation (mm)": (weather_data_df, "Blues"),
            "Temperature (°C)": (weather_data_df, "Reds"),
            "Drought": (weather_data_df, "Blues"),
            "Heavy Rain": (weather_data_df, "Blues"),
            "Heat Wave": (weather_data_df, "Blues"),
        }
    else:
        dict_value_cols = {
            "Precipitation (mm)": (precipitation_indicators, "Blues"),
            "Temperature (°C)": (temperature_indicators, "Reds"),
            "Drought": (precipitation_indicators, "Blues"),
            "Heavy Rain": (precipitation_indicators, "Blues"),
            "Heat Wave": (temperature_indicators, "Blues"),
        }

    weather_indicators = {
        "Precipitation (mm)": "precipitation",
        "Temperature (°C)": "temperature",
        "Drought": "spi_index",
        "Heavy Rain": "heavy_rain_index",
        "Heat Wave": "heatwave_index",
    }

    poverty_indicators = {
        "Overall Poverty": "unicef_poverty_index",
        "Housing Poverty": "shelter_indicator",
        "Health Poverty": "health_indicator",
        "Nutrition Poverty": "nutrition_indicator",
        "Sanitation Poverty": "sanitation_indicator",
        "Education Poverty": "education_indicator",
        "Water Poverty": "water_indicator",
    }

    legends = {
        "Precipitation (mm)": "precipitation (mm)",
        "Temperature (°C)": "temperature (°C)",
        "Drought": "SPI",
        "Heavy Rain": "deviation from average",
        "Heat Wave": "deviation from average",
    }

    weather_columns = []

    combined_dfs = {}
    for weather in weather_dropdown:
        weather_data_name = weather_indicators[weather]
        weather_columns.append(weather_data_name)

        if level == "daily":
            agg_dict = {weather_data_name: "mean"}
            level = weather_data_name
        else:
            agg_dict = {
                "mean": "mean",
                "min": "mean",
                "max": "mean",
            }
        st.toast("Combining weather data to maps", icon="⌛")
        with st.spinner("Combining weather data to maps..."):
            combined_df = combine_map_weather(
                nigeria_shape_df=nigeria_shape_df,
                weather_df=dict_value_cols[weather][0],
                col_dissolve=admin_choice,
                weather_data_name=weather_indicators[weather],
                agg_dict=agg_dict,
                level=level,
                target_epsg=target_epsg,
            )
            combined_dfs[weather_data_name] = combined_df

    if weather_dropdown is None:
        weather_size = 0
    else:
        weather_size = len(weather_dropdown)

    if poverty_index_dropdown is None:
        poverty_index_size = 0
    else:
        poverty_index_size = 1

    # Counts the amount of selected features
    size = weather_size + poverty_index_size

    print(len(weather_dropdown), poverty_index_size, size)

    if (
        len(weather_dropdown) == 2
        and size < 3
        and time_choice_dropdown != "Survey-Dependent"
    ):
        st.toast("Generating visualizations", icon="⌛")
        with st.spinner("Generating visualizations..."):
            # filter df
            filtered_df_1 = filter_weather(
                weather_df=combined_dfs[weather_columns[0]].copy(),
                year=year_choice_dropdown,
                month=month_choice_dropdown,
                season=season_choice,
            )
            filtered_df_2 = filter_weather(
                weather_df=combined_dfs[weather_columns[1]].copy(),
                year=year_choice_dropdown,
                month=month_choice_dropdown,
                season=season_choice,
            )

            if level == "month":
                aggregated_prec_grid_1 = aggr_monthly(
                    df=dict_value_cols[weather_dropdown[0]][0].copy(),
                    column_aggr=weather_columns[0],
                )
                aggregated_prec_grid_2 = aggr_monthly(
                    df=dict_value_cols[weather_dropdown[1]][0].copy(),
                    column_aggr=weather_columns[1],
                )
            elif level == "year":
                aggregated_prec_grid_1 = aggr_yearly(
                    df=dict_value_cols[weather_dropdown[0]][0].copy(),
                    column_aggr=weather_columns[0],
                )
                aggregated_prec_grid_2 = aggr_yearly(
                    df=dict_value_cols[weather_dropdown[1]][0].copy(),
                    column_aggr=weather_columns[1],
                )
            elif level == "season":
                aggregated_prec_temp_1 = aggr_monthly(
                    df=dict_value_cols[weather_dropdown[0]][0].copy(),
                    column_aggr=weather_columns[0],
                )
                aggregated_prec_grid_1 = aggr_seosonal_nigeria(
                    df=aggregated_prec_temp_1,
                )
                aggregated_prec_temp_2 = aggr_monthly(
                    df=dict_value_cols[weather_dropdown[0]][0].copy(),
                    column_aggr=weather_columns[0],
                )
                aggregated_prec_grid_2 = aggr_seosonal_nigeria(
                    df=aggregated_prec_temp_2,
                )

            filtered_grid_1 = filter_weather(
                weather_df=aggregated_prec_grid_1.copy(),
                year=year_choice_dropdown,
                month=month_choice_dropdown,
                season=season_choice,
            )
            filtered_grid_2 = filter_weather(
                weather_df=aggregated_prec_grid_2.copy(),
                year=year_choice_dropdown,
                month=month_choice_dropdown,
                season=season_choice,
            )

            st.markdown(
                f"<h4 style='text-align: center; color: black;'>Bivariate map for {weather_dropdown[0]} and {weather_dropdown[1]} </h4>",
                unsafe_allow_html=True,
            )
            bivariate_map = generate_bivariate_map(
                combined_df_1=filtered_df_1,
                combined_df_2=filtered_df_2,
                column_1="mean",
                column_2="mean",
                legend_1=legends[weather_dropdown[0]],
                legend_2=legends[weather_dropdown[1]],
                admin=admin_choice,
            )
            folium_static(bivariate_map)

            if computation == "high_resource":
                time_series_1 = filter_weather(
                    weather_df=dict_value_cols[weather_dropdown[0]][0].copy(),
                    year=year_choice_dropdown,
                )
                time_series_2 = filter_weather(
                    weather_df=dict_value_cols[weather_dropdown[1]][0].copy(),
                    year=year_choice_dropdown,
                )

                st.plotly_chart(
                    generate_interactive_time_series(
                        df=time_series_1.copy(), weather_data_name=weather_columns[0]
                    )
                )
                st.plotly_chart(
                    generate_interactive_time_series(
                        df=time_series_2.copy(), weather_data_name=weather_columns[1]
                    )
                )

                st.markdown(
                    f"<h4 style='text-align: center; color: black;'>Heatmap for {weather_dropdown[0]} </h4>",
                    unsafe_allow_html=True,
                )
                st.pyplot(
                    plot_heatmap_grid_on_map(
                        df=filtered_grid_1,
                        value_col="mean",
                        geo_df=nigeria_shape_df,
                        legend_title=legends[weather_dropdown[0]],
                        cmap=dict_value_cols[weather_dropdown[0]][1],
                    )
                )
                st.markdown(
                    f"<h4 style='text-align: center; color: black;'>Heatmap for {weather_dropdown[1]} </h4>",
                    unsafe_allow_html=True,
                )
                st.pyplot(
                    plot_heatmap_grid_on_map(
                        df=filtered_grid_2,
                        value_col="mean",
                        geo_df=nigeria_shape_df,
                        legend_title=legends[weather_dropdown[1]],
                        cmap=dict_value_cols[weather_dropdown[1]][1],
                    )
                )

            st.markdown(
                f"<h4 style='text-align: center; color: black;'>Univariate map for {weather_dropdown[0]} </h4>",
                unsafe_allow_html=True,
            )
            folium_static(
                generate_choropleth(
                    combined_df=filtered_df_1,
                    admin=admin_choice,
                    column="mean",
                    legend_name=legends[weather_dropdown[0]],
                    fill_color=dict_value_cols[weather_dropdown[0]][1],
                )
            )

            st.markdown(
                f"<h4 style='text-align: center; color: black;'>Univariate map for {weather_dropdown[1]} </h4>",
                unsafe_allow_html=True,
            )
            folium_static(
                generate_choropleth(
                    combined_df=filtered_df_2,
                    admin=admin_choice,
                    column="mean",
                    legend_name=legends[weather_dropdown[1]],
                    fill_color=dict_value_cols[weather_dropdown[1]][1],
                )
            )

    elif (
        (len(weather_dropdown) == 1)
        and (poverty_index_size == 1)
        and (time_choice_dropdown == "Survey-Dependent")
    ):
        st.toast("Generating visualizations", icon="⌛")
        with st.spinner("Generating visualizations..."):
            # filter df
            filtered_df_1 = filter_survey(
                survey_df=survey_data_df.copy(),
                target_epsg=target_epsg,
                wave=wave_choice,
            )
            filtered_df_2 = filter_weather(
                weather_df=combined_dfs[weather_columns[0]].copy(),
                year=year_choice_dropdown,
                month=month_choice_dropdown,
                season=season_choice,
            )

            aggregated_prec_grid_1 = aggr_monthly(
                df=dict_value_cols[weather_dropdown[0]][0].copy(),
                column_aggr=weather_columns[0],
            )
            filtered_grid_1 = filter_weather(
                weather_df=aggregated_prec_grid_1.copy(),
                year=year_choice_dropdown,
                month=month_choice_dropdown,
                season=season_choice,
            )

            aggregated_prec_grid_1_year = aggr_yearly(
                df=filtered_grid_1.copy(),
                column_aggr="mean",
            )

            combined_df_1 = combine_with_poverty_index(
                map_df=nigeria_shape_df,
                household_df=filtered_df_1.copy(),
                col_dissolve=admin_choice,
                wave=wave_choice,
                poverty_index_col_name=poverty_indicators[poverty_index_dropdown],
            )

            st.markdown(
                f"<h4 style='text-align: center; color: black;'>Bivariate map for {weather_dropdown[0]} and {poverty_index_dropdown} </h4>",
                unsafe_allow_html=True,
            )
            bivariate_map = generate_bivariate_map(
                combined_df_1=combined_df_1.copy(),
                combined_df_2=filtered_df_2.copy(),
                column_1=poverty_indicators[poverty_index_dropdown],
                column_2="mean",
                legend_1=poverty_legend,
                legend_2=legends[weather_dropdown[0]],
                admin=admin_choice,
            )
            folium_static(bivariate_map)

            if computation == "high_resource":
                st.plotly_chart(
                    generate_interactive_time_series(
                        df=filtered_df_2.copy(), weather_data_name="mean"
                    )
                )
                st.plotly_chart(
                    generate_interactive_time_series(
                        df=survey_data_df.copy(),
                        weather_data_name=poverty_indicators[poverty_index_dropdown],
                    )
                )

                st.markdown(
                    f"<h4 style='text-align: center; color: black;'>Heatmap for {weather_dropdown[0]} </h4>",
                    unsafe_allow_html=True,
                )
                st.pyplot(
                    plot_heatmap_grid_on_map(
                        df=aggregated_prec_grid_1_year.copy(),
                        geo_df=nigeria_shape_df,
                        value_col="mean",
                        legend_title=legends[weather_dropdown[0]],
                        cmap=dict_value_cols[weather_dropdown[0]][1],
                    )
                )

            st.markdown(
                f"<h4 style='text-align: center; color: black;'>Univariate map for {poverty_index_dropdown} </h4>",
                unsafe_allow_html=True,
            )
            folium_static(
                generate_choropleth(
                    combined_df=combined_df_1,
                    admin=admin_choice,
                    column=poverty_indicators[poverty_index_dropdown],
                    legend_name=poverty_legend,
                    fill_color="Reds",
                )
            )

            st.markdown(
                f"<h4 style='text-align: center; color: black;'>Univariate map for {weather_dropdown[0]} </h4>",
                unsafe_allow_html=True,
            )
            folium_static(
                generate_choropleth(
                    combined_df=filtered_df_2,
                    admin=admin_choice,
                    column="mean",
                    legend_name=legends[weather_dropdown[0]],
                    fill_color=dict_value_cols[weather_dropdown[0]][1],
                )
            )

            st.markdown(
                f"<h4 style='text-align: center; color: black;'>Households on map for {poverty_index_dropdown} </h4>",
                unsafe_allow_html=True,
            )
            st.pyplot(
                plot_poverty_index(
                    wave_panel_df=filtered_df_1,
                    map_nigeria=nigeria_shape_df,
                    column=poverty_indicators[poverty_index_dropdown],
                )
            )

    elif (
        (len(weather_dropdown) == 1)
        and (poverty_index_size == 0)
        and (time_choice_dropdown == "Survey-Dependent")
    ):
        st.error(
            "Error: Please make sure to select the Survey-Dependent option in the time aggregation dropdown \
                    only when selecting the poverty indicators",
            icon="🚨",
        )

    elif (len(weather_dropdown) == 1) and (poverty_index_size == 0):
        st.toast("Generating visualizations", icon="⌛")
        with st.spinner("Generating visualizations..."):
            filtered_df_1 = filter_weather(
                weather_df=combined_dfs[weather_columns[0]].copy(),
                year=year_choice_dropdown,
                month=month_choice_dropdown,
                season=season_choice,
            )

            if level == "month":
                aggregated_prec_grid_1 = aggr_monthly(
                    df=dict_value_cols[weather_dropdown[0]][0].copy(),
                    column_aggr=weather_columns[0],
                )

            elif level == "year":
                aggregated_prec_grid_1 = aggr_yearly(
                    df=dict_value_cols[weather_dropdown[0]][0].copy(),
                    column_aggr=weather_columns[0],
                )

            elif level == "season":
                aggregated_prec_temp = aggr_monthly(
                    df=dict_value_cols[weather_dropdown[0]][0].copy(),
                    column_aggr=weather_columns[0],
                )

                aggregated_prec_grid_1 = aggr_seosonal_nigeria(
                    df=aggregated_prec_temp.copy(),
                )

            filtered_grid_1 = filter_weather(
                weather_df=aggregated_prec_grid_1.copy(),
                year=year_choice_dropdown,
                month=month_choice_dropdown,
                season=season_choice,
            )

            if computation == "high_resource":
                st.plotly_chart(
                    generate_interactive_time_series(
                        df=filtered_df_1.copy(), weather_data_name=weather_columns[0]
                    )
                )

                time_series_1 = filter_weather(
                    weather_df=dict_value_cols[weather_dropdown[0]][0].copy(),
                    year=year_choice_dropdown,
                )
                st.plotly_chart(
                    generate_interactive_time_series(
                        df=time_series_1.copy(), weather_data_name=weather_columns[0]
                    )
                )

                st.markdown(
                    f"<h4 style='text-align: center; color: black;'>Heatmap for {weather_dropdown[0]} </h4>",
                    unsafe_allow_html=True,
                )
                st.pyplot(
                    plot_heatmap_grid_on_map(
                        df=filtered_grid_1,
                        geo_df=nigeria_shape_df,
                        value_col="mean",
                        legend_title=legends[weather_dropdown[0]],
                        cmap=dict_value_cols[weather_dropdown[0]][1],
                    )
                )

            st.markdown(
                f"<h4 style='text-align: center; color: black;'>Univariate map for {weather_dropdown[0]} </h4>",
                unsafe_allow_html=True,
            )
            folium_static(
                generate_choropleth(
                    combined_df=filtered_df_1,
                    admin=admin_choice,
                    column="mean",
                    legend_name=legends[weather_dropdown[0]],
                    fill_color=dict_value_cols[weather_dropdown[0]][1],
                )
            )

    elif (
        (weather_size == 0)
        and (poverty_index_size == 1)
        and time_choice_dropdown == "Survey-Dependent"
    ):
        st.toast("Generating visualizations", icon="⌛")
        with st.spinner("Generating visualizations..."):
            filtered_df_1 = filter_survey(
                survey_df=survey_data_df.copy(),
                target_epsg=target_epsg,
                wave=wave_choice,
            )

            print(filtered_df_1[poverty_indicators[poverty_index_dropdown]].unique())

            combined_df_1 = combine_with_poverty_index(
                map_df=nigeria_shape_df,
                household_df=filtered_df_1.copy(),
                col_dissolve=admin_choice,
                wave=wave_choice,
                poverty_index_col_name=poverty_indicators[poverty_index_dropdown],
            )

            st.markdown(
                f"<h4 style='text-align: center; color: black;'>Univariate map for {poverty_index_dropdown} </h4>",
                unsafe_allow_html=True,
            )
            folium_static(
                generate_choropleth(
                    combined_df=combined_df_1,
                    admin=admin_choice,
                    column=poverty_indicators[poverty_index_dropdown],
                    legend_name=poverty_legend,
                    fill_color="Reds",
                )
            )

            if computation == "high_resource":
                st.plotly_chart(
                    generate_interactive_time_series(
                        df=survey_data_df.copy(), weather_data_name=weather_columns[0]
                    )
                )

            st.markdown(
                f"<h4 style='text-align: center; color: black;'>Households on map for {poverty_index_dropdown} </h4>",
                unsafe_allow_html=True,
            )
            st.pyplot(
                plot_poverty_index(
                    wave_panel_df=filtered_df_1,
                    map_nigeria=nigeria_shape_df,
                    column=poverty_indicators[poverty_index_dropdown],
                )
            )

    elif size > 2:
        st.error("Error: Too many dropdowns selected, please delete one", icon="🚨")

    else:
        st.error(
            "No filters were selected, please choose one and a time frame in order to use this tool.",
            icon="🚨",
        )


# Side Bar Set Up
st.sidebar.markdown(
    """
        <style>
            [data-testid="stVerticalBlock"] > img:first-child {
                margin-top: -60px;
            }

            [data-testid=stImage]{
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
            }
        </style>
        """,
    unsafe_allow_html=True,
)

# Adding the "About the App" Infomration at the bottom of the Page
with st.sidebar.expander("About the App"):
    st.write(
        """
                This project, in collaboration with the Data Science for Social Good (DSSG 2023) organization, 
                the United Nation's Child Emergency Fund (UNICEF), and Save the Children (STC), was made by 
                team JMPST as a way to combat cross-visualization challenges between extreme weather events 
                and child poverty.
                """
    )

st.sidebar.markdown(
    f"<h5 style='text-align: center; color: black;'>Copyright (c) 2023 Data Science for Social Good (RPTU and DFKI) </h4>",
    unsafe_allow_html=True,
)