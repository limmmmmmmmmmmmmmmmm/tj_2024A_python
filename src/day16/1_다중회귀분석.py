# day16 > 1_다중회귀분석.py
# [1] 데이터 수집
import pandas as pd
data = pd.DataFrame({
    '운동시간': [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6],
    '게임시간': [2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7],
    '체중': [60, 62, 64, 66, 68, 65, 67, 69, 71, 73, 62, 64, 66, 68, 70, 64, 66, 68, 70, 72]
})
# [2] 데이터 통계분석  # 게임시간 과 운동시간에 따른 체중 변화 비교
Rformula = '체중 ~ 운동시간 + 게임시간'  # 1. 모형 수식 정의
from statsmodels.formula.api import ols
model = ols( Rformula , data = data ).fit()     # 2. 모델 피팅
print( model.params )     # 3. 모델 결과 확인 ( 회귀 계수 )
print( model.pvalues )   # 3. 모델 결과 확인 ( p값 )
