import numpy as numpy
from sklearn.linear_model import LinerarRegression
from sklearn.metrics import mean_squared_error

def main():
	df=pd.read_csv("Filename")
	ans1=max(df.std(axis=1))


	#2
	filter1 = (df['Town2'] >= 90) & (df['Town2'] < 100)
	df_2 = df[filter1]
	ans2 = df_2['NYC'].median(axis=1)

	#3
	Y = df['NYC']
	beta_array = []
	MSE_array = []

	for (col_name, col_data) in df.iteritems():
		X = col_data
		reg = LinerarRegression().fit(X,Y)
		beta_array.append(abs(reg.coef_[0]))
		
		y_pred = reg.predict(X)
		mse = sklearn.metrics.mean_squared_error(Y, y_pred)
		MSE_array.append((col_name,mse))

	ans3 = sum(beta_array)

	#4
	ans4 = min(MSE_Array)







