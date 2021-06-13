import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class eda:
	
	def __init__(self):
	
		""" Generic class for performing EDA on a Pandas dataframe in preparation
        for applying machine learning algorithms.
	
		Attributes:
			df (Pandas dataframe)
			"""
		
		self.df = pd.DataFrame()


	def read_data_file(self, file_name):
	
		"""Function to read in data from a CSV file in tidy format.
				
		Args:
			file_name (string): name of a file to read from
		
		Returns:
			None
		
		"""
	
		self.df = pd.read_csv(file_name)

