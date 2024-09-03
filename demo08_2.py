#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	File name: demo08_2.py
	Author:  Shawn Hutchinson
	Description: Example script that selects Kansas counties through which a major river passes
	Data created: 9/13/2023
	Python version: 3.9.16
"""

# Import arcpy module and set environments
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "D:/GIS_Teaching/GEOG728_TeachingProjects/Exercise04/Exercise04.gdb"

# Establish local variables
inputFeatures = "ks_major_rivers"
sqlExpression = "GNIS_Name = 'Kansas River'"
selectFeatures = "Tiger2010_Census_County"
outputFeatures = "SelectedCounties"

# Perform geoprocessing
selectRiver = arcpy.management.SelectLayerByAttribute(inputFeatures, "NEW_SELECTION", sqlExpression)

selectCounties = arcpy.management.SelectLayerByLocation(selectFeatures, "INTERSECT", selectRiver, "", "NEW_SELECTION")

arcpy.management.CopyFeatures(selectCounties, outputFeatures)