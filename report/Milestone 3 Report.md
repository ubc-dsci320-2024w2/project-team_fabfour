## Research Questions
[ Here will we will include our research questions again ]

**Allison's** research question is: **What is the impact of the respondent's age on their survey responses?**
- Does Age Influence the Relationship Between Music Genre Preferences and Mental Health Scores? How do music preferences correlate with mental health scores for different age groups? 
- How Does Age Influence the Relationship Between Music Engagement and Mental Health Outcomes? Examine how different forms of music engagement (e.g., instrumentalist, composer) correlate with mental health outcomes across various age groups. Do those who engage with music in more dimensions (e.g. composer or musician) form distinct groups?

**Judy's** research question is: **How does the favorite genre and the diversity of music genres an individual listens to influence the perceived music effects on their well-being and their self-reported mental health conditions?**

Some sub-research questions worth exploring would be:
- Are there specific favorite genres that are more commonly associated with positive or negative perceived effects of music on well-being?
- Are individuals who listen to a variety of music genres more likely to report that music improves their well-being compared to those with low diversity, regardless of their favorite genre?
- Do individuals with different mental health conditions (anxiety, depression, insomnia, OCD) tend to have distinct music preferences?

**Helena's** research question is: **What is the relationship between specific mental illnesses and listening habits?**
- Are any mental illnesses associated with specific listening habits (specific platforms, favourite genre, listening while working, frequency of specific genres, exploratory tastes, foreign languages, etc.)?

**Jessica's** research question is: **How does response bias play a role in self-reporting mental health severity?**

Further questions worth exploring might be:
- What are the patterns and anomalies in self-reported mental health severities?
- How do demographics (eg. mental illness), music listening habits contribute to biased self-reporting?
- Are there any reasons for extreme/invalid response values that can be identified based on other responses?
- How do illogical, invalid responses influence data reliability?
The visualization may be a dashboard with interactions, or SPLOM with outlier points that are linked bi-directionally to other visualizations.

## Visualizations

[ For each visualization/view ]...

### The relationship between music preferences, musical engagement, and mental health across age groups.
*Member: Allison Fellhauer*

This visual exploration aims to better understand how age and musical engagement—both passive (favourite genres) and active (playing or composing music)—relate to self-reported mental health. Each chart was designed to answer a specific question, motivated by an interest in how people experience and interact with music across different life stages and mental health conditions.

One focus was on whether age shaped musical taste, and if certain genres were more common among younger or older groups. Another key question was whether different forms of musical engagement—such as playing an instrument, composing, or simply listening—had any connection to self-reported levels of anxiety, depression, insomnia, or OCD.

#### **How does the average age of listeners vary across favorite music genres, and what does the age distribution look like for each genre?**

<img src="../images/pm3/allie_viz1.gif" />

#### *Summary and Explanations*:
**Tasks**
This visualization supports the following tasks:

1. **Compute Derived Value** – It displays the average age of respondents for each favourite genre.
2. **Determine Range** – It reveals the distribution and variation of ages within each genre.

The dot plot on the left shows the **average age** for each genre along the x-axis, allowing for quick comparisons across genres to identify those preferred by older vs. younger individuals. Hovering over a point provides a tooltip with exact values for both average age and count.

The linked histogram on the right shows the distribution of ages for the selected genre, binned into 5-year intervals. This enables viewers to identify skewness (e.g., Latin or Gospel), spot multiple peaks, and observe the distribution of ages within genres.

**Visualization Choices**
1) Dot plot
- Mark: Point (mark_circle)
- Channels:
     - _Horizontal_: encodes average age
     - _Vertical_: encodes genre category
     - _Size_: encodes respondent count
     - _Colour_: indicates selected genre during interaction
     - _Line_: indicates the overall average
     - _Text_: indicates genre label
Justification: The point mark was chosen instead of bars since the average does not need to originate at zero and it supports effective encoding of count using size. The size channel is able to highlight genre popularity. Colour serves a supporting aesthetic role, helping users visually track the selected genre. The use of the line was also important to serve as an anchor for the points, and to show how the values did not vary too much from the overall mean. Due to the points being far from the axis, the labels were removed and placed near their corresponding point.

2) Histogram
- Mark: Bar (mark_bar)
- Channels:
     - _Horizontal_: binned age (5-year intervals)
     - _Vertical_: count per bin
     - _Colour_: matches dot plot to reflect selected genre
Justification: A bar chart provides a clear, consistent representation of age distributions, and exploits the common scale to support comparison of bin heights. The consistent bin width enables easy identification of skew, peaks, and gaps.

**Interactions and Interactivity**
The visualization employs a mouseover interaction on the dot plot. When a genre is hovered over:
- The histogram updates to reflect the age distribution for that genre.
- The genre name updates dynamically in the histogram title.
- The selected genre is highlighted using colour, while others fade to gray.

In addition, the visualization also uses a radio button for specific lookup.

This design avoids overwhelming the viewer with all 16 genres simultaneously and removes the need for a legend. Since there are the presence of genres with smaller counts (e.g. Latin), including tolerance in the interaction allows for easier selection. A tooltip is used for value lookup, providing exact average age and respondent count, supporting retrieval tasks.

#### *Critique of View*
This visualization is effective due to its strong use of marks, position channels, and interaction design. The use of a common scale in both the dot plot and the histogram enables comparison, which is one of the primary tasks of this visualization. Although area can be less obvious than length when making comparison, its use here helps highlight the popularity of different genres, especially the extremes. This allows the viewer to immediately see that even though gospel has the greatest average age, this is as a result of few individuals choosing this genre (count = 3). In addition, colour is used in this visualization to express transition between categories and the connection between the dot plot and the histogram. Only seven colours were used overall, which reduced stimulation while still providings distinction between neighbouring categories. By faceting and filtering, only a single category is shown at once time, bypassing the need to distinguish colours. Finally, the interaction used is sophisticated (many moving parts including the genre labels, colour, histogram filtering, and title filter), yet very simple and intuitive. It allows for easy parusal and removes all clutter caused by displaying all charts simultenously.

#### **How does the age distribution vary across different severity levels of mental health conditions?**

<img src="../images/pm3/allie_viz2.gif" />

**Tasks**
This visualization supports the following tasks:

1. **Determine Range** – Reveals the full distribution of age for each severity level (Low, Medium, High) across various mental health conditions.
2. **Retrieve Value** – Allows inspection of how age is distributed for each selected condition and severity level.
3. **Identify Trends** – Investigates whether younger individuals are more likely to report high severity scores (as observed by researchers).

The violin plot presents the smoothed distribution of age for each mental health severity level (Low, Medium, High), for a selected condition (e.g., Anxiety, Depression, etc.). Users can switch between conditions via a dropdown.

This visualization is specifically designed to support exploration of a potential reporting bias among older individuals, who may be less likely to rate themselves as highly anxious or depressed. If this bias exists, it should be reflected in narrower violins for older ages in the “High” category, or in a general shift of the “High” distribution toward younger age groups.

**Visualization Choices**
- Mark: Area (mark_area with interpolate='monotone' and orient='horizontal')
- Channels:
    - _Horizontal_: Smoothed density of respondents (stacked center)
    - _Vertical_: Age
    - _Colour_: Severity Level (Low, Medium, High); change in saturation
    - _Column_: Faceting by Level
Justification: The area mark was chosen for its ability to show density smoothly, and it was preferred over a boxplot due to its ability to represent bimodal data and display trends more clearly [Source](https://clauswilke.com/dataviz/boxplots-violins.html). Faceting by level allows for direct comparison of age distributions across severity categories without interference or crowding. Overlapping violins (one per level) would be visually messy and difficult to interpret. Colour saturation is used over hue to correctly encode the ordinal variable.

**Interactions and Interactivity**
The visualization introduces a dropdown menu for the mental health condition (e.g., Anxiety, Depression, etc.). Upon selection:
- The violin plots dynamically update to show the age distributions for that condition across severity levels.
- Tooltips allow for value lookup, offering precise information about the estimated age and density at any point along the violin.

This interaction is simple but effective. It avoids overloading the user with too many violins at once and allows the user to explore one condition at a time.

#### *Critique of View*
This visualization effectively reveals distribution shapes, which is essential for addressing the core question of whether younger individuals report higher severity. The width of each violin at different age points represents the relative density of respondents, allowing users to assess whether high severity is concentrated among younger people. The violin plot was chosen to emphasize density, display multiple peaks, and reduce the impact of noisy outliers. By combining this mark with faceting, each severity level appears in its own column, enabling clear and uncluttered comparisons. The dropdown interaction also enhances usability by allowing side-by-side comparisons across mental health conditions without introducing visual clutter.

However, a limitation of this approach is the presence of long tails at the top of the violins, which is misleading since it suggests the presence of data where none exists ([Source](https://clauswilke.com/dataviz/boxplots-violins.html)). Additionally, violin plots are generally less intuitive than histograms, which may pose a challenge for novice viewers. However, the posi

#### **How do musical hobbies relate to mental health scores across age, and which are most represented within different age and score ranges?**

<img src="../images/pm3/allie_viz3.gif" />

#### *Summary and Explanations*:
**Tasks**
This visualization supports the following tasks:
1. **Filter** – It filters by musical hobby (both, instrumentalist, composer, or neither) and mental health condition to explore associations between musical hobbies, age, and mental health scores.
2. **Retrieve Value** – It retrieves the count of respondents per musical hobbies, as well as the range and distribution of mental health scores.
3. **Determine Range** – It enables examination of score distribution across ages and musical hobby groups.
   
The scatterplot on top visualizes individual responses, plotting age on the x-axis and the selected mental health condition score on the y-axis. Colour encodes musical hobby. An interval selection (brush) filters the data shown in the linked bar chart to aleviate overplotting.

The bar chart below shows the count of respondents per musical hobby for the brushed region. This helps answer if people with higher scores tend to play music, or if certain musical hobbies cluster at different score levels.

**Visualization Choices**
1. Scatter Plot
- Mark: Point (mark_circle)
- Channels:
    - _Horizontal_: Age
    - _Vertical_: Mental health score
    - _Colour_: Musical hobbies (Both, Instrumentalist, Composer, Neither)
Justification: A scatterplot was selected to reveal trends in mental health scores across age for different musical identities. Colour helps differentiate groups while preserving clarity. The dropdown enables users to compare how different mental health conditions. A brush interaction was added to for linked filtering and to help with overplotting.

2. Bar Chart
- Mark: Bar (mark_bar)
- Channels:
    - _Horizontal_: Count
    - _Vertical_: Musical Hobby
    - _Colour_: Same hobbies as scatterplot
Justification: The bar chart provides a simple yet effective view of how many individuals fall into each musical category for a selected region of the scatterplot. This helps answer whether certain musical identities appear more frequently at high or low mental health scores. The use of length and aligned bars supports direct comparison.

**Interactions and Interactivity**
The visualization allows for multiple interactions, including:
- A brush selection on the scatterplot highlights points and filters the bar chart accordingly.
- A color selection on the bar chart allows filtering the scatterplot to view specific musical hobbies.
- A dropdown menu lets users change the mental health condition (Anxiety, Depression, etc.), updating the y-axis.
- A tooltip which displays score, age, and category.

These interactions support bidirectional exploration: users can begin by selecting a musical hobby or a region of interest (e.g., high anxiety and younger age) and observe how counts shift below. 

**Crtitque of View**
This visualization does a strong job of helping users explore how musical hobbies relates to age and mental health across different conditions. The scatterplot shows patterns in how scores change with age and lets viewers spot clusters and outliers. Color is used effectively to separate the four musical hobby groups, and the same color palette ties both charts together clearly. The interaction is both easy to use and useful. Brushing (clicking and dragging) on the scatterplot filters the bar chart below, giving instant feedback. Users can also click on a bar to filter the scatterplot, making it easy to focus on just one group. The problem with using a large dataset is that the raw data can be overwhelming and display overplotting. By adding a filter, the noise is reduced, and the user can performed focused exploration. 

One small limitation is that only one mental health condition can be viewed at a time (because of the dropdown). However, this keeps the view clean and avoids overwhelming the viewer. The bar chart works well with only four categories, and it makes it easy to compare counts across groups.

### View 2
TODO: Helena
1. Screenshot/gif of visualization
2. Summary of tasks and how they accomplish the task
3. Explain/justify viz choices
    1. Marks
    2. Channels
    3. Characteristics of channels exploited
    4. Describe new interactions
    5. Characteristics of interactions and interactivity
    6. Critique the view


### The relationship between the diversity of genres an individual listens to, their self-reported mental health conditions, and the different perceived music effects.
*Member: Judy Lee*


#### **What is the relationship between the variety of genres an individual listens to and their self-reported mental health conditions?**

<img src="../images/pm3/judy_viz1.gif" />

#### *Summary and Explanations*:

**Tasks**
This visualization supports the following tasks:

1. **Correlate** – Examines the relationship between an individual's genre diversity score and their self-reported mental health conditions (anxiety, depression, insomnia, OCD).
2. **Determine Range** – Identifies how mental health scores vary across different levels of genre diversity.
3. **Retrieve Value** - Shows the count of individuals within selected ranges for each condition.
4. **Filter** - Allows the selection of a subset of the data points.

The view helps to identify the relationship between genre diversity and self-reported mental health conditions. It consists of a scatterplot, a bar chart and a correlation heatmap. The scatterplot allows users to visually assess whether higher or lower genre diversity scores correspond to particular mental health conditions. It consists of mental health score on the x-axis and genre diversity score on the y-axis. It has an interactive brushing component that enables filtering subsets of data. Since there are multiple points on the scatterplot that are overlaid on top of each other, there is a bar chart that displays the count of the points for the selection for each mental health condition for more clarity. the bar chart has the number of individuals on the x-axis and the mental health condition on the y-axis. The correlation heatmap helps to view the correlation value between genre diversity score and self-reported mental health condition with one variable on each axis.

**Visualization Choices**
1. *Scatterplot*
   
- Mark: Point (mark_circle)
- Channels:
    - Position on a common scale: The horizontal position encodes mental health score which is a quantitative value and the vertical position encodes the genre diversity score which is also quantitative and a magnitude channel is best at representing these quantitative values.
    - Size: Encodes the count of mental health conditions in the scatterplot and it is effectively used since count is a quantitative value.
    - Color hue: Encodes mental health condition which is categorical and thus color hue is an appropriate identity channel to distinguish between the various levels.
- Justification: Scatterplots are ideal for showing the relationship between two quantitative variables. Using position along common scales effectively shows the distribution and potential correlations. Size is added to show the number of conditions overlapping, which addresses overplotting. The color hue helps differentiate the mental health conditions.

2. *Bar chart*
- Mark: Line (mark_bar)
- Channels:
    - Length: Encodes the count and is used to express that quantitative value
    - Color hue: Encodes mental health condition and it is used to differentiate between the levels of the categorical attribute of mental health condition.
    - Spatial regions: There is one per mark which is separated vertically, and aligned horizontally.
- Justification: Bar charts are good for comparing counts of categorical data. Using length to represent count allows for easy comparison between different mental health conditions within the selected range of the scatterplot.

3. *Correlation heatmap*
- Mark: Point (mark_point)
- Channels:
    - Color saturation: Encodes the correlation value which is quantitative. Lower values of saturation means lowest correlation and higher saturation indicates higher correlation.
    - 2D shared position: Encodes the two variables as a cell.
- Justification: Heatmaps are effective in displaying correlation matrices and the color saturation used represents the correlation value where its intensity helps to quuickly identify strong or weak relationships, and the 2D shared position clearly shows which variables are being correlated.

#### *Interactions and Interactivity*
- The brushing on the scatterplot allows users to select a range of data points and filters the bar chart to show counts within that range. Double-clicking on the background of the scatterplot should undo the selection.
- There is a tooltip on the individual data points of the scatterplot that shows the mental health condition, mental health score and genre diversity score for that point.
- There is also a tooltip on the correlation heatmap that shows the variable 1, variable 2 and the correlation between the two variables.

*Characteristics of the interactions and interactivity*: 
- Linked Views: The scatterplot and bar chart are linked and provide dynamic filtering and exploration.
- Selection: Brushing allows for interactive selection of data subsets.
- Overview and Detail: The scatterplot provides an overview, while the bar chart offers detailed counts for selected subsets.

#### *Critique of View*
The view effectively shows the relationship between genre diversity and mental health conditions. The scatterplot provides an overview, while the bar chart and heatmap offer more detailed insights. The color coding, which differentiates mental health conditions, is consistent across both the scatterplot and bar chart, making it easier for users to track data across different views. The interactive brushing feature is also great since it allows users to filter the scatterplot and see the corresponding counts in the bar chart which enables users to explore in more detail. While the scatterplot tries to reduce overplotting by adjusting point sizes, this might not fully solve the issue in areas with dense data. However, the bar chart complements this by clearly showing counts within selected ranges. Additionally, the heatmap helps investigate the correlation by highlighting the relationships between variables using a correlation value. Overall, the view helps answer the question.

#### What is the distribution of genre diversity scores among individuals who report different effects of music on their well-being?
<img src="../images/pm3/judy_viz2.gif" />

#### Summary and Explanations:

**Tasks**

This visualization supports the following tasks:

1. **Characterize Distribution** – Examines the distribution of genre diversity scores across different perceived music effects.
2. **Determine Range** - Displays the range of genre diversity scores across different perceived music effects.
3. **Retrieve Value** – Shows the count of individuals within each genre diversity score range for each music effect.
4. **Filter** - Filter by music effect to view the respective distribution.
   
The view helps identify how genre diversity scores are distributed among individuals who report different effects of music on their well-being. It consists of a violin plot, a histogram, and a rug plot. The violin plot allows users to visually assess the distribution shape and density of genre diversity scores for each music effect. The histogram displays the count of individuals within each genre diversity score range, segmented by music effect. The rug plot provides a detailed view of individual data points along the genre diversity score axis.

**Visualization Choices**

1. *Violin Plot*

- Mark: Area (mark_area)
- Channels:
  - Position on a common scale: Encodes genre diversity score which is a quantitative value as vertical position.]
  - Color hue: used to encode different categories of music effects which helps in differentiating between them.
- Justification: Violin plots are effective for showing the distribution of quantitative data across categorical groups. They combine the features of box plots and kernel density plots and thus provide insights into the data's shape and density.
  
2. *Stacked Histogram*

- Mark: Vertical stack of area marks (mark_bar)
- Channels:
  - Position on a common scale where the horizontal position encodes the genre diversity score and length (frequency attribute) encodes the vertical position.
  - Color Hue: Encodes the categorical variable music effects which helps differentiate between each level of the attribute.
- Justification: Histograms are used to show the distribution of a quantitative variable which is genre diversity score in this view. The segmented bars, colored by music effects, enables the comparison of the distribution of genre diversity scores among the different music effects.
  
3. *Rug Plot*

- Mark: Line (mark_tick)
- Channels:
  - Position on a common scale: Encodes the genre diversity score as vertical position.
  - Color hue: Used to encode the categorical levels of the music effects attribute.
- Justification: Rug plots provide a detailed view of individual data points along a single axis, showing the distribution of genre diversity scores.

#### Interactions and Interactivity

- Interactive legend that enables filtering to view the distribution and range of each music effect.
- Range slider that enables users to view the violin plot for a specific range on the y-axis. 

*Characteristics of the interactions and interactivity*:

- Linked Views: The violin plot, histogram, and rug plot are linked to provide a comprehensive view of the data.
- Selection: The interactive legend of music effects allows selection of a music effect and filtering views across specific music effects.
- Overview and Detail: The violin plot provides an overview of the distributions, while the histogram and rug plot offer more detailed insights.

#### Critique of View
The view effectively shows the distribution of genre diversity scores across different perceived music effects. The violin plot illustrates the distribution shapes and densities for each music effect and enables easy comparison across music effects. The histogram provides a detailed view of the counts within each genre diversity score range, filtered by music effect. The rug plot offers a granular view of individual data points which helps to understand the distribution of the genre diversity score. The consistent color coding across the violin plot and histogram helps users track data across views. One limitation is that while the linked views and interactive legend are useful, the violin plots lack direct interactivity. Users cannot directly select or hover over specific data points or density areas within the violin plots to get precise values, counts, or ranges. This limits the ability to explore the nuanced distributions in the violin plots directly.

### How does the frequency of listening to different music genres relate to self-reported mental health conditions and the perceived effects of music?
<img src="../images/pm3/judy_viz3.gif" />

### Summary and Explanations:

**Tasks**

This visualization supports the following tasks:

- **Characterize distribution**: Examining the distribution of mental health scores based on the frequency of listening to a specific favorite genre.
- **Filter** – Allows filtering by music effect and mental health condition to focus on specific subsets of data.
- **Retrieve Value** – Shows the proportion of respondents within each mental health condition level for each genre listening frequency.
- **Find Extremum** – Determining which favorite genre has the highest proportion of individuals reporting the effects of music on their well-being.
  
The view helps identify how the frequency of listening to different music genres relates to self-reported mental health conditions and the perceived effects of music. It consists of a normalized stacked bar chart and a radial chart. The normalized stacked bar chart displays the proportion of respondents with different mental health condition levels for each genre listening frequency. The radial chart shows the distribution of music effects across different favorite genres.

**Visualization Choices**

1. *Radial Chart*

- Mark: 2D Area mark (mark_arc)
- Channels:
  - Polar position: Encodes the favorite music genre as angular position and the proportion of individuals as radial position.
  - Color Hue: Encodes the favorite genres which is a categorical attribute and an identity channel like color hue is ideal for higher discriminability.
- Justification: The radial chart is suitable for visualizing the distribution of music effects across different genres, as it effectively uses angular and radial encoding to display proportions. The angular position represents the different genres, while the radius shows the proportion of individuals reporting each effect. This enables an intuitive comparison between genres. The use of color enhances the ability to differentiate between the different categories of genres. Additionally, the radial layout provides a compact way to represent categorical data and makes it easy to determine which favorite genre has the highest proportion of individuals per music effect.
  
3. *Normalized Stacked Bar Chart*

- Mark: Vertical stack of line marks (mark_bar)
- Channels:
  - Length: Encodes the proportion of respondents within each mental health condition level for each genre listening frequency which is a quantitative value so a magnitude channel like length is effective.
  - Color Hue: Encodes the categorical variable mental health condition level and helps differentiate between the levels of low, medium and high.
  - Spatial regions: Encoded as one per glyph 
- Justification: Normalized stacked bar charts are effective for showing proportions of different categories within a whole and comparing them across different groups. Length is used to represent proportions, and color hue differentiates mental health condition levels. The normalized stacked bar structure ensures that each bar represents a complete whole which enables direct comparison of proportions.

#### Interactions and Interactivity

- Bidirectional linking between the radial plot and the normalized stacked bar chart. Selecting a genre on the radial plot shows the distribution of the genre on the normalized stacked bar chart and selecting a section of the stacked bar chart shows the respective genre on the radial plot.
- Dropdown menus to select music effect and mental health condition which allows filtering across the entire view.
- Tooltips on the radial plot (favorite genre, count of individuals that has this genre as favorite genre, and the proportion) and on the normalized stacked bar chart (favorite genre, frequency, mental health condition level and proportion)
    
*Characteristics of the interactions and interactivity*:

- Filtering: Dropdown menus allow filtering data based on music effects and mental health conditions.
- Linked Views: The normalized stacked bar chart and radial chart are linked through the filtering option.
  
#### Critique of View
The view effectively shows the relationship between genre listening frequency, mental health conditions, and perceived music effects. The normalized stacked bar chart clearly displays the proportions of different mental health condition levels across various listening frequencies which helps easy comparison. The radial chart provides an overview of how different favorite genres are associated with perceived music effects. The filtering options allow users to focus on specific subsets of the data which encourages exploration. The consistent use of color coding across the view helps users track data across different representations. However, one possible limitation is that the radial chart might be challenging to interpret accurately, especially when comparing areas or angles across different genres and music effects. It relies heavily on angle and area encoding, which are known to be less precise for human perception compared to length or position. This can make it difficult to accurately compare proportions for different genre-effect combinations, which can ultimately limit the chart's effectiveness in communicating precise information.

### Response bias in self-reported mental health severity
*Member: Jessica Luo*

One limitation of this data set is the use of self-report.
Although self-report can often be a simple way to gather large amounts of data from the public,
responses may be subjected to bias.

**Response bias** refers to systematic distortions in how people answer surveys or self-report data,
leading to inaccurate or misleading results.
It occurs when respondents provide answers that are not entirely truthful
or reflective of their actual thoughts, feelings, or behaviors.
This can happen due to various factors, such as social desirability (wanting to appear in a certain way),
misunderstanding questions, extreme response tendencies (always choosing the highest or lowest options),
or even response/survey fatigue.
Response bias is particularly relevant to this dataset of self-reported mental health severity,
as individuals may overstate or understate their symptoms based on personal perceptions, stigma,
or other influences, potentially impacting the reliability of this data, 
and in turn, our results and perceptions of the visualizations above.

#### **What is the distribution of self-reported mental health scores based on opinions of music on mental health?**

<img src="../images/pm3/jess_vis1.gif" />

#### *Summary and Explanations*:
Above, we can see four violin plots, one of each mental health condition, overlaid by boxplots.
By default, the gray violin plots, using `.mark_area()` and `.transform_density()`,
show self-reported mental health severity score 
(tasks: **characterize distribution**, **determine range**) 
of each mental health condition. 
Boxplots, using `.mark_boxplot()`, are overlaid to show the medians and interquartile ranges (IQR)
to add another layer of insight into the central tendencies of responses.
Different **colors**, using `alt.Color()`, represent the perceived effects of
music on well-being (Improve, No effect, No response, Worsen).
The **X-axis** encodes the self-reported mental health severity on a 0-10 scale.
Horizontal violin and boxplots were used since encoding scores left to right, instead of down to up,
are more similar to traditional histogram density plots,
making it easier for a novice viewer to understand this vis.
The width of the violin plot represent the **distribution** of responses,
showing where responses are more or less frequent.
Using the legend, we can **interactively view** the violin plot - splitting (task: **filter**) by music effects. 

#### *Critique of view*
The combination of violin plots/density ridges and boxplots effectively balances distribution and summary statistics.
The use of color for mental health scores are expressive and meaningful;
in my vis, dark green relates to "Improves", light green relates to "No effect", and dark purple relates to "Worsen".
For these choices, I assume the viewer also lives in my society where green means "good" 
and dark green means "very good" while light green means "ok".
The vis also uses a colourblind friendly palette, obtained from
[ColorBrewer2.org](https://colorbrewer2.org/#type=diverging&scheme=PRGn&n=4).
Boxplots may be difficult to interpret due to their small size within the larger ridges,
but larger box plots may make the violin plot splits more difficult to see.
Showing only one mental health condition at a time can be very effective, allowing for better focus.


#### **What are the response patterns (and anomalies) for self-reported mental health scores?**

<img src="../images/pm3/jess_vis2.gif"/>

#### *Summary and Explanations*:
Here, we can see a multi-bar plot and a dotplot, using `.mark_bar()` and `.mark_circle()`, respectively.
By default, the plots display mental health self-report scores by color.
The bars can easily show any noticeable response patterns 
(tasks: **compare**, **find extremums**) for each mental health condition. 
The **X-axis** encodes the self-reported mental health severity on a 0-10 scale (same as above).
The **Y position/height** of each bar and size of dots represent the counts for self-reported responses,
showing where responses are more or less frequent.
The **colors** represent different mental illnesses for more clarity and differentiation.
The multi-bar plot, using `.mark_bar()` allow us to **characterize distribution** 
and is linked with a **brush** that corresponds to the dotplot below.
A brush can be used in both the multi-bar and dot-plot.
Using the brush, we can interactively view the plots by splitting (task: **filter**) based on self-report score. 
Showing only range may help focus the viewer on patterns within a smaller frame, allowing for better effectiveness.
Using the dot-plot, we can easily see the **anomolies** of self-reported mental health:
we can see that `3.5` was a self-reported score for some people with anxiety and insomnia.

#### *Critique of view*:
The combination of a bar chart (top) and a bubble chart (bottom) provides two perspectives on the same data, which can be helpful for interpretation.
Use of the different colors shows effective distinction across visualizations,.
Bar height to show count of records, on a common axis, is regarded as the most effective and expressive; 
use of circle area to show Count of Records is regarded as less effective,
but when placed in a line and separated by color, can be useful for filtering and comparing with the barplot above.
When using only the multibar plot, is difficult to see the Counts of infrequent responses,
but the dotplot makes it easier to see these anomalies.

#### **Can we group individuals into clusters based on their music preferences and mental health scores?**

<img src="../images/pm3/jess_vis3.gif"/>

#### *Summary and Explanations*:
This visualization consists of four scatter plots arranged in a facet grid format,
each representing a different mental health condition: Anxiety, Depression, Insomnia, and OCD. 
The four subplots allow for direct **comparisons** across mental health conditions 
while keeping the same x- and y-positions for consistency and effectiveness.
The **x-axis** for each plot corresponds to self-reported severity scores (ranging from 0 to 10).
The **y-axis** represents an unspecified variable labeled "y", and can be interacted with.
The **dropdow**n allows for interactivity, such that users may to switch the y-axis to other possible variables. 
The scatter plots use **color** encoding to show different music effects on individuals' mental health responses.
This allows the viewer to visually separate trends (task: **compare**, **cluster**) 
in how music affects different conditions.
Each dot (`mark_circle`)represents an individual data point, corresponding to a survey respondent.
The density of points in certain areas indicates where responses are more common.
Points are slightly transparent/have different **opacities**) to avoid excessive overplotting.
For each condition, self-reported severity scores appear to be distributed across all ages without a clear trend.
Most points are dark green, suggesting that music tends to improve mental health conditions.
Few purple points (`Music effects=Worsen`) suggest that negative effects of music are rare.
The concentration of points at certain severity scores (e.g., 0, 5, 10) suggests that participants may favor specific scores rather than evenly distributing their responses.

#### *Critique of view*:
The use of a linked brush can allow us to identify potential clusters across the four views.
The addition of a tooltip with each respondent's mental health scores allows us to 
retrieve specific values for a certain points,which may help us understand anomalies.
The y-axis could have a title that changes with the dropdown, which would improve clarity.
This vis may benefit with reduced overplotting; we could consider jittering the points slightly to prevent overlap.


#### **How do demographics (eg. music listening habits) contribute to unique self-reported mental health scores?**

<img src="../images/pm3/jess_vis4.gif" width="550" height="500"/>

#### *Summary and Explanations*:
This visualization allows users to compare different **mental health scores** across groups. The tasks it supports include: **comparing** two mental health variables (X and Y axes) to explore relationships, identifying frequency **distributions** using bubble size to show count, **clustering**/categorizing data points using color to differentiate between groups, and viewing any **correlations** between mental health self-report scores. You may **interact with dropdowns** to dynamically change the X-axis, Y-axis, and category groupings. You can also **hover over points** to display detailed information about data points. **Size Encoding on Circles**: Larger circles indicate higher frequencies, making it easy to spot trends. **Positions X and Y** represent the selected mental health score variable on the horizontal and vertical axes, respectively. Nominal **color** categories are used to differentiate between participant groups based on the selected legend variable (e.g., "Yes," "No," "Unknown"). **Dropdown menus** allow users to change the X-axis, Y-axis, and color grouping dynamically. **Hovering over points** reveals additional information via tooltips.  

#### *Critique of view*:
This visualization is an effective use of bubble chart for frequency comparison. 
There is good use of color to differentiate categories and the interactivity enhances usability by allowing users to customize their view. However, the use of three dropdowns may be too much for someone who is not interested in interacting with the visualization and may take more time. Furthermore, there is no way to save a select combination/view, which forces the user to memorize the view when looking at a new comparison/view. Color choices may be refined such that `music effects` have the same color as other visualization, and colors for other legend categories should parallel other member's visualization for continuity.

This dataset was not a validated or standardized questionnaire.
Although our findings may be interesting, the validity of the data should be kept in mind.
Future work may include re-creating these visualizations using data from validated questionnaires and responses from a larger sample.
