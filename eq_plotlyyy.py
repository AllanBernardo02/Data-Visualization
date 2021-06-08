import streamlit as st #Streamlit is an open-source Python library that makes it easy to build beautiful custom web-apps for machine learning and data science.
import pandas as pd #Pandas is mainly used for data analysis. Pandas allows importing data from various file formats such as comma-separated values, JSON, SQL, Microsoft Excel. 
import plotly.express as px #Once you import Plotly Express (usually as px ), most plots are made with just one function call that accepts a tidy Pandas data frame. If you want a basic scatter plot, it's just px.
from PIL import Image #PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.



#
st.markdown("""# :point_right: :earth_americas: Global Earthquake Magnitude Perspective/report :earth_asia: :point_left:""")


ops = {
    'Past 30 Days':'significant_month (2).csv',
  "Past 7 Days" : 'all_week (2).csv',
  "Past days": 'all_day (3).csv'
}
ops1 = {
    'Top20 EarthQuake in the World':'top20.csv'
}


slider = st.sidebar
map1= st.beta_container()
slider1 = st.sidebar
map2= st.beta_container()


def tap(dta):
  df = pd.read_csv(dta)
  fig = px.scatter_geo(df, lat='latitude', lon='longitude', 
                          hover_name="place", hover_data=["magnitude", "type", "time"], color='magnitude', color_continuous_scale="Rainbow", 
                          size='magnitude')

  st.plotly_chart(fig)


def lap(dta1):
  dff = pd.read_csv(dta1)
  fig1 = px.scatter_geo(dff, lat='latitude', lon='longitude', 
                          hover_name="place", hover_data=["magnitude", "Date", "Top"], color='magnitude', color_continuous_scale="Rainbow", 
                          size='magnitude')
  st.plotly_chart(fig1)




with slider:
  #image = Image.open('eqq.jpg')
  image = Image.open('yellow.png')
  st.image(image)
  st.markdown("""## User Input Features :mag_right:""")
  select = st.sidebar.selectbox('Choose the Significant EarthQuake', options = list(ops.keys()), index = 0)
  tx = '{}'.format(ops[select])

with slider1:
  select1 = st.sidebar.selectbox('Choose', options = list(ops1.keys()), index = 0)
  tx1 = '{}'.format(ops1[select1])
 

 


#st.markdown("<h1 style='text-align: justify; font-size: 20px; color: black;'></h1>", unsafe_allow_html=True)

with map1:
  if st.sidebar.checkbox('Show Introduction to the Problem/Research'):
    #st.title("INTRODUCTION TO THE PROBLEM/Research")
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
    

  if st.sidebar.checkbox('Show Description of the Data'):
    #st.title("Description of the Data")
    st.markdown("<h1 style='text-align: center; font-size: 30px; color: white;'>Description of the Data</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>The researchers have gathered the data at the United States Geological Survey’s website. The United States Geological Survey estimates that several million earthquakes occur worldwide each year.  The USGS currently records roughly 50 earthquakes each day, for a total of 20,000 each year.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Seismographs are equipment that record earthquakes. A seismogram is the name for the recording they produce. A hefty weight swings free from the seismograph's base, which is securely planted in the ground. The Advanced National Seismic System (ANSS), which is around 40% complete, is helping the USGS enhance its earthquake monitoring and reporting capabilities. Using the data gathered, they discovered that a seismographic network is used to record earthquakes. </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>The movement of the earth at each seismic station in the network is measured. In an earthquake, the movement of one block of rock over another release’s energy, causing the ground to tremble. The most frequent way of determining the size of an earthquake is to use its magnitude. The strong motion data acquired by USGS stations during large earthquakes are documented in Earthquake Data Reports. Earthquake Data from the USGS Earthquakes Hazards Program (EHP) provides a downloadable data in CSV file on global earthquakes for the last 7 days and highlights the history of earthquake occurrences around the world. </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; font-size: 20px; color: white;'>Earthquakes are represented on maps with links to data including latitude, longitude, magnitude, and time. Symbols representing earthquakes are varied in size, representing magnitude, and in color, representing time of earthquake occurrence (within the last hour, the last 24 hours, or the last 7 days). The site also provides general trends, interesting facts or trivia about earthquakes, documentation of the largest earthquakes to ever occur specifically the Top 20 largest earthquakes in the World. </p>", unsafe_allow_html=True)

  if st.sidebar.checkbox('Show Data Preprocess'):
    #st.title("Data Preprocess (Cleaning & Transformation)") 
    st.markdown("<h1 style='text-align: center; font-size: 30px; color: white;'>Data Preprocess (Cleaning & Transformation)</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; font-size: 20px; color: black;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; font-size: 20px; color: black;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; font-size: 20px; color: black;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; font-size: 20px; color: black;'></h1>", unsafe_allow_html=True)

  if st.sidebar.checkbox('Show Data Visualization'):
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


  if st.sidebar.checkbox('Show Map1'):
    st.markdown("""### Map1 :earth_africa:""")
    tap(tx)


with map2:

  if st.sidebar.checkbox('Show Map2'):
    st.markdown("""### Top20 Largest EarthQuakes in the World :earth_africa:""",True)
    st.markdown("""### Map2 :earth_africa:""")
    lap(tx1)

  if st.sidebar.checkbox('Show Recommendation & Insights'):
    #st.title("Recommendation / /Action Points based on the Insights")
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
  
