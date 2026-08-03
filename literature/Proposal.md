## 1. Background

The UK currently lacks complete and consistently produced spatial data on off-street surface parking. This makes it difficult to compare the amount of land used for parking across cities or examine its relationship with urban density.

This study will apply a parking segmentation model trained on US data to UK aerial imagery. The model will first be evaluated using manual annotations in Leeds and will then be applied to other UK cities. The resulting data will be used to compare the amount and spatial distribution of parking land and consider its possible relevance to urban densification.

## 2. Research Questions

The study will address the following questions:

1. How well does a model trained on US data perform in UK cities?
2. What types of errors does the model make when applied to UK aerial imagery?
3. How do the area and spatial distribution of surface parking differ between UK cities?
4. How might parking land be related to population density and distance from the city centre?
5. How can spatial parking data inform discussions about urban densification in the UK?

## 3. City Selection

Leeds will be the main city used for model validation and possible model adjustment.

The initial cities considered for the comparative analysis are:

- Leeds;
- Manchester;
- Birmingham.

If data and time allow, the study may also include:

- York;
- Glasgow.

The final study is expected to include between three and five cities. The selection will depend on research progress and data availability.

To support comparison, the study will consider using an equally sized central urban area in each city rather than directly comparing administrative areas of very different sizes.

## 4. Data

The main imagery source is Digimap. The Leeds imagery currently being used has a spatial resolution of 25 centimetres.

The study will mainly consider:

- Digimap aerial imagery;
- model-predicted parking polygons;
- OSM building, road and parking data;
- manually annotated data for Leeds;
- population-density data;
- city-centre locations and distance from the city centre;
- necessary city-boundary data.

Model predictions and OSM parking data will be retained separately so that differences between the two sources can be examined.

Public transport, detailed land use, building density and land value will not initially form part of the core analysis. They may be considered as extensions if suitable data can be obtained later.

## 5. Work Completed

The main preprocessing, prediction and post-processing stages for UK aerial imagery have already been developed. These include:

- converting Digimap aerial imagery into correctly georeferenced GeoTIFF files;
- dividing large images into smaller patches suitable for the model;
- generating parking predictions using a pretrained SegFormer model;
- reconstructing the predictions and converting them into geospatial polygons;
- merging results from multiple image tiles;
- using OSM building footprints to remove buildings incorrectly identified as parking;
- creating road buffers based on UK road classifications and removing road areas; and
- establishing procedures for comparing model predictions with OSM and manual annotations.

The checkpoint weights currently come entirely from the original US model. No UK training data have yet been used to adjust them.

The main current task is completing the manual annotation of Leeds. Manual annotation is time-consuming and the available data remain limited, but the main technical pipeline has been established.

## 6. Leeds Manual Annotation and Model Validation

An early small-scale test was conducted in an area of approximately nine square kilometres in Leeds. However, this area was located away from the city centre, was selected informally, used insufficiently clear annotation rules and did not include the later UK-specific post-processing. It will therefore only be treated as a technical test and will not be included in the formal dissertation results.

The current annotation covers a new area of approximately 25 square kilometres around Leeds city centre. It does not overlap with the earlier test area and will provide the formal model-validation area.

The area will be divided into twenty-five one-square-kilometre grid cells. The following measures will be calculated for each cell:

- precision;
- recall;
- IoU;
- model-predicted parking area;
- manually annotated parking area.

This will provide an overall measure of model performance while also showing how performance varies between locations. It will also allow an initial examination of whether accuracy is related to population density or distance from the city centre.

Based on the current annotation work, the main observed false positives are:

- concrete or asphalt basketball courts;
- storage areas that resemble densely parked vehicles; and
- on-street parking, which is outside the scope of the study.

## 7. Model Adjustment

If the quantity of manually annotated Leeds data is sufficient, the study will attempt to adjust the existing checkpoint weights to make the model more suitable for UK aerial imagery.

This will be exploratory. The limited amount of manually annotated data means that adjustment may not produce a clear improvement. The study will compare the original US model with the adjusted model without assuming that fine-tuning will necessarily be successful.

After the Leeds validation, the other cities will mainly be processed using the final selected model and the UK-specific post-processing workflow.

## 8. Multi-City Parking Analysis

Each city will, where possible, use an equally sized central urban study area divided into consistent one-square-kilometre grid cells.

The main measures for each city will include:

- total model-predicted parking area;
- total OSM-recorded parking area;
- parking area as a share of the study area;
- parking area and parking share in each grid cell;
- agreement and differences between model and OSM results; and
- changes in parking land from the city centre towards outer areas.

The analysis will focus on parking area and parking share. The number of model-generated polygons will not be interpreted directly as the number of car parks because post-processing may divide one car park into several polygons.

If model accuracy is limited, model predictions and OSM parking data will be analysed separately rather than being combined into a single result. Comparing the two sources will help communicate uncertainty in the findings.

## 9. Data Analysis

The initial core explanatory variables will be:

- population density;
- distance from the city centre.

For each one-square-kilometre grid cell, the study will aim to obtain:

- city;
- model-predicted parking area and parking share;
- OSM parking area and parking share;
- area identified by both the model and OSM;
- population density;
- distance from the city centre.

Maps and descriptive statistics will first be used to show:

- total parking area and average parking share in each city;
- the internal spatial distribution of parking land;
- grid cells with relatively concentrated parking; and
- differences between model and OSM data.

The analysis will then focus on two main relationships.

### Parking Share and Population Density

Parking shares will be compared between grid cells with different population densities to examine whether higher- and lower-density areas display different parking patterns.

Correlation analysis, grouped comparisons or simple regression may be used to assess whether there is a noticeable relationship.

### Parking Share and Distance from the City Centre

Parking shares will be compared across different distances from the city centre to examine how parking land changes from central to outer areas.

The analysis will not assume that parking necessarily increases or decreases with distance. Maps and observed data will be used to identify the form of the relationship.

### Multi-City Comparison

The analysis will examine whether these relationships are similar across cities. For example, grid cells with similar population densities may have different parking shares in different cities.

The analysis will be repeated separately using model and OSM parking data. Similar findings from both sources would increase confidence in the results. Different findings would require discussion of the limitations of each source.

The study will examine spatial associations and will not interpret them directly as causal relationships.

## 10. Expected Results and Research Value

The amount and spatial distribution of parking land are expected to vary between cities. Parking share may be associated with population density and distance from the city centre, although the form of these relationships will be determined through the analysis.

The study will seek to understand:

- how much land near UK city centres is used for surface parking;
- how parking land is distributed within cities;
- which areas have relatively high parking shares;
- whether high-density areas still contain substantial surface parking; and
- whether cities display different spatial parking patterns.

The results will help describe how much urban space is occupied by surface parking and whether parking may affect how intensively urban land is used.

The study will not determine whether an individual car park should be redeveloped. Instead, the parking maps and city comparisons will provide basic spatial evidence for discussions about urban densification.

## 11. Expected Outputs

The study is expected to produce:

- a parking-identification and post-processing workflow for UK Digimap aerial imagery;
- approximately 25 square kilometres of manual parking annotations around Leeds city centre;
- an assessment of model accuracy and errors in a UK urban environment;
- an exploratory attempt to adjust the model weights using Leeds data;
- parking maps and spatial comparisons for three to five UK cities;
- an analysis of relationships between parking share, population density and distance from the city centre; and
- an initial discussion of the relationship between parking land and urban densification.

The main purpose is to evaluate the applicability of a US-trained model in the UK and, while clearly presenting model error and data uncertainty, provide new spatial information about parking land and urban density in UK cities.