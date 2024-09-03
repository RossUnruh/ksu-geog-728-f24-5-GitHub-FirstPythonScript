#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	File name: demo08_1.py
	Author:  Shawn Hutchinson
	Description: Example script that selects Kansas counties through which a major river passes
	Data created: 9/13/2023
	Python version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "D:/GIS_Teaching/GEOG728_TeachingProjects/Exercise04/Exercise04.gdb"

# Perform geoprocessing
selectRiver = arcpy.management.SelectLayerByAttribute("ks_major_rivers", "NEW_SELECTION", "GNIS_Name = 'Kansas River'")

selectCounties = arcpy.management.SelectLayerByLocation("TIGER2010_Census_County", "INTERSECT", selectRiver, "", "NEW_SELECTION")

arcpy.management.CopyFeatures(selectCounties, "SelectedCounties")