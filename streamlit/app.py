import streamlit as st
import pandas as pd
import seaborn as sns

# Header
st.subheader('Mini Project')
st.title(':chart_with_upwards_trend: 엔터사 주식 데이터 분석')

st.divider()

## Section 1 ###################
st.header('1. 엔터주 상관관계 분석')
st.write("대한민국 대표 엔터사들(JYP, YG, SM, HYBE)의 주가가 서로 유사하게 움직이는 지를 알아보기 위해 **피어슨 상관관계**를 구하고자 한다. HYBE의 주식 상장일을 기준으로 하여 최근까지의 주가를 크롤링 해서 대표 엔터사들 간의 상관계수를 구해보자.")
st.caption(":pencil2: 피어슨 상관계수는 주가를 바탕으로 -1에서 1 사이의 값을 리턴한다. 만약 상관계수가 0보다 크다면, 두 기업의 주가 사이에 양의 상관관계가 있다고 해석하고, 반대의 경우는 음의 상관관계가 있다고 해석 한다.")

# 대표 엔터사 주식 데이터 
stocks_df = pd.read_csv("./data/stocks_df.csv")


# EDA
st.subheader('1) EDA')
col1, col2 = st.columns(2)

col1.markdown("##### 데이터프레임")
col1.dataframe(data=stocks_df, width=340, height=330)
col2.write("##### 기초통계량")
col2.dataframe(data=stocks_df.describe(), width=340, height=330)


# DA
st.subheader('2) Data Analysis')

col3, col4 = st.columns(2)
col3.markdown("##### Stock price Graph")
col3.line_chart(stocks_df.iloc[:,1::])

# correlation plot
col4.write("##### Correlation Analysis Heatmap")
plot = sns.heatmap(stocks_df.corr(method = 'pearson', numeric_only=True), cmap='YlOrRd', annot=True)
col4.pyplot(plot.get_figure())

st.markdown("##### :pushpin: 상관관계 분석 결과")
st.markdown('''
    - HYBE와 YG는 중간정도의 양의 상관관계를 가진다.
    - JYP와 SM은 :red[0.84]로 큰 양의 상관관계를 가지므로 거의 유사하게 주가가 변동함을 알 수 있다. 
    - JYP와 YG는 중간 정도의 양의 상관관계를 가진다. 
    - SM과 YG는 중간 정도의 양의 상관관계를 가진다. 
    ''')

st.markdown('''
            **대표 엔터 3사(JYP, SM, YG)는 전체적으로 유사하게 주가가 변동함을 알 수 있고, HYBE는 YG를 제외하고는 상관관계가 약하다는 것을 알 수 있다.
            때문에, :red[HYBE를 제외하여 대표 엔터 3사의 상관계수 분석을 기간을 5년으로 늘려 분석하고자 한다.]**
            ''')

st.divider()

## Section 2 ############################
st.header('2. 대표 엔터 3사 주식 상관관계 분석')

# 대표 엔터 3사 주식 데이터 
stocks_3_df = pd.read_csv("./data/stocks_3_df.csv")


# EDA
st.subheader('1) EDA')
col5, col6 = st.columns(2)

col5.markdown("##### 데이터프레임")
col5.dataframe(data=stocks_3_df, width=340, height=330)
col6.write("##### 기초통계량")
col6.dataframe(data=stocks_3_df.describe(), width=340, height=330)


# DA
st.subheader('2) Data Analysis')

col7, col8 = st.columns(2)
col7.markdown("##### Stock price Graph")
col7.line_chart(stocks_3_df.iloc[:,1::])

# correlation plot
col8.write("##### Correlation Analysis Heatmap")
plot = sns.heatmap(stocks_3_df.corr(method = 'pearson', numeric_only=True), cmap='YlOrRd', annot=True)
col8.pyplot(plot.get_figure())

st.markdown("##### :pushpin: 상관관계 분석 결과")
st.markdown('''
    - JYP, SM, YG 모두 강한 양의 상관관계가 있다. 
    ''')

st.markdown("**3사 모두 큰 양의 상관관계가 있음을 알 수 있다. 그렇다면, :red[엔터사 별로 소속가수의 앨범이 나왔을 때 그 회사의 주가가 다른 회사들에 비해 변동성이 큰지 알아보자.]**")


st.divider()

## Section 3 ##############################################################
st.header('3. 연간 엔터사별 Top 앨범 출시에 따른 주가 변동률 분석')
st.markdown('''
            - **가설: 소속 가수의 앨범이 나오면 화제성 및 수익이 증가하므로 해당 엔터사의 주가 또한 상승할 것으로 예측된다.**
            - 대표 3사의 주가 경향성이 비슷하므로, 한 회사의 소속가수가 컴백할 기간에 그 회사만 주가 변동성이 높은지 알아보고자 한다. **때문에, 연간 대표 3사의 Top 앨범을 선정하여 앨범 출시일 이후 10 거래일 간의 주가 변동률 분석한다.**
            ''')

st.caption(":pencil2: 써클차트(가온차트) 연간 앨범 판매량 순위 중 3사와 관련된 앨범 데이터만 수집하여 Top 앨범을 선정하고, 컴백 날짜 이후 10 거래일을 컴백 기간으로 설정한다.")

# 대표 엔터사 주식 데이터 
yearly_top_album_df = pd.read_csv("./data/yearly_top_album_df.csv")

st.markdown("##### :small_orange_diamond: 연간 Top 앨범 데이터프레임")
st.dataframe(data=yearly_top_album_df, width=1000, height=330)

st.subheader('1) 2018년도 SM Top 앨범 출시에 따른 주가 변동률 분석')
st.markdown("##### :small_orange_diamond: 2018년도 SM Top 앨범 데이터")
st.dataframe(yearly_top_album_df.head(1))

# 2018년도 SM TOP 앨범 출시일 이후 10 거래일 간 주가 변동 데이터
st.markdown("##### :small_orange_diamond: 2018년도 SM TOP 앨범 출시일 이후 10 거래일 간 주가 변동 데이터")
sm_2018_df = pd.read_csv("./data/sm_2018_df.csv")
st.dataframe(sm_2018_df)

col9, col10 = st.columns(2)
col9.caption("- drc = 일간 변동률(daily rate of change)")
col10.caption("- cs = 변동률 누적 합계(cumulative sum rate of change)")

st.markdown("##### :pushpin: 주가 변동률 분석 결과")
st.markdown('''
    - JYP 8.22%, **SM 11.84%**, yg 7.76% 
    - 2018년도 SM의 Top 앨범 출시일에 따른 **주가 변동성은 SM이 제일 높다**
    ''')

st.divider()

## Section 4 ################################################# 
st.header('4. 5년 간 엔터사별 Top 앨범 출시에 따른 주가 변동률 분석')

# 5 년 간 주가 변동률 데이터
stock_price_fluctuation_rate = pd.read_csv("./data/stock_price_fluctuation_rate.csv")

st.markdown("##### :small_orange_diamond: 5 년간 주가 변동률 데이터")
st.dataframe(data=stock_price_fluctuation_rate, width=1000, height=330)

col11, col12 = st.columns(2)
col11.caption("- cs = 변동률 누적 합계(cumulative sum rate of change)")
col12.caption("- result = 두 회사보다 모두 주가 변동률이 높으면 True")

st.markdown("##### :pushpin: 최종 결론")
st.markdown('''
    - True: 5
    - False: 10
    - True 비율: 약 33.3%
    ''')
st.markdown('''주가 변동률이 두 회사보다 모두 큰 경우는 :red[약 33%] 정도로 낮다. 그러므로, :red[**앨범 출시와 엔터사 주식과는 큰 관계가 없어 가설을 입증할 수 없다.**] 또한, 분석 데이터로 보아 2020년 YG의 주가 변동률이 매우 높은 것으로 보이는데 이는 해당 날짜의 소속사에 큰 논란이 있었던 것으로 확인된다.  
:blue[**때문에, 소속사에 관한 긍정/부정적인 기사와 주가와의 연관성을 분석해보는 것도 좋을 것 같다.**]
            ''')