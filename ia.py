import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.model_selection import train_test_split


tabela = pd.read_csv('train.csv')
print (tabela.columns)
tabela.drop_duplicates()
tabela.fillna(0)
tabela['volume'] = tabela['volume'].astype('category').cat.codes
x = tabela[['open', 'high', 'low', 'close']] 
y = tabela['volume']


ia = RandomForestRegressor(n_estimators=100, random_state=42)
X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.02, random_state=42)
ia.fit(X_train, Y_train)
previsao = ia.predict(X_test)
resultado = ia.score(X_test, Y_test)

print (f'IA DEU A SUA PREVISÃO {resultado:.2%}')
joblib.dump(ia, 'ia pronta.pkl')
print ('IA PRONTA COM SUCESSO!')