import pandas as pd

RANGE = 20


class CustomParser:

    def __init__(self, response_data) -> None:
        self.raw_data = response_data
        self.data_date = self.raw_data['date']
        self.raw_df = self.parse_raw_data()
        self.extracted_df = self.drop_redundant_columns()
        self.sorted_data_foreign = self.extracted_df.iloc[:, [
            0, 1, 2]].sort_values(by='外陸資買賣超股數(不含外資自營商)', ascending=False)
        self.sorted_data_trust = self.extracted_df.iloc[:, [
            0, 1, 3]].sort_values(by='投信買賣超股數', ascending=False)
        self.sorted_data_dealer = self.extracted_df.iloc[:, [
            0, 1, 4]].sort_values(by='自營商買賣超股數', ascending=False)

    def parse_raw_data(self):
        try:
            df = pd.DataFrame(self.raw_data['data'])
            header_data = self.raw_data['fields']
            for i in range(len(header_data)):
                header_data[i] = f'{i}_{header_data[i]}'
            df.columns = header_data
        except KeyError:
            df = self.raw_data
        return df

    def drop_redundant_columns(self):
        df = self.raw_df.copy()
        cols = [2, 3, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17]
        df.drop(self.raw_df.columns[cols], axis=1, inplace=True)
        df.columns = [item.split('_')[1] for item in list(df.columns)]
        df.dropna()
        for col in df.columns[2:]:
            df[col] = df[col].str.replace(',', '').astype(int)
        return df

    def get_top_20(self, type):
        if type == 'foreign':
            return self.sorted_data_foreign.head(RANGE)
        elif type == 'trust':
            return self.sorted_data_trust.head(RANGE)
        else:
            return self.sorted_data_dealer.head(RANGE)

    def get_bottom_20(self, type):
        if type == 'foreign':
            return self.sorted_data_foreign.tail(RANGE)
        elif type == 'trust':
            return self.sorted_data_trust.tail(RANGE)
        else:
            return self.sorted_data_dealer.tail(RANGE)

    def get_final_data(self, type):
        return self.concat(self.get_top_20(type), self.get_bottom_20(type))

    def concat(self, df_top, df_bottom):
        return pd.concat([df_top, df_bottom], ignore_index=True, sort=False)
