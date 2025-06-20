import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

pd.set_option('display.unicode.east_asian_width',True)
insurance_df=pd.read_csv('D:\streamlit_env\Chapter9_resources\insurance-chinese.csv',encoding='gbk')

output=insurance_df['医疗费用']
features=insurance_df[['年龄','性别','BMI','子女数量','是否吸烟','区域']]
features=pd.get_dummies(features)


x_train,x_test,y_train,y_test=train_test_split(features,output,train_size=0.8)

rfr=RandomForestRegressor()
rfr.fit(x_train,y_train)
y_pred=rfr.predict(x_test)
r2=r2_score(y_test,y_pred)
with open('D:\streamlit_env\rfr_model.pkl','wb') as f:
    pickle.dump(rfr,f)
print('保存成功，已生成相关文件')


