def calc_per_with_files(self, times):
    performance = 0
    self.sf_df = pd.read_csv('./result/freq/num' + str(self.SSA_num) + 'times' + str(times) + '.csv')
    if self.sf_df.shape[0] == 100 or self.sf_df.shape[1] == 100:
        print('OK')
    else:
        self.sf_df = self.sf_df.iloc[1:, :]
        performance = 0
        print(self.sf_df.shape[0], self.sf_df.shape[1])

    self.max_view_time_df = pd.read_csv(
        './result/max_view_time/num' + str(self.SSA_num) + 'times' + str(times) + '.csv')

    def calc_importance(row_, col_):
        importance = (self.ff_df.iloc[row_, col_] * 1000 + self.fs_df.iloc[
            row_, col_] / 100 + 2) * (self.sf_df.iloc[row_, col_] / times) - \
                     self.max_view_time_df.iloc[row_, col_] * 0.03
        return importance

    for row in range(100):
        for col in range(100):
            performance += calc_importance(row, col)
    print(performance)
    return performance