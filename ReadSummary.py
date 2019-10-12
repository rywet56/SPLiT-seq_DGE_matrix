class GetReadSummary:

    def __init__(self, ED_dic, query):
        self.ED0 = []
        self.ED1 = []
        self.ED2 = []
        self.ED3 = []
        self.ED4 = []
        self.ED5 = []
        self.sequence = query
        self.ED_dic = ED_dic
        self.ED_list = [self.ED0, self.ED1, self.ED2, self.ED3, self.ED4, self.ED5]
        self.populate_ED_lists()
        self.ED_list = [self.ED0, self.ED1, self.ED2, self.ED3, self.ED4, self.ED5]

    def populate_ED_lists(self):

        self.ED0 = self.extract_positions((filter(lambda entry: entry[1] == 0, self.ED_dic.items())))
        self.ED1 = self.extract_positions((filter(lambda entry: entry[1] == 1, self.ED_dic.items())))
        self.ED2 = self.extract_positions((filter(lambda entry: entry[1] == 2, self.ED_dic.items())))
        self.ED3 = self.extract_positions((filter(lambda entry: entry[1] == 3, self.ED_dic.items())))
        self.ED4 = self.extract_positions((filter(lambda entry: entry[1] == 4, self.ED_dic.items())))
        self.ED5 = self.extract_positions((filter(lambda entry: entry[1] == 5, self.ED_dic.items())))

    def extract_positions(self, pos_iterator):
        pos_dic = []
        for pos in pos_iterator:
            pos_dic.append(pos[0])
        return pos_dic
