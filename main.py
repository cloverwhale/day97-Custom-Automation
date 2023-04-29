from tradingdata import TradingData
from customparser import CustomParser


trading_data = TradingData()
raw_data = trading_data.daily()

cp = CustomParser(raw_data)
raw_data_date = cp.data_date

cp.get_final_data('foreign').to_csv(f'{raw_data_date}_foreign.csv', index=None)
cp.get_final_data('trust').to_csv(f'{raw_data_date}_trust.csv', index=None)
cp.get_final_data('dealer').to_csv(f'{raw_data_date}_dealer.csv', index=None)
