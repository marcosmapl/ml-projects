"""
Author: Marcos A. P. de Lima
Email: marcos.lima@icomp.ufam.edu.br
Since: Feb, 13, 2021
Version: 1.0.0
"""
import matplotlib.image as img
from PIL import Image
import numpy as np
import pandas as pd
import os
import requests

import streamlit as st

from scipy.cluster.vq import kmeans,vq,whiten


def get_color_json(hex):
	"""
	Gets color json data from TheColorAPI service.

	:param: hex: color hex string

	:returns: a python json object
	"""
	if '#' in hex:
		hex = hex.replace('#', '')

	r = requests.get(f'https://www.thecolorapi.com/id?format=json&hex={hex}')
	return r.json()


def rgb2hex(r,g,b):
	"""
	Convert RGB integers to hex equivalent string.

	:param: r: red value.
	:param: g: green value.
	:param: b: blue value:

	:returns: hex string in #ffffff format.
	"""
	return "#{:02x}{:02x}{:02x}".format(r,g,b)


def image_to_dataframe(image):
	"""
	Transforms a image into a pixel dataframe.

	:params: image: image pixel array.

	:returns: pandas dataframe object with all image pixels splitted into RGB columns.
	"""
	r = []
	g = []
	b = []

	for row in image:
	    for pixel in row:
	        r.append(pixel[0])
	        g.append(pixel[1])
	        b.append(pixel[2])

	return pd.DataFrame({
	    'red': r,
	    'green': g,
	    'blue': b
	})


def scale_dataframe(dataframe, function):
	"""
	Scales dataframe features using a scaling function. This function returns a new dataframe with all original features and new ones too.

	:params: dataframe: dataframe to be scaled.
	:params: function: scaling function to be applied in each dataframe's feature.

	:returns: 
	"""
	new_df = dataframe.copy()
	for c in new_df.columns:
		new_df[f'scaled_{c}'] = function(new_df[c])
	return new_df


def file_selector(folder_path='img/'):
	"""
	Creates list down element in app side. The list shows all files into a given folder.

	:params: folder_path: the images directory (path).

	:returns: A string with the selected file path.
	"""
	filenames = os.listdir(folder_path)
	selected_filename = st.sidebar.selectbox('1 - Select a imagem', filenames)
	return os.path.join(folder_path, selected_filename)

if __name__ == '__main__':
	
	st.title('KMeans Image Predominant Colors Detection')
	st.markdown('## This is a Streamlit App using KMeans to extract predominant colors from images')

	filename = file_selector()
	image = img.imread(filename)

	st.image(Image.open(filename), use_column_width=False)
	st.write('File {} ({}x{})'.format(filename, image.shape[0], image.shape[1]))
	st.write(image.shape)

	pixels_df = image_to_dataframe(image)
	pixels_df = scale_dataframe(pixels_df, whiten)

	clusters = st.sidebar.selectbox(
    	'2 - Choose the number of desired colors',
    	range(2,20)
    )

	centers, _ = kmeans(pixels_df[['scaled_red','scaled_green','scaled_blue']], int(clusters))
	r_std, g_std, b_std = pixels_df[['red','green','blue']].std()
	colors = []

	for center in centers:
		scaled_r, scaled_g, scaled_b = center
		colors.append(
			[scaled_r * r_std / 255, scaled_g * g_std / 255, scaled_b * b_std / 255]
		)

	colors = np.array([np.array(xi) for xi in colors])

	for i,color in enumerate(colors, start=1):

		color_hex = rgb2hex(int(color[0]*255), int(color[1]*255), int(color[2]*255))
		json = get_color_json(color_hex)
		
		color_name = json['name']['value']
		closest_hex = json['name']['closest_named_hex']
		match = json['name']['exact_match_name']
		color_rgb = json['rgb']['value']
		color_hsl = json['hsl']['value']
		color_hsv = json['hsv']['value']
		color_image = json['image']['bare']
		st.markdown(f'## Color {i}: {color_name}')
		st.write(f'Closest named hex: {closest_hex}')
		st.write(f'Exact match: {match}')
		st.write(f'RGB value: {color_rgb}')
		st.write(f'HSL value: {color_hsl}')
		st.write(f'HSV value: {color_hsv}')
		st.markdown(f'![{color_name}]({color_image})')
		st.write('')
	