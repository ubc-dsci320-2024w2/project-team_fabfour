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

### View 1 
TODO: Allison
1. Screenshot/gif of visualization
2. Summary of tasks and how they accomplish the task
3. Explain/justify viz choices
    1. Marks
    2. Channels
    3. Characteristics of channels exploited
    4. Describe new interactions
    5. Characteristics of interactios and interactivity
    6. Critique the view

### View 2
TODO: Judy
1. Screenshot/gif of visualization
2. Summary of tasks and how they accomplish the task
3. Explain/justify viz choices
    1. Marks
    2. Channels
    3. Characteristics of channels exploited
    4. Describe new interactions
    5. Characteristics of interactios and interactivity
    6. Critique the view

### View 3
TODO: Helena
1. Screenshot/gif of visualization
2. Summary of tasks and how they accomplish the task
3. Explain/justify viz choices
    1. Marks
    2. Channels
    3. Characteristics of channels exploited
    4. Describe new interactions
    5. Characteristics of interactios and interactivity
    6. Critique the view

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
ColorBrewer2.org[https://colorbrewer2.org/#type=diverging&scheme=PRGn&n=4].
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

<img src="../images/pm3/jess_vis4.gif" width="500" height="500"/>

#### *Summary and Explanations*:
This visualization allows users to compare different **mental health scores** across groups. The tasks it supports include: **comparing** two mental health variables (X and Y axes) to explore relationships, identifying frequency **distributions** using bubble size to show count, **clustering**/categorizing data points using color to differentiate between groups, and viewing any **correlations** between mental health self-report scores. You may **interact with dropdowns** to dynamically change the X-axis, Y-axis, and category groupings. You can also **hover over points** to display detailed information about data points. **Size Encoding on Circles**: Larger circles indicate higher frequencies, making it easy to spot trends. **Positions X and Y** represent the selected mental health score variable on the horizontal and vertical axes, respectively. Nominal **color** categories are used to differentiate between participant groups based on the selected legend variable (e.g., "Yes," "No," "Unknown"). **Dropdown menus** allow users to change the X-axis, Y-axis, and color grouping dynamically. **Hovering over points** reveals additional information via tooltips.  

#### *Critique of view*:
This visualization is an effective use of bubble chart for frequency comparison. 
There is good use of color to differentiate categories and the interactivity enhances usability by allowing users to customize their view. However, the use of three dropdowns may be too much for someone who is not interested in interacting with the visualization and may take more time. Furthermore, there is no way to save a select combination/view, which forces the user to memorize the view when looking at a new comparison/view. Color choices may be refined such that `music effects` have the same color as other visualization, and colors for other legend categories should parallel other member's visualization for continuity.

This dataset was not a validated or standardized questionnaire.
Although our findings may be interesting, the validity of the data should be kept in mind.
Future work may include re-creating these visualizations using data from validated questionnaires and responses from a larger sample.
