import streamlit as st #Streamlit is an open-source Python library that makes it easy to build beautiful custom web-apps for machine learning and data science.
import pandas as pd #Pandas is mainly used for data analysis. Pandas allows importing data from various file formats such as comma-separated values, JSON, SQL, Microsoft Excel. 
import plotly.express as px #Once you import Plotly Express (usually as px ), most plots are made with just one function call that accepts a tidy Pandas data frame. If you want a basic scatter plot, it's just px.
from PIL import Image #PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.



#   for this line of code, we used st.markdown to display the text on our interactive webpage with emoji.
#   because you can use it to flexibly insert rich content into your application.
st.markdown("""# :point_right: :earth_americas: Global Earthquake Magnitude Perspective/report :earth_asia: :point_left:""")

#   Start in line 14 to line 21, we use ops dictionaries to assigns the datasets contained in curly braces with keys such as Past 30 days
#   Past 7 Days, Past Days and especially the Top20 Eq in the world.
ops = {
    'Past 30 Days':'significant_month (2).csv', # This datasets contained data about earthquake for the Past 30 days.
  "Past 7 Days" : 'all_week (2).csv',           # This datasets contained data about earthquake for the Past 7 days.
  "Past days": 'all_day (3).csv'                # This datasets contained data about earthquake for the Past days.
}
ops1 = {
    'Top20 EarthQuake in the World':'top20.csv' # This datasets contained data about Largest earthquake ocurred for the Past day, week,
}                                               # month, year and decade.


slider = st.sidebar         #  For this line of code, we used slider and st.sidebar. means all widgets in slider is placed in a left panel slider.
map1= st.beta_container()   #  For this line of code, we use map1 as a variable name to assign that the map1 is a beta_container
                            #  that helps you organize your app.

slider1 = st.sidebar        # Same explanation for line 24 :)
map2= st.beta_container()   # Same explanation for line 25 :)

# Start in line 37 to 47. All of this code is about ops dictionaries with keys such as past 30 days, past week and day in line 14.
def tap(dta):  # This line of code is already function, because def is the keyword for defining a function. function def followed 
               # by the function name which is tap to hold all data in function def and parameters which is the dta to hold na data included 
               # in a csv then assign it to a dataframe or df for short.

  df = pd.read_csv(dta)  # this line of code, we use df to hold the csv file in ops dictionaries line 14 with parameters dta.
  fig = px.scatter_geo(df, lat='latitude', lon='longitude', 
                          hover_name="place", hover_data=["magnitude", "type", "time"], color='magnitude', color_continuous_scale="Rainbow", 
                          size='magnitude') # for this line of code, we use fig to hold all data in px.scatter_geo. Lets start about px,
                                            # px is high-level API for creating figures then scattergeo which can be used to control
                                            # the appearance of the base map onto which data is plotted. So that, px.scatter_geo is function
                                            # for a geographical scatter plot. The size argument is used to set the size of markers from a 
                                            # given column of the DataFrame. latitude, longitude, magnitude  can be seen in the csv file 
                                            # and they are all visible in the interactive map.

  st.plotly_chart(fig)  # for this line of code, after we assign all fields in a fig, line 37. We use now st.plotly_chart To show Plotly chart 
                        # in Streamlit with fig variable. But all this like parameters, fields and the scattergeo to plot the fields are in 
                        # the function name which is tap for easy to call.


def lap(dta1): # This line of code is already function, because def is the keyword for defining a function. function def followed 
               # by the function name which is lap to hold all data in function def and parameters which is the dta1 to hold na data included 
               # in a csv then assign it to a dataframe or df for short.
  dff = pd.read_csv(dta1)  # this line of code, we use dff to hold the csv file in ops1 dictionaries line 19 with parameters dta1.
  fig1 = px.scatter_geo(dff, lat='latitude', lon='longitude', 
                          hover_name="place", hover_data=["magnitude", "Date", "Top"], color='magnitude', color_continuous_scale="Rainbow", 
                          size='magnitude') # for this line of code, we use fig1 to hold all data in px.scatter_geo. Lets start about px,
                                            # px is high-level API for creating figures then scattergeo which can be used to control
                                            # the appearance of the base map onto which data is plotted. So that, px.scatter_geo is function
                                            # for a geographical scatter plot. The size argument is used to set the size of markers from a 
                                            # given column of the DataFrame. latitude, longitude, magnitude  can be seen in the csv file 
                                            # and they are all visible in the interactive map.

  st.plotly_chart(fig1)# for this line of code, after we assign all fields in a fig1, line 55. We use now st.plotly_chart To show Plotly chart 
                       # in Streamlit with fig1 variable. But all this like parameters, fields and the scattergeo to plot the fields are in  
                       # the function name which is lap for easy to call.




with slider: # This line of code, we use with statement to exception handling to make the code cleaner and much more readable.
             # The content for the slider will start with a colon. The first line After colon  is the first one that can be seen 
             # in the slider panel/bar.
  image = Image.open('yellow.png') # This line of code, we use image name to hold the Image from the file
  st.image(image)  # This code is about to display the image with name and type 'yellow.png'.
  st.markdown("""## User Input Features :mag_right:""") # This code is about to display the text before the selectbox that placed in a sidebar
  select = st.sidebar.selectbox('Choose the Significant EarthQuake', options = list(ops.keys()), index = 0) # This line of code, we use 
                  # select name to hold all list and keys from ops dictionary with caption name 'Choose the...' then indicate to index = 0
                  # to show the first keys in the selectbox that placed in ops dictionary which is the 'Past 30 days'
  tx = '{}'.format(ops[select]) # for this line of code, we use tx to hold dataset specified in ops dictionary '{}' with format specified 
                                # in select name in line 77. We use it to be much more organize. 

with slider1: # This line of code, we use another slider which is slider1 to create another selectbox for the datasets Top20 EQ in the world.
  select1 = st.sidebar.selectbox('Choose', options = list(ops1.keys()), index = 0) # This line of code, we use 
                  # select1 name to hold all list and keys from ops1 dictionary with caption name 'Choose' then indicate to index = 0
                  # to show the first keys in the selectbox that placed in ops dictionary which is the 'Top20 EarthQuake'
  tx1 = '{}'.format(ops1[select1]) # for this line of code, we use tx1 to hold dataset specified in ops1 dictionary '{}' with format specified 
                                # in select name in line 84. We use it to be much more organize. 
 


with map1: # For this line of code, we use with statement again to help be more organize your content.
  # In line 95, we use if statement for st.sidebar.checkbox() to know if the condition is true. if you check the checkbox then,
  # you will see all the content which is all st.markdown, meaning the condition is true.
  if st.sidebar.checkbox('Show Introduction to the Problem/Research'):

    # Start in line 99 to line 110, it’s all about the Introduction. We use st.markdown to display all the content for the introduction 
    # and to change the style of the text because st.markdown is the only tool for custom HTML within a streamlit app that you can edit text.
    st.markdown("<h1 style='text-align: center; font-size: 30px; color: white;'>INTRODUCTION TO THE PROBLEM/Research</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; font-size: 20px; color: white;'>1.1 Background of the Study</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-family:Avantgarde; font-size: 20px; color: white;'>Geologic mapping is a highly interpretive, scientific process that can produce a range of map products for many different uses, including assessing ground-water quality and contamination risks; predicting earthquake, volcano, and landslide hazards; characterizing energy and mineral resources and their extraction costs; waste repository siting; land management and land-use planning; and general education.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>The USGS, or United States Geological Survey, is a scientific agency of the United States government, studying the landscape and natural resources of the United States. There are four major disciplines contained within the United States Geological Survey: biology, geography, geology, and hydrology. The purpose of USGS findings is research, not regulations.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>The USGS is a very large mapping agency, best known for its topographic maps of the United States, drawn at 1:24,000 scale. The USGS publishes many maps, charts, and related documents. These maps are sold by multiple business partners and used by commercial web mapping services.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Other functions of the USGS include monitoring worldwide earthquake activity, magnetic field activity, astrogeology research, and other scientific research programs.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>The USGS monitors and reports on earthquakes, assesses earthquake impacts and hazards, and conducts targeted research on the causes and effects of earthquakes. </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>An earthquake is the consequence of a unexpected release of energy in the Earth’s crust. This sudden energy release causes the seismic waves that make the ground shake that could create seismic waves. Due to the consequence rock breaking, have result in energy waved which is seismic wave. It kind of energy that travels all the way through the earth. Seismic waves pass through either the length of the earth's surface or through the earth's interior.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Earthquakes caused too many damaging effects to the surrounding they act upon. This includes damage to man-made buildings structure and in worst cases the human death. The destruction of structures such as bridges, dams and buildings are caused by the rumbling impacts which originated from the earthquake. Besides, earthquake can also trigger landslides that have bad effect on human life and animal life.</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; font-size: 20px; color: white;'>1.2 Problem Statement </h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Citizens, emergency responders, and engineers rely on the USGS for accurate and timely information on where an earthquake occurred, how much the ground shook in different locations, the expected economic and human impacts, and what the likelihood is of future significant ground shaking.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Citizens, emergency responders, and engineers rely on the USGS for accurate and timely information on where an earthquake occurred, how much the ground shook in different locations, the expected economic and human impacts, and what the likelihood is of future significant ground shaking.</p>", unsafe_allow_html=True)
  
  # In line 114, we use if statement for st.sidebar.checkbox() to know if the condition is true. if you check the checkbox then,
  # you will see all the content which is all st.markdown, meaning the condition is true.
  if st.sidebar.checkbox('Show Description of the Data'): 

    # Start in line 118 to line 122, it’s all about the Description_data. We use st.markdown to display all the content in the description 
    # and to change the style of the text because st.markdown is the only tool for custom HTML within a streamlit app that you can edit text.
    st.markdown("<h1 style='text-align: center; font-size: 30px; color: white;'>Description of the Data</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>The researchers have gathered the data at the United States Geological Survey’s website. The United States Geological Survey estimates that several million earthquakes occur worldwide each year.  The USGS currently records roughly 50 earthquakes each day, for a total of 20,000 each year.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Seismographs are equipment that record earthquakes. A seismogram is the name for the recording they produce. A hefty weight swings free from the seismograph's base, which is securely planted in the ground. The Advanced National Seismic System (ANSS), which is around 40% complete, is helping the USGS enhance its earthquake monitoring and reporting capabilities. Using the data gathered, they discovered that a seismographic network is used to record earthquakes. </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>The movement of the earth at each seismic station in the network is measured. In an earthquake, the movement of one block of rock over another release’s energy, causing the ground to tremble. The most frequent way of determining the size of an earthquake is to use its magnitude. The strong motion data acquired by USGS stations during large earthquakes are documented in Earthquake Data Reports. Earthquake Data from the USGS Earthquakes Hazards Program (EHP) provides a downloadable data in CSV file on global earthquakes for the last 7 days and highlights the history of earthquake occurrences around the world. </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Earthquakes are represented on maps with links to data including latitude, longitude, magnitude, and time. Symbols representing earthquakes are varied in size, representing magnitude, and in color, representing time of earthquake occurrence (within the last hour, the last 24 hours, or the last 7 days). The site also provides general trends, interesting facts or trivia about earthquakes, documentation of the largest earthquakes to ever occur specifically the Top 20 largest earthquakes in the World. </p>", unsafe_allow_html=True)

  # In line 126, we use if statement for st.sidebar.checkbox() to know if the condition is true. if you check the checkbox then,
  # you will see all the content which is all st.markdown, meaning the condition is true.
  if st.sidebar.checkbox('Show Data Preprocess'):

    # In line 130 to line 131, it’s all about the Data Preprocess. We use st.markdown to display all the content in the Data Preprocess 
    # and to change the style of the text because st.markdown is the only tool for custom HTML within a streamlit app that you can edit text.
    st.markdown("<h1 style='text-align: center; font-size: 30px; color: white;'>Data Preprocess (Cleaning & Transformation)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Our dataset is in CSV Format provided by USGS on their website. Data in GEOJSON format contains a lot of data that can be confusing for human reading. But we familiarize ourselves and managed to get the necessary data to be used for our graphs. We encountered some errors when using the data because of anomalies in it such as negative values. We performed data cleaning manually by converting the negative values into absolute values. That means converting any negative values into positive so that data will go through our graph without throwing an error.</p>", unsafe_allow_html=True)

  # In line 135, we use if statement for st.sidebar.checkbox() to know if the condition is true. if you check the checkbox then,
  # you will see all the content which is all st.markdown, meaning the condition is true.
  if st.sidebar.checkbox('Show Data Visualization'):

    # In line 140 to line 159, it’s all about the Data Visualization. We use st.title, st.markdown to display all the content in the Data 
    # Visualization and to change the style of the text because st.markdown is the only tool for custom HTML within a streamlit app that you
    # can edit text. Next is image1 and image2 to hold and show the image form the file with name and type.
    st.title("Data Visualization & Analysis/Insights")
    st.markdown("<h1 style='text-align: justify; font-size: 20px; color: white;'>Data Visualization</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>As we all know, Earthquakes are clustered along fault lines. Showing the quantity and magnitude of earthquakes cumulatively over time is a challenge due to visual overlap. In our Data Visulation shows all the continents where an earthquake has occurred.</p>", unsafe_allow_html=True)
    image1 = Image.open('save1.png')
    st.image(image1,  caption='Figure 1.1')
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Shown in figure 1.1 is about what our interactive map shows. In figure 1.1 this is our graph about Global EarthQuake that you can see the past data about where there was an Earthquake in Past Day, Week and Past Month especially the Largest EarthQuake in the World. On the right side of the Interactive Webpage you can see here the colorbar that represents different magnitudes that match the specific color. The different color of circle is shown on the map. This color circle represents how strong the magnitude is, if it is Magnitude 5, 6, 3 or 8. When you hover the mouse cursor over the color circles you will see different fields like magnitude, coordinates such as latitude and longitude, type , time and escpecially location where there was an Earthquake occured.</p>", unsafe_allow_html=True)
    image2 = Image.open('save2.png')
    st.image(image2,  caption='Figure 1.2')
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Shown in figure 1.2 this is our map about Top 20 Largest EarthQuake in the World that you can see the past data about where there was an Earthquake in Past more years. When you hover the mouse cursor over the color circles you will see different fields like magnitude, coordinates such as latitude and longitude, top , Date&Time,  and escpecially location where there was an Earthquake occured.</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; font-size: 20px; color: white;'>Analysis / Insights</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Based on our perspective/insights about data visualization there is another country where no earthquake occurred and there is also a country that rarely has an earthquake, Because of inactive faults. Inactive faults are structures that we can identify, but which do no have earthquakes or do not display any seismic activity. Some  countries experience a series of earthquakes or there are always earthquakes, Because Earthquakes are usually caused when rock underground suddenly breaks along a fault. This sudden release of energy causes the seismic waves that make the ground shake. The second reason is The Pacific Ring of Fire boasts the world's highest concentration of volcanoes, as well as 90 percent of the planet's earthquakes that cause triggering frequent seismic and volcanic activity. In Palawan there has been no earthquake. According to PHIVOLCS, it has no active faults lines, no active volcanoes, and no deep trenches but it is still vulnerable to earthquake hazards.</p>", unsafe_allow_html=True)


# In line 155, we use if statement for st.sidebar.checkbox() to know if the condition is true. if you check the checkbox then,
# you will see all the content which is st.markdown, meaning the condition is true.
  if st.sidebar.checkbox('Show Map1'):
    st.markdown("""### Map1 :earth_africa:""")
    tap(tx)  # for this line of code, This is a final to show the map, because we called the function name tap. because with the function 
             # name tap, this is where the plotting of the fields on our map with the help of plotly and scattergeo happens
             # and for the tx, here is how to format the selection in our selectbox and usually use index = 0 to show the first keys 
             # listed in the ops dictionary in line 14 :).


with map2: # For this line of code, we use with statement again to help be more organize your content.
  # In line 167, we use if statement for st.sidebar.checkbox() to know if the condition is true. if you check the checkbox then,
  # you will see all the content which is all st.markdown, meaning the condition is true.

  if st.sidebar.checkbox('Show Map2'):
    st.markdown("""### Top20 Largest EarthQuakes in the World :earth_africa:""")
    st.markdown("""### Map2 :earth_africa:""")
    lap(tx1) # for this line of code, This is a final to show the map2, because we called the function name lap. because with the function 
             # name lap, this is where the plotting of the fields on our map with the help of plotly and scattergeo happens
             # and for the tx1, here is how to format the selection in our selectbox and usually use index = 0 to show the first keys 
             # listed in the ops dictionary in line 19 :).

  # In line 177, we use if statement for st.sidebar.checkbox() to know if the condition is true. if you check the checkbox then,
  # you will see all the content which is st.markdown, meaning the condition is true.
  if st.sidebar.checkbox('Show Recommendation & Insights'):
    
    # Start in line 181 to line 192, it’s all about the Recommendation. We use st.markdown to display all the content in the description 
    # and to change the style of the text because st.markdown is the only tool for custom HTML within a streamlit app that you can edit text.
    st.markdown("<h1 style='text-align: center; font-size: 30px; color: white;'>Recommendation/Action Points based on the Insights</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>The aims of the study can be restated as follows:     •	To examine the existing data made by USGS in the domain of location of earthquakes and count of quakes around the world, to focus on how many quakes and the magnitude and, intensity will happen per month.      •	To Test the findings of the graph gathered in USGS earthquake locator.         •	To spearhead the realistic effort of development and strategies of making data visualization. </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Pursuing the aims of the study, the research design had the following major features: Self-administered questionaires distributed to subjects, focus group discussions in accordance with the first aim of the project, the USGS will provide data information for us to collect and create a graph by making its own web program and the graph will provide the information within the month. </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Regarding the second aim, the result of data from USGS earthquake locator the data that they gave are the one we will set on the data visualization by determine the magnitude and the intensity in current location on the map.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Lastly the result of the data visualization is mast be accurate and the information according to the graph is well be given, they must make sure that the information and data are well polish within the graph.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Given these there’s a place can be an earthquake will occur, the only dangerous ones are those contained and hit by the pacific ring of fire because volcanoes the tectonic plates are more active there, I believe that this project, makes an important contribution to providing guidance for a way forward in terms of how people might respond to daily active of earthquake around the world.</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 30px; color: white;'>Recommendation</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>The project wishes to make some recommendations, which, if taken into consideration, might bring some positive changes to the current approach.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>•	since it is difficult to predict the earthquake, we just need maybe we are aware of where we are located if he is prone to an earthquake, we really need awareness and immediate emergency</p>", unsafe_allow_html=True)  
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>•	we can still add a graph line graph showing or determining the intensity and time or day like that.</p>", unsafe_allow_html=True) 
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>•	provide accurate information on the graph with the specific content to the targeted location. This implies ensuring that the user will understand the fabricate information from what is implied. There is no need to tease user</p>", unsafe_allow_html=True) 
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>•	friendly User interface and the color of the background mast is not hurt the eyes of the user </p>", unsafe_allow_html=True) 
  
